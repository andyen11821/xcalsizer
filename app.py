import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    selected_city = request.form['city']
    output = "No match found."
    try:
        with open('Cap Rates.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # This will strip extra whitespace from headers and values
                row = {k.strip(): v.strip() for k, v in row.items()}
                # Adjust the key here to match your CSV header
                if row['City'].strip().lower() == selected_city.lower():
                    output = row['Average Cap Rate']
                    break
    except csv.Error as e:
        output = f"Error reading CSV file: {e}"
    except KeyError as e:
        output = f"Column not found in CSV file: {e}"
    except Exception as e:
        output = f"An unexpected error occurred: {e}"

    # Return the matching output or an error message
    return f"The information for {selected_city.capitalize()} is: {output}"

if __name__ == '__main__':
    app.run(debug=True)
