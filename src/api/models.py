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

class Favorites(db.Model):
    __tablename__ = "favorites"
    user_id = db.Column(db.Integer, db.ForeignKey(User.id),nullable=False)
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    job_title_text = db.Column(db.String(120), nullable=False)
    location_name = db.Column(db.String(120), nullable=False)

        
    def __repr__(self):
        return f'<Favorites {self.user_id}>'

    def serialize(self):
        return {
            "user_id": self.user_id,
            "id": self.id,
            "job_title_text": self.job_title_text,
            "location_name": self.location_name
            
        }
