from flask import Blueprint, render_template, request, flash, url_for

import random

from werkzeug.utils import redirect
from . import db
import sys

views = Blueprint("views", __name__)

@views.route("/")
def pokemon():
    GENERATE_POKEMON_NUM = random.randrange(492)
    pokemon_string = str(GENERATE_POKEMON_NUM) + ".png"

    return render_template("pokemon.html", image_number = pokemon_string)

@views.route("/", methods=['GET', 'POST'])
def skip():
    GENERATE_POKEMON_NUM = random.randrange(492)
    pokemon_string = str(GENERATE_POKEMON_NUM) + ".png"

    if request.method == "POST":
        return render_template("pokemon.html", image_number = pokemon_string)

@views.route("/" , methods=["GET", "POST"])
def check_pokemon():
    # if (request.method == "POST"):
    #     userAnswer = request.form["pokeName"]
        
    #     if (name.poke_names[userAnswer] == GENERATE_POKEMON_IMAGE_NUMBER):
    #         newUser.incrementScore()
    #         flash(userAnswer)
    #         return (render_template("pokemon.html", title="Pokemon", imageNumber=str(GENERATE_POKEMON_IMAGE_NUMBER) + ".png"))
    # else:
    #     flash("Please Enter Pokemon Name")

    if request.method == "POST":
        user_guess = request.form["pokemon_name"]

        flash("Your guess is: ", user_guess)

        return redirect(url_for("views.about"))
    
    return render_template("about.html")

@views.route("/about")
def about():
    return (render_template("about.html", title = "About Me"))


@views.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('views.about'))
    return render_template('login.html', error=error)