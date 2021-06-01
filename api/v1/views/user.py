from flask_restful import reqparse, Resource
from sqlalchemy.sql.expression import update
from models.user import Users
from flask import abort, jsonify, make_response, request
from api.v1.app import db
from datetime import datetime
from datetime import timezone
from flask_jwt_extended import (
    get_jwt, create_access_token, create_refresh_token, jwt_required, get_jwt_identity)

# ***************** signup Requirment ****************************** #
signup = reqparse.RequestParser()
signup.add_argument('Email', help='This field cannot be blank', required=True)
signup.add_argument(
    'Password', help='This field cannot be blank', required=True)
signup.add_argument('CIN', help='This field cannot be blank', required=True)
signup.add_argument(
    'FirstName', help='This field cannot be blank', required=True)
signup.add_argument(
    'LastName', help='This field cannot be blank', required=True)
signup.add_argument('Phone', help='This field cannot be blank', required=True)
signup.add_argument(
    'Adresse', help='This field cannot be blank', required=True)
signup.add_argument(
    'PermitId', help='This field cannot be blank', required=True)
#signup.add_argument('PermitValidation', help = 'This field cannot be blank', required = True)
signup.add_argument(
    'CompanyToken', help='This field cannot be blank', required=True)
# ***************** login Requirment ******************************#
login = reqparse.RequestParser()
login.add_argument('Email', help='This field cannot be blank', required=True)
login.add_argument(
    'Password', help='This field cannot be blank', required=True)

update = reqparse.RequestParser()
update.add_argument(
    'FirstName', help='This field cannot be blank', required=True)
update.add_argument(
    'LastName', help='This field cannot be blank', required=True)

# user either company admin or user as client


class Login(Resource):
    """ Login : Post : Login by email and password
        If client not found error  400
        if Client Found and admin Authonticated True Admin else user
        and generate token
    """

    def post(self):
        data = login.parse_args()
        print(data)
        current_user = Users.query.filter_by(email=data['Email']).one_or_none()
        password = request.json.get("Password", None)
        if not current_user:
            return make_response(jsonify({'message': 'User {} doesn\'t exist'.format(data['Email'])}), 400)
        else:
            if current_user.authenticated == 1:
                if current_user.verify_password(password):
                    access_token = create_access_token(
                        identity=current_user.id, additional_claims=current_user.to_dict())
                    refresh_token = create_refresh_token(
                        identity=current_user.id)
                    body = {
                        'User': ' {}'.format(current_user.email),
                        'token': '{}'.format(access_token),
                        'Authonticate': current_user.authenticated
                    }
                    header = {}
                    header['refresh_token'] = refresh_token
                    header['access_token'] = access_token
                    return make_response(jsonify(body), 200, header)
                else:
                    return make_response(jsonify({'message': 'Wrong credentials'}), 400)
            else:
                if current_user.verify_password(password):
                    access_token = create_access_token(
                        identity=current_user.id)
                    refresh_token = create_refresh_token(
                        identity=current_user.id)
                    body = {
                        'User': ' {}'.format(current_user.email),
                        'Client': '{}'.format(current_user.comany_token),
                        'token': '{}'.format(access_token),
                        'Authonticate': current_user.authenticated
                    }
                    header = {}
                    header['refresh_token'] = refresh_token
                    header['access_token'] = access_token
                    print(make_response(jsonify(body), 200, header))
                    return make_response(jsonify(body), 200, header)
                else:
                    return make_response(jsonify({'message': 'Wrong credentials'}), 400)


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        # retrive the user's identity from the refresh token using a Flask-JWT-Extended built-in method
        current_user = get_jwt_identity()
        # return a non-fresh token for the user
        new_token = create_access_token(identity=current_user, fresh=False)
        return make_response(jsonify({'token': new_token}), 201)


class Logout(Resource):
    """
        Revoke token
    """
    @jwt_required()
    def post(self):
        from api.v1.app import TokenBlocklist
        jti = get_jwt()["jti"]
        now = datetime.now(timezone.utc)
        db.session.add(TokenBlocklist(jti=jti, created_at=now))
        db.session.commit()
        return make_response(jsonify(msg="JWT revoked"), 202)


class sign_up(Resource):
    """
    create user :
    """

    def post(self):
        if not request.get_json():
            abort(400, description="Not a JSON")
        data = signup.parse_args()

        if Users.query.filter_by(email=data['Email']).first() is not None:
            abort(400, "user already registred") 
        if Users.query.filter_by(permit_id=data['PermitId']).first() is not None:
            abort(400, "user already registred")
        if Users.query.filter_by(CIN=data['CIN']).first() is not None:
            abort(400, "user already registred")
        #date =  datetime.strptime(data['PermitValidation'], '%a, %d %b %Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        user = Users(email=data['Email'], token=data['CompanyToken'], f_name=data['FirstName'], l_name=data['LastName'],
                     phone=data['Phone'], p_id=data['PermitId'], p_v=datetime.now(), addr=data['Adresse'], cin=data['CIN'])
        user.hash_password(data['Password'])
        user.save_to_db()
        jwt = user.id
        access_token = create_access_token(identity=jwt)
        refresh_token = create_refresh_token(identity=jwt)
        body = {
            'User': ' {}'.format(user.email),
            'Client': '{}'.format(user.comany_token),
            'Authonticate': user.authenticated
        }
        header = {}
        header['refresh_token'] = refresh_token
        header['access_token'] = access_token
        return make_response(jsonify(body), 201, header)


class ClientUserForm(Resource):
    """
        Put : modefie 
        GET : Current user

    """
    @jwt_required()
    def put(self):
        if not request.get_json():
            abort(400, description="Not a JSON")
        current_user_id = get_jwt_identity()
        user = Users.query.filter_by(id=current_user_id).first()
        try:
            data = update.parse_args()
            name = request.json.get('FirstName')
            l_name = request.json.get('LastName')
            user.first_name = name
            user.last_name = l_name
            #user.adresse = request.json.get('adresse')
            #user.car_id = request.json.get('car_id')
            #user.phone = request.json.get('phone')
            #user.permit_id = request.json.get('permit_id')
            #user.permit_validation = request.json.get('permit_validation')
            user.save_to_db()
        except:
            abort(400, description="missing information  or invalid data")
        return make_response(jsonify({"User ": user.email, "Id": user.id}), 201)

    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        user = Users.query.filter_by(id=current_user_id).first()
        return make_response(user.to_dict(), 201)
