from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Device emulation running.'

@app.route('/data')
def data():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)