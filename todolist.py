from flask import Flask, request, Response
from flask_alchemy import SQLAlchemy
from config import Config
import json

app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)

db = SQLAlchemy(app)

class Movies(db.Model)
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255))
    release_year = db.Column(db.Integer)


@app.route('/')
def todo():
    return todo_db

#READ
@app.route("/todo/<todo_id>")
def get_todo(todo_id):
    return json.dumps(todo_db[todo_id])

   # movies = Movies.query.all()

#CREATE

@app.route('/todo/add' , methods=['POST'])
def add_todo():
    req_data = request.get_json()
    job = req_data['todo']

    new_job = { "4" : todo }
    todo_db.update(new_job)
    return "Added to To Do List"

@app.route("/first")
def world():
    return "<h1> todolist </h1>"


if __name__ == "__main__":
    app.run(host='127.0.0.1')

#New To Do
# { "id" : { "task" : "to do", "progress": "to do"}}