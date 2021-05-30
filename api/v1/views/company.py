
from models.car import Car
from models.comapny import Company
from models.user import Users
from models.report import Report
from flask_restful import reqparse, Resource
from flask import abort, jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

rapport = reqparse.RequestParser()
rapport.add_argument('Email', help='This field cannot be blank', required=True)


class company_route_all(Resource):
    """
        Create new company : Post
        List all companys : GET
    """

    def post(self):
        if not request.get_json():
            abort(400, description="Not a JSON")
        name = request.json.get('name')
        if name is None:
            abort(400, "missing arguments")  # missing arguments
        if Company.query.filter_by(name=name).first() is not None:
            abort(400, "company already registred")  # existing user
        company = Company(name=name)
        company.save_to_db()
        return make_response(jsonify({"comapny ": company.name, "id": company.id}), 201)

    def get(self):
        all = Company.query.all()
        companys = {}
        for x in all:
            data = x.to_dict()
            key = x.__class__ + '.' + x.id
            companys[key] = data
        return make_response(jsonify(companys), 200)


class CompanyAllClient(Resource):
    """
        All Client  to this company if admin 
    """
    @jwt_required()
    def get(self):
        id = get_jwt_identity()
        admin = Users.query.filter_by(id=id).first()
        if admin.authenticated == True:
            users = Users.query.filter_by(
                comany_token=admin.comany_token).all()
            all_users = {}
            for i in users:
                value = i.to_dict()
                if value['authenticated'] == 0:
                    key = value['__class__'] + "." + value['id']
                    all_users[key] = value
            return make_response(jsonify(all_users), 200)
        else:
            abort(400, "You are not an admin")


class AdminUserID(Resource):
    """
        Get specific user by id
    """
    @jwt_required()
    def get(self, id):
        Admin_id = get_jwt_identity()
        admin = Users.query.filter_by(id=Admin_id).first()
        if admin.authenticated == True:
            user = Users.query.filter_by(id=id).first()
            if user is not None:
                return make_response(jsonify(user.to_dict()), 200)
            else:
                return make_response(jsonify({"error": "Client not found"}), 401)
        else:
            return make_response(jsonify({"error": "permission denied"}), 401)


def repport_builder(cls, client, car):
    user = Users.query.filter_by(id=client).first()
    car = Car.query.filter_by(id=car, CIN=user.CIN).first()
    data = {**user.to_dict(), **car.to_dict(), "DriverName": cls.driver_name}
    del data['__class__']
    del data['authenticated']
    return data


class CompanyAllRepport(Resource):
    @jwt_required()
    def get(self):
        id = get_jwt_identity()
        admin = Users.query.filter_by(id=id).first()
        if admin.authenticated == True:
            report = Report.query.filter_by(
                compnay_id=admin.comany_token).all()
            all_report = {}
            for i in report:
                try:
                    value = i.to_dict()
                    if value['authenticated'] == 0:
                        key = i.id
                        all_report[key] = repport_builder(
                            i, i.client_id, i.car_id)
                except:
                    abort(400)
            return make_response(jsonify(all_report), 200)
