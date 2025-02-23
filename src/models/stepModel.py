from typing import Union

from src.enums.controllerType import ControllerType

class StepModel():

    INGREDIENT_FIELD_NAME = "ingredient"
    CONTROLLER_TYPE_FIELD_NAME = "controller_type"
    PICTURE_FIELD_NAME = "picture"
    DESCRIPTION_FIELD_NAME = "description"
    AMOUNT_FIELD_NAME = "amount"

    def __init__(self, ingredient: str, controller_type: Union[ControllerType, str], picture:str, description:str, amount:any) -> None:
        self._ingredient = ingredient
        self._controllerType = self._getControllerType(controller_type)
        self._picture = picture
        self._description = description
        self._amount = amount

    def getIngredient(self) -> str:
        return self._ingredient

    def setIngredient(self, value: str) -> None:
        self._ingredient = value

    def getControllerType(self) -> ControllerType:
        return self._controllerType

    def setControllerType(self, value: ControllerType) -> None:
        self._controllerType = value

    def getPicture(self) -> str:
        return self._picture

    def setPicture(self, value: str) -> None:
        self._picture = value

    def getDescription(self) -> str:
        return self._description

    def setDescription(self, value: str) -> None:
        self._description = value

    def getAmount(self) -> any:
        return self._amount

    def setAmount(self, value: any) -> None:
        self._amount = value

    def toJson(self) -> dict:
        return {
            self.INGREDIENT_FIELD_NAME: self._ingredient,
            self.CONTROLLER_TYPE_FIELD_NAME: self._controllerType.value,
            self.PICTURE_FIELD_NAME: self._picture,
            self.DESCRIPTION_FIELD_NAME: self._description,
            self.AMOUNT_FIELD_NAME: self._amount
        }

    def _getControllerType(self, controllerType: Union[ControllerType, str]) -> ControllerType:
        if isinstance(controllerType, ControllerType):
            return controllerType
        try:
            return ControllerType(controllerType)
        except ValueError:
            return None