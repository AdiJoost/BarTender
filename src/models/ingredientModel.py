from src.enums.controllerType import ControllerType

class IngredientModel():

    def __init__(self, name:str, controllerType: ControllerType, picture:str, description:str) -> None:
        self._name = name
        self._controllerType = controllerType
        self._picture = picture
        self._description = description

    def getName(self) -> str:
        return self._name

    def setName(self, value) -> None:
        self._name = value

    def getControllerType(self) -> ControllerType:
        return self._controllerType

    def setControllerType(self, value: ControllerType) -> None:
        self._controllerType = value

    def getPicture(self) -> str:
        return self._picture

    def setPicture(self, value) -> None:
        self._picture = value

    def getDescription(self) -> str:
        return self._description

    def setDescription(self, value) -> None:
        self._description = value
