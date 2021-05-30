
import os
from models.car import Car
from models.comapny import Company
from models.user import Users
from models.report import Report
from flask_restful import reqparse, Resource
from flask import abort, jsonify, make_response, request, render_template, make_response, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
import pdfkit
from models.RapportMatcher import RapportCar

UPLOAD_DIRECTORY = "media"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


class AllMedia(Resource):
    def get(self):
        """Endpoint to list files on the server."""
        files = []
        for filename in os.listdir(UPLOAD_DIRECTORY):
            path = os.path.join(UPLOAD_DIRECTORY, filename)
            if os.path.isfile(path):
                files.append(filename)
        return jsonify(files)


class Media(Resource):
    def get(self, path):
        return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

    def post(self, filename):

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

pdf_reader = reqparse.RequestParser()
pdf_reader.add_argument(
    'CarA', help='This field cannot be blank', required=True)
pdf_reader.add_argument(
    'CarB', help='This field cannot be blank', required=True)


class ReportNew(Resource):
    @jwt_required()
    def post(self):
        client_id = get_jwt_identity()
        data = rapport.parse_args()
        user = Users.query.filter_by(id=client_id).first()
        rp = Report(driver=data['DriverName'], client=client_id,
                    car=data['CarId'], company_id=user.comany_token)
        rp.save_to_db()
        return make_response(jsonify(rp.to_dict()), 201)

    @jwt_required()
    def get(self):
        client_id = get_jwt_identity()
        user = Users.query.filter_by(id=client_id).first()
        all_report = Report.query.filter_by(client_id=client_id).all()
        all = {}
        for i in all_report:
            key = i.id
            all[key] = repport_builder(i, i.client_id, i.car_id)
        return make_response(jsonify(all), 200)


def repport_builder(cls, client, car):
    user = Users.query.filter_by(id=client).first()
    car = Car.query.filter_by(id=car, CIN=user.CIN).first()
    data = {**user.to_dict(), **car.to_dict(), "DriverName": cls.driver_name}
    del data['__class__']
    del data['authenticated']
    return data


class Reportid(Resource):
    @jwt_required()
    def get(self, id):
        client_id = get_jwt_identity()
        user = Users.query.filter_by(id=client_id).first()
        report = Report.query.filter_by(client_id=client_id, id=id).first()
        data = repport_builder(report, report.client_id, report.car_id)
        return make_response(jsonify(data), 200)


class ReportPdf(Resource):
    def get(self, a):
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
            pdf = pdfkit.from_string(render, False)
            response = make_response(pdf)
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = 'attachent; filename={}.pdf'.format(
                a)
            return response
        except:
            return abort(500)
