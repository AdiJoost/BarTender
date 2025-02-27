from bson import ObjectId
from bson.errors import InvalidId
from flask import Response, jsonify
from flask_restful import Resource, reqparse
from typing import List, Type

from src.enums.paginationOptions import PaginationOption
from src.models.baseModel import BaseModel
from src.api.utils import createResponse

class BaseResource(Resource):

    def handleGetResponse(self, modelClass: Type[BaseModel], data: dict) -> Response:
        try:
            objectId = ObjectId(data["_id"])
        except InvalidId as e:
            return createResponse(str(e), 400)
        
        model = modelClass.get(objectId)
        if not model:
            return createResponse(f"Pump with ID: <{objectId}> not found", 404)
        return createResponse(model.toJson(), 200)
    
    def handlePostResponse(self, modelClass: Type[BaseModel], data: dict) -> Response:
        model = modelClass(**data)
        model.save()
        return createResponse(model.toJson(), 201)
    
    def handlePut(self, modelClass: Type[BaseModel], data: dict) -> Response:
        try:
            model, isNew = self._getModelForPut(modelClass, data)
        except InvalidId as e:
            return createResponse(str(e), 400)
        model.save()
        if isNew:
            return createResponse(model.toJson(), 201)
        return createResponse("",204)
    
    def handleDelete(self, modelClass: Type[BaseModel], data: dict) -> Response:
        try:
            objectId = ObjectId(data["_id"])
            modelClass.delete(objectId)
            return createResponse("", 204)
        except InvalidId:
            return createResponse("", 204)
        
    def handleGetMany(self, modelClass: Type[BaseModel], data: dict) -> Response:
        offset: int = data.get(PaginationOption.OFFSET.value) if data.get(PaginationOption.OFFSET.value) else 0
        limit: int = data.get(PaginationOption.LIMIT.value) if data.get(PaginationOption.LIMIT.value) else 20
        result: list= modelClass.getMany(limit=limit, offset=offset)
        returnValue = [item.toJson() for item in result]
        return createResponse(returnValue, 200)
    
    @classmethod
    def _getParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument("_id",
                        type=str,
                        required=True)
        return parser
    
    @classmethod
    def _deleteParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument("_id",
                        type=str,
                        required=True)
        return parser
    
    @classmethod
    def _pagingParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument(PaginationOption.OFFSET.value,
                        type=int)
        parser.add_argument(PaginationOption.LIMIT.value,
                        type=int)
        return parser

    @classmethod
    def _getModelForPut(cls, modelClass: Type[BaseModel], data: dict) -> tuple:
        model = modelClass.get(ObjectId(data.get("_id")))
        isNew = False
        if not model:
            model = modelClass(**data)
            isNew = True
        else:
            cls._getUpdatedModel(model, data)
        return (model, isNew)
    
    @classmethod
    def _getUpdatedModel(cls, model: any, data: dict) -> None:
        return model
