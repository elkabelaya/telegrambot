from app import app
from app import utils
from app import settings
import git
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello!!!"

@app.route('/update_repo/', methods=["POST"])
def update():
    x_hub_signature = request.headers.get('X-Hub-Signature')
    if utils.is_valid_signature(x_hub_signature, request.data, settings.WEBHOOK_SECRET_KEY):
        repo = git.Git('mysite')
        repo.pull('origin', 'main')
        return "OK"
    else:
        return "Error", 401
