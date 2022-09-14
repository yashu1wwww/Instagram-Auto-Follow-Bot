from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        password = generate_password_hash(password=request.form["password"], method="pbkdf2:sha256", salt_length=8)

        if not User.query.filter_by(email=request.form["email"]).first():
            new_user = User(
                name=request.form["name"],
                email=request.form["email"],
                password=password
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)

            return redirect(url_for("secrets", name=new_user.name))
        else:
            flash("User already exists, Please select different email address.")
            return redirect(url_for("register"))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()

        if user != None:
            if check_password_hash(pwhash=user.password, password=request.form["password"]):
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Invalid Password.")
                return redirect(url_for("login"))
        else:
            flash("User doesn't exists.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/download')
def download():
    return send_from_directory(directory="static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
