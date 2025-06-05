from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    todos = [("Talk to Lene", False),
             ("Get home safely", True)
             ]
    # todos = []

    @app.route("/")
    def home():
        return render_template("home.html", todos=todos)

    @app.route("/<string:todo>")
    def todo_item(todo: str):
        for text, completed in todos:
            if text == todo:
                completedText = "[x]" if completed else "[]"
                title = f"{completedText} - Todos"
                return render_template("todo.html", title=title, text=text, completed=completed)
        else:
            return render_template("notFound.html", text=todo, title="Not found")

    return app
