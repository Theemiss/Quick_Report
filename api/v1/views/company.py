
from api.v1.views.ClientRapport import Reportid
from models.car import Car
from models.comapny import Company
from models.user import Users
from models.report import Report
from flask_restful import reqparse, Resource
from flask import abort, jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful_swagger import swagger
rapport = reqparse.RequestParser()
rapport.add_argument('Email', help='This field cannot be blank', required=True)


class company_route_all(Resource):
    @swagger.operation(
        notes='create a company',
        responseClass=Company.__name__,
        nickname='create',
        parameters=[
            {
              "name": "name",
              "description": "company name.",
              "required": True,
              "allowMultiple": False,
              "dataType": "string",
              "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 201,
                "message": {"name": "name"}
            },
            {
                "code": 400,
                "message": "missing arguments or company already registred"
            }
        ]
    )
    def post(self):
        """
        New company
        """
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

    @swagger.operation(
        notes='get  all company',
        responseClass=Company.__name__,
        nickname='all company',
        responseMessages=[
            {
              "code": 201,
              "message": "all company"
            },
            {
                "code": 400,
                "message": "missing arguments or company already registred"
            }
        ]
    )
    def get(self):
        """
        Get All company
        """
        all = Company.query.all()
        companys = {}
        for x in all:
            data = x.to_dict()
            key = key = data['__class__'] + '.' + data['id']
            companys[key] = data
        return make_response(jsonify(companys), 200)


class CompanyAllClient(Resource):
    """
        All Client  to this company if admin
    """
    @swagger.operation(
        notes='get  all client to this company you need jwt required',
        responseClass=Users.__name__,
        nickname='all Client belong to company',
        parameters=[{
            "name": "token",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "header"
        }],
        responseMessages=[
            {
                "code": 200,
                "message": "all client"
            },
            {
                "code": 400,
                "message": "you are not admin"
            }
        ]
    )
    @jwt_required()
    def get(self):
        """
        All Client  to this company if admin
        """
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

    @swagger.operation(
        notes='get  a client belong to this company you need jwt required',
        responseClass=Users.__name__,
        nickname=' Client belong to company',
        parameters=[{
            "name": "token",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "header"
        }],
        responseMessages=[
            {
                "code": 200,
                "message": "Client"
            },
            {
                "code": 400,
                "message": "you are not admin"
            }
        ]
    )
    @jwt_required()
    def get(self, id):
        """
        Get specific user by id
        """
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
    user = Users.query.filter_by(id=client).first().to_dict()
    if (user["authenticated"]) == False:
        car = Car.query.filter_by(id=car, CIN=user["CIN"]).first()
        rapport = cls.to_dict()
        data = {**user, **car.to_dict(), **rapport}
        del data['__class__']
        del data['comany_token']
        del data['authenticated']
        return data


class CompanyAllRepport(Resource):

    @swagger.operation(
        notes='get  a rapport belong to this company you need jwt required',
        responseClass=Report.__name__,
        nickname=' Client belong to company',
        parameters=[{
            "name": "token",
            "description": "autho",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "header"
        }],
        responseMessages=[
            {
                "code": 200,
                "message": "all report"
            },
            {
                "code": 400,
                "message": "you are not admin"
            }
        ]
    )
    @jwt_required()
    def get(self):
        """
        Get All rapport belong to company
        """
        admin_id = get_jwt_identity()
        admin = Users.query.filter_by(id=admin_id).first()
        if admin.authenticated == True:

            report = Report.query.filter_by(
                compnay_id=admin.comany_token).all()
            all_report = {}
            for i in report:
                try:
                    value = repport_builder(
                        i, i.client_id, i.car_id)
                    key = i.id
                    all_report[key] = value
                except:
                    return make_response(jsonify({"error": "Failed"}), 401)
            return make_response(jsonify(all_report), 200)
        else:
            return make_response(jsonify({"error": "Failed"}), 401)
def builderSingle(rapportid,carid,clientid):
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
    data = {**report_info,**Car_info,**client_info}
    return data


class CompanySingleRapport(Resource):
    @swagger.operation(
        notes='get  a rapport belong to this company you need jwt required',
        responseClass=Report.__name__,
        nickname=' Client belong to company',
        parameters=[{
              "name": "token",
              "description": "autho",
              "required": True,
              "allowMultiple": False,
              "dataType": "string",
              "paramType": "header"
            }],
        responseMessages=[
            {
                  "code": 200,
                  "message": "all report"
              },
            {
                  "code": 400,
                  "message": "you are not admin"
              }
            ]
    )
    @jwt_required()
    def get(self, id):
        Admin_id = get_jwt_identity()
        admin = Users.query.filter_by(id=Admin_id).first()
        if admin.authenticated == True:
            report = Report.query.filter_by(id=id).first()
            if report is not None:
                data = builderSingle(report,report.car_id,report.client_id)
                return make_response(jsonify(data), 200)
            else:
                return make_response(jsonify({"error": "Report not found"}), 401)
        else:
            return make_response(jsonify({"error": "permission denied"}), 401)
