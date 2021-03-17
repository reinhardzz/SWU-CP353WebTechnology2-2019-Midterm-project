from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class students(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    studentID = db.Column(db.Integer, nullable=False)
    studentimage = db.Column(db.String(255))