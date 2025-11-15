from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
todos = db["todos"]


@app.route('/')
def index():
    all_todos = todos.find()   
    return render_template('index.html', todos=all_todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        todos.insert_one({'task': task, 'done': False})
    return redirect(url_for('index'))

@app.route('/complete/<string:task_id>')
def complete_task(task_id):
    from bson import ObjectId
    todos.update_one({'_id': ObjectId(task_id)}, {'$set': {'done': True}})
    return redirect(url_for('index'))

@app.route('/delete/<string:task_id>')
def delete_task(task_id):
    from bson import ObjectId
    todos.delete_one({'_id': ObjectId(task_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
