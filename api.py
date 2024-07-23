

import sys, os

import arcpy
import json
import requests

from datetime import datetime

from utils import CODS_IBGE, DOMINIOS_ENCERRAMENTO

from dotenv import load_dotenv, find_dotenv
import importlib;
importlib.reload(sys)

load_dotenv(find_dotenv())

# Authentication
AUTH_CLIENT_GRANT_TYPE = os.environ.get('SOE_AUTH_CLIENT_GRANT_TYPE')
AUTH_CLIENT_ID = os.environ.get('SOE_AUTH_CLIENT_ID')
AUTH_CLIENT_SECRET = os.environ.get('SOE_AUTH_CLIENT_SECRET')



DATE_FORMAT = '%d/%m/%Y'

dirpath = os.path.dirname(os.path.abspath(__file__))
conf_filename = os.path.join(dirpath, 'conf.json')
CONF = None
with open(conf_filename) as json_file:
    CONF = json.load(json_file)



def executa_requisicao(url, method='GET', headers={}, data={}):
    # dados de acesso da imagem ao web service
    headers.update({
        # "matricula": CONF['ws_matricula'],
        # "organizacao": CONF['ws_organizacao'],       
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    })
    if method.upper() == 'POST':
        response = requests.post(url, headers=headers, data=json.dumps(data))
    else:
        response = requests.get(url, headers=headers, data=data)
    return response


def _recupera_bearer_token(url, headers={}):

    body = {'grant_type' : '{}'.format(AUTH_CLIENT_GRANT_TYPE), 'client_id' : '{}'.format(AUTH_CLIENT_ID), 'client_secret' : '{}'.format(AUTH_CLIENT_SECRET) }
    
    headers.update({              
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    })
    
    response = requests.post(url, headers=headers, data=body)

    return response, _verifica_response_token_ok(response)   
    

def get_bearer_token():
    return _recupera_bearer_token(CONF['url_SOE_token'])  

def _verifica_response_token_ok(response):
    if response.status_code == 200:
        r = response.json()        
        if len(dict(r)['access_token']) > 0:            
            return True         
    return False 


def _verifica_response_ok(response, key_api):
    if response.status_code == 200:
        r = response.json()
        if len(r) == 0:
            return True       
        if len(r) > 0 and key_api in r[0]:
            return True      
    return False


def get_domininio_servico_abertura(headers={}):
    r = executa_requisicao(CONF['url_dominio_servico_abertura'],'GET', headers)
    return r, _verifica_response_ok(r, 'cdServicoAbertura')


def get_domininio_servico_encerramento(headers={}):
    r = executa_requisicao(CONF['url_dominio_servico_encerramento'], 'GET', headers)
    return r, _verifica_response_ok(r, 'cdServicoEncerramento')


def get_os(cod_ibge, cods_abertura, data_ini, data_fim, headers={}):
    '''
        modelo de envio:
            {
            "cdIbge": 4304606,
            "cdServicoAbertura": [
                940
            ],
            "dataFinal": "11/07/2019",
            "dataInicial": "01/07/2019"
            }

        modelo resposta:

    '''
    data = {
        "cdIbge": cod_ibge,
        "cdServicoAbertura": cods_abertura,
        "dataInicial": data_ini,
        "dataFinal": data_fim
    }
    r = executa_requisicao(CONF['url_os'], 'POST', headers, data=data)
    return r, _verifica_response_ok(r, 'cdIbge')



if __name__ == "__main__":
    r, OK = get_domininio_servico_abertura()
    result = r.json()
    cods = [result[x]['cdServicoAbertura'] for x in range(10)]
    r, OK = get_os(4304606, cods, '01/07/2019')
    print (r.content)
    print (r, OK)

# {
#   "cdIbge": 4304606,
#   "cdServicoAbertura": [
#     0, 280, 940, 945, 174, 699, 290, 300, 350, 355
#   ],
#   "dataFinal": "15/07/2019",
#   "dataInicial": "01/07/2019"
# }
