
# Dean Mcdonald <dean@appdome.com>

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()  # get data from POST request
    if not data:
        return jsonify({'message': 'No input data provided'}), 400  # bad request

    # check if the data meets your criteria
    # here as an example I check if the data has a "key" field with a value "value"
    if data.get('key') == 'value':
        return jsonify({'message': 'Success'}), 201  # 201 OK
    else:
        return jsonify({'message': 'Invalid input data'}), 400  # bad request

if __name__ == "__main__":
    app.run(debug=True)

