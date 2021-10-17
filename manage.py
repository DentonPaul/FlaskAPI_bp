from app.main import create_app
from app import blueprint
import os
import logging

# env_name should be set on computer/server... default = 'dev'
env_name = os.getenv("FLASK_API_ENV_VAR", 'dev')

app = create_app(env_name)
logging.info(f'flask env = {env_name}')
app.register_blueprint(blueprint)

if __name__ == '__main__':
    # these are usually defined in IIS if you are using that
    HOST = os.getenv('FLASK_HOST', 'localhost')
    PORT = int(os.getenv('FLASK_PORT', '1234'))

    app.run(HOST, PORT)