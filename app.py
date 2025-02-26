from flask import Flask, render_template
from parser import parse_logs

app = Flask(__name__)

@app.route("/")
def home():
    logs = parse_logs()
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
