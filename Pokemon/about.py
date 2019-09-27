# ----------------------------------------------------------------------------------------
# Author: Kevin Lu
# Date: 7/10/2019
# File: about.py
# Purpose: Links about.html to the website.
# Modification: N/A
# ----------------------------------------------------------------------------------------

from flask import Flask, template_rendered


@app.route('/about')
def about():
    return (template_rendered("about.html", title="About"))