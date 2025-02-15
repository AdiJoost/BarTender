from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from config.rootPath import getRootPath
from src.resources.pumpResource import PumpResource

app = Flask(__name__)
api = Api(app)

swaggerPath = str(getRootPath().joinpath("src/api/swagger.yaml"))
swagger = Swagger(app, template_file=swaggerPath)


@app.route("/")
def hello():
    return "hello world!"

api.add_resource(PumpResource, "/pump")