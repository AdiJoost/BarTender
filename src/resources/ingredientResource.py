from typing import Type
from flask_restful import reqparse

from src.api.utils import createResponse
from src.enums.controllerType import ControllerType
from src.exceptions.controllerTypeException import ControllerTypeInvalidException
from src.models.baseModel import BaseModel
from src.models.ingredientModel import IngredientModel
from src.resources.baseResource import BaseResource

class IngredientResource(BaseResource):

    def get(self):
        data = self._getParser().parse_args()
        return self.handleGetResponse(IngredientModel, data)

    def post(self):
        data = self._postParser().parse_args()
        try:
            self._assigneControllerType(data)
        except ControllerTypeInvalidException as e:
            return createResponse(str(e), 400)
        return self.handlePostResponse(IngredientModel, data)

    def put(self):
        data = self._putParser().parse_args()
        try:
            self._assigneControllerType(data)
        except ControllerTypeInvalidException as e:
            return createResponse(str(e), 400)
        return self.handlePut(IngredientModel, data)

    def delete(self):
        data = self._deleteParser().parse_args()
        return self.handleDelete(IngredientModel, data)
    
    def _assigneControllerType(self, data: dict) -> None:
        controllerTypeString = data.get(IngredientModel.CONTROLLER_TYPE_FIELD_NAME)
        if controllerTypeString:
            try:
                data[IngredientModel.CONTROLLER_TYPE_FIELD_NAME] = ControllerType(controllerTypeString)
            except ValueError:
                raise ControllerTypeInvalidException(controllerTypeString)

    
    @classmethod
    def _postParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument(IngredientModel.INGREDIENT_NAME_FIELD_NAME,
                        type=str,
                        required=True)
        parser.add_argument(IngredientModel.CONTROLLER_TYPE_FIELD_NAME,
                        type=str,
                        required=True)
        parser.add_argument(IngredientModel.PICTRUE_FIELD_NAME,
                        type=str,
                        required=True)
        parser.add_argument(IngredientModel.DESCRIPTION_FIELD_NAME,
                        type=str,
                        required=True)
        return parser
    
    @classmethod
    def _putParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument("_id",
                        type=str)
        parser.add_argument(IngredientModel.INGREDIENT_NAME_FIELD_NAME,
                        type=str)
        parser.add_argument(IngredientModel.CONTROLLER_TYPE_FIELD_NAME,
                        type=str)
        parser.add_argument(IngredientModel.PICTRUE_FIELD_NAME,
                        type=str)
        parser.add_argument(IngredientModel.DESCRIPTION_FIELD_NAME,
                        type=str)
        return parser

    @classmethod
    def _getUpdatedModel(cls, model: Type[BaseModel], data: dict) -> None:
        if data.get(IngredientModel.INGREDIENT_NAME_FIELD_NAME):
            model.setName(data.get(IngredientModel.INGREDIENT_NAME_FIELD_NAME))
        if data.get(IngredientModel.CONTROLLER_TYPE_FIELD_NAME):
            model.setControllerType(data.get(IngredientModel.CONTROLLER_TYPE_FIELD_NAME))
        if data.get(IngredientModel.PICTRUE_FIELD_NAME):
            model.setPicture(data.get(IngredientModel.PICTRUE_FIELD_NAME))
        if data.get(IngredientModel.DESCRIPTION_FIELD_NAME):
            model.setDescription(data.get(IngredientModel.DESCRIPTION_FIELD_NAME))

class IngredientsResource(BaseResource):

    def get(self):
        data = self._pagingParser().parse_args()
        return self.handleGetMany(IngredientModel, data)