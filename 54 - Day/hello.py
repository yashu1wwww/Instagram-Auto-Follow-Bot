from flask import Flask
import random


app = Flask(__name__)

print(__name__)
print(random.__name__)
print(random.__all__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/blog")
def blog():
    return "BLOG"


if __name__ == "__main__":
    app.run()
