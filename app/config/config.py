from dotenv import load_dotenv
import os
import ast

load_dotenv()


class DevConfig:
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    SECRET_KEY = os.getenv("SECRET_KEY")
    # OAUTHLIB_INSECURE_TRANSPORT = ast.literal_eval(
    #     os.getenv("OAUTHLIB_INSECURE_TRANSPORT")
    # )


config_by_name = dict(development=DevConfig)
