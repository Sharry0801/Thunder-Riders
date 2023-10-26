from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/departments")
def departments():
    return render_template('departments.html')


@app.route("/aboutteam")
def aboutteam():
    return render_template('aboutteam.html')


@app.route("/suggestions")
def suggestions():
    return render_template('suggestions.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
