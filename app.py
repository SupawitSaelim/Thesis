from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_snmp_data', methods=['GET'])
def get_snmp_data():
    result = subprocess.run(['node', 'static/snmp.js'], capture_output=True, text=True)
    
    return jsonify({'output': result.stdout, 'error': result.stderr})

if __name__ == '__main__':
    app.run(debug=True)
