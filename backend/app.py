from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

#Allows request from any origin
CORS(app)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hi from back!"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)