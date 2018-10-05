#api/helpers.py
import datetime
import psycopg2
import psycopg2.extras
import os
from api.app import db

conn = db.conn
cur = db.cursor

# conn = psycopg2.connect("dbname='stackoverflow_db' user='andrew' host='localhost' password='password'")

# cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)


def insert_user(users):
    cur.execute("""INSERT INTO users(name,email,password) VALUES('%s', '%s', '%s');"""%(
        users.name,
        users.email,
        users.password))
    conn.commit()

def get_user(email):
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    if user is None:
        return None
    conn.commit()
    return user

def create_question(questions):
    cur.execute("""INSERT INTO questions(question,date_posted,user_id) VALUES('%s', now(), '%s')"""%(
        questions.question,
        questions.user_id))
    conn.commit()

def get_questions():
    # cur.execute("SELECT * FROM QUESTIONS WHERE user_id =%s",(user_id,)) extra credit feature
    cur.execute("SELECT * FROM QUESTIONS")
    questions = cur.fetchall()
    rows = []
    for row in questions:
        rows.append(dict(row))
    if rows is None:
        return None  
    conn.commit()
    return rows

def get_question(id):
    cur.execute("SELECT * FROM QUESTIONS WHERE id = %s", (id,))
    question = cur.fetchone()
    if question is None:
        return None
    conn.commit()
    return question

def edit_question(id, question):
    cur.execute("UPDATE questions SET question = %s, date_posted = %s WHERE id = %s", (
        question['question'],
        question['date_posted'],
        id))
    conn.commit()

def delete_question(id):
    cur.execute("DELETE FROM questions WHERE id = %s", (id,))
    conn.commit()

def post_answer(answers):
    cur.execute("""INSERT INTO answers(answer, date_posted, status, question_id) VALUES('%s','%s','%s','%s')"""%(
        answers.answer,
        answers.question_id,
        answers.date_posted,
        'pending',
        ))
    conn.commit()
    return cur.fetchone().get('id')