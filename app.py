from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')

# Handle PostgreSQL URL from Railway
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///ufv_ai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/why-department')
def why_department():
    return render_template('why-department.html')

@app.route('/problem-opportunity')
def problem_opportunity():
    return render_template('problem-opportunity.html')

@app.route('/plan')
def plan():
    return render_template('plan.html')

@app.route('/ai-ethics')
def ai_ethics():
    return render_template('ai-ethics.html')

@app.route('/ai-teaching')
def ai_teaching():
    return render_template('ai-teaching.html')

@app.route('/interface')
def interface():
    return render_template('interface.html')

@app.route('/programming')
def programming():
    return render_template('programming.html')

@app.route('/programming-languages')
def programming_languages():
    return render_template('programming-languages.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == 'POST':
        data = request.json
        new_contact = Contact(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({'message': 'Thank you for your message!'}), 200

@app.route('/get-involved')
def get_involved():
    return render_template('get-involved.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 