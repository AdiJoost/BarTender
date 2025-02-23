import json
from typing import List
from flask import Response, make_response, jsonify

from src.models.stepModel import StepModel

def createResponse (body: str, status: int) -> Response:
    response = make_response(jsonify(body), status)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:6969')
    return response

def parseArgToSteps(data: list) -> List[StepModel]:
    try:
        return [StepModel(**item) for item in data]
    except TypeError as e:
        raise ValueError (f"An Item in the list is not a step. -> {e}")

def _parseArgToSteps(values: list) -> List[StepModel]:
    try:
        data = json.loads(value)
        if not isinstance(data, list):
            raise ValueError("Argument is not of type List")
        return _castToStepModel(data)
    except Exception as e:
        raise ValueError(f"Argument is not a list of steps. -> {e}")
    
def _castToStepModel(data: List) -> List[StepModel]:
    try:
        return [StepModel(**item) for item in data]
    except TypeError as e:
        raise ValueError (f"An Item in the list is not a step. -> {e}")