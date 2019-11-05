# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 7/10/2019
# File: pokemonGame.py
# Purpose: Main file for handling the Pokemon Guessing aspect.
# Modification: - Re-done the entire project. Moved LOTS of things around.
#               - Separating project so it is well organized and structured.
# ----------------------------------------------------------------------------------------

from flask import render_template, request, flash
from Pokemon import app

import random
from Pokemon import pokemonName     # Importing the dictionary name so we can check user answer.
from Pokemon import user            # Importing User class.

generateNumberForImage = random.randrange(492)

@app.route('/', methods=("GET", "POST"))
@app.route('/pokemon', methods=("GET", "POST"))
def renderPokemonImage():
    return (render_template("pokemon.html", title="Pokemon", imageNumber=str(generateNumberForImage) + ".png"))

# Checking answers taken from users.
@app.route('/pokemon', methods=("GET", "POST"))
def checkPokemonName(name):
    
    newUser = user.User()

    if (request.method == "POST"):
        userAnswer = request.form["pokeName"]
        
        if (pokemonName.pokemonNames[userAnswer] == generateNumberForImage):
            newUser.incrementScore()
            flash(userAnswer)
            return (render_template("pokemon.html", title="Pokemon", imageNumber=str(generateNumberForImage) + ".png"))
    else:
        flash("Please Enter Pokemon Name")
