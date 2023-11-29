from flask import Flask
from views.user import user_blueprint
from views.home import home_blueprint
from database import db

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ctf:password@ctf_postgres:5432/ctf"

app.register_blueprint(home_blueprint)
app.register_blueprint(user_blueprint)

db.init_app(app)

with app.app_context():
    db.create_all()
