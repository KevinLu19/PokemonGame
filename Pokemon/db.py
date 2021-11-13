from os import error

import sqlite3
from sqlite3.dbapi2 import Cursor
import names

def link_connection(db_file):
    conn = False

    try: 
        conn = sqlite3.connect(db_file)
    
        return conn
    except error as e:
        print(e)

    return conn

def create_table(conn, sql_create_table_command):
    table_cursor = conn.cursor()
    
    table_cursor.execute(sql_create_table_command)


def insert_to_pokemon_table(conn):
    cur = conn.cursor()

    pokemon_dict = names.poke_names
    
    for item in pokemon_dict:
        pokemon_value =  pokemon_dict[item]

        # print (pokemon_value, pokemon_key)
        #print (pokemon_value)

        cur.execute("""INSERT INTO pokemon VALUES (?, ?, ?)""", (None, pokemon_value, item))
    
    conn.commit()



def pokemon_image_number():
    all_pokemon_value = names.poke_names

    for value in all_pokemon_value:
        # print (all_pokemon_value[value])
        return all_pokemon_value[value]

def dictionary_pokemon_names():
    all_pokemon_key = names.poke_names

    for key in all_pokemon_key:
        # print (key)
        return key

def main():
    path = "C:\\users\\kevin\\desktop\\pokemongame\\pokemon\\pokemon.db" 

    create_table_command = """CREATE TABLE IF NOT EXISTS pokemon (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    image_num TEXT NOT NULL,
                                    name TEXT NOT NULL
    );"""

    conn = link_connection(path)

    if conn is not None:
        create_table(conn, create_table_command)
        insert_to_pokemon_table(conn)
    else:
        print("Something happened.")

if __name__ == "__main__":
    main()
