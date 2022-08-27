from flask import Flask


app = Flask(__name__)


#   make bold text
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


#   make underline
def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
def home():
    return "<h1 style='text-align:center'>Home</h1>" \
           "<p>This is paragraph</p>" \
           "<img src='https://media2.giphy.com/media/uWYjSbkIE2XIMIc7gh/giphy.gif?cid=ecf05e47cw2crjmhqizgawr4uwvfzpcob07uuqtka3967aoz&rid=giphy.gif&ct=g' width=200 height=300 />"


@app.route("/contact")
@make_bold
@make_underline
def contact():
    return "Contact"


@app.route("/username/<name>/<int:age>")
def user(name, age):
    return f"Hello {name}, you are {age} years old."


if __name__ == "__main__":
    app.run(debug=True)
