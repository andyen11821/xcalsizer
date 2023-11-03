import requests
import csv
from io import StringIO

@app.route('/submit', methods=['POST'])
def submit():
    selected_city = request.form['city']

    # URL to the raw CSV file on GitHub
    csv_url = 'https://raw.githubusercontent.com/yourusername/yourrepo/branch/path/to/Cap%20Rates.csv'
    
    # Fetch the CSV file from GitHub
    response = requests.get(csv_url)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    
    # Use StringIO to make the string response behave like a file object for the csv.reader
    csv_file = StringIO(response.text)

    # Read the CSV data
    output = "No match found."
    reader = csv.DictReader(csv_file)
    for row in reader:
        if row['City'].lower() == selected_city.lower():
            output = row['Average Cap Rate']  # Adjust the key if necessary
            break

    # Return the matching output
    return f"The information for {selected_city.capitalize()} is: {output}"
