
import configparser

def getconfig():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    return config