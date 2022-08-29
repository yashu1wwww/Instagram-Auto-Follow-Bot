from flask import Flask, render_template
import random
from datetime import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    rand_number = random.randint(0, 10)
    current_year = dt.now().year
    return render_template("index.html", num=rand_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
