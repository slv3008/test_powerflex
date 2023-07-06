from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Factory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sprocket_production_actual = db.Column(db.PickleType)  # This can hold a list of integers
    sprocket_production_goal = db.Column(db.PickleType)  # This can hold a list of integers
    time = db.Column(db.PickleType)  # This can hold a list of integers

class Sprocket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teeth = db.Column(db.Integer)
    pitch_diameter = db.Column(db.Float)
    outside_diameter = db.Column(db.Float)
    pitch = db.Column(db.Float)