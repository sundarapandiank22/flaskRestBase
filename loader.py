from os import environ

import yaml
from flask_mongoengine import MongoEngine


class Loader:
    def __init__(self):
        pass

    def load_configs_from_yml_file(app):
        app_environment = environ.get('APP_ENV', None)
        print("app_environment: {}".format(app_environment))

        yml_file_name = './src/config.yml'
        stream = open(yml_file_name, 'r')
        dictionary = yaml.safe_load(stream)
        mongodb_dict = dictionary.get("mongodb")
        app.config["MONGODB_SETTINGS"] = mongodb_dict

        # mongo_uri = mongodb_dict.get("uri")
        # database = MongoEngine(mongo_uri)
        # # client = MongoClient(mongo_uri)
        # # database = client.get_database()
        # app.config["DB_NAME"] = database

