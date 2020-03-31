import sqlite3
from flask import Flask, render_template, request, g, redirect, url_for

app = Flask(__name__)


DATABASE = 'to_do.db'


@app.route('/')
def index():
    db = sqlite3.connect(DATABASE)
    curr = db.cursor()

    tasks = curr.execute("SELECT id, task FROM current_tasks").fetchall()
    finished = curr.execute("SELECT id, task FROM finished_tasks").fetchall()

    db.close()

    return render_template("index.html", tasks=tasks, finished=finished)


@app.route('/delete', methods=["POST"])
def delete():
	"""deletes task from current tasks"""
	db = sqlite3.connect(DATABASE)
	curr = db.cursor()

	index = int(request.form.get("index"))

	curr.execute("DELETE FROM current_tasks WHERE id=:id", {"id": index})
	db.commit()

	db.close()

	return redirect(url_for("index"))

@app.route("/add", methods=["POST"])
def add():
	"""adds task to the current tasks"""
	db = sqlite3.connect(DATABASE)
	curr = db.cursor()

	task = request.form.get("task")

	curr.execute("INSERT INTO current_tasks (task) VALUES (:task)", {"task":task})
	db.commit()

	db.close()
	
	return redirect(url_for("index"))

@app.route("/done", methods=["POST"])
def done():
	"""moves task from current to finished"""
	db = sqlite3.connect(DATABASE)
	curr = db.cursor()

	index = int(request.form.get("done"))

	task = curr.execute("SELECT task FROM current_tasks WHERE id=:id", {"id": index}).fetchone()
	curr.execute("INSERT INTO finished_tasks (task) VALUES (?)", (task))
	curr.execute("DELETE FROM current_tasks WHERE id=:id", {"id": index})
	db.commit()

	db.close()

	return redirect(url_for("index"))


@app.route("/terminate", methods=["POST"])
def terminate():
	"""delites task from finished tasks"""
	db = sqlite3.connect(DATABASE)
	curr = db.cursor()

	index = int(request.form.get("terminate"))

	curr.execute("DELETE FROM finished_tasks WHERE id=:id", {"id": index})
	db.commit()

	db.close()

	return redirect(url_for("index"))



 