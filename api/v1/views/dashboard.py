
from models.car import Car
from models.user import Users
from models.RapportMatcher import ReportCar
from models.report import Report
from flask_restful import  Resource
from flask import  jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
"""
    Admin Dashboard Route
"""


class FetchCar(Resource):
    """
        Fetch User Single Car Route
    """
    @jwt_required()
    def get(self, id):
        car = Car.query.filter_by(id=id).first()
        if car is None:
            return make_response(jsonify({"message": "Not found"}), 401)
        else:
            return make_response(jsonify(car.to_dict()), 200)


class Dashboard(Resource):
    """
        Dashboard Statics Route
    """
    @jwt_required()
    def get(self):
        admin_id = get_jwt_identity()
        admin = Users.query.filter_by(id=admin_id).first()
        print(admin.to_dict())
        user_count = Users.query.filter_by(
            comany_token=admin.comany_token, authenticated=False).count()
        report_count = Report.query.filter_by(
            compnay_id=admin.comany_token).count()
        Count = {"user": user_count, "report": report_count}
        return make_response(jsonify(Count), 200)


def builderSingle(rapportid, carid, clientid):
    """
        Build A Report
    """
    report_info = rapportid.to_dict()
    del report_info['__class__']
    del report_info['compnay_id']
    Car_info = Car.query.filter_by(id=carid).first().to_dict()
    del Car_info['id']
    del Car_info['created_at']
    del Car_info["updated_at"]
    client_info = Users.query.filter_by(id=clientid).first().to_dict()
    del client_info['id']
    del client_info['created_at']
    del client_info["updated_at"]
    data = {**report_info, **Car_info, **client_info}
    return data


class GetBReport(Resource):
    """
        Get Car B information 
    """
    @jwt_required()
    def get(self, id):
        data = ReportCar.query.filter_by(CAR_A=id,).first()
        if data is not None:
            report = Report.query.filter_by(id=data.CAR_B).first()
            if report is None:
                return make_response(jsonify({}), 200)
            else:
                new_data = builderSingle(
                    report, report.car_id, report.client_id)
                return make_response(jsonify(new_data), 200)
        else:
            return make_response(jsonify({}), 201)


class AllClientCar(Resource):
    """
        Get  a Client all  Cars
    """
    @jwt_required()
    def get(self, id):
        user = Users.query.filter_by(id=id).first()
        if user is not None:
            cars = Car.query.filter_by(CIN=user.CIN).all()
            if cars is None:
                return make_response(jsonify({}), 200)
            else:
                car = {}
                for x in cars:
                    data = x.to_dict()
                    key = key = data['__class__'] + '.' + data['id']
                    car[key] = data
                return make_response(jsonify(car), 200)
        else:
            return make_response(jsonify({}), 400)
