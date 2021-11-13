from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy
import secret_key

# Creating Flask instance
app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key.FLASK_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemon.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

pokemon_database = SQLAlchemy(app)


from .views import views
from .auth import auth


app.register_blueprint(views, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")



# import Pokemon.about        # Linked via Setup.py
# import Pokemon.game          # Link pokemon Game
# import Pokemon.skip         # Linking button
# import Pokemon.names         # Linking name of pokemon