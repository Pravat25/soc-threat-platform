from flask import Flask, render_template
from detection.detector import analyze_logs

app = Flask(__name__)

def read_logs():
    try:
        with open("logs/sample.log", "r") as f:
            logs = f.readlines()[::-1]
    except:
        logs = ["No logs found"]

    return logs


@app.route("/")
def home():
    logs = read_logs()
    processed_logs, stats, top_ip, top_count = analyze_logs(logs)

    return render_template(
        "index.html",
        logs=processed_logs,
        stats=stats,
        top_ip=top_ip,
        top_count=top_count
    )


if __name__ == "__main__":
    app.run(debug=True)
