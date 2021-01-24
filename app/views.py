from app import app
from setting import WEBHOOK_SECRET_KEY
from utils import is_valid_signature
import git

@app.route('/')
@app.route('/index')
def index():
    return "Hello!"

@app.route('/update_repo/', methods=["POST"])
def update():
    x_hub_signature = request.headers.get('X-Hub-Signature')
    if is_valid_signature(x_hub_signature, request.data, WEBHOOK_SECRET_KEY):
        repo = git.Git('mysite')
        repo.pull('origin', 'main')
        return "OK"
    else:
        return "Error", 401
