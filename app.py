from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Women Techsters Group A! 🚀"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # 0.0.0.0 makes the app visible outside the machine (or container)
    app.run(host="0.0.0.0", port=5000)
