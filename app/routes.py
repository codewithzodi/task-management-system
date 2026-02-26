from flask import Blueprint, render_template, request, redirect, session
from .db import mysql
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint("main", __name__)

# ================= ADMIN EMAIL =================
ADMIN_EMAIL = "admin@gmail.com"


# ================= LOGIN CHECK =================
def login_required():
    return "user" in session


# ================= ADMIN CHECK =================
def admin_required():
    return "email" in session and session["email"] == ADMIN_EMAIL


# ================= HOME PAGE =================
@main.route("/")
def index():

    if not login_required():
        return redirect("/login")

    cur = mysql.connection.cursor()

    # Admin sees all tasks
    if admin_required():
        cur.execute("SELECT * FROM tasks")
    else:
        cur.execute(
            "SELECT * FROM tasks WHERE created_by=%s",
            (session["user"],)
        )

    tasks = cur.fetchall()

    return render_template(
        "index.html",
        tasks=tasks,
        username=session["user"]
    )


# ================= CREATE TASK =================
@main.route("/create", methods=["GET","POST"])
def create():

    if not login_required():
        return redirect("/login")

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        due_date = request.form["due_date"]
        remarks = request.form["remarks"]

        cur = mysql.connection.cursor()

        cur.execute("""
        INSERT INTO tasks
        (title,description,due_date,status,
         remarks,created_by)
        VALUES(%s,%s,%s,'Pending',%s,%s)
        """,
        (title, description,
         due_date, remarks,
         session["user"]))

        mysql.connection.commit()

        return redirect("/")

    return render_template("create_task.html")


# ================= DELETE =================
@main.route("/delete/<int:id>")
def delete(id):

    if not login_required():
        return redirect("/login")

    cur = mysql.connection.cursor()

    # ADMIN DELETE ANY TASK
    if admin_required():
        cur.execute("DELETE FROM tasks WHERE id=%s",(id,))
    else:
        cur.execute("""
        DELETE FROM tasks
        WHERE id=%s AND created_by=%s
        """,(id,session["user"]))

    mysql.connection.commit()

    return redirect("/")


# ================= EDIT =================
@main.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):

    if not login_required():
        return redirect("/login")

    cur = mysql.connection.cursor()

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        remarks = request.form["remarks"]
        status = request.form["status"]

        cur.execute("""
        UPDATE tasks
        SET title=%s,
            description=%s,
            remarks=%s,
            status=%s,
            updated_by=%s
        WHERE id=%s
        """,
        (title, description,
         remarks, status,
         session["user"],
         id))

        mysql.connection.commit()

        return redirect("/")

    cur.execute("SELECT * FROM tasks WHERE id=%s",(id,))
    task = cur.fetchone()

    return render_template("edit_task.html", task=task)


# ================= SEARCH =================
@main.route("/search", methods=["POST"])
def search():

    if not login_required():
        return redirect("/login")

    keyword = request.form["keyword"]

    cur = mysql.connection.cursor()

    if admin_required():
        cur.execute("""
        SELECT * FROM tasks
        WHERE title LIKE %s OR status LIKE %s
        """,
        (f"%{keyword}%", f"%{keyword}%"))
    else:
        cur.execute("""
        SELECT * FROM tasks
        WHERE created_by=%s
        AND (title LIKE %s OR status LIKE %s)
        """,
        (session["user"],
         f"%{keyword}%",
         f"%{keyword}%"))

    tasks = cur.fetchall()

    return render_template("index.html", tasks=tasks)


# ================= REGISTER =================
@main.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        password = generate_password_hash(
            request.form["password"]
        )

        cur = mysql.connection.cursor()

        cur.execute("""
        INSERT INTO users(name,email,password)
        VALUES(%s,%s,%s)
        """,(name,email,password))

        mysql.connection.commit()

        return redirect("/login")

    return render_template("register.html")


# ================= LOGIN =================
@main.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cur.fetchone()

        if user and check_password_hash(user[3], password):

            session["user"] = user[1]
            session["user_id"] = user[0]
            session["email"] = user[2]

            return redirect("/")

    return render_template("login.html")


# ================= ADMIN DASHBOARD =================
@main.route("/admin")
def admin():

    if not admin_required():
        return redirect("/")

    cur = mysql.connection.cursor()

    # ALL USERS
    cur.execute("SELECT id,name,email,role FROM users")
    users = cur.fetchall()

    # ALL TASKS
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()

    return render_template(
        "admin_dashboard.html",
        users=users,
        tasks=tasks
    )


# ================= LOGOUT =================
@main.route("/logout")
def logout():
    session.clear()
    return redirect("/login")