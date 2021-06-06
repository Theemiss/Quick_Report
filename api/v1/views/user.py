from flask_restful import reqparse, Resource
from sqlalchemy.sql.expression import update
from models.user import Users
from flask import abort, jsonify, make_response, request
from api.v1.app import db
from datetime import datetime
from flask_restful_swagger import swagger
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
    @swagger.operation(
        notes='Login',
        responseClass=Users.__name__,
        nickname=' login',
        parameters=[{
            "name" : "Email",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },{
            "name" : "Password",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }],
        responseMessages=[
            {
              "code": 200,
              "message": "token jwt"
            },
            {
              "code": 400,
              "message": "invalid"
            }
          ]
        )
    def post(self):
        """ Login : Post : Login by email and password
        If client not found error  400
        if Client Found and admin Authonticated True Admin else user
        and generate token
        """
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
                        'token': '{}'.format(access_token),
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
    @swagger.operation(
        notes='refrech token',
        responseClass=Users.__name__,
        nickname=' login',
        parameters=[{
            "name" : "token",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }],
        responseMessages=[
            {
              "code": 200,
              "message": "token jwt"
            },
            {
              "code": 400,
              "message": "invalid"
            }
          ]
        )    
    @jwt_required(refresh=True)
    def post(self):
        """
        return a non-fresh token for the user
        """
        # retrive the user's identity from the refresh token using a Flask-JWT-Extended built-in method
        current_user = get_jwt_identity()
        # return a non-fresh token for the user
        new_token = create_access_token(identity=current_user, fresh=False)
        return make_response(jsonify({'token': new_token}), 201)


class Logout(Resource):

    @swagger.operation(
        notes='Login',
        responseClass=Users.__name__,
        nickname=' login',
        parameters=[{
            "name" : "Token",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }],
        responseMessages=[
            {
              "code": 202,
              "message": "Jwt revoked"
            }
          ]
        )
    @jwt_required()
    def post(self):
        """
        Revoke token and logout
        """
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
    @swagger.operation(
        notes='Login',
        responseClass=Users.__name__,
        nickname=' login',
        parameters=[{
            "name" : "Email",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },{
            "name" : "Password",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
        {
            "name" : "CompanyToken",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
         {
            "name" : "CIN",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
         {
            "name" : "FirstName",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }, {
            "name" : "LastName",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
        {
            "name" : "Adresse",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
        {
            "name" : "Phone",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
         {
            "name" : "PermitId",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }],
        responseMessages=[
            {
              "code": 201,
              "message": "token jwt"
            },
            {
              "code": 400,
              "message": "user already registred"
            }
          ]
        )
    def post(self):
        """
        create user :
        """
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
            'token': '{}'.format(access_token),
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
    @swagger.operation(
        notes='Modefie',
        responseClass=Users.__name__,
        nickname=' modefie ',
        parameters=[{
            "name" : "Token",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }],
        responseMessages=[
            {
              "code": 202,
              "message": "modefied"
            }
          ]
        )
    @jwt_required()
    def put(self):
        """
            Modefie user
        """
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
    @swagger.operation(
        notes='Get Curent User info',
        responseClass=Users.__name__,
        nickname=' modefie ',
        parameters=[{
            "name" : "Token",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }],
        responseMessages=[
            {
              "code": 202,
              "message": "all User info "
            }
          ]
        )
    @jwt_required()
    def get(self):
        """
            Get current logged in info
        """
        current_user_id = get_jwt_identity()
        user = Users.query.filter_by(id=current_user_id).first()
        return make_response(user.to_dict(), 201)
