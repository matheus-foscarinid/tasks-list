from flask import Flask
from .models import db
from .routes import tasks_bp

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
  db.init_app(app)

  with app.app_context():
    db.create_all()

  app.register_blueprint(tasks_bp)

  return app
