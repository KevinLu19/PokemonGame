from os import error

import sqlite3
import names
import database_location

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
    path = database_location.DATABASE_PATH_LOCATION

    create_table_command = database_location.sql_create_table_command

    conn = link_connection(path)

    if conn is not None:
        create_table(conn, create_table_command)
        insert_to_pokemon_table(conn)
    else:
        print("Something happened.")

if __name__ == "__main__":
    main()
