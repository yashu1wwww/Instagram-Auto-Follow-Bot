from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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
    data = clean_df.head(10)
    # data = clean_df
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

    #   chart
    # width=16 height=8
    plt.figure(figsize=(16, 10))

    # x and y font size
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    # x and y labels
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Number of Posts", fontsize=14)

    # ylim
    plt.ylim(0, 38000)

    # chart
    # for column in df_columns:
    #     plt.plot(clean_df.index, clean_df[column])

    chart = plt.plot(clean_df.index, clean_df["Starting Median Salary"])

    return render_template("index.html", columns=df_columns, rows=rows, chart=chart)


if __name__ == "__main__":
    app.run(debug=True)
