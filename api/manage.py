"""
import the adapter and try to connect to the database
"""

import os
import psycopg2

def migrate(app):

    conn = psycopg2.connect("dbname='stackoverflow_db' user='andrew' host='localhost' password='password' port='5432'")

    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    	id serial PRIMARY KEY,
    	name varchar,
    	email varchar UNIQUE,
    	password varchar
    	);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS questions(
        id serial PRIMARY KEY,
        question varchar,
        date_posted TIMESTAMP,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id)
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS answers(
        id serial PRIMARY KEY,
        question_id INT,
        answer varchar,
        FOREIGN KEY (question_id) REFERENCES questions(id)
        );""")
    
    print("Database connected")
    conn.commit()

# except:
#     	print ("I am unable to connect to the database")


    