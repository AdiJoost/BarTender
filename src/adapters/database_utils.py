from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.results import InsertOneResult, UpdateResult
from bson import ObjectId
from config.applicationConfig.applicationConfigFields import ApplicationConfigFields
from config.configFiles import ConfigFiles
from config.configManager import getConfig
from config.mongoDBConfig.mongoDbConfigFields import MongoDBConfigFields

def getDocumentById(objectId: str, databaseName: str, collectionName: str) -> dict:
    collection = _getCollection(databaseName=databaseName, collectionName=collectionName)
    return collection.find_one({"_id": objectId})

def saveDocument(document: dict, databaseName: str, collectionName: str) -> any:
    if document.get("_id") is None:
        return _insertDocument(document, databaseName, collectionName)
    else:
        return _updateDocument(document, databaseName, collectionName)
    
def deleteDocument(objectId: ObjectId, databaseName: str, collectionName: str) -> None:
    collection = _getCollection(databaseName=databaseName, collectionName=collectionName)
    collection.delete_one({"_id": objectId})

def _insertDocument(document: dict, databaseName: str, collectionName: str) -> any:
    collection = _getCollection(databaseName=databaseName, collectionName=collectionName)
    result: InsertOneResult = collection.insert_one(document)
    return result.inserted_id

def _updateDocument(document: dict, databaseName: str, collectionName: str) -> any:
    collection = _getCollection(databaseName=databaseName, collectionName=collectionName)
    result: UpdateResult = collection.update_one({"_id": document["_id"]}, {"$set": document}, upsert=True)
    return result.upserted_id

def _getCollection(databaseName: str, collectionName: str) -> Collection:
    client = _getClient()
    database = client[databaseName]
    return database[collectionName]

def _getClient() -> None:
    username = getConfig(MongoDBConfigFields.USERNAME.value, ConfigFiles.MONGO_DB_CONFIG)
    password = getConfig(MongoDBConfigFields.PASSWORD.value, ConfigFiles.MONGO_DB_CONFIG)
    host = getConfig(MongoDBConfigFields.HOST.value, ConfigFiles.MONGO_DB_CONFIG)
    port = getConfig(MongoDBConfigFields.PORT.value, ConfigFiles.MONGO_DB_CONFIG)
    return MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
