from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route("/")
def home():
    df = pd.read_csv("salaries_by_college_major.csv")

    clean_df = df.dropna()

    #   columns
    df_columns = clean_df.columns

    for col in df_columns:
        print(col)

    #   rows
    rows = []
    # data = clean_df.head(10)
    data = clean_df
    for i in range(len(data)):
        rows.append({
            "ID": i + 1,
            "Undergraduate Major": data["Undergraduate Major"][i],
            "Starting Median Salary": data["Starting Median Salary"][i],
            "Mid-Career Median Salary": data["Mid-Career Median Salary"][i],
            "Mid-Career 10th Percentile Salary": data["Mid-Career 10th Percentile Salary"][i],
            "Mid-Career 90th Percentile Salary": data["Mid-Career 90th Percentile Salary"][i],
            "Group": data["Group"][i]
        })

    return render_template("index.html", columns=df_columns, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
