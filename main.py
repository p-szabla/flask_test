from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "test"


@app.route("/")
def home():
    return render_template("index.html")
    # return "Hello! this is the main page <h1>HELLO<h1>"

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
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
