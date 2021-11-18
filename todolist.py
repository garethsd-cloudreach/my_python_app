from flask import Flask, request, Response
import json

app = Flask(__name__)

todo_db = {
    "1": { 'task': 'laundry', 'progress': 'not started'},
    "2": { 'task': 'windows', 'progress': 'not started'},
    "3": { 'task': 'wash car', 'progress': 'not started'}
}

@app.route('/')
def todo():
    return todo_db

#READ
@app.route("/todo/<todo_id>")
def get_todo(todo_id):
    return json.dumps(todo_db[todo_id])

#CREATE

@app.route('/add' , methods=['POST'])
def add_todo():
    req_data = request.get_json()
    job = req_data['todo']

    new_job = { "4" : todo }
    todo_db.update(new_job)
    return "Added to To Do List"

#UPDATE

@app.route('/update' , methods=['PUT'])
def update_todo():
    req_data = request.get_json()
    job = req_data['todo']

    update_job = {"todo": {"task" : "laundry", "progress" : "not started"}}
    todo_db.update(update_job)
    return "Updated to do list"

#DELETE

@app.route('/delete' , methods=['DELETE'])
def delete_todo():
    req_data = request.get_json()
    job = req_data['todo']

    delete_todo = {"todo": {"task" : "windows", "progress" : "not started"}}
    todo_db.update(delete_todo)
    return "Job Deleted"

@app.route("/first")
def world():
    return "<h1> todolist </h1>"


if __name__ == "__main__":
    app.run(host='127.0.0.1')

#New To Do
# { "id" : { "task" : "to do", "progress": "to do"}}