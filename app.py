
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return """
    <h1>Welcome to my CI/CD project - version 2</h1>
    <p>My first cloud deployment application.</p>
    """


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/api/info")
def info():
    return jsonify({
        "application": "CI/CD Cloud Project",
        "version": "2",
        "framework": "Flask"
    }), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
