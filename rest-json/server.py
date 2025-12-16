# rest-json/server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()
    if not data or 'value' not in data:
        return jsonify({"error": "Missing 'value' field"}), 400
    
    original = data['value']
    reversed_str = original[::-1]
    
    print(f"REST request: '{original}' → '{reversed_str}'")
    return jsonify({"result": reversed_str})

if __name__ == '__main__':
    print("REST/JSON server running on http://localhost:9002")
    app.run(port=9002, debug=False)