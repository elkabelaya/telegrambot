from app import app
import git

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!!!"

@app.route('/update_repo/', methods=["POST"])
def update():
    repo = git.Repo('/home/elkabelaya/mysite/')
    origin = repo.remotes.origin
    origin.pull()
    return "OK"
