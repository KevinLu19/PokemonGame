from flask import Blueprint, render_template, request

import random
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

def check_pokemon():
    # if (request.method == "POST"):
    #     userAnswer = request.form["pokeName"]
        
    #     if (name.poke_names[userAnswer] == GENERATE_POKEMON_IMAGE_NUMBER):
    #         newUser.incrementScore()
    #         flash(userAnswer)
    #         return (render_template("pokemon.html", title="Pokemon", imageNumber=str(GENERATE_POKEMON_IMAGE_NUMBER) + ".png"))
    # else:
    #     flash("Please Enter Pokemon Name")

    pass

@views.route("/about")
def about():
    return (render_template("about.html", title = "About Me"))