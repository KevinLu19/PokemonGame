# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 7/10/2019
# File: pokemonGame.py
# Purpose: Main file for handling the Pokemon Guessing aspect.
# Modification: - Re-done the entire project. Moved LOTS of things around.
#               - Separating project so it is well organized and structured.
# ----------------------------------------------------------------------------------------

from flask import render_template
from Pokemon import app

generateNumberForImage = random.randrange(492)

@app.route('/pokemon')
def pokemonGame():
    return (render_template("pokemon.html"))