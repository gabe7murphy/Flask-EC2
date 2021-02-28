from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

class Employee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    items = db.relationship('Item', backref='author', lazy=True)

    def __repr__(self):
        return f"Employee('{self.username}')"


class Item(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(30), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    employee_id = db.Column(db.Integer, db.ForeignKey(
        'employee.id'), nullable=False)

    def __repr__(self):
        return f"Item('{self.label}','{self.date_added}')"