from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the value from the dropdown
    selected_city = request.form['City'].lower()

    # Open and read the CSV file
    output = "No match found."
    try:
        with open('Cap Rates.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['city'].lower() == selected_city:
                    output = row['Average Cap Rate']  # This should match the header in your CSV for the cap rates
                    break
    except FileNotFoundError:
        output = "File not found."

    # Return the matching output
    # You can also redirect to the main page with a message or to a new template
    return render_template('index.html', message=f"The average cap rate for {selected_city.title()} is: {output}")

if __name__ == '__main__':
    app.run(debug=True)
