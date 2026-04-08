from flask import Flask, render_template, request
from pymongo import MongoClient
import csv
import os
from user import User  # Make sure your User class is defined in user.py

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "survey_data.csv")

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")  
db = client["survey_db"]
collection = db["users"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Collect form data
    age = int(request.form["age"])
    gender = request.form["gender"]
    income = float(request.form["income"])

    # Expenses
    expenses = {
        "utilities": float(request.form.get("utilities", 0)),
        "entertainment": float(request.form.get("entertainment", 0)),
        "school_fees": float(request.form.get("school_fees", 0)),
        "shopping": float(request.form.get("shopping", 0)),
        "healthcare": float(request.form.get("healthcare", 0)),
    }

    # Create a User instance
    user = User(age, gender, income, expenses)

    # Save to CSV
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow([
                "Age", "Gender", "Income",
                "Utilities", "Entertainment",
                "School Fees", "Shopping", "Healthcare"
            ])
        writer.writerow(user.to_csv_row())

    # Save to MongoDB
    collection.insert_one({
        "age": age,
        "gender": gender,
        "income": income,
        "expenses": expenses
    })

    return "Saved successfully"

if __name__ == "__main__":
    app.run(debug=True)
