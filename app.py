from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from model import predict_bill

app = Flask(__name__)

CSV_FILE = "data.csv"


# Login Page
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            return redirect(url_for("dashboard"))
        else:
            return render_template(
                "login.html",
                error="Invalid Username or Password"
            )

    return render_template("login.html")


# Dashboard
@app.route('/dashboard')
def dashboard():

    df = pd.read_csv("data.csv")

    total_records = len(df)

    avg_units = round(df["Units_Used"].mean(), 2)

    max_bill = df["Bill_Amount"].max()

    return render_template(
        "dashboard.html",
        total_records=total_records,
        avg_units=avg_units,
        max_bill=max_bill
    )


# Add Data
@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':

        month = request.form['month']
        year = request.form['year']

        month_year = f"{month}-{year}"
        
        units = int(request.form['units'])

        # Auto bill generation

        if units <= 100:
            bill = units * 4

        elif units <= 200:
            bill = units * 5

        elif units <= 300:
            bill = units * 6

        else:
            bill = units * 7

        df = pd.read_csv("data.csv")

        new_row = pd.DataFrame({
            "Month_Year": [month_year],
            "Units_Used": [units],
            "Bill_Amount": [bill]
        })

        df = pd.concat([df, new_row], ignore_index=True)

        df.to_csv("data.csv", index=False)

        return redirect('/view')

    return render_template('add.html')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):

    df = pd.read_csv("data.csv")

    if request.method == 'POST':

        month = request.form['month']
        units = int(request.form['units'])

        if units <= 100:
            bill = units * 4
        elif units <= 200:
            bill = units * 5
        elif units <= 300:
            bill = units * 6
        else:
            bill = units * 7

        df.loc[index, 'Month_Year'] = month
        df.loc[index, 'Units_Used'] = units
        df.loc[index, 'Bill_Amount'] = bill

        df.to_csv("data.csv", index=False)

        return redirect('/view')

    record = df.iloc[index]

    return render_template('edit.html', record=record)

@app.route('/delete/<int:index>')
def delete(index):

    df = pd.read_csv("data.csv")

    df = df.drop(index)

    df.reset_index(drop=True, inplace=True)

    df.to_csv("data.csv", index=False)

    return redirect('/view')

# Prediction
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    result = None

    if request.method == 'POST':

        units = int(request.form['units'])

        result = predict_bill(units)

    return render_template(
        'predict.html',
        result=result
    )


@app.route('/view')
def view():

    df = pd.read_csv("data.csv")

    data = df.to_dict(orient='records')

    return render_template(
        'view.html',
        data=data
    )


if __name__ == "__main__":
    app.run(debug=True)