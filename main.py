# -*- coding: utf-8 -*-

import os
import json
import sys

import arcpy
import requests

from datetime import datetime

from controller import main
from log import Log
import importlib;
importlib.reload(sys)


if __name__ == "__main__":

    dirpath = os.path.dirname(os.path.abspath(__file__))
    conf_filename = os.path.join(dirpath, 'conf.json')
    CONF = None
    with open(conf_filename) as json_file:
        CONF = json.load(json_file)

    DATA_ATUAL_STR = datetime.now().date().strftime('%d/%m/%Y')
    ini = datetime.now()
    log = Log(CONF['log_path'], CONF['log_file_name'])
    
    try:
        log.logger.info('INICIA INTEGRACAO OS')
        data_ini = CONF['ultima_data_atualizacao']
        
        main(log, data_ini, DATA_ATUAL_STR)
        CONF['ultima_data_atualizacao'] = DATA_ATUAL_STR
        with open(conf_filename, 'w+') as json_file:
            json_file.write(json.dumps(CONF, indent=4))
    except:
        log.logger.exception("")
