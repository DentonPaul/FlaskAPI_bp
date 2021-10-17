# intialize api namespaces/blueprints here

from flask_restplus import Namespace, fields

class Example:
    api = Namespace('example', description="an example endpoint... tests logging capabilities")