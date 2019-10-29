# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 7/10/2019
# File: pokemonGame.py
# Purpose: Main file for handling the Pokemon Guessing aspect.
# Modification: - Re-done the entire project. Moved LOTS of things around.
#               - Separating project so it is well organized and structured.
# ----------------------------------------------------------------------------------------

from flask import render_template, request
from Pokemon import app

import random
<<<<<<< HEAD
from Pokemon import pokemonName
=======
import PokemonGame.pokemonName
>>>>>>> a08be33cfc49cdf108c509177ac73eba5208d731

generateNumberForImage = random.randrange(492)

@app.route('/', methods=("GET", "POST"))
@app.route('/pokemon', methods=("GET", "POST"))
def renderPokemonImage():
    return (render_template("pokemon.html", title="Pokemon", imageNumber=str(generateNumberForImage) + ".png"))

<<<<<<< HEAD
# Checking answers taken from users.
@app.route('/pokemon', methods=("GET", "POST"))
def checkPokemonName(name):
    userAnswer = request.form["pokeName"]
=======

# Checking answers taken from users.
def checkPokemonName(name):
>>>>>>> a08be33cfc49cdf108c509177ac73eba5208d731
    pass