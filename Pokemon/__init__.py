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
<<<<<<< HEAD
import Pokemon.pokemonName  # Linking name of pokemon
=======
import Pokemon.pokemonNames # Linking pokemonDictionary
>>>>>>> a08be33cfc49cdf108c509177ac73eba5208d731
