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
    selected_city = request.form['city'].lower()

    # URL of the CSV file
    csv_url = 'https://github.com/andyen11821/xcalsizer/blob/8cdb43015f97de48a8164fb1c18a41b80cf097b8/Cap%20Rates.csv'

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
            if row['city'].lower() == selected_city:
                output = row['Average Cap Rate']  # This should match the header in your CSV for the cap rates
                break
    except requests.HTTPError as e:
        output = f"HTTP Error occurred: {e}"
    except requests.RequestException as e:
        output = f"Request Exception occurred: {e}"
    except Exception as e:
        output = f"An error occurred: {e}"

    # Return the matching output
    return render_template('index.html', message=f"The average cap rate for {selected_city.title()} is: {output}")

if __name__ == '__main__':
    app.run(debug=True)
