from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return "OK"

@app.route("/run", methods=["GET", "POST"])
def run_command():
    output = ""

    if request.method == "POST":
        cmd = request.form.get("command")
        print("CMD RECEIVED:", cmd)

        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout if result.stdout else result.stderr

    return render_template("run_command.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)