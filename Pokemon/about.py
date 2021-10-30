from flask import render_template

from Pokemon import app

@app.route('/about')
def about():
    return (render_template("about.html", title="About Me"))