import json
from flask import Flask, request


webserver = Flask(__name__)


@webserver.route('/', methods=['GET'])
def main():
    return 'Welcome to the Flask web server!'


@webserver.route('/api', methods=['POST'])
def test_api():
    req_data = request.get_json()
    return json.dumps(req_data)


if __name__ == '__main__':
    webserver.run(host='0.0.0.0', debug=True)
