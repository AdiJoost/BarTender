from bson import ObjectId
from config.configFiles import ConfigFiles
from config.configManager import getConfig
from config.mongoDBConfig.mongoDbConfigFields import MongoDBConfigFields
from src.adapters.database_utils import deleteDocument, getDocumentById, saveDocument

class BaseModel():

    DATABASE_NAME = getConfig(MongoDBConfigFields.DATABASE_NAME.value, ConfigFiles.MONGO_DB_CONFIG)
    COLLECTION_NAME = None

    def getId(self) -> ObjectId:
        return self._id
    
    def setId(self, _id: ObjectId) -> None:
        self._id = _id

    def addIdToJson(self, values: dict) -> dict:
        if self._id is not None:
            values["_id"] = str(self._id)
        return values

    def save(self) -> None:
        upserResult: ObjectId = saveDocument(self.toJson(), databaseName=self.DATABASE_NAME, collectionName=self.COLLECTION_NAME)
        if upserResult is not None:
            self._id = upserResult
    
    @classmethod
    def get(cls, objectId: ObjectId):
        result: dict = getDocumentById(objectId, databaseName=cls.DATABASE_NAME, collectionName=cls.COLLECTION_NAME)
        if result is None:
            return None
        result["_id"] = objectId
        return cls(**result)
    
    @classmethod
    def delete(cls, objectId: ObjectId):
        deleteDocument(objectId, databaseName=cls.DATABASE_NAME, collectionName=cls.COLLECTION_NAME)