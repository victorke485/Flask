from flask import Flask, render_template
import random
from datetime import datetime
from utilis import get_gender, get_age, get_blogs

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    return render_template("guess.html", age=age, gender=gender, name=name.capitalize())

@app.route("/blog")
def blog():
    all_blogs = get_blogs()
    return render_template("blog.html", blogs=all_blogs)

if __name__ == "__main__":
    app.run(debug=True)