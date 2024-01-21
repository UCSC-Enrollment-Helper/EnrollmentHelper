from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import subprocess
from professor_stats import run

app = Flask(__name__)
CORS(app)

@app.route('/run_python_script')
@cross_origin()
def run_python_script():
    try:
        value = request.args.get('param_name')
        result = run(value)
        response_data = {'success': True, 'result': result}
    except subprocess.CalledProcessError as e:
        response_data = {'success': False, 'error': str(e)}

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)