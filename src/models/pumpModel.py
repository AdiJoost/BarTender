class PumpModel():

    def __init__(self, ingredient: str, mlPerSecond: float, pinNumber: int, pumpType: str):
        self._ingredient = ingredient
        self._mlPerSecond = mlPerSecond
        self._pinNumber = pinNumber
        self._pumpType = pumpType

    def getIngredient(self) -> str:
        return self._ingredient

    def setIngredient(self, value: str):
        self._ingredient = value

    def getMlPerSecond(self) -> float:
        return self._mlPerSecond

    def setMlPerSecond(self, value: float):
        self._mlPerSecond = value

    def getPinNumber(self) -> int:
        return self._pinNumber

    def setPinNumber(self, value: int):
        self._pinNumber = value

    def getPumpType(self) -> str:
        return self._pumpType

    def setPumpType(self, value: str):
        self._pumpType = value


    