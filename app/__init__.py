from flask_restplus import Api
from flask import Blueprint

# import all endpoints here
# then add it as a namespace
from app.main.topic_one.controller.test_logging import api as test_logging_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='API TITLE HERE',
    version='1.0',
    description='DESCRIPTION HERE'
)

api.add_namespace(test_logging_ns)