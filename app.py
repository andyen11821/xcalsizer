from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_cap_rates', methods=['POST'])
def get_cap_rates():
    city = request.form.get('city')
    return f'Cap rates for {city} are currently unavailable.'

if __name__ == '__main__':
    app.run(debug=True)
