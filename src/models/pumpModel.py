from bson import ObjectId
from config.configFiles import ConfigFiles
from config.configManager import getConfig
from config.mongoDBConfig.mongoDbConfigFields import MongoDBConfigFields
from src.models.baseModel import BaseModel

class PumpModel(BaseModel):

    COLLECTION_NAME = getConfig(MongoDBConfigFields.PUMP_COLLECTION_NAME.value, ConfigFiles.MONGO_DB_CONFIG)
    INGREDIENT_FIELD_NAME = "ingredient"
    ML_PER_SECOND_FIELD_NAME = "ml_per_second"
    PIN_NUMBER_FIELD_NAME = "pin_number_field_name"
    PUMP_TYPE_FIELD_NAME = "pump_type"

    def __init__(self, ingredient: str, ml_per_second: float, pin_number_field_name: int, pump_type: str, _id: ObjectId=None):
        self._id = _id
        self._ingredient = ingredient
        self._mlPerSecond = ml_per_second
        self._pinNumber = pin_number_field_name
        self._pumpType = pump_type

    def getIngredient(self) -> str:
        return self._ingredient

    def setIngredient(self, value: str):
        self._ingredient = value

    def getMlPerSecond(self) -> float:
        return self._mlPerSecond

    def setMlPerSecond(self, value: float):
        self._mlPerSecond = value

    def getPinNumber(self) -> int:
        return self._pinNumber

    def setPinNumber(self, value: int):
        self._pinNumber = value

    def getPumpType(self) -> str:
        return self._pumpType

    def setPumpType(self, value: str):
        self._pumpType = value

    def toJson(self) -> dict:
        values = {
            self.INGREDIENT_FIELD_NAME: self._ingredient,
            self.ML_PER_SECOND_FIELD_NAME: self._mlPerSecond,
            self.PIN_NUMBER_FIELD_NAME: self._pinNumber,
            self.PUMP_TYPE_FIELD_NAME: self._pumpType
        }
        return self.addIdToJson(values)