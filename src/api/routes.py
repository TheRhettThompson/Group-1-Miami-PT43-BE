from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS, cross_origin

api = Blueprint('api', __name__)
CORS(api)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = jsonify(message="Simple server is running")
    response_body.headers.add("Access-Control-Allow-Origin", "*")
    return response_body, 200

# This is where our user registers 
@api.route("/signup", methods=["POST"])
@cross_origin()
def signup():
    if request.method == 'POST':
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        firstname = request.json.get('firstname', None)
        lastname = request.json.get('lastname', None)
        username = request.json.get('username', None)
        validationcode = request.json.get('validationcode', None)
        email = request.json.get('email', None)
        comments = request.json.get('comments', None)
        datejoined = request.json.get('datejoined', None)
        lastlogin = request.json.get('lastlogin', None)
        active = request.json.get('active', None)
       

        if not email:
            return 'Email is required', 401
        if not password:
            return 'Password is required', 401
        
        email_query = User.query.filter_by(email=email).first()
        if email_query:
            return 'This email already exists' , 402

        user = User()
        user.firstname = firstname 
        user.lastname = lastname 
        user.username = username 
        user.password = password
        user.validationcode = validationcode 
        user.email = email 
        user.comments = comments 
        user.datejoined = datejoined 
        user.lastlogin = lastlogin 
        user.active = active 



        user.password = password
        user.is_active = True
        print(user)
        db.session.add(user)
        db.session.commit()

        response = {
            'message': 'User added successfully',
            'email': email
        }
        return jsonify(response), 200

# password
# firstname
# lastname
# username
# validationcode
# email
# comments
# datejoined
# lastlogin
# active
