from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired("Please enter your email"), Email(message="Please enter valid email")])
    password = PasswordField(label="Password", validators=[DataRequired("Please enter your password"), Length(min=4)])
    submit = SubmitField("Log In")


app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)