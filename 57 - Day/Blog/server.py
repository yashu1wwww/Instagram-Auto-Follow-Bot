from flask import Flask, render_template
from post import Post


posts = Post()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts.posts())


@app.route("/blog/<int:post_id>")
def get_blog(post_id):
    data = None
    for post in posts.posts():
        if post["id"] == post_id:
            data = post

    return render_template("post.html", post=data)


if __name__ == "__main__":
    app.run(debug=True)
