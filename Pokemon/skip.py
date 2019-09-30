# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 9/29/2019
# File: skip.py
# Purpose: Handles the skip button POST request. When button is pressed, return a new pokemon.
# Modification: N/A
# ----------------------------------------------------------------------------------------

from flask import render_template

from Pokemon import app

@app.route('/')
@app.route('/pokemon')
def skip():
    return (render_template("skip.html", title="Pokemon"))