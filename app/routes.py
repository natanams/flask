from flask import Blueprint, render_template, request
import subprocess
from .models import CommandHistory
from . import db


main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/run", methods=["GET", "POST"])
def run_command():
    output = ""

    if request.method == "POST":
        cmd = request.form.get("command")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout if result.stdout else result.stderr

        # Save to DB
        entry = CommandHistory(command=cmd, output=output)
        db.session.add(entry)
        db.session.commit()

    return render_template("run_command.html", output=output)

@main.route("/history")
def history():
    records = CommandHistory.query.order_by(CommandHistory.timestamp.desc()).all()
    return render_template("history.html", records=records)
