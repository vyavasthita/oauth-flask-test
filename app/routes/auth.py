from flask.blueprints import Blueprint
from flask import render_template, request
from app import configuration
from app.utils.oauth_helper import get_access_token, get_user_data


auth_blueprint = Blueprint("auth", __name__, template_folder="templates")


@auth_blueprint.route("/index", methods=["GET"])
@auth_blueprint.route("/", methods=["GET"])
def index():
    data = {"data": "Hello from github oauth json endpoint"}

    return data, 200


@auth_blueprint.route("/home", methods=["GET"])
def home() -> str:
    """Provide the user with the option to register with GitHub."""
    return render_template("home.html", client_id=configuration.CLIENT_ID), 200


@auth_blueprint.route("/github/callback", methods=["GET"])
def github_callback():
    """Authenticate the user and displays their data."""
    args = request.args
    request_token = args.get("code")

    CLIENT_ID = configuration.CLIENT_ID
    CLIENT_SECRET = configuration.CLIENT_SECRET
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, request_token)

    user_data = get_user_data(access_token)
    return render_template("dashboard.html", userData=user_data)
