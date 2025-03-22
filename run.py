from src.api.app import app
from config.configManager import getConfig
from config.applicationConfig.applicationConfigFields import ApplicationConfigFields
from src.controller.pumpController.pumpController import PumpController

def main():
    pumpController = PumpController(PIN=17)
    pumpController.run()
    pumpController.cleanUp()

if __name__ == "__main__":
    main()
