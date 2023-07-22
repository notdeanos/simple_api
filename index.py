
# Dean Mcdonald <dean@appdome.com>
# Simple API to be used for Mobile Bot Defense Demo


import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Enable logging and set log level to DEBUG
app.logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()  # get data from POST request
    if not data:
        return jsonify({'message': 'No input data provided'}), 400  # bad request

    # check if the data meets your criteria
    # here as an example, I check if the data has a "key" field with a value "value"
    if data.get('appdome') == 'appdo.me123':
        return jsonify({'message': 'Success'}), 201  # 201 OK
    else:
        return jsonify({'message': 'Request Failed'}), 400  # bad request


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3002, debug=True)