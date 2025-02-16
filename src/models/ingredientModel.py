from bson import ObjectId
from config.configFiles import ConfigFiles
from config.configManager import getConfig
from config.mongoDBConfig.mongoDbConfigFields import MongoDBConfigFields
from src.enums.controllerType import ControllerType
from src.models.baseModel import BaseModel

class IngredientModel(BaseModel):

    COLLECTION_NAME = getConfig(MongoDBConfigFields.INGREDIENTS_COLLECTION_NAME.value, ConfigFiles.MONGO_DB_CONFIG)
    INGREDIENT_NAME_FIELD_NAME = "name"
    CONTROLLER_TYPE_FIELD_NAME = "controller_type"
    PICTRUE_FIELD_NAME = "picture"
    DESCRIPTION_FIELD_NAME = "description"

    def __init__(self, name:str, controllerType: ControllerType, picture:str, description:str, _id: ObjectId=None) -> None:
        self._name = name
        self._controllerType = controllerType
        self._picture = picture
        self._description = description
        self._id = _id

    def getName(self) -> str:
        return self._name

    def setName(self, value) -> None:
        self._name = value

    def getControllerType(self) -> ControllerType:
        return self._controllerType

    def setControllerType(self, value: ControllerType) -> None:
        self._controllerType = value

    def getPicture(self) -> str:
        return self._picture

    def setPicture(self, value) -> None:
        self._picture = value

    def getDescription(self) -> str:
        return self._description

    def setDescription(self, value) -> None:
        self._description = value
