
from models.car import Car
from models.user import Users
from models.insurance import Insurance
from flask_restful import reqparse, Resource
from flask import abort, jsonify, make_response, request
from datetime import datetime
from flask_jwt_extended import (jwt_required, get_jwt_identity)

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
        Create new Insurance
    """

    def post(self):
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
        Create new Car
    """
    def post(self):
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
        Match User by his car
    """
    @jwt_required()
    def get(self):
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
    """
        Get Current user Car by id
    """
    @jwt_required()
    def get(self, id):
        id_user = get_jwt_identity()
        user = Users.query.filter_by(id=id_user).first()
        Cars = Car.query.filter_by(CIN=user.CIN, id=id).first()
        if Cars is None:
            return make_response(jsonify({'error': 'Not Found'}), 403)
