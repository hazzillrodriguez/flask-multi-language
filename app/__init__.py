from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
# Configuration
if app.config['ENV'] == 'development':
	app.config.from_object('config.DevelopmentConfig')
else:
	app.config.from_object('config.ProductionConfig')

babel = Babel(app)

from app import views