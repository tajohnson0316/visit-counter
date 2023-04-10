from flask import Flask, render_template, redirect, session

application = Flask(__name__)
application.secret_key = "secret_key123"


@application.route("/")
def index():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1

    return render_template("index.html")


@application.route("/twice")
def twice():
    session["counter"] += 1

    return redirect("/")


@application.route("/destroy_session")
def reset():
    if "counter" in session:
        session.clear()
    else:
        print("No counter is available yet!")

    return redirect("/")


if __name__ == "__main__":
    application.run(port=5001, debug=True)
