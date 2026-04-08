# Final Project – Survey Tool for Income & Spending Analysis

## Overview

This project implements a **survey tool** to collect participants' data on income and expenses for healthcare market analysis. The tool uses **Flask** for web collection, stores data in **CSV** (and optionally **MongoDB**), and performs analysis using **Python** in a Jupyter Notebook.

## Project Structure

final_project/
│
├─ app.py                # Flask web application
├─ user.py               # User class for processing form data
├─ templates/
│   └─ index.html        # HTML form for collecting user data
├─ survey_data.csv       # CSV file storing collected survey data
├─ analysis.ipynb        # Jupyter Notebook for analysis and visualization
├─ income_by_age.png      # Chart: Income by Age
├─ spending_by_gender.png  # Chart: Spending by Gender
└─ README.md             # Project documentation

## Features

1. **Web Application with Flask**

   * Form collects:

     * Age
     * Gender
     * Total Income
     * Expenses: Utilities, Entertainment, School Fees, Shopping, Healthcare
   * Submits data via the `/submit` route.
   * Data is saved to `survey_data.csv` automatically.

2. **Data Storage**

   * **CSV file:** `survey_data.csv` stores all form submissions.
   * **MongoDB:** Data stored in `survey_db.users` collection if MongoDB is running.

3. **Data Processing**

   * `User` class in `user.py` converts form submissions into structured CSV rows.

4. **Data Analysis & Visualization**

   * `analysis.ipynb` loads `survey_data.csv` for analysis.
   * Visualizations include:

     * **Income by Age** – identifies age groups with the highest income.
     * **Spending by Gender** – shows gender distribution across expense categories.
   * Charts exported as PNG files for use in PowerPoint presentations.

5. **Deployment**

   * Flask app can be deployed on **AWS EC2** or similar cloud services.

## Instructions – Running the Project

1. Open VS Code, then open the **final_project** folder and run `app.py`.
2. Open `http://127.0.0.1:5000/` in your browser.
3. Fill out the survey form for participants.
4. Submissions are saved automatically to `survey_data.csv` (and MongoDB if running).
5. Open `analysis.ipynb` in Jupyter Notebook to:

   * Load `survey_data.csv`
   * Generate charts for **Income by Age** and **Spending by Gender**
   * Export charts for use in presentations.

## Notes

* Keep the `templates` folder in the same directory as `app.py`.
* CSV updates automatically with each form submission.
* The `User` class ensures consistent data structure for analysis.
* **Charts are generated using Matplotlib only.**
* Ensure MongoDB is running if you want to store data in the database.  
* The project is designed for easy deployment on cloud platforms like AWS EC2.  
* Use the exported PNG charts in your PowerPoint presentations for visual insights.  
