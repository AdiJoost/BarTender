
from bson import ObjectId
from config.configFiles import ConfigFiles
from config.configManager import getConfig
from config.mongoDBConfig.mongoDbConfigFields import MongoDBConfigFields
from src.models.baseModel import BaseModel

class GlasModel(BaseModel):

    COLLECTION_NAME = getConfig(MongoDBConfigFields.GLAS_COLLECTION_NAME.value, ConfigFiles.MONGO_DB_CONFIG)
    GLAS_NAME_FIELD_NAME = "name"
    PICTURE_FIELD_NAME = "picture"
    VOLUME_FIELD_NAME = "volume"

    def __init__(self, name: str, picture: str, volume: float, _id: ObjectId=None):
        self._id = _id
        self._name = name
        self._picture = picture
        self._volume = volume

    def getName(self) -> str:
        return self._name
    
    def setName(self, name: str) -> None:
        self._name = name

    def getpicture(self) -> str:
        return self._picture
    
    def setName(self, picture: str) -> None:
        self._picture = picture

    def getVolume(self) -> float:
        return self._volume
    
    def setName(self, volume: float) -> None:
        self._volume = volume

    def toJson(self) -> dict:
        values = {
            self.GLAS_NAME_FIELD_NAME: self._name,
            self.PICTURE_FIELD_NAME: self._picture,
            self.VOLUME_FIELD_NAME: self._volume
        }
        return self.addIdToJson(values)
