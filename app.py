"""."""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """Home page."""
    return "Hello world"


if __name__ == '__main__':
    app.run(port=8000, debug=True)