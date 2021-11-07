from flask import Flask, url_for

import os
import secret_key

# Creating Flask instance
app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key.FLASK_SECRET_KEY

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")

# import Pokemon.about        # Linked via Setup.py
# import Pokemon.game          # Link pokemon Game
# import Pokemon.skip         # Linking button
# import Pokemon.names         # Linking name of pokemon