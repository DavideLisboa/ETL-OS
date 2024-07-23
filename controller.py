# -*- coding: utf-8 -*-

import sys, os

import arcpy
import json
import requests

from datetime import datetime
from dateutil.parser import parse
from decimal import Decimal

import utils

from api import get_domininio_servico_abertura, get_domininio_servico_encerramento, get_os, get_bearer_token 
from utils import CODS_IBGE, DOMINIOS_ENCERRAMENTO, list_split

import importlib;
importlib.reload(sys)



DATE_FORMAT = '%d/%m/%Y'

dirpath = os.path.dirname(os.path.abspath(__file__))
conf_filename = os.path.join(dirpath, 'conf.json')
CONF = None
with open(conf_filename) as json_file:
    CONF = json.load(json_file)



class ResponseNaoEsperado(Exception):
    pass


def _prepare_dominios_encerramento(response_json):
    result = {}
    for r in response_json:
        result[r['cdServicoEncerramento']] = r['dsServicoEncerramento']
    return result

def delete_codOs_database(cods_os, log):
    # deleta as cod os que vieram novamente
    # no WS para serem novamente inseridas
    qt_deletados = 0
    if cods_os:
        log.logger.info('# Iniciando split da lista para deletar')
        cods_list = list_split(cods_os, 1000)
        log.logger.info('# Split finalizado')
        for cods in cods_list:
            where_clause = 'COD_ABERTURA_OS in (%s)' % ', '.join([str(v) for v in cods])
            
            # deleta da table
            with arcpy.da.UpdateCursor(
                CONF['tb_os'],
                field_names=['OID@'],
                where_clause=where_clause
            ) as cursor:
                for row in cursor:
                    cursor.deleteRow()
                    qt_deletados += 1
            del cursor

            # deleta da fc
            with arcpy.da.UpdateCursor(
                CONF['fc_os'],
                field_names=['OID@'],
                where_clause=where_clause
            ) as cursor:
                for row in cursor:
                    cursor.deleteRow()
            del cursor
    return qt_deletados


def insert(data_sem_geo, data_com_geo):
    fields_table = utils.tb_os_map.keys()
    fields_fc = utils.fc_os_map.keys()

    qt_inserido_table = len(data_sem_geo)
    qt_inserido_fc = 0
    cursor_table = arcpy.da.InsertCursor(CONF['tb_os'], field_names=list(fields_table))

    # insere dados sem geo
    for data in data_sem_geo:
        row = utils.prepare_row_to_update(fields_table, utils.tb_os_map, data)
        cursor_table.insertRow(row)

    # insere dados com geo, table
    for data in data_com_geo:
        row_tb = utils.prepare_row_to_update(fields_table, utils.tb_os_map, data)
        cursor_table.insertRow(row_tb)
        qt_inserido_table += 1

    del cursor_table

    cursor_fc = arcpy.da.InsertCursor(CONF['fc_os'], field_names=list(fields_fc))
    # insere dados com geo, fc
    for data in data_com_geo:
        row_fc = utils.prepare_row_to_update(fields_fc, utils.fc_os_map, data)
        cursor_fc.insertRow(row_fc)
        qt_inserido_fc += 1

    del cursor_fc

    return qt_inserido_table, qt_inserido_fc

def prepare_data_dict(cod_ibge, response_json):
    # os dados retornados da OS,
    # so devem ser inseridos no dicionario se o
    # cod de fechamento estiver nos DOMINIOS_ENCERRAMENTO
    result = []
    cod_imoveis = []
    cods_abertura_os = []
    dict_result = {}
    for _dict_response in response_json:
        result.append(_dict_response)
        if _dict_response['cdImovel']:
            cod_imoveis.append(_dict_response['cdImovel'])
        if _dict_response['cdOsAbertura']:
            cods_abertura_os.append(_dict_response['cdOsAbertura'])

    if result:
        dict_result[cod_ibge] = result
    return cods_abertura_os, cod_imoveis, dict_result


def get_cod_imovel_e_ibge(cod_imoveis):
    result = {}
    if cod_imoveis:
        cods_imoveis = list_split(cod_imoveis, 1000)
        for cods in cods_imoveis:
            where_clause = 'CODIMOVEL in (%s)' % ', '.join([str(x) for x in cods])
            with arcpy.da.SearchCursor(
                CONF['fc_consumidores'],
                field_names=['CODIMOVEL', 'COD_IBGE', 'Shape@'],
                where_clause=where_clause
            ) as cursor:
                for row in cursor:
                    result[row[0]] = {
                        'cod_ibge': int(row[1]) if row[1] else None,
                        'geom': row[2]
                    }

    return result


class ValidaLimites(object):

    def valida_limite_estadual(self, geom):
        if not hasattr(self, '_geom_estadual'):
            with arcpy.da.SearchCursor(CONF['fc_rs'], field_names=['Shape@']) as cursor:
                for row in cursor:
                    self._geom_estadual = row[0]

        return self._geom_estadual.contains(geom)


    def valida_limite_municipal(self, geom):
        if not hasattr(self, '_geoms_municipais'):
            self._geoms_municipais = {}
            with arcpy.da.SearchCursor(CONF['fc_municipios'], field_names=['Shape@', 'CD_GEOCODM']) as cursor:
                for row in cursor:
                     self._geoms_municipais[row[1]] = row[0]

        for ibge, geom_m in self._geoms_municipais.items():
            if geom_m.contains(geom):
                return int(ibge), geom_m

        return None, None 


valida_limites = ValidaLimites()


def gen_geom_latlong(data):
    geom = None
    # 1) gerar geometria pelo lat/long
    if data['vlLatitude'] and data['vlLongitude']:
        point = arcpy.Point()
        point.X, point.Y = data['vlLongitude'], data['vlLatitude']
        # proj WSG84 to SIRGAS 2000
        geom = arcpy.PointGeometry(point, arcpy.SpatialReference(4326)).projectAs(arcpy.SpatialReference(4674))

    return geom


class ESPACIALIZACAO:
        ESPACIALIZADO_VIA_COORDS = 1
        ESPACIALIZADO_VIA_CONSUMIDOR = 2
        NAO_ESPACIALIZADO = 3

class FLAG_LOCALIZACAO_OS:
    CORRETA = 0
    INCORRETA = 1


def valida(list_dict, codimoveis_x_cod_ibge, dominios_encerramento):
    '''
    '''

    com_geo = []
    sem_geo = []
    for data in list_dict:
        _data = None
        _data = data.copy()
        geom = gen_geom_latlong(data)
        if not geom:
            if not data['cdImovel'] or data['cdImovel'] == 0:
                # se nao espacializado via coods e nao ha cod imovel
                _data['ESPACIALIZACAO'] = ESPACIALIZACAO.NAO_ESPACIALIZADO
                # insere apenas na tb de os
                sem_geo.append(_data)
                continue

            # verifica se codimovel do WS existe no GIS
            if data['cdImovel'] in codimoveis_x_cod_ibge:
                geom = codimoveis_x_cod_ibge[data['cdImovel']]['geom']
                _data['ESPACIALIZACAO'] = ESPACIALIZACAO.ESPACIALIZADO_VIA_CONSUMIDOR
            else:
                # cod ibge vindo do WS eh diferente do consumidor
                _data['ESPACIALIZACAO'] = ESPACIALIZACAO.NAO_ESPACIALIZADO
                # insere apenas na tb de os
                sem_geo.append(_data)
                continue
        else:
            if valida_limites.valida_limite_estadual(geom):
                _data['ESPACIALIZACAO'] = ESPACIALIZACAO.ESPACIALIZADO_VIA_COORDS
            else:
                _data['ESPACIALIZACAO'] = ESPACIALIZACAO.NAO_ESPACIALIZADO
                sem_geo.append(_data)
                continue

        if _data['ESPACIALIZACAO'] == ESPACIALIZACAO.ESPACIALIZADO_VIA_CONSUMIDOR:
            if data['cdIbge'] == codimoveis_x_cod_ibge[data['cdImovel']]['cod_ibge']:
                _data['FLAG_LOCALIZACAO_OS'] = FLAG_LOCALIZACAO_OS.CORRETA
            else:
                _data['FLAG_LOCALIZACAO_OS'] = FLAG_LOCALIZACAO_OS.INCORRETA
        else:
            cod_ibge, _ = valida_limites.valida_limite_municipal(geom)
            if cod_ibge and data['cdIbge'] == cod_ibge:
                _data['FLAG_LOCALIZACAO_OS'] = FLAG_LOCALIZACAO_OS.CORRETA
            else:
                _data['FLAG_LOCALIZACAO_OS'] = FLAG_LOCALIZACAO_OS.INCORRETA

        # campos calculados
        _data['COD_DESC_SERVICO_ENCERRAMENTOS'] = u'{} - {}'.format(
            _data['cdServicoEncerrramento'],
            dominios_encerramento.get(_data['cdServicoEncerrramento'])
        )

        data_ini = parse(_data['dtAberturaOs'])
        data_fim = parse(_data['dtFinalExecucaoOs'])
        duracao = ((data_fim - data_ini).total_seconds() / 60.0) / 60.0
        duracao = float(Decimal(str(duracao)).quantize(Decimal('0.00')))
        _data['TEMPO_ATENDIMENTO'] = duracao
        _data['municipio'] = CODS_IBGE.get(_data['cdIbge'])

        _data['geom'] = geom
        com_geo.append(_data)

    return com_geo, sem_geo


def main(log, data_ini, data_fim):
    arcpy.env.workspace = CONF['gdb_path']

    response_token, OK = get_bearer_token()

    if not OK:
        log.logger.exception(response_token.content)
        raise ResponseNaoEsperado()

    auth_token = dict(json.loads(response_token.content))['access_token']

    headers = {'Authorization': 'Bearer ' + auth_token}

    response, OK = get_domininio_servico_abertura(headers)
    DATA_DICT_COM_GEO = []
    DATA_DICT_VALIDACAO_SEM_GEO = []
    cod_imoveis = []
    # dicionario com os dados, ja filtrados
    # para ser analisado
    DATA_DICT = {}
    # lista de cod abertura das OS do WS
    COD_ABERTURA_OS = []

    if OK:
        results_da_json = response.json()
        dominios_abertura = [result['cdServicoAbertura'] for result in results_da_json]
        dominios_encerramento, OK = get_domininio_servico_encerramento(headers)
        if not OK:
            log.logger.exception(dominios_encerramento.content)
            raise ResponseNaoEsperado()
        dominios_encerramento = _prepare_dominios_encerramento(dominios_encerramento.json())
        for cod_ibge, municipio in CODS_IBGE.items():
            log.logger.info('BUSCA OS DO MUNICIPIO: %s' % municipio)
            response_os, OK = get_os(cod_ibge, dominios_abertura, data_ini, data_fim, headers)
            if not OK:
                log.logger.exception(response_os.content)
                raise ResponseNaoEsperado()
            results_os_json = response_os.json()
            if results_os_json:
                cods_abertura_os, cod_imoveis, data_dict_result = prepare_data_dict(cod_ibge, results_os_json)
                COD_ABERTURA_OS.extend(cods_abertura_os)
                if data_dict_result:
                    DATA_DICT.update(data_dict_result)

        # pega os cod ibge de cada codimovel que veio no WS
        codimoveis_x_cod_ibge = get_cod_imovel_e_ibge(cod_imoveis)
        # inicia processo de gerar geom e salvar em feature e/ou tabela
        for key, value in DATA_DICT.items():
            com_geo, sem_geo = valida(value, codimoveis_x_cod_ibge, dominios_encerramento)
            DATA_DICT_COM_GEO.extend(com_geo)
            DATA_DICT_VALIDACAO_SEM_GEO.extend(sem_geo)

        edit = arcpy.da.Editor(arcpy.env.workspace)
        edit.startEditing(False, False)
        edit.startOperation()
        qt_deletados = delete_codOs_database(COD_ABERTURA_OS, log)
        log.logger.info('QT DELETADOS: %d' % qt_deletados)
        qt_sem_geo_inseridos, qt_com_geo_inseridos = insert(DATA_DICT_VALIDACAO_SEM_GEO, DATA_DICT_COM_GEO)
        edit.stopOperation()
        edit.stopEditing(True)

        log.logger.info('INSERIDOS NA TABLE DE OS: %d' % qt_sem_geo_inseridos)
        log.logger.info('INSERIDOS NA FC DE OS: %d' % qt_com_geo_inseridos)
    else:
        if not OK:
            log.logger.exception(response.content)
            raise ResponseNaoEsperado()
    
    return DATA_DICT_COM_GEO, DATA_DICT_VALIDACAO_SEM_GEO


if __name__ == "__main__":
    com_geo, sem_geo = main('LOG_FUTURO', '01/01/2019')
    print ('COM GEO ---------------')
    for d in com_geo:
        print (d['geom'], d['vlLongitude'], d['vlLatitude'])

    print ('SEM GEO ------------- ')
    for d in sem_geo:
        print (d['vlLongitude'], d['vlLatitude'])
    print ('FIM')
