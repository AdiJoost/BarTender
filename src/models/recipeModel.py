from bson import ObjectId
from config.configFiles import ConfigFiles
from config.configManager import getConfig
from config.mongoDBConfig.mongoDbConfigFields import MongoDBConfigFields
from src.models.baseModel import BaseModel
from src.models.stepModel import StepModel

class RecipeModel(BaseModel):

    COLLECTION_NAME = getConfig(MongoDBConfigFields.RECIPE_COLLECTION_NAME.value, ConfigFiles.MONGO_DB_CONFIG)
    RECIPE_NAME_FIELD_NAME = "name"
    PICTURE_FIELD_NAME = "picture"
    STEPS_FIELD_NAME = "steps"

    def __init__(self, name: str, picture: str, steps: list[StepModel], _id: ObjectId=None):
        self._name = name
        self._picture = picture
        self._steps = steps

    def getName(self) -> str:
        return self._name
    
    def setName(self, name: str) -> None:
        self._name = name

    def getPicture(self) -> str:
        return self._picture
    
    def setPicture(self, picture: str) -> None:
        self._picture = picture

    def getSteps(self) -> list[StepModel]:
        return self._steps
    
    def setSteps(self, steps: list[StepModel]) -> None:
        self._steps = steps

    def toJson(self) -> dict:
        values = {
            self.RECIPE_NAME_FIELD_NAME: self._name,
            self.PICTURE_FIELD_NAME: self._picture,
            self.STEPS_FIELD_NAME: [step.toJson() for step in self._steps]
        }
        return self.addIdToJson(values)