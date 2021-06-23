
from models.car import Car
from models.user import Users
from models.insurance import Insurance
from flask_restful import reqparse, Resource
from flask import abort, jsonify, make_response, request
from datetime import datetime
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from flask_restful_swagger import swagger
"""
    Car Routes
"""
# --------------------------- Car Data Checker in the Request -------------------------
car_helper = reqparse.RequestParser()
car_helper.add_argument(
    'Mark', help='This field cannot be blank', required=True)
car_helper.add_argument(
    'Type', help='This field cannot be blank', required=True)
car_helper.add_argument(
    'InsuranceId', help='This field cannot be blank', required=True)
car_helper.add_argument(
    'CIN', help='This field cannot be blank', required=True)


class NewInsurance(Resource):
    """
        Create new Insurance Route
    """
    @swagger.operation(
        notes='New Insurance ',
        responseClass=Insurance.__name__,
        nickname=' new Insurance',
        parameters=[{
            "name": "valid",
            "description": "date",
            "required": True,
            "allowMultiple": False,
            "dataType": "DATETIME",
            "paramType": "body"
        }],
        responseMessages=[
            {
                "code": 201,
                "message": "new Insurance"
            },
            {
                "code": 400,
                "message": "Not a JSON"
            },
            {
                "code": 401,
                "message": "missing date"
            }

        ]
    )
    def post(self):
        """
        Create new Insurance Route

            Post Request
            
        """
        if not request.get_json():
            abort(400, description="Not a JSON")
        date = request.json.get("valid", None)
        if date is None:
            abort(401, description="missing date")
        else:
            new = Insurance(date=datetime.now())
            new.save_to_db()
        return make_response(jsonify(new.to_dict()), 201)


class NewCar(Resource):
    """
        Create new Car Route
    """

    @swagger.operation(
        notes='New Car ',
        responseClass=Car.__name__,
        nickname='car  ',
        parameters=[{
            "name": "InsuranceId",
            "description": "id of Insurance",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "body"
        },
            {
            "name": "Type",
            "description": "Type of car",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "body"
        },
            {
            "name": "Mark",
            "description": "Mark of  car",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "body"
        },
            {
            "name": "CIN",
            "description": "CIN of the owner of the car",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "body"
        }],
        responseMessages=[
            {
                "code": 201,
                "message": "new Car info"
            },
            {
                "code": 400,
                "message": "Not a JSON"
            },
            {
                "code": 401,
                "message": "Not a valid insurance id"
            }

        ]
    )
    def post(self):
        """
        Create new Car Route
            Post Request 
        """
        data = car_helper.parse_args()
        inID = Insurance.query.filter_by(id=data['InsuranceId']).first()
        if inID is None:
            return make_response(jsonify({"error": "Not a valid insurance id"}), 401)
        else:
            new = Car(type_c=data["Type"], ins=data['InsuranceId'],
                      mark=data['Mark'], cin=data["CIN"])
            new.save_to_db()
            return make_response(jsonify(new.to_dict()), 201)


class GetUserCar(Resource):
    """
        Match User by his car Route
    """
    @swagger.operation(
        notes='Get current logged user Car ',
        responseClass=Insurance.__name__,
        nickname=' car ',
        parameters=[{
            "name": "Token",
            "description": "jwt token",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "header"
        }],
        responseMessages=[
            {
                "code": 200,
                "message": "all car belong to current logged in user"
            }


        ]
    )
    @jwt_required()
    def get(self):
        """
        Match User by his car Route 
        Get Request 
            
        """
        id_user = get_jwt_identity()
        user = Users.query.filter_by(id=id_user).first()
        Cars = Car.query.filter_by(CIN=user.CIN).all()
        all = {}
        for i in Cars:
            data = i.to_dict()
            key = data['__class__'] + '.' + data['id']
            all[key] = i.to_dict()
        return make_response(jsonify(all), 200)


class GetClientCarId(Resource):

    @swagger.operation(
        notes='Get current logged user Car by id ',
        responseClass=Insurance.__name__,
        nickname='  car',
        parameters=[{
            "name": "Token",
            "description": "jwt token",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "header"
        }],
        responseMessages=[
            {
                "code": 200,
                "message": "car id info"
            },
            {
                "code": 403,
                "message": "Not Found"
            }


        ]
    )
    @jwt_required()
    def get(self, id):
        """
        Get Current user Car by id
        """
        id_user = get_jwt_identity()
        user = Users.query.filter_by(id=id_user).first()
        Cars = Car.query.filter_by(CIN=user.CIN, id=id).first()
        if Cars is None:
            return make_response(jsonify({'error': 'Not Found'}), 403)
