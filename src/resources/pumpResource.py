from typing import Type
from flask_restful import reqparse

from src.models.baseModel import BaseModel
from src.models.pumpModel import PumpModel
from src.resources.baseResource import BaseResource

class PumpResource(BaseResource):

    def get(self):
        data = self._getParser().parse_args()
        return self.handleGetResponse(PumpModel, data)

    def post(self):
        data = self._postParser().parse_args()
        return self.handlePostResponse(PumpModel, data)

    def put(self):
        data = self._putParser().parse_args()
        return self.handlePut(PumpModel, data)

    def delete(self):
        data = self._deleteParser().parse_args()
        return self.handleDelete(PumpModel, data)
    
    @classmethod
    def _postParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument(PumpModel.INGREDIENT_FIELD_NAME,
                        type=str,
                        required=True)
        parser.add_argument(PumpModel.ML_PER_SECOND_FIELD_NAME,
                        type=float,
                        required=True)
        parser.add_argument(PumpModel.PIN_NUMBER_FIELD_NAME,
                        type=int,
                        required=True)
        parser.add_argument(PumpModel.PUMP_TYPE_FIELD_NAME,
                        type=str,
                        required=True)
        return parser
    
    @classmethod
    def _putParser(cls) -> reqparse.RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument("_id",
                        type=str)
        parser.add_argument(PumpModel.INGREDIENT_FIELD_NAME,
                        type=str)
        parser.add_argument(PumpModel.ML_PER_SECOND_FIELD_NAME,
                        type=float)
        parser.add_argument(PumpModel.PIN_NUMBER_FIELD_NAME,
                        type=int)
        parser.add_argument(PumpModel.PUMP_TYPE_FIELD_NAME,
                        type=str)
        return parser

    @classmethod
    def _getUpdatedModel(cls, model: Type[BaseModel], data: dict) -> None:
        if data.get(PumpModel.INGREDIENT_FIELD_NAME):
            model.setIngredient(data.get(PumpModel.INGREDIENT_FIELD_NAME))
        if data.get(PumpModel.ML_PER_SECOND_FIELD_NAME):
            model.setMlPerSecond(data.get(PumpModel.ML_PER_SECOND_FIELD_NAME))
        if data.get(PumpModel.PIN_NUMBER_FIELD_NAME):
            model.setPinNumber(data.get(PumpModel.PIN_NUMBER_FIELD_NAME))
        if data.get(PumpModel.PUMP_TYPE_FIELD_NAME):
            model.setPumpType(data.get(PumpModel.PUMP_TYPE_FIELD_NAME))

class PumpsResource(BaseResource):

    def get(self):
        data = self._pagingParser().parse_args()
        return self.handleGetMany(PumpModel, data)