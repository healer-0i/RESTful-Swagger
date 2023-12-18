from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

app = Flask(__name__)
api = Api(app)
swag = swagger(app)

# ... (Flask RESTful resource with Swagger)
