from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello</h1>'

@app.route('/bye')
def bye():
    return '<p>Bye</p>'

# Variables
@app.route("/username/<name>")
def greet(name):
    return f"<p>Hello {name.capitalize()}</p>"

if __name__ == "__main__":
    app.run(debug=True)