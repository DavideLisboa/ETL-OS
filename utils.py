# -*- coding: utf-8 -*-
from collections import OrderedDict
import dateutil.parser


def prepare_row_to_update(fields, fields_map_converter, row_search):
    new_row = []
    for field in fields:
        new_row.append(fields_map_converter[field](row_search))
    return tuple(new_row)

def list_split(lista, tamanho):
    if isinstance(lista, set):
        lista = list(lista)
    if len(lista) > tamanho:
        n = tamanho
        return [lista[i:i + n] for i in range(0, len(lista), n)]
    else:
        return [lista]


def to_date(v):
    if v:
        return dateutil.parser.parse(v)
    return None


tb_os_map = OrderedDict((
    ('COD_IBGE', lambda dados: dados['cdIbge']),  # Double
    ('COD_US', lambda dados: dados['cdUs']),  # Double
    ('COD_IMOVEL', lambda dados: dados['cdImovel']),  # String
    ('COD_IMOVEL_NUM', lambda dados: dados['cdImovel']),  # Double
    ('COD_SERVICO', lambda dados: dados['cdServicoAbertura']),  # Double
    ('DESCRICAO_SERVICO', lambda dados: dados['dsServicoAbertura']),  # String
    ('DT_ABERTURA_OS', lambda dados: to_date(dados['dtAberturaOs'])),  # Date
    ('DT_FINAL_EXECUCAO_OS', lambda dados: to_date(dados['dtFinalExecucaoOs'])),  # Date
    ('DT_ENCERRAMENTO_OS', lambda dados: to_date(dados['dtEncerramentoOs'])),  # Date
    ('NOME_LOGRD', lambda dados: dados['nmLogradouro']),  # String
    ('LATITUDE', lambda dados: dados['vlLatitude']),  # Double
    ('LONGITUDE', lambda dados: dados['vlLongitude']),  # Double
    ('COD_ABERTURA_OS', lambda dados: dados['cdOsAbertura']),
    ('COD_ENCERRAMENTO_OS', lambda dados: dados['cdOsEncerramento']),
    ('COD_SERVICO_ENCERRAMENTO', lambda dados: dados['cdServicoEncerrramento']),
    # CAMPOS ADD VIA VALIDACAO
    ('ESPACIALIZACAO', lambda dados: dados['ESPACIALIZACAO']),  # SmallInteger
    # ('OBSERVACAO', lambda dados: dados['OBSERVACAO']),  # String
    # ('CATEGORIA_OS', lambda dados: dados['CATEGORIA_OS']),  # String
))


fc_os_map = OrderedDict((
    ('COD_IBGE', lambda dados: dados['cdIbge']),  # Double
    ('NM_MUNICIPIO', lambda dados: dados['municipio']),  # String
    ('COD_US', lambda dados: dados['cdUs']),  # Double
    ('COD_IMOVEL', lambda dados: dados['cdImovel']),  # String
    ('COD_IMOVEL_NUM', lambda dados: dados['cdImovel']),  # Double
    ('COD_SERVICO', lambda dados: dados['cdServicoAbertura']),  # Double
    ('DESCRICAO_SERVICO', lambda dados: dados['dsServicoAbertura']),  # String
    ('DT_ABERTURA_OS', lambda dados: to_date(dados['dtAberturaOs'])),  # Date
    ('DT_FINAL_EXECUCAO_OS', lambda dados: to_date(dados['dtEncerramentoOs'])),  # Date
    ('DT_ENCERRAMENTO_OS', lambda dados: to_date(dados['dtEncerramentoOs'])),  # Date
    ('NOME_LOGRD', lambda dados: dados['nmLogradouro']),  # String
    ('LATITUDE', lambda dados: dados['vlLatitude']),  # Double
    ('LONGITUDE', lambda dados: dados['vlLongitude']),  # Double
    ('COD_ABERTURA_OS', lambda dados: dados['cdOsAbertura']),
    ('COD_ENCERRAMENTO_OS', lambda dados: dados['cdOsEncerramento']),
    ('COD_SERVICO_ENCERRAMENTO', lambda dados: dados['cdServicoEncerrramento']),
    # ('OBSERVACAO', lambda dados: dados['OBSERVACAO']),  # String

    # CAMPOS ADD VIA VALIDACAO
    ('COD_DESC_SERVICO_ENCERRAMENTO', lambda dados: dados['COD_DESC_SERVICO_ENCERRAMENTOS']),
    ('TEMPO_ATENDIMENTO', lambda dados: dados['TEMPO_ATENDIMENTO']),  # Double
    ('FLAG_LOCALIZACAO_OS', lambda dados: dados['FLAG_LOCALIZACAO_OS']),  # SmallInteger
    ('ESPACIALIZACAO', lambda dados: dados['ESPACIALIZACAO']),  # SmallInteger
    ('SHAPE@', lambda dados: dados['geom']),  # Geometry
))


CODS_IBGE = OrderedDict((
    (4300034, U"ACEGUÁ"),
    (4300059, U"ÁGUA SANTA"),
    (4300109, U"AGUDO"),
    (4300208, U"AJURICABA"),
    (4300307, U"ALECRIM"),
    (4300406, U"ALEGRETE"),
    (4300505, U"ALPESTRE"),
    (4300554, U"ALTO ALEGRE"),
    (4300604, U"ALVORADA"),
    (4300638, U"AMARAL FERRADOR"),
    (4300646, U"AMETISTA DO SUL"),
    (4300802, U"ANTÔNIO PRADO"),
    (4300851, U"ARAMBARÉ"),
    (4300901, U"ARATIBA"),
    (4301008, U"ARROIO DO MEIO"),
    (4301057, U"ARROIO DO SAL"),
    (4301206, U"ARROIO DO TIGRE"),
    (4301107, U"ARROIO DOS RATOS"),
    (4301305, U"ARROIO GRANDE"),
    (4301404, U"ARVOREZINHA"),
    (4301552, U"ÁUREA"),
    (4301636, U"BALNEÁRIO PINHAL"),
    (4301651, U"BARÃO"),
    (4301701, U"BARÃO DE COTEGIPE"),
    (4301750, U"BARÃO DO TRIUNFO"),
    (4301859, U"BARRA DO GUARITA"),
    (4301875, U"BARRA DO QUARAÍ"),
    (4301909, U"BARRA DO RIBEIRO"),
    (4301800, U"BARRACÃO"),
    (4302006, U"BARROS CASSAL"),
    (4302105, U"BENTO GONÇALVES"),
    (4302204, U"BOA VISTA DO BURICÁ"),
    (4302303, U"BOM JESUS"),
    (4302378, U"BOM PROGRESSO"),
    (4302402, U"BOM RETIRO DO SUL"),
    (4302451, U"BOQUEIRÃO DO LEÃO"),
    (4302501, U"BOSSOROCA"),
    (4302600, U"BRAGA"),
    (4302709, U"BUTIÁ"),
    (4302808, U"CAÇAPAVA DO SUL"),
    (4302907, U"CACEQUI"),
    (4303004, U"CACHOEIRA DO SUL"),
    (4303103, U"CACHOEIRINHA"),
    (4303202, U"CACIQUE DOBLE"),
    (4303301, U"CAIBATÉ"),
    (4303400, U"CAIÇARA"),
    (4303509, U"CAMAQUÃ"),
    (4303608, U"CAMBARÁ DO SUL"),
    (4303673, U"CAMPESTRE DA SERRA"),
    (4303707, U"CAMPINA DAS MISSÕES"),
    (4303806, U"CAMPINAS DO SUL"),
    (4303905, U"CAMPO BOM"),
    (4304002, U"CAMPO NOVO"),
    (4304101, U"CAMPOS BORGES"),
    (4304200, U"CANDELÁRIA"),
    (4304309, U"CÂNDIDO GODÓI"),
    (4304408, U"CANELA"),
    (4304507, U"CANGUÇU"),
    (4304606, U"CANOAS"),
    (4304630, U"CAPÃO DA CANOA"),
    (4304663, U"CAPÃO DO LEÃO"),
    (4304689, U"CAPELA DE SANTANA"),
    (4304671, U"CAPIVARI DO SUL"),
    (4304705, U"CARAZINHO"),
    (4304804, U"CARLOS BARBOSA"),
    (4304903, U"CASCA"),
    (4304952, U"CASEIROS"),
    (4305009, U"CATUÍPE"),
    (4305124, U"CERRITO"),
    (4305173, U"CERRO GRANDE DO SUL"),
    (4305207, U"CERRO LARGO"),
    (4305306, U"CHAPADA"),
    (4305355, U"CHARQUEADAS"),
    (4305405, U"CHIAPETTA"),
    (4305439, U"CHUÍ"),
    (4305447, U"CHUVISCA"),
    (4305454, U"CIDREIRA"),
    (4305504, U"CIRÍACO"),
    (4305603, U"COLORADO"),
    (4305702, U"CONDOR"),
    (4305801, U"CONSTANTINA"),
    (4305900, U"CORONEL BICACO"),
    (4305959, U"COTIPORÃ"),
    (4306007, U"CRISSIUMAL"),
    (4306056, U"CRISTAL"),
    (4306106, U"CRUZ ALTA"),
    (4306205, U"CRUZEIRO DO SUL"),
    (4306304, U"DAVID CANABARRO"),
    (4306320, U"DERRUBADAS"),
    (4306379, U"DILERMANDO DE AGUIAR"),
    (4306403, U"DOIS IRMÃOS"),
    (4306502, U"DOM FELICIANO"),
    (4306601, U"DOM PEDRITO"),
    (4306700, U"DONA FRANCISCA"),
    (4306734, U"DOUTOR MAURÍCIO CARDOSO"),
    (4306767, U"ELDORADO DO SUL"),
    (4306809, U"ENCANTADO"),
    (4306908, U"ENCRUZILHADA DO SUL"),
    (4306957, U"ENTRE RIOS DO SUL"),
    (4306932, U"ENTRE-IJUÍS"),
    (4306973, U"EREBANGO"),
    (4307005, U"ERECHIM"),
    (4307203, U"ERVAL GRANDE"),
    (4307302, U"ERVAL SECO"),
    (4307401, U"ESMERALDA"),
    (4307500, U"ESPUMOSO"),
    (4307559, U"ESTAÇÃO"),
    (4307609, U"ESTÂNCIA VELHA"),
    (4307708, U"ESTEIO"),
    (4307807, U"ESTRELA"),
    (4307864, U"FAGUNDES VARELA"),
    (4307906, U"FARROUPILHA"),
    (4308003, U"FAXINAL DO SOTURNO"),
    (4308052, U"FAXINALZINHO"),
    (4308102, U"FELIZ"),
    (4308201, U"FLORES DA CUNHA"),
    (4308300, U"FONTOURA XAVIER"),
    (4308409, U"FORMIGUEIRO"),
    (4308458, U"FORTALEZA DOS VALOS"),
    (4308508, U"FREDERICO WESTPHALEN"),
    (4308607, U"GARIBALDI"),
    (4308706, U"GAURAMA"),
    (4308805, U"GENERAL CÂMARA"),
    (4308904, U"GETÚLIO VARGAS"),
    (4309001, U"GIRUÁ"),
    (4309050, U"GLORINHA"),
    (4309100, U"GRAMADO"),
    (4309209, U"GRAVATAÍ"),
    (4309308, U"GUAÍBA"),
    (4309407, U"GUAPORÉ"),
    (4309506, U"GUARANI DAS MISSÕES"),
    (4307104, U"HERVAL"),
    (4309605, U"HORIZONTINA"),
    (4309704, U"HUMAITÁ"),
    (4309803, U"IBIAÇÁ"),
    (4309902, U"IBIRAIARAS"),
    (4310009, U"IBIRUBÁ"),
    (4310108, U"IGREJINHA"),
    (4310207, U"IJUÍ"),
    (4310306, U"ILÓPOLIS"),
    (4310330, U"IMBÉ"),
    (4310405, U"INDEPENDÊNCIA"),
    (4310439, U"IPÊ"),
    (4310504, U"IRAÍ"),
    (4310538, U"ITAARA"),
    (4310579, U"ITAPUCA"),
    (4310603, U"ITAQUI"),
    (4310702, U"ITATIBA DO SUL"),
    (4310751, U"IVORÁ"),
    (4310850, U"JABOTICABA"),
    (4310900, U"JACUTINGA"),
    (4311007, U"JAGUARÃO"),
    (4311106, U"JAGUARI"),
    (4311122, U"JAQUIRANA"),
    (4311205, U"JÚLIO DE CASTILHOS"),
    (4311239, U"LAGOA BONITA DO SUL"),
    (4311304, U"LAGOA VERMELHA"),
    (4311254, U"LAGOÃO"),
    (4311403, U"LAJEADO"),
    (4311502, U"LAVRAS DO SUL"),
    (4311601, U"LIBERATO SALZANO"),
    (4311718, U"MAÇAMBARÁ"),
    (4311700, U"MACHADINHO"),
    (4311759, U"MANOEL VIANA"),
    (4311809, U"MARAU"),
    (4311908, U"MARCELINO RAMOS"),
    (4311981, U"MARIANA PIMENTEL"),
    (4312005, U"MARIANO MORO"),
    (4312054, U"MARQUES DE SOUZA"),
    (4312104, U"MATA"),
    (4312203, U"MAXIMILIANO DE ALMEIDA"),
    (4312252, U"MINAS DO LEÃO"),
    (4312302, U"MIRAGUAÍ"),
    (4312401, U"MONTENEGRO"),
    (4312450, U"MORRO REDONDO"),
    (4312476, U"MORRO REUTER"),
    (4312500, U"MOSTARDAS"),
    (4312617, U"MUITOS CAPÕES"),
    (4312658, U"NÃO-ME-TOQUE"),
    (4312708, U"NONOAI"),
    (4312807, U"NOVA ARAÇÁ"),
    (4312906, U"NOVA BASSANO"),
    (4313003, U"NOVA BRÉSCIA"),
    (4313037, U"NOVA ESPERANÇA DO SUL"),
    (4313102, U"NOVA PALMA"),
    (4313201, U"NOVA PETRÓPOLIS"),
    (4313300, U"NOVA PRATA"),
    (4313359, U"NOVA ROMA DO SUL"),
    (4313375, U"NOVA SANTA RITA"),
    (4313508, U"OSÓRIO"),
    (4313607, U"PAIM FILHO"),
    (4313656, U"PALMARES DO SUL"),
    (4313706, U"PALMEIRA DAS MISSÕES"),
    (4313805, U"PALMITINHO"),
    (4313904, U"PANAMBI"),
    (4313953, U"PANTANO GRANDE"),
    (4314001, U"PARAÍ"),
    (4314050, U"PAROBÉ"),
    (4314068, U"PASSA SETE"),
    (4314100, U"PASSO FUNDO"),
    (4314159, U"PAVERAMA"),
    (4314175, U"PEDRAS ALTAS"),
    (4314209, U"PEDRO OSÓRIO"),
    (4314308, U"PEJUÇARA"),
    (4314498, U"PINHEIRINHO DO VALE"),
    (4314506, U"PINHEIRO MACHADO"),
    (4314605, U"PIRATINI"),
    (4314704, U"PLANALTO"),
    (4314803, U"PORTÃO"),
    (4315008, U"PORTO LUCENA"),
    (4315073, U"PORTO VERA CRUZ"),
    (4315107, U"PORTO XAVIER"),
    (4315206, U"PUTINGA"),
    (4315305, U"QUARAÍ"),
    (4315404, U"REDENTORA"),
    (4315503, U"RESTINGA SECA"),
    (4315552, U"RIO DOS ÍNDIOS"),
    (4315602, U"RIO GRANDE"),
    (4315701, U"RIO PARDO"),
    (4315750, U"RIOZINHO"),
    (4315800, U"ROCA SALES"),
    (4315909, U"RODEIO BONITO"),
    (4316006, U"ROLANTE"),
    (4316105, U"RONDA ALTA"),
    (4316204, U"RONDINHA"),
    (4316402, U"ROSÁRIO DO SUL"),
    (4316451, U"SALTO DO JACUÍ"),
    (4316501, U"SALVADOR DO SUL"),
    (4316600, U"SANANDUVA"),
    (4316709, U"SANTA BÁRBARA DO SUL"),
    (4316808, U"SANTA CRUZ DO SUL"),
    (4316972, U"SANTA MARGARIDA DO SUL"),
    (4316907, U"SANTA MARIA"),
    (4316956, U"SANTA MARIA DO HERVAL"),
    (4317202, U"SANTA ROSA"),
    (4317301, U"SANTA VITÓRIA DO PALMAR"),
    (4317004, U"SANTANA DA BOA VISTA"),
    (4317400, U"SANTIAGO"),
    (4317509, U"SANTO ÂNGELO"),
    (4317608, U"SANTO ANTÔNIO DA PATRULHA"),
    (4317707, U"SANTO ANTÔNIO DAS MISSÕES"),
    (4317806, U"SANTO AUGUSTO"),
    (4317905, U"SANTO CRISTO"),
    (4317954, U"SANTO EXPEDITO DO SUL"),
    (4318002, U"SÃO BORJA"),
    (4318101, U"SÃO FRANCISCO DE ASSIS"),
    (4318200, U"SÃO FRANCISCO DE PAULA"),
    (4318408, U"SÃO JERÔNIMO"),
    (4318424, U"SÃO JOÃO DA URTIGA"),
    (4318440, U"SÃO JORGE"),
    (4318465, U"SÃO JOSÉ DO HERVAL"),
    (4318499, U"SÃO JOSÉ DO INHACORÁ"),
    (4318507, U"SÃO JOSÉ DO NORTE"),
    (4318606, U"SÃO JOSÉ DO OURO"),
    (4318622, U"SÃO JOSÉ DOS AUSENTES"),
    (4318804, U"SÃO LOURENÇO DO SUL"),
    (4318903, U"SÃO LUIZ GONZAGA"),
    (4319000, U"SÃO MARCOS"),
    (4319109, U"SÃO MARTINHO"),
    (4319158, U"SÃO MIGUEL DAS MISSÕES"),
    (4319208, U"SÃO NICOLAU"),
    (4319356, U"SÃO PEDRO DA SERRA"),
    (4319406, U"SÃO PEDRO DO SUL"),
    (4319505, U"SÃO SEBASTIÃO DO CAÍ"),
    (4319604, U"SÃO SEPÉ"),
    (4319703, U"SÃO VALENTIM"),
    (4319802, U"SÃO VICENTE DO SUL"),
    (4319901, U"SAPIRANGA"),
    (4320008, U"SAPUCAIA DO SUL"),
    (4320107, U"SARANDI"),
    (4320206, U"SEBERI"),
    (4320230, U"SEDE NOVA"),
    (4320305, U"SELBACH"),
    (4320354, U"SENTINELA DO SUL"),
    (4320404, U"SERAFINA CORRÊA"),
    (4320503, U"SERTÃO"),
    (4320552, U"SERTÃO SANTANA"),
    (4320602, U"SEVERIANO DE ALMEIDA"),
    (4320651, U"SILVEIRA MARTINS"),
    (4320701, U"SOBRADINHO"),
    (4320800, U"SOLEDADE"),
    (4320909, U"TAPEJARA"),
    (4321006, U"TAPERA"),
    (4321105, U"TAPES"),
    (4321204, U"TAQUARA"),
    (4321303, U"TAQUARI"),
    (4321329, U"TAQUARUÇU DO SUL"),
    (4321352, U"TAVARES"),
    (4321402, U"TENENTE PORTELA"),
    (4321436, U"TERRA DE AREIA"),
    (4321477, U"TIRADENTES DO SUL"),
    (4321501, U"TORRES"),
    (4321600, U"TRAMANDAÍ"),
    (4321667, U"TRÊS CACHOEIRAS"),
    (4321709, U"TRÊS COROAS"),
    (4321808, U"TRÊS DE MAIO"),
    (4321907, U"TRÊS PASSOS"),
    (4321956, U"TRINDADE DO SUL"),
    (4322004, U"TRIUNFO"),
    (4322103, U"TUCUNDUVA"),
    (4322202, U"TUPANCIRETÃ"),
    (4322301, U"TUPARENDI"),
    (4322376, U"UNISTALDA"),
    (4322509, U"VACARIA"),
    (4322608, U"VENÂNCIO AIRES"),
    (4322806, U"VERANÓPOLIS"),
    (4322905, U"VIADUTOS"),
    (4323002, U"VIAMÃO"),
    (4323101, U"VICENTE DUTRA"),
    (4323200, U"VICTOR GRAEFF"),
    (4323309, U"VILA FLORES"),
    (4323457, U"VILA NOVA DO SUL"),
    (4323507, U"VISTA ALEGRE"),
    (4323705, U"VISTA GAÚCHA"),
    (4323804, U"XANGRI-LÁ"),
))

DOMINIOS_ENCERRAMENTO = {
    37: u"Abertura Registro de Rede6",
    860: u"Acompanhamento e Serviços Prestados",
    194: u"Adequação de Nicho",
    618: u"Alvenarias",
    410: u"Ampliação de Rede de Água",
    6180: u"Ampliação de Rede Esgoto",
    3811: u"Análise de Efluentes - Aterro Sanitário",
    2002: u"Aprovação do Orçamento da Limpeza de Fossa",
    2005: u"Aprovação orçamento continuidade da Limpeza Fossa",
    624: u"Armaduras",
    416: u"Assentamento Tubo Ceramico Junta Asfática",
    419: u"Assentamento Tubo Ceramico Junta Cerâmica Elastica",
    417: u"Assentamento Tubo de  Concreto Junta Elástica",
    413: u"Assentamento Tubo de Ferro Fundido Junta Elástica",
    415: u"Assentamento Tubos de PVC Junta Elástica",
    630: u"Avaliação do Serviço",
    786: u"Bloco de ancoragem",
    616: u"Caixas e Poços",
    210: u"Caminhão Pipa",
    238: u"Caminhão Pipa - Abastecimento Emergencial",
    224: u"Capeamento de Rede de Água",
    2025: u"Coleta Dados Embalagem HD",
    880: u"Coleta de Água para Análise",
    228: u"Coleta de Esgoto em Fossa Séptica Coletiva",
    226: u"Coleta de Esgoto em Sumidouro",
    394: u"Coletar dados da Caixa de Inspeção",
    391: u"Coletar dados da rede de água",
    392: u"Coletar Dados da Rede de Esgoto",
    622: u"Concreto",
    223: u"Cons.Vaz. Adutora Água Bruta-Causado por Terceiros",
    351: u"Conserto de Adutora de Água Bruta",
    350: u"Conserto de Adutora de Água Tratada",
    792: u"Conserto de Rede Pluvial",
    219: u"Conserto de Vazamento Adutora Água Bruta",
    218: u"Conserto de Vazamento Adutora Água Tratada",
    9001: u"Conserto de Vazamento em Rede de Água",
    120: u"Conserto de Vazamento no Quadro",
    217: u"Conserto de Vazamento Ramal",
    216: u"Conserto de Vazamento Rede de Água",
    759: u"Conserto Dispositivos de Rede",
    805: u"Conserto e/ou Manutenção de Chuveiro Público",
    220: u"Conserto Vaz.  Rede Água - Causado por Terceiros",
    222: u"Conserto Vaz. Adutora Água - Causado por Terceiros",
    221: u"Conserto Vaz. Ramal Água - Causado por Terceiros",
    201: u"Conserto Vazamento de Ramal de Água",
    6050: u"Conserto Vazamento de Ramal Esgoto",
    6070: u"Conserto Vazamento na Rede Esgoto",
    215: u"Conserto Vazamento Rede de Água",
    749: u"Construção de Caixa de Proteção",
    6004: u"Dados do Ramal de Esgoto",
    6005: u"Dados do Ramal Intradomiciliar de Esgoto",
    626: u"Demolições",
    6302: u"Desassoreamento e Limpeza de Caixa em EBE",
    6301: u"Desassoreamento e Limpeza de Poço de Sucção",
    6303: u"Desassoreamento e Limpeza em ETE",
    199: u"Deslocamento Caminhão Caçamba",
    204: u"Deslocamento Caminhão Pipa",
    203: u"Deslocamento Escavadeira Hidraulica",
    205: u"Deslocamento Mini Escavadeira",
    198: u"Deslocamento Retroescavadeira",
    9000: u"Deslocamento/Viagem Equipamento TESTE",
    6136: u"Desobstrução de Ramal de Esgoto",
    6134: u"Desobstrução Rede de Esgoto",
    3808: u"Ensaio para Particulares - Água (DEAL)",
    3807: u"Ensaio para Particulares - Água (ETA)",
    3809: u"Ensaio para Particulares - Esgoto (ETE)",
    3810: u"Ensaio para Particulares - Esgoto (LABCES)",
    8001: u"Entrega de Aviso de Manobra",
    8000: u"Entrega de Aviso de Suspensão",
    779: u"Escavação de Rocha Branda Localizada a Frio",
    782: u"Escavação de Rocha Branda Valas",
    780: u"Escavação de Rocha Dura Localizada a Fogo",
    783: u"Escavação de Rocha Dura Valas",
    778: u"Escavação de Solo Localizada Manual",
    784: u"Escavação de Solo Localizada Mecânica",
    781: u"Escavação de Solo Valas Manual",
    785: u"Escavação de Solo Valas Mecânica",
    775: u"Escoramento de Vala",
    774: u"Esgotamento",
    776: u"Esgotamento com bombas",
    291: u"Excução Ramal Água - MND",
    793: u"Execução de Bloco de Ancoragem",
    611: u"Execução de IT - Inspeção Tubular",
    2001: u"Execução de limpeza de fossa",
    1517: u"Execução de Limpeza de Fossas",
    192: u"Execução de Nicho",
    6200: u"Execução de PV - Poço de Visita",
    182: u"Execução Ramal Água",
    290: u"Execução Ramal Água - VALA",
    6003: u"Execução Ramal Esgoto",
    794: u"Execução/interligação Ramal Predial à Cx Inspeção",
    170: u"Expurgo de Água no Quadro",
    295: u"Expurgo de Água no Ramal",
    390: u"Expurgo de Água Pela Rede Distribuidora",
    297: u"Expurgos (Limpeza de Rede/Ramal)",
    375: u"Fechamento Registro de Rede",
    701: u"Fiscalização da Repavimentação de Rua",
    703: u"Fiscalização da Repavimentação Passeio",
    251: u"Fiscalização Final Esgoto Conectado",
    244: u"Fiscalização Ligação Intradomiciliar",
    628: u"Formas e Cimbramentos",
    3800: u"G1 - ETA (Ensaio para Particulares)",
    3802: u"G1 - ETE (Ensaios para Particulares)",
    3806: u"G2 - Ensaio para Outorga de Poços",
    3801: u"G2 - ETA (Ensaios para Particulares)",
    3803: u"G2 - ETE (Ensaios para Particulares)",
    3805: u"G2 - LABCES (Ensaios para Particulares)",
    3804: u"G2 DEAL (Ensaio para Particulares)",
    241: u"Informação de leitura atual",
    261: u"Informação vazamento gera consumo",
    604: u"Inslatação Equipamento Medição",
    6198: u"Inspeção de Esgotamento Indevido",
    195: u"Instalação de Caixa Padrão em Nicho",
    597: u"Instalação de Dispositivo de Rede",
    2010: u"Instalação de Hidrômetro",
    180: u"Instalação de Lacre nas Conexões do Quadro",
    595: u"Instalação de Macromedidor",
    160: u"Instalação de Quadro",
    940: u"Instalação de Registrador de Pressão",
    594: u"Instalação de VRP",
    125: u"Instalação do Registro no Quadro",
    450: u"Interligação de Rede de Água",
    791: u"Interligação Ramal Esgoto à Caixa de Inspeção",
    838: u"Interrupção do abastecimento estado de calamidade",
    839: u"Interrupção do abastecimento por ato de terceiros",
    840: u"Interrupção do serv de abast de água - Fortuito",
    826: u"Interrupção do serviço de abastecimento de água",
    837: u"Interrupção programada do serviço de abastecimento",
    788: u"Lançamento de tubulação - Método Não Destrutivo",
    789: u"Lançamento de tubulação em Estrutura Portante",
    790: u"Lançamento de tubulação Sub Aquatica",
    196: u"Leitura de Poços",
    252: u"Leitura de Poços e Macromedidores",
    7601: u"Ligação de Água 3/4 com Pavimento",
    7600: u"Ligação de Água 3/4 sem Pavimento",
    7603: u"Ligação de Água Maior 3/4 com Pavimento",
    7602: u"Ligação de Água Maior 3/4 sem Pavimento",
    243: u"Ligação de Esgoto Intradomiciliar",
    2004: u"Limpar sujeira",
    2003: u"Limpeza da fossa",
    282: u"Limpeza e Desobstrução de ramal predial DN>150",
    229: u"Limpeza e Desobstrução de Rede coletora DN até 200",
    230: u"Limpeza e Desobstrução de Rede coletora DN>200",
    6202: u"Limpeza e desobstrução manual de PV'S e PI'S",
    279: u"Limpeza e Desobstrução manual PV'S e IT'S",
    747: u"Limpeza e Remoção de Entulho na Via Pública",
    881: u"Limpeza nos Crivos da Captação",
    615: u"Locação e Nivelamento Ramal Esgoto",
    412: u"Locação para obras de condutos forçados",
    418: u"Locação para obras de condutos livres",
    374: u"Manobras de Registro de Rede",
    796: u"Manutenção Caixa de Inspeção",
    751: u"Manutenção de Caixa de Proteção",
    227: u"Manutenção de Caixa de Proteção",
    593: u"Manutenção de Macromedidor",
    6201: u"Manutenção de PV e IT (Esgoto)",
    592: u"Manutenção de VRP",
    601: u"Manutenção Dispositivos de Rede",
    1052: u"Medição de Área e Pontos de Água",
    1096: u"Medição de Área e Pontos de água de Beneficiário",
    956: u"Medição de Pressão",
    957: u"Medição de Pressão Final",
    955: u"Medição de Pressão na Rede",
    612: u"Medição de Vazão",
    600: u"Montagem / Recolocação de tampão de ferro para IT",
    609: u"Montagem / Recolocação de tampão de ferro para PV",
    6197: u"Montagem de Caixa de Inspeção para Ramal Esgoto",
    795: u"Montagem de Caixa de Inspeção para Ramal Esgoto",
    608: u"Montagem de pré-moldados de concreto para PV",
    145: u"Mudança de Local do Quadro com Material",
    150: u"Mudança de Local do Quadro sem Material",
    287: u"Mudança Local do Ramal com Pavimento",
    286: u"Mudança Local do Ramal sem Pavimento",
    0: u"Não informado",
    240: u"Orçamento Ligação de Esgoto Intradomiciliar",
    140: u"Padronização do Quadro",
    892: u"Passagem de PIG",
    746: u"Reaterro",
    284: u"Rebaixamento de Ramal",
    777: u"Rebaixamento Lençol Freático",
    745: u"Recomposição de Base para Pavimentos",
    617: u"Recuperação de Tampão - PV e IT",
    627: u"Recuperação Estrutura - PV e IT",
    613: u"Recuperação Fundos Almofadas - PV e IT",
    607: u"Registro de Leituras",
    262: u"REGISTRO SITUAÇÃO ANTERIOR A EXECUÇÃO",
    2125: u"Regularizar Posição do Hidrômetro",
    5030: u"Religação do Corte à Pedido",
    5020: u"Religação no Quadro com Tampão",
    5025: u"Religação no Quadro com Trava  Retentora",
    5040: u"Religação no Ramal com Tampão",
    5045: u"Religação no Ramal com Trava Retentora",
    411: u"Remanejamento de Interferência Rede Água",
    591: u"Remoção de Macromedidor",
    705: u"Remoção de Pavimento Passeio",
    704: u"Remoção de Pavimento Rua",
    621: u"Remoção de Trecho danificado",
    590: u"Remoção de VRP",
    614: u"Reparo Caixa de Inspeção",
    787: u"Reparos em Muros e Paredes de Alvenaria",
    699: u"Repavimentação",
    702: u"Repavimentação Passeio",
    700: u"Repavimetação Rua",
    193: u"Restauração de Nicho",
    598: u"Retirada de Dispositivo de Rede",
    2020: u"Retirada de Hidrômetro",
    161: u"Retirada de Lacres do Quadro",
    135: u"Retirada de Quadro",
    945: u"Retirada de Registrador de Pressão",
    299: u"Retirada Derivação/Intervenção Ramal",
    4066: u"Retirada do Ramal",
    126: u"Retirada do Registro do Quadro",
    606: u"Retirada Equipamento Medição",
    629: u"Revestimentos e Tratamento de Superfícies",
    1050: u"Revisão Cadastral",
    1053: u"Revisão Cadastral Alteração de Titularidade",
    1051: u"Revisão de Categorias/Economias",
    200: u"Serviço de Conserto Vazamento de Ramal",
    750: u"Serviço de Construção de Caixa de Proteção",
    6155: u"Serviço de Desobstrução Ramal Esgoto",
    6145: u"Serviço de Desobstrução Rede Esgoto",
    6135: u"Serviço de Desobstrução Rede/Ramal Esgoto",
    894: u"Serviço de Draga",
    599: u"Serviço de Instalação de Dispositivos de Rede",
    893: u"Serviço de Mergulho",
    277: u"Serviço de Pintura",
    980: u"Serviço de Pitometria",
    285: u"Serviço de Rebaixamento Ramal",
    603: u"Serviço de Retirada Dispositivos de Rede",
    6196: u"Serviço de Vistoria nas Instalações de Esgoto",
    950: u"Serviços de Geofonia",
    596: u"Serviços Dispositivo de Rede",
    890: u"Serviços na EBE",
    885: u"Serviços na ETA",
    887: u"Serviços na ETE",
    895: u"Sinalização na Via Pública ou Passeio",
    7002: u"Somente Conexão Com a Rede",
    610: u"Subsituição de Equipamento de Medição",
    6548: u"Substituição Caixa de Inspeção",
    2030: u"Substituição de Hidrômetro",
    185: u"Substituição de Lacres nas Conexões do Quadro",
    176: u"Substituição de Limitador de Vazão",
    6140: u"Substituição de Ramal de Esgoto",
    360: u"Substituição de Rede de Água",
    6160: u"Substituição de Rede Esgoto",
    602: u"Substituição Dispositivos de Rede",
    130: u"Substituição do Quadro",
    281: u"Substituição do Ramal de Esgoto",
    127: u"Substituição do Registro do Quadro",
    275: u"Substituição Parcial do Ramal",
    6210: u"Substituição Tampa Caixa de Inspeção",
    280: u"Substituição Total do Ramal",
    4070: u"Supressão Ligação de Água",
    4065: u"Supressão Ramal Suprimido ou Sem Instal. Violado",
    4030: u"Suspensão a Pedido do Usuário",
    4020: u"Suspensão no Quadro com Tampão",
    4025: u"Suspensão no Quadro com Trava Retentora",
    4040: u"Suspensão no Ramal com Tampão",
    4045: u"Suspensão no Ramal com Trava Retentora",
    4145: u"Suspensão/Supressão em Vigor",
    202: u"Uso Retro / Caminhão Caçamba",
    830: u"Verificação  Falta de Água - Imóvel",
    821: u"Verificação da Qualidade da Água No Imóvel",
    1510: u"Verificação de Consumo Excessivo",
    835: u"Verificação de Falta de Água-Geral",
    850: u"Verificação de Falta de Pressão - Imóvel",
    2408: u"Verificação do Nº HD/Leitura/Lacre",
    2407: u"Verificação do Numero Hidrômetro e Leitura",
    400: u"Vistoria Ampliação/Substituição de Rede de Água",
    6179: u"Vistoria Ampliação/Substituição Rede Esgoto",
    6002: u"Vistoria da Conexão de Esgoto Intradomiciliar",
    708: u"Vistoria Dados Pavimento",
    1515: u"Vistoria de Dados do Imóvel",
    851: u"Vistoria de Excesso de Pressão - Imóvel",
    7004: u"Vistoria de Ligação de Água",
    7000: u"Vistoria de Ligação de Água e/ou Esgoto",
    2000: u"Vistoria de limpeza de fossa",
    2409: u"Vistoria do Lacre do Quadro",
    260: u"Vistoria Final de Falta de Água em Imóvel",
    7001: u"Vistoria Ligação de Água",
    8010: u"Vistoria nas instalações da ETA/ETE/EBE/EBA",
    6195: u"Vistoria nas Instalações de Esgoto",
    8020: u"Vistoria nas instalações na ETE/EBE",
    1512: u"Vistoria nas Instalações para Redução Autorizada",
    245: u"Vistoria no Ramal Intradomicilar de Esgoto",
    1097: u"Vistoria para Concessão de Benefício Social",
    7613: u"Vistoria para Instalação de Telemetria",
    7003: u"Vistoria para Ligação de Esgoto",
    1516: u"Vistoria para Limpeza de Fossa Séptica",
    1513: u"Vistoria para Suspensão a Pedido do Usuário",
    6194: u"Vistoria Situação Sanitária Imóvel",
    7608: u"Vistoria Vazamento + Conserto Adutora Água Bruta",
    7607: u"Vistoria Vazamento + Conserto Adutora Água Tratada",
    7606: u"Vistoria Vazamento + Conserto Ramal Água",
    7610: u"Vistoria Vazamento + Conserto Ramal Esgoto",
    7605: u"Vistoria Vazamento + Conserto Rede Água",
    7609: u"Vistoria Vazamento + Conserto Rede Esgoto",
    7611: u"Vistoria Vazamento Água",
    1514: u"Vistoria Vazamento Água p/ Red Autorizada",
    1511: u"Vistoria Vazamento de Água",
    7612: u"Vistoria Vazamento Esgoto",
    248: u"Vistoriar Esgoto"
}
