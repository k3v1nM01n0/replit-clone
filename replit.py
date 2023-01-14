from flask import Flask, request
import subprocess
import json


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/run_code', methods=['POST'])
def run_code():

    code = request.get_json()['code']
    language = request.get_json()['language']

    try:

        if language == 'python':
            result = subprocess.run(
                ['python', '-c', code], capture_output=True, text=True)

        elif language == 'go':
            with open('main.go', 'w') as f:
                f.write(code)
            result = subprocess.run(
                ['go', 'run', 'main.go'], capture_output=True, text=True)
                
        response = {'output': result.stdout, 'error': result.stderr}
        return json.dumps(response), 200

    except subprocess.CalledProcessError as e:
        return json.dumps({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5004)
