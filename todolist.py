from flask import Flask, request, Response
import json

app = Flask(__name__)

todo_db = {
    "1": { 'name': 'laundry', 'status': 'to do'},
    "2": { 'name': 'windows', 'status': 'to do'},
    "3": { 'name': 'wash car', 'status': 'to do'}
}

@app.route('/')
def todo():
    return todo_db

#READ
@app.route("/todo/<todo_id>")
def get_todo(todo_id):
    return json.dumps(todo_db[todo_id])

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
# { "todo" : { "name" : "to do", "status": "to do"}}