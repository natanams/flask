from . import db
from datetime import datetime

class CommandHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(500))
    output = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
