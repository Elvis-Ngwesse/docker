from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    raise Exception("Intentional Server Error!")  # Simulates 500 error


# Log 500 errors
@app.errorhandler(500)
def internal_error(error):
    logger.error("500 Internal Server Error: %s", error, exc_info=True)
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
