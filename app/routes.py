from flask import Blueprint, render_template, request, redirect
from .db import mysql

main = Blueprint("main", __name__)

# ================= HOME PAGE =================
@main.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    return render_template("index.html", tasks=tasks)


# ================= CREATE TASK =================
@main.route("/create", methods=["GET","POST"])
def create():

    if request.method == "POST":

        title = request.form["title"]
        desc = request.form["description"]
        due = request.form["due_date"]

        cur = mysql.connection.cursor()

        cur.execute("""
        INSERT INTO tasks
        (title,description,due_date,status,created_by)
        VALUES(%s,%s,%s,'Pending','Admin')
        """,(title,desc,due))

        mysql.connection.commit()

        return redirect("/")

    return render_template("create_task.html")
@main.route("/delete/<int:id>")
def delete(id):

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s",(id,))
    mysql.connection.commit()

    return redirect("/")
@main.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):

    cur = mysql.connection.cursor()

    if request.method == "POST":

        title = request.form["title"]
        status = request.form["status"]

        cur.execute("""
        UPDATE tasks
        SET title=%s,
            status=%s
        WHERE id=%s
        """,(title,status,id))

        mysql.connection.commit()

        return redirect("/")

    cur.execute("SELECT * FROM tasks WHERE id=%s",(id,))
    task = cur.fetchone()

    return render_template("edit_task.html", task=task)