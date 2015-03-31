from flask.ext.login import LoginManager

from blog import app
from .database import session
from .models import User

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login_get"
login_manager.login_message_category = "danger"
app.secret_key = 'why would I tell you my secret key?'

@login_manager.user_loader
def load_user(id):
    return session.query(User).get(int(id))