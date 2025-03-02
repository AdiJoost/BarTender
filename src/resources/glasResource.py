from typing import Type
from flask_restful import reqparse

from src.models.baseModel import BaseModel
from src.models.glasModel import GlasModel
from src.resources.baseResource import BaseResource

class GlasResource(BaseResource):

    def get(self):
        return self.handleGetResponse(GlasModel)

    def post(self):
        data = self._postParser().parse_args()
        return self.handlePostResponse(GlasModel, data)

    def put(self):
        data = self._putParser().parse_args()
        return self.handlePut(GlasModel, data)

    def delete(self):
        return self.handleDelete(GlasModel)
    
    @classmethod
    def _postParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument(GlasModel.GLAS_NAME_FIELD_NAME,
                        type=str,
                        required=True)
        parser.add_argument(GlasModel.PICTURE_FIELD_NAME,
                        type=str,
                        required=True)
        parser.add_argument(GlasModel.VOLUME_FIELD_NAME,
                        type=float,
                        required=True)
        return parser
    
    @classmethod
    def _putParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument("_id",
                        type=str)
        parser.add_argument(GlasModel.GLAS_NAME_FIELD_NAME,
                        type=str)
        parser.add_argument(GlasModel.PICTURE_FIELD_NAME,
                        type=str)
        parser.add_argument(GlasModel.VOLUME_FIELD_NAME,
                        type=float)
        return parser
    
    @classmethod
    def _getUpdatedModel(cls, model: Type[BaseModel], data: dict) -> None:
        if data.get(GlasModel.GLAS_NAME_FIELD_NAME):
            model.setName(data.get(GlasModel.GLAS_NAME_FIELD_NAME))
        if data.get(GlasModel.PICTURE_FIELD_NAME):
            model.setPicture(data.get(GlasModel.PICTURE_FIELD_NAME))
        if data.get(GlasModel.VOLUME_FIELD_NAME):
            model.setVolume(data.get(GlasModel.VOLUME_FIELD_NAME))

class GlasesResource(BaseResource):

    def get(self):
        return self.handleGetMany(GlasModel)