from app import app
import git

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!!"

@app.route('/update_repo/', methods=["POST"])
def update(request):
    repo = git.Repo("elkabelaya.pythonanywhere.com/")
    origin = repo.remotes.origin
    origin.pull()
    return "OK"
