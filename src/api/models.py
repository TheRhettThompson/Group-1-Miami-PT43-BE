from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#CREATE YOUR DATABASE TABLES HERE
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120), unique = False, nullable=False)
    lastname = db.Column(db.String(120), unique = False, nullable=False)
    password = db.Column(db.String(120), unique = False,  nullable=False)
    email = db.Column(db.String(120), unique = True, nullable=False)
    
    


    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,

           
            # do not serialize the password, its a security breach
        }
