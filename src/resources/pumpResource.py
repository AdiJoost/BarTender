from flask_restful import Resource, reqparse
from bson import ObjectId
from bson.errors import InvalidId


from src.api.utils import createResponse
from src.models.pumpModel import PumpModel

class PumpResource(Resource):

    def get(self):
        data = self._getParser().parse_args()

        try:
            objectId = ObjectId(data["_id"])
        except InvalidId as e:
            return createResponse(str(e), 400)
        
        pumpModel = PumpModel.get(objectId)
        if not pumpModel:
            return createResponse(f"Pump with ID: <{objectId}> not found", 404)
        return createResponse(pumpModel.toJson(), 200)

    def post(self):
        data = self._postParser().parse_args()
        pumpModel = PumpModel(**data)
        pumpModel.save()
        return createResponse(pumpModel.toJson(), 201)

    def put(self):
        data = self._putParser().parse_args()

        try:
            pumpModel, isNewPump = self._getPumpModelForPut(data)
        except InvalidId as e:
            return createResponse(str(e), 400)
           
        pumpModel.save()
        if isNewPump:
            return createResponse(pumpModel.toJson(), 201)
        return createResponse("",204)

    def delete(self):
        data = self._deleteParser().parse_args()
        try:
            objectId = ObjectId(data["_id"])
            PumpModel.delete(objectId)
            return createResponse("", 204)
        except InvalidId:
            return createResponse("", 204)

    @classmethod
    def _getParser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("_id",
                        type=str,
                        required=True)
        return parser
    
    @classmethod
    def _postParser(cls):
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
    def _putParser(cls):
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
    def _deleteParser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument("_id",
                        type=str,
                        required=True)
        return parser
    
    @classmethod
    def _getPumpModelForPut(cls, data: dict) -> tuple:
        pumpModel = PumpModel.get(ObjectId(data.get("_id")))
        isNewPump = False
        if not pumpModel:
            pumpModel = PumpModel(**data)
            isNewPump = True
        else:
            cls._getUpdatedModel(pumpModel, data)
        return (pumpModel, isNewPump)
    
    @classmethod
    def _getUpdatedModel(cls, pumpModel:PumpModel, data: dict) -> None:
        if data.get(PumpModel.INGREDIENT_FIELD_NAME):
            pumpModel.setIngredient(data.get(PumpModel.INGREDIENT_FIELD_NAME))
        if data.get(PumpModel.ML_PER_SECOND_FIELD_NAME):
            pumpModel.setMlPerSecond(data.get(PumpModel.ML_PER_SECOND_FIELD_NAME))
        if data.get(PumpModel.PIN_NUMBER_FIELD_NAME):
            pumpModel.setPinNumber(data.get(PumpModel.PIN_NUMBER_FIELD_NAME))
        if data.get(PumpModel.PUMP_TYPE_FIELD_NAME):
            pumpModel.setPumpType(data.get(PumpModel.PUMP_TYPE_FIELD_NAME))