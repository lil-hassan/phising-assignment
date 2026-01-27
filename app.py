from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/save-user", methods=["POST"])
def save_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    username = data.get("username")
    password = data.get("password")
    
    # Save directly to text file
    with open("info.txt", "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"Time: {timestamp}\n")
        f.write(f"Username: {username}\n")
        f.write(f"Password: {password}\n")
        f.write("-" * 40 + "\n")

    return jsonify({"message": "Saved successfully"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5500, debug=True)