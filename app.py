from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, User, Feedback
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], role=data['role']).first()
    if user:
        return jsonify({"message": "Login successful", "user_id": user.id, "role": user.role})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/feedback/<int:employee_id>', methods=['GET', 'POST'])
def manage_feedback(employee_id):
    if request.method == 'POST':
        data = request.json
        feedback = Feedback(
            employee_id=employee_id,
            manager_id=data['manager_id'],
            strengths=data['strengths'],
            improvements=data['improvements'],
            sentiment=data['sentiment']
        )
        db.session.add(feedback)
        db.session.commit()
        return jsonify({"message": "Feedback added"})
    else:
        feedbacks = Feedback.query.filter_by(employee_id=employee_id).all()
        return jsonify([f.serialize() for f in feedbacks])

if __name__ == '__main__':
    app.run(debug=True)