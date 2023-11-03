from flask import Flask, render_template, request
import csv
import requests
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the value from the dropdown
    selected_city = request.form['City-drowdown'].lower()

    # URL of the CSV file
    csv_url = 'https://raw.githubusercontent.com/andyen11821/xcalsizer/main/Cap%20Rates.csv'

    # Initialize output variable
    output = "No match found."

    try:
        # Fetch the content of the CSV file
        response = requests.get(csv_url)
        response.raise_for_status()  # Will raise HTTPError if the HTTP request returned an unsuccessful status code

        # Use StringIO to make the fetched CSV content appear as a file-like object
        csvfile = StringIO(response.content.decode('utf-8'))

        # Read the file-like object as CSV
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['City'].lower() == selected_city:
                output = row['Average Cap Rate']  # This should match the header in your CSV for the cap rates
                break
    except FileNotFoundError:
        output = "File not found."
    except csv.Error as e:
        output = f"CSV error: {e}"
    except ValueError as e:
        output = f"Value error: {e}"
    except Exception as e:
        output = f"An unexpected error occurred: {e}"

    # Return the matching output
    return render_template('index.html', message=f"The average cap rate for {selected_city.title()} is: {output}")

if __name__ == '__main__':
    app.run(debug=True)
