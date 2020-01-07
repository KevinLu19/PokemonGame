# Welcome To My Version of Who's That Pokemon
This is a standalone game taken from the Pokemon animated series "Who's That Pokemon" that was popular during our youth days.

NOTE: This guessing game will only have Pokemon from generation 1 - 3. Any Pokemon after that would not be here.

## How to play (WIP not near completion at all)
The game is currently being hosted on PythonAnyWhere. Link to the game: http://rumii7.pythonanywhere.com/

Very simple actually, there will be a random silhouette picture of a pokemon and the player's goal is to guess the name of the pokemon. Each correctly guessed Pokemon would reward player a point on the score board. Any incorrect guess would simply skip the current image pokemon.

## Work Priority 
* Focusing on deploying the game without silhouette. Along with working score board.
* Porting all platforms. 
* Add other generations to the game. Currently the system only have 1st generation Pokemon.


### Prerequisites
```
Programming Language: Python 3+ (Rest In Peace Python 2)
Framework Required: Flask 

API Used: Google API (Still deciding if want to continue to use Gmail api for notification)     
         
Works on Visual studio or Visual Studio Code. I will be using Visual Studio Code
```

### Installing

I recommend installing and running code in a Python Virtual Environment which instills different version of Pythons. 

```
If using Git: 
  git clone https://github.com/KevinLu19/PokemonGame.git
  
Or download repository code.

```

Install Python Virutal Environment: 

```
Mac/ Linux: 
  python3 -m pip install --user virtualenv
  
Windows: 
  py -m pip install --user virtualenv
  
In order to activate virtual environemnt, type into terminal: 

source/bin/activate
```

```
Install Gmail API:
Ctrl + shift + P to open Command Palette. Enter NuGet Package Manager and enter in "Google.Apis.Gmail.v1"
```

## Running the tests

In order to run, type into terminal: python3 app.py.

## Built With

* [Flask] (http://flask.palletsprojects.com/en/1.1.x/) - Main framwork used.
* [National PokeDex] (https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number) - Seek out the National PokeDex.

Languages: 
* Python 3
* HTML/ CSS
* Javascript
