from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def form():
    # A simple form with a dropdown
    return render_template_string('''
        <form action="/submit" method="post">
            <select name="city">
              <option value="losangeles">Los Angeles</option>
              <option value="pheonix">Phoenix</option>
              <option value="chicago">Chicago</option>
              <option value="houston">Houston</option>
              <option value="newyork">New York</option>
            </select>
            <input type="submit">
        </form>
    ''')
    
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
                output = row['Average Cap Rate']  # Assume 'info' is the corresponding output column in your CSV
                break
    
    # Return the matching output
    return f"The information for {selected_city} is: {output}"

if __name__ == '__main__':
    app.run(debug=True)
