from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class MovieForm(FlaskForm):
    rating = StringField("Your rating out of 10 e.g 7.5")
    review = StringField("Your review")
    submit = SubmitField("Done")


class AddMovie(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)


db.create_all()


# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    data = Movie.query.all()
    return render_template("index.html", movies=data)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    current_id = request.args.get("id")
    current_movie = Movie.query.get(current_id)
    form = MovieForm()

    if form.validate_on_submit():
        current_movie.rating = float(form.rating.data)
        current_movie.review = form.review.data

        db.session.commit()

        return redirect(url_for("home"))
    return render_template("edit.html", movie=current_movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)

    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovie()

    if form.validate_on_submit():

        #   GET MOVIES LIST
        parameter = {
            "api_key": "ac26b35b267982816fb9894546ee2f67",
            "query": form.title.data
        }
        response = requests.get(url=f"https://api.themoviedb.org/3/search/movie", params=parameter)
        response.raise_for_status()
        movies = response.json()
        results = movies["results"]

        return render_template("select.html", results=results)

    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
