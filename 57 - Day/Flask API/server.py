from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(url=f"https://api.agify.io/?name={name}")
    age_response.raise_for_status()
    age_data = age_response.json()
    age = age_data["age"]

    gender_response = requests.get(url=f"https://api.genderize.io/?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get(url="https://api.npoint.io/e5592fcd4a56c826fe64")
    response.raise_for_status()
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
