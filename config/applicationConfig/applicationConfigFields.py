from enum import Enum

class ApplicationConfigFields(Enum):
    APPLICATION_NAME = "applicationName"
    LOG_LEVEL = "logLevel"
    CHATTY_LEVEL = "chattyLevel"
    OVERWRITE_MECHANISM = "overwriteMechanism"
    PORT = "PORT"
    MONGO_DB_HOST = "MONGO_DB_HOST"
    MONGO_DB_PORT = "MONGO_DB_PORT"
    MONGO_DB_USERNAME = "MONGO_DB_USERNAME"
    MONGO_DB_PASSWORD = "MONGO_DB_PASSWORD"