"""
import the adapter and try to connect to the database
"""

import os
# import psycopg2

def reset_migration():
    from api.app import db

    # conn = psycopg2.connect("dbname='test_stackoverflow_db' user='postgres' host='localhost' password='postgres' port='5432'")

    # cur = conn.cursor()
    conn = db.conn
    cur = db.cursor

    cur.execute("""DELETE FROM answers;""")

    cur.execute("""DELETE FROM questions;""")

    cur.execute("""DELETE FROM users;""")

    conn.commit()

def migrate():
    from api.app import db
    conn = db.conn
    cur = db.cursor

    # conn = psycopg2.connect("dbname='stackoverflow_db' user='andrew' host='localhost' password='password' port='5432'")

    # cur = conn.cursor()

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


    