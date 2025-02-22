from src.api.app import app
from config.configManager import getConfig
from config.applicationConfig.applicationConfigFields import ApplicationConfigFields

def main():
    port = getConfig(name=ApplicationConfigFields.PORT.value)
    app.run(host="0.0.0.0" ,port=port, debug=True)

if __name__ == "__main__":
    main()
