from flask import Flask, render_template, request
import requests
from send_mail import send_mail


app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/7fb3ea579b2efa3f5500")
response.raise_for_status()
all_post = response.json()


@app.route("/")
def index():
    return render_template("index.html", posts=all_post)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    data = None
    for post in all_post:
        if post["id"] == post_id:
            data = post
    return render_template("post.html", post=data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        send_mail(name=name, email=email, phone=phone, message=message)

        return render_template("contact.html", message="Successfully sent message")

    return render_template("contact.html", message="Contact Me")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
