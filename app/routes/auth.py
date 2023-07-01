from flask import redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
from app import configuration


github_blueprint = make_github_blueprint(
    client_id=configuration.CLIENT_ID, client_secret=configuration.CLIENT_SECRET
)


@github_blueprint.route("/")
def login_to_github():
    if not github.authorized:
        return redirect(url_for("github.login"))
    else:
        print("Already Authorized")

    res = github.get("/user")

    return f"You are {res.json()['login']} on GitHub"
