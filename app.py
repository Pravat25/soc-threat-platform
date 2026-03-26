from flask import Flask, render_template

app = Flask(__name__)

def read_logs():
    try:
        with open("logs/sample.log", "r") as f:
            logs = f.readlines()[::-1]  # latest first
    except:
        logs = ["No logs found"]

    return logs


@app.route("/")
def home():
    logs = read_logs()
    return render_template("index.html", logs=logs)


if __name__ == "__main__":
    app.run(debug=True)
