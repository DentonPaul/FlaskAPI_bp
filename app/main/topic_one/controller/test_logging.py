from flask import request
from flask_restplus import Resource
import logging

from app.main.roots import Example
# from service directory
from app.main.topic_one.service.test_logging import get_messages

api = Example.api

@api.route('/endpoint1')
class TestLogs(Resource):
    
    def get(self):
        "This will log a message to info_file, error_file, and send out an error email"

        msg1, msg2, msg3 = get_messages()
        logging.info(msg1)
        logging.error(msg2)
        logging.exception(msg3)
        return {'status': 'success', 'message': 'successfully logged messages'}