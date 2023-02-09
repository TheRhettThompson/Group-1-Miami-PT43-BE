from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

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
        firstname = request.json.get('firstname', None)
        lastname = request.json.get('lastname', None)
        password = request.json.get('password', None)
        email = request.json.get('email', None)
       
        if not firstname:
            return 'First name is required', 401
        if not lastname:
            return 'Last name is required', 401
        if not password:
            return 'Password is required', 401
        if not email:
            return 'Email is required', 401

        email_query = User.query.filter_by(email=email).first()
        if email_query:
            return 'This email already exists' , 402

        user = User()
        user.firstname = firstname 
        user.lastname = lastname 
        user.password = password
        user.email = email 

        db.session.add(user)
        db.session.commit()

        response = {
            'message': 'User added successfully',
            'email': email
        }
        return jsonify(response), 200

# LOGIN
@api.route("/login", methods=["POST"])
@cross_origin()
def login():
    if request.method == 'POST':   
        password = request.json.get('password', None)
        email = request.json.get('email', None)
       
        if not password:
            return 'Password is required', 401
        if not email:
            return 'Email is required', 401

        user = User.query.filter_by(email=email, password=password).first()
        if not user:
            return 'User not found' , 402

        token = create_access_token(identity=user.id)

        response = {
            'message': 'Successfully logged in',
            'token': token
        }
        return jsonify(response), 200

