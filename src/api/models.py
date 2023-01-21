from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#CREATE YOUR DATABASE TABLES HERE
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120),  nullable=False)
    password = db.Column(db.String(120),  nullable=False)
    validationcode = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    comments = db.Column(db.String(250), nullable=True)
    datejoined = db.Column(db.Date, nullable=True)
    lastlogin = db.Column(db.Date, nullable=True)
    active = db.Column(db.Boolean, nullable=True)


    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname, 
            "username": self.username, 
            "validationcode": self.validationcode, 
            "email": self.email, 
            "comments": self.comments,
            "datejoined": self.datejoined, 
            "lastlogin": self.lastlogin, 
            "active": self.active

           
            # do not serialize the password, its a security breach
        }
