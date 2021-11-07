# from flask import render_template, request, flash
# from Pokemon import app

# import sys
# import random
# import Pokemon.names as name
# from Pokemon import user            # Importing User class.

# GENERATE_POKEMON_IMAGE_NUMBER = random.randrange(492)

# @app.route('/', methods=("GET", "POST"))
# @app.route('/pokemon', methods=("GET", "POST"))
# def renderPokemonImage():
#     pokemon_image = str(GENERATE_POKEMON_IMAGE_NUMBER) + ".png"

#     return (render_template("pokemon.html", title="Pokemon", imageNumber=pokemon_image))

# # Checking answers taken from users.
# @app.route('/pokemon', methods=("GET", "POST"))
# def checkPokemonName(name):
#     newUser = user.User()

#     if (request.method == "POST"):
#         userAnswer = request.form["pokeName"]
        
#         if (name.poke_names[userAnswer] == GENERATE_POKEMON_IMAGE_NUMBER):
#             newUser.incrementScore()
#             flash(userAnswer)
#             return (render_template("pokemon.html", title="Pokemon", imageNumber=str(GENERATE_POKEMON_IMAGE_NUMBER) + ".png"))
#     else:
#         flash("Please Enter Pokemon Name")

# @app.route('/pokemon', methods=("GET", "POST"))
# def skip():
#     if (request.method == "POST"):
#         generate_new_pokemon = str(GENERATE_POKEMON_IMAGE_NUMBER) + ".png"
#         print(generate_new_pokemon, file=sys.stderr)
#         print("Page Refreshed", file=sys.stderr)
#         return (render_template("pokemon.html", title="Pokemon", imageNumber = generate_new_pokemon))