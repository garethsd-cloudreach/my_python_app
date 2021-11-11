from flask import Flask, request, Response
import json

app = Flask(__name__)

todolist = {
    "1" : "washing up",
    "2" : "shopping",
    "3" : "studying",
    "4" : "laundry"
}

@app.route("/")
def todo():
    return todolist

#READ
@app.route("/todo/<todo_id>")
def get_todo(todo_id):
    return json.dumps(todolist[todo_id])

@app.route("/first")
def world():
    return "<h1> todolist </h1>"


if __name__ == "__main__":
    app.run(host='127.0.0.1')