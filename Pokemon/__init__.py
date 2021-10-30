from flask import Flask, url_for

import os

# Creating Flask instance
app = Flask(__name__)

import Pokemon.about        # Linked via Setup.py
import Pokemon.game          # Link pokemon Game
import Pokemon.skip         # Linking button
import Pokemon.names         # Linking name of pokemon
