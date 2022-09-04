from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
all_books = []


# db = sqlite3.connect("books-collections.db")
# cursor = db.cursor()


#   CREATE NEW TABLE
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# ADD DATA
# cursor.execute("INSERT INTO books VALUES('Harry Potter', 'J. K. Rowling', '9.3')")
# cursor.execute("INSERT OR IGNORE INTO books VALUES(2, 'Harry Potter 1', 'J. K. Rowling 1', '9.3')")
# cursor.execute("INSERT OR IGNORE INTO books VALUES(3, 'Harry Potter 2', 'J. K. Rowling 2', '9.3')")
# db.commit()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()


x = Book(title="Harry Portter", author="Arunesh", rating=4.3)
db.session.add(x)
db.session.commit()


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]

        data = {
            "title": title,
            "author": author,
            "rating": rating
        }

        all_books.append(data)

        print(all_books)

        return redirect(url_for("home"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
