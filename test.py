app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
