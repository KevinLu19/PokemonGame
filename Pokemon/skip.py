# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/29/2019
# File: skip.py
# Purpose: Handles the skip button POST request. When button is pressed, return a new pokemon.
# Modification: N/A
# ----------------------------------------------------------------------------------------

from flask import render_template, request

from Pokemon import app
from Pokemon import game as pg

@app.route('/pokemon', methods=("GET", "POST"))
def skip():
    if (request.method == "POST"):
        generate_new_pokemon = str(pg.GENERATE_POKEMON_IMAGE_NUMBER) + ".png"
        print(generate_new_pokemon)
        return (render_template("pokemon.html", title="Pokemon", imageNumber = generate_new_pokemon))