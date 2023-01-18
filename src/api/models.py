from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#CREATE YOUR DATABASE TABLES HERE
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }
