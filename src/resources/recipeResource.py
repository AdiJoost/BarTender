from typing import Type
from flask_restful import reqparse
import json

from src.api.utils import parseArgToSteps
from src.models.baseModel import BaseModel
from src.models.recipeModel import RecipeModel
from src.resources.baseResource import BaseResource

class RecipeResource(BaseResource):
    
    def get(self):
        data = self._getParser().parse_args()
        return self.handleGetResponse(RecipeModel, data)

    def post(self):
        data = self._postParser().parse_args()
        return self.handlePostResponse(RecipeModel, data)

    def put(self):
        data = self._putParser().parse_args()
        return self.handlePut(RecipeModel, data)

    def delete(self):
        data = self._deleteParser().parse_args()
        return self.handleDelete(RecipeModel, data)
    
    @classmethod
    def _postParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument(RecipeModel.RECIPE_NAME_FIELD_NAME,
                        type=str,
                        required=True)
        parser.add_argument(RecipeModel.PICTURE_FIELD_NAME,
                        type=str,
                        required=True)
        parser.add_argument(RecipeModel.STEPS_FIELD_NAME,
                        type=parseArgToSteps,
                        location="json",
                        required=True)
        return parser
    
    @classmethod
    def _putParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument("_id",
                        type=str)
        parser.add_argument(RecipeModel.RECIPE_NAME_FIELD_NAME,
                        type=str)
        parser.add_argument(RecipeModel.PICTURE_FIELD_NAME,
                        type=str)
        parser.add_argument(RecipeModel.STEPS_FIELD_NAME,
                        type=parseArgToSteps,
                        location="json")
        return parser
    
    @classmethod
    def _getUpdatedModel(cls, model: Type[BaseModel], data: dict) -> None:
        if data.get(RecipeModel.RECIPE_NAME_FIELD_NAME):
            model.setName(data.get(RecipeModel.RECIPE_NAME_FIELD_NAME))
        if data.get(RecipeModel.PICTURE_FIELD_NAME):
            model.setPicture(data.get(RecipeModel.PICTURE_FIELD_NAME))
        if data.get(RecipeModel.STEPS_FIELD_NAME):
            model.setSteps(data.get(RecipeModel.STEPS_FIELD_NAME))

class RecipesResource(BaseResource):

    def get(self):
        data = self._pagingParser().parse_args()
        return self.handleGetMany(RecipeModel, data)