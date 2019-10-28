# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 7/10/2019
# File: __init__.py
# Purpose: Tells Python that this is part of the package. Useful for distributing code to others.
# Modification: N/A
# ----------------------------------------------------------------------------------------

from flask import Flask, url_for

import os

# Creating Flask instance
app = Flask(__name__)

import Pokemon.about        # Linked via Setup.py
import Pokemon.pokemonGame  # Link pokemon Game
import Pokemon.skip         # Linking button
import Pokemon.pokemonNames # Linking pokemonDictionary