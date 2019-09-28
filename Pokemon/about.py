# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 7/10/2019
# File: about.py
# Purpose: Links about.html to the website along with supplying the main file with the re-route
#       of about page.
# Modification: N/A
# ----------------------------------------------------------------------------------------

from flask import render_template

from Pokemon import app

@app.route('/about')
def about():
    return (render_template("about.html", title="About Me"))