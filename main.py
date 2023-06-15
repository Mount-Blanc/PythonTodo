from flask import Flask,render_template, request, redirect


app = Flask(__name__)
app.debug = True

tasks = ["Task 1", "Task 2", "Task 3"]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    task = request.form['task']
    tasks.remove(task)
    return redirect('/')
