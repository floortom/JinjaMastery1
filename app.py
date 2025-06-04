from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    todos = ["Talk to Lene",
             "Get home safely"
             ]
    # todos = []

    @app.route("/")
    def home():
        return render_template("home.html", todos=todos)

    @app.route("/todos")
    def to_dos():
        return render_template("todos.html", todos=todos)

    return app
