# -*- coding: utf-8 -*-
import datetime
import os

import logging

def init(name, logPath):
    
    if not os.path.exists(logPath):
        os.makedirs(logPath)

    filename_log = logPath + '\\' + datetime.datetime.now().strftime("%Y-%m-%d")
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Here we define our formatter
    formatter = logging.Formatter(
        #fmt='%(asctime)s | %(levelname)-8s | %(name)-10s | %(lineno)-5s | %(funcName)-15s | %(message)s',
        #fmt='%(asctime)s | %(levelname)-8s | %(name)-10s | %(funcName)-15s | %(message)s',
        #fmt='%(asctime)s | %(levelname)-8s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    # create a file handler
    handler = logging.FileHandler(filename_log + "-info.log", "a", "utf-8")
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    #warning_handler = logging.FileHandler(filename_log + "-warning.log", "a", "utf-8")
    #warning_handler.setLevel(logging.WARNING)
    #warning_handler.setFormatter(formatter)

    #error_handler = logging.FileHandler(filename_log + "-error.log", "a", "utf-8")
    #error_handler.setLevel(logging.ERROR)
    #error_handler.setFormatter(formatter)

#    critical_handler = logging.FileHandler(filename_log + "-critical.log", "a", "utf-8")
#    critical_handler.setLevel(logging.CRITICAL)
#    critical_handler.setFormatter(formatter)

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    # add the handlers to the logger
    if not logger.handlers:
        logger.addHandler(handler)
        #logger.addHandler(warning_handler)
        #logger.addHandler(error_handler)
    #    logger.addHandler(critical_handler)
        logger.addHandler(console)
    return logger
def func():
    with open('C:\\Users\\Aluno\\Desktop\\garcia\\2019-11-27-info.log') as fj:
        print("jsodjso")

