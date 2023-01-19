from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#CREATE YOUR DATABASE TABLES HERE
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True),
    firstname = db.Column(db.String(120), primary_key=False, nullable=False),
    lastname = db.Column(db.String(120), primary_key=False, nullable=False),
    username = db.Column(db.String(120), primary_key=False, nullable=False),
    password = db.Column(db.String(120), primary_key=False, nullable=False),
    validationcode = db.Column(db.String(120), primary_key=False, nullable=False),
    email = db.Column(db.String(120), primary_key=False, nullable=False),
    comments = db.Column(db.String(250), primary_key=False, nullable=True),
    datejoined = db.Column(db.Date, primary_key=False, nullable=True),
    lastlogin = db.Column(db.Date, primary_key=False, nullable=True),
    active = db.Column(db.Boolean, primary_key=False, nullable=True),


    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "first name" :
            # do not serialize the password, its a security breach
        }
