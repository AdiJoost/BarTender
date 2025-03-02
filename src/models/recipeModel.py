from bson import ObjectId
from typing import Union

from config.configFiles import ConfigFiles
from config.configManager import getConfig
from config.mongoDBConfig.mongoDbConfigFields import MongoDBConfigFields
from src.adapters.database_utils import getOnlyAutomaticRecipes
from src.models.baseModel import BaseModel
from src.models.stepModel import StepModel

class RecipeModel(BaseModel):

    COLLECTION_NAME = getConfig(MongoDBConfigFields.RECIPE_COLLECTION_NAME.value, ConfigFiles.MONGO_DB_CONFIG)
    RECIPE_NAME_FIELD_NAME = "name"
    PICTURE_FIELD_NAME = "picture"
    STEPS_FIELD_NAME = "steps"

    def __init__(self, name: str, picture: str, steps: Union[list[StepModel], list[dict]], _id: ObjectId=None):
        self._id = _id
        self._name = name
        self._picture = picture
        self._steps = self._castToSteps(steps)

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
    
    @classmethod
    def getOnlyAutomatic(cls, limit: int, offset: int) -> list:
        result: list = getOnlyAutomaticRecipes(limit=limit, offset=offset, databaseName=cls.DATABASE_NAME, collectionName=cls.COLLECTION_NAME)
        if result is None:
            return None
        return [cls(**item) for item in result]
    
    def _castToSteps(self, steps: Union[list[StepModel], list[dict]]) -> list[StepModel]:
        if (all(isinstance(item, StepModel) for item in steps)):
            return steps
        try:
            return [StepModel(**item) for item in steps if isinstance(item, dict)]
        except Exception as e:
            raise ValueError(f"Could not cast to Step: -> {e}")