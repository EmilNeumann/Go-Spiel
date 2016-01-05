'''
Created on 29.11.2015

@author: Emil
'''
import ConfigParser, os

def config_read():
    config = ConfigParser.ConfigParser()
    configfilepath = '../'+os.curdir+'/go.ini'
    config.read(configfilepath)
    return config

if __name__ == '__main__':
    print os.listdir(os.curdir)