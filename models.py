from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    manager_id = db.Column(db.Integer, nullable=False)
    strengths = db.Column(db.Text, nullable=False)
    improvements = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'manager_id': self.manager_id,
            'strengths': self.strengths,
            'improvements': self.improvements,
            'sentiment': self.sentiment
        }