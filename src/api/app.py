from flask import Flask
from flask_restful import Api

from src.resources.pumpResource import PumpResource

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return "hello world!"

api.add_resource(PumpResource, "/pump")