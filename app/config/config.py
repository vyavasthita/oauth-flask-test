from dotenv import load_dotenv
import os

load_dotenv()


class DevConfig:
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")


config_by_name = dict(development=DevConfig)
