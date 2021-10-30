from flask import render_template, request, flash
from Pokemon import app

import random
import Pokemon.names as name
from Pokemon import user            # Importing User class.

GENERATE_POKEMON_IMAGE_NUMBER = random.randrange(492)

@app.route('/', methods=("GET", "POST"))
@app.route('/pokemon', methods=("GET", "POST"))
def renderPokemonImage():
    return (render_template("pokemon.html", title="Pokemon", imageNumber=str(GENERATE_POKEMON_IMAGE_NUMBER) + ".png"))

# Checking answers taken from users.
@app.route('/pokemon', methods=("GET", "POST"))
def checkPokemonName(name):
    from Pokemon import pokemonName     # Importing the dictionary name so we can check user answer.
    
    newUser = user.User()

    if (request.method == "POST"):
        userAnswer = request.form["pokeName"]
        
        if (name.poke_names[userAnswer] == GENERATE_POKEMON_IMAGE_NUMBER):
            newUser.incrementScore()
            flash(userAnswer)
            return (render_template("pokemon.html", title="Pokemon", imageNumber=str(GENERATE_POKEMON_IMAGE_NUMBER) + ".png"))
    else:
        flash("Please Enter Pokemon Name")
