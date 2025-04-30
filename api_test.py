from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, Flask!'})

@app.route('/status')
def status():
    return jsonify({'status': 'Running', 'uptime': '99.99%'})

if __name__ == '__main__':
    app.run(debug=True)
