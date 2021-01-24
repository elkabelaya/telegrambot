from app import app
import git

@app.route('/')
@app.route('/index')
def index():
    return "Hello"

@app.route('/update_repo/', methods=["POST"])
def update():
    repo = git.Git('mysite')
    repo.pull('origin', 'main')
    return "OK"
