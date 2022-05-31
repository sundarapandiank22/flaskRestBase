from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask import Flask

from loader import Loader
from routes import Routes

app = Flask(__name__)
api = Api(app)
Routes.initialize_routes(api)
Loader.load_configs_from_yml_file(app)

db= MongoEngine(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)
