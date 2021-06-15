
from datetime import datetime
import os
from models.car import Car
from models.comapny import Company
from models.feedback import Feedback
from models.user import Users
from models.report import Report
from flask_restful import reqparse, Resource
from flask import abort, json, jsonify, make_response, request, render_template, make_response, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
import pdfkit
from models.RapportMatcher import RapportCar
from flask_restful_swagger import swagger
#from flask_wkhtmltopdf import Wkhtmltopdf

UPLOAD_DIRECTORY = "media"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


class AllMedia(Resource):
    @swagger.operation(
        notes='Get files ',
        responseClass=Report.__name__,
        nickname='  files',
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
                "message": "all file in server"
            }


        ]
    )
    def get(self):
        """Endpoint to list files on the server."""
        files = []
        for filename in os.listdir(UPLOAD_DIRECTORY):
            path = os.path.join(UPLOAD_DIRECTORY, filename)
            if os.path.isfile(path):
                files.append(filename)
        return jsonify(files)


class Media(Resource):
    @swagger.operation(
        notes='get  file ',
        responseClass=Report.__name__,
        nickname='  get a file',
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
                "message": "file"
            }


        ]
    )
    def get(self, path):
        """
            get file
        """
        return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

    @swagger.operation(
        notes='send  file ',
        responseClass=Report.__name__,
        nickname='  send a file',
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
                "message": "transfered"
            }


        ]
    )
    def post(self, filename):
        """
            send a file
        """
        if "/" in filename:
            # Return 400 BAD REQUEST
            abort(400, "no subdirectories allowed")

        with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
            fp.write(request.data)

        # Return 201 CREATED
        return make_response(jsonify({"File": "added"}), 201)


rapport = reqparse.RequestParser()
rapport.add_argument(
    'DriverName', help='This field cannot be blank', required=True)
rapport.add_argument('CarId', help='This field cannot be blank', required=True)
rapport.add_argument(
    'DriverLastName', help='This field cannot be blank', required=True)
rapport.add_argument(
    'DriverPermit', help='This field cannot be blank', required=True)
rapport.add_argument('DriverPermitValidation',
                     help='This field cannot be blank', required=True)
rapport.add_argument(
    'DriverAdresse', help='This field cannot be blank', required=True)


pdf_reader = reqparse.RequestParser()
pdf_reader.add_argument(
    'CarA', help='This field cannot be blank', required=True)
pdf_reader.add_argument(
    'CarB', help='This field cannot be blank', required=True)


class ReportNew(Resource):
    """
        Create new rapport
    """
    @swagger.operation(
        notes='Create new repport  ',
        responseClass=Report.__name__,
        nickname='  new  a repport',
        parameters=[{
            "name": "Token",
            "description": "jwt token",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "header"
        }, {
            "name": "DriverName",
            "description": "DriverName",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
            {
            "name": "CarId",
            "description": "CarId",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }, {
            "name": "DriverLastName",
            "description": " DriverLastName",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
            {
            "name": "DriverAdresse",
            "description": "DriverAdresse",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
            {
            "name": "DriverPermit",
            "description": "DriverPermit",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        },
            {
            "name": "DriverPermitValidation",
            "description": "DriverPermitValidation",
            "required": True,
            "allowMultiple": False,
            "dataType": "date",
            "paramType": "body"
        },
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "rapport created info"
            }


        ]
    )
    @jwt_required()
    def post(self):
        """
            Create new repport
        """
        client_id = get_jwt_identity()
        data = rapport.parse_args()
        user = Users.query.filter_by(id=client_id).first()
        rp = Report(driver=data['DriverName'], client=client_id,
                    car=data['CarId'], company_id=user.comany_token, l_name=data['DriverLastName'], addr=data['DriverAdresse'], per=data['DriverPermit'], per_v=datetime.utcnow())  # data['DriverPermitValidation']
        rp.save_to_db()
        return make_response(jsonify(rp.to_dict()), 201)

    @swagger.operation(
        notes='get all report belong to this User ',
        responseClass=Report.__name__,
        nickname='all report',
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
                "message": "ALL report info"
            }


        ]
    )
    @jwt_required()
    def get(self):
        """
            Get all raport belong to this client
        """
        client_id = get_jwt_identity()
        user = Users.query.filter_by(id=client_id).first()
        all_report = Report.query.filter_by(client_id=client_id).all()
        all = {}
        for i in all_report:
            key = i.id
            all[key] = repport_builder(i, i.client_id, i.car_id)
        return make_response(jsonify(all), 200)


def repport_builder(cls, client, car):
    """
        Build a rapport dict
    """
    user = Users.query.filter_by(id=client).first()
    car = Car.query.filter_by(id=car, CIN=user.CIN).first()
    data = {**user.to_dict(), **car.to_dict(), "DriverName": cls.driver_name}
    del data['__class__']
    del data['authenticated']
    return data


class Reportid(Resource):
    """
        Get Rapport by id
    """
    @swagger.operation(
        notes='get repport by id  belong to this User ',
        responseClass=Report.__name__,
        nickname=' report',
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
                "message": "one  report info"
            },
            {
                "code": 400,
                "message": "not found"
            }


        ]
    )
    @jwt_required()
    def get(self, id):
        """
            get Rapport by id
        """
        client_id = get_jwt_identity()
        user = Users.query.filter_by(id=client_id).first()
        report = Report.query.filter_by(client_id=client_id, id=id).first()
        if report is not None:
            data = repport_builder(report, report.client_id, report.car_id)
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify({}), 200)


class ReportPdf(Resource):
    @swagger.operation(
        notes='Generate pdf',
        responseClass=Report.__name__,
        nickname=' report',
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
                "message": "pdf file"
            },
            {
                "code": 400,
                "message": "invalid"
            }


        ]
    )
    def get(self, a):
        """
            Generate pdf file for the rapport
        """
        try:
            rapportmatcher = RapportCar.query.filter_by(id=a).first()
            CarA = Report.query.filter_by(id=rapportmatcher.CAR_A).first()
            CarB = Report.query.filter_by(id=rapportmatcher.CAR_B).first()
            CompanyA = Company.query.filter_by(id=CarA.compnay_id).first()
            CompanyB = Company.query.filter_by(id=CarB.compnay_id).first()

            ClientA = Users.query.filter_by(id=CarA.client_id).first()
            ClientB = Users.query.filter_by(id=CarB.client_id).first()
            ClientCarA = Car.query.filter_by(id=CarA.car_id).first()
            ClientCarB = Car.query.filter_by(id=CarB.car_id).first()
            Client1 = {**ClientA.to_dict(), **ClientCarA.to_dict(),
                       **CompanyA.to_dict()}

            del Client1['__class__']
            del Client1['updated_at']
            del Client1['created_at']

            del Client1['insurred']
            del Client1['comany_token']
            del Client1['authenticated']
            Client2 = {**ClientB.to_dict(), **ClientCarB.to_dict(),
                       **CompanyB.to_dict()}

            del Client2['__class__']
            del Client2['updated_at']
            del Client2['created_at']
            del Client2['insurred']
            del Client2['comany_token']
            del Client2['authenticated']

            render = render_template("constat.html", ClientA=Client1, ClientB=Client2,
                                     DriverA=CarA.driver_name, DriverB=CarB.driver_name)
            pdf = pdfkit.from_string(render)
            print("response")
            response = make_response(pdf)

            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = 'attachent; filename={}.pdf'.format(
                a)

            return response
        except:
            return make_response(jsonify({"error": "failed"}), 402)


feedback = reqparse.RequestParser()
feedback.add_argument(
    'Descreption', help='This field cannot be blank', required=True)
feedback.add_argument(
    'Report', help='This field cannot be blank', required=True)


class NewFeedBack(Resource):
    @swagger.operation(
        notes='Feedback create ',
        responseClass=Feedback.__name__,
        nickname=' Feedback',
        parameters=[{
            "name": "Token",
            "description": "jwt token",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "header"
        }, {
            "name": "Report",
            "description": "report id",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }, {
            "name": "Descreption",
            "description": "Descreption ",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"
        }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "new feedback "
            },
            {
                "code": 400,
                "message": "invalid"
            }


        ]
    )
    @jwt_required()
    def post(self):
        """
            Create new feedback by admin
        """
        admin_id = get_jwt_identity()
        admin = Users.query.filter_by(id=admin_id).first()
        data = feedback.parse_args()
        repport_id = Report.query.filter_by(id=data['Report']).first()
        if repport_id is None:
            return make_response(jsonify({'error': "Wrong Information"}), 401)
        else:
            new_feedback = Feedback(
                description=data['Descreption'], rapport=data['Report'])
            new_feedback.save_to_db()
        make_response(jsonify(new_feedback.to_dict()), 201)


class MatcherA(Resource):
    @jwt_required()
    def post(self):
        user = get_jwt_identity()
        Matcher = reqparse.RequestParser()
        Matcher.add_argument(
            'car_a', help='This field cannot be blank', required=True)
        data = Matcher.parse_args()
        new = RapportCar(a=data['car_a'])
        new.save_to_db()
        return make_response(jsonify({"id": new.id}), 200)


class MatcherB(Resource):
    """
    """
    @jwt_required()
    def post(self):
        user = get_jwt_identity()
        Matcher = reqparse.RequestParser()
        Matcher.add_argument(
            'car_b', help='This field cannot be blank', required=True)
        Matcher.add_argument(
            'id', help='This field cannot be blank', required=True)
        data = Matcher.parse_args()
        report = RapportCar.query.filter_by(id=data['id']).first()
        report.CAR_B = data['car_b']
        report.save_to_db()
        return make_response(jsonify({"id": report.id}), 200)
