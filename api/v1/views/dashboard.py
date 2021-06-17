
from api.v1.views.ClientRapport import Reportid
from models.car import Car
from models.comapny import Company
from models.user import Users
from models.RapportMatcher import RapportCar
from models.report import Report
from flask_restful import reqparse, Resource
from flask import abort, jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful_swagger import swagger



class FetchCar(Resource):
    @jwt_required()
    def get(self,id):
        car = Car.query.filter_by(id=id).first()
        if car is None:
            return make_response(jsonify({"message": "Not found"}),401)
        else:
            return make_response(jsonify(car.to_dict()),200)


class Dashboard(Resource):
    @jwt_required()
    def get(self):
        admin_id = get_jwt_identity()
        admin = Users.query.filter_by(id=admin_id).first()
        user_count = Users.query.filter_by(comany_token=admin.comany_token).count()
        report_count = Report.query.filter_by(compnay_id=admin.compnay_token).count()
        Count = {"user" : user_count,"report":report_count}
        return make_response(jsonify(Count),200)

def builderSingle(rapportid, carid, clientid):
    """
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
    @jwt_required()
    def get(self,id):
        data = RapportCar.query.filter_by(CAR_A=id).first()
        if data is not None:
            report = Report.query.filter_by(id=data.Car_B).first()
            if report is None:
                return make_response(jsonify({}),200)
            else:
                new_data = builderSingle(report, report.car_id, report.client_id)
                return make_response(jsonify(new_data),200)
        else:
           return make_response(jsonify({}),201)
