from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the value from the dropdown
    selected_city = request.form['city']
    
    # Open and read the CSV file
    output = "No match found."
    with open('Cap Rates.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['city'].lower() == selected_city:
                output = row['info']  # Assume 'info' is the corresponding output column in your CSV
                break
    
    # Return the matching output
    return f"The information for {selected_city} is: {output}"

if __name__ == '__main__':
    app.run(debug=True)
