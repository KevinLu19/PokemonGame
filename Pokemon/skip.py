# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/29/2019
# File: skip.py
# Purpose: Handles the skip button POST request. When button is pressed, return a new pokemon.
# Modification: N/A
# ----------------------------------------------------------------------------------------

from flask import render_template, request

from Pokemon import app
from Pokemon import pokemonGame as pg

@app.route('/')
@app.route('/pokemon')
def skip():
    # Boolean variable.
    skipCurrentImage = False
    
    if (request.method == "POST"):
        skipCurrentImage = True

        if (skipCurrentImage == True):
            return (render_template("pokemon.html", title="Pokemon", imageNumber = str(pg.generateNumberForImage) + ".png"))