"""
import the adapter and try to connect to the database
"""
import psycopg2
# from resources.app import db

def migrate(app):

	try:
	    conn = psycopg2.connect("dbname='stackoverflow_db' user='andrew' host='localhost' password='password'")

	    cur.execute("""CREATE TABLE IF NOT EXISTS users(
	    	id serial PRIMARY KEY,
	    	name varchar,
	    	email varchar UNIQUE,
	    	username varchar,
	    	password varchar
	    	);""")

	    cur.execute("""CREATE TABLE IF NOT EXISTS questions(
	        id serial PRIMARY KEY,
	        question varchar,
	        date_posted TIMESTAMP
	        user_id INT,
	        FOREIGN KEY (user_id) REFERENCES users(id),
	        );""")

	    cur.execute("""CREATE TABLE IF NOT EXISTS answers(
	        id serial PRIMARY KEY,
	        question_id INT
	        answer varchar,
	        FOREIGN KEY (question_id) REFERENCES question(id),

	        );""")
	    conn.commit()

	except:
	    print ("I am unable to connect to the database")


    