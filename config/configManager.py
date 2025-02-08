import json
import copy
from pathlib import Path
from config.rootPath import getRootPath
from config.configNames import ConfigNames

CONFIG_FOLDER = "config"


application_config = {}


with open(getRootPath().joinpath(CONFIG_FOLDER, "applicationConfig.json"), "r") as file:
    application_config = json.load(file)



def loadConfig():
    return "Hello"

def getConfig(name: str, config: ConfigNames=ConfigNames.APPLICATION_CONFIG) -> any:
    if config == ConfigNames.APPLICATION_CONFIG:
        return _getConfig(name, application_config)

def _getConfig(name:str, config: dict) -> any:
    return _returnCopy(config.get(name))

def _returnCopy(object) -> any:
    if object == None:
        return None
    if isinstance(object, list) or isinstance(object, dict):
        return copy.deepcopy(object)
    return object
    