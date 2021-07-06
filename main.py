from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "test"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")
    # return "Hello! this is the main page <h1>HELLO<h1>"

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("you have been logged out","info")
    return redirect(url_for("login"))


#
# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"
#
#
# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))



if __name__ == '__main__':
    app.run(debug = True)
