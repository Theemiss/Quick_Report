from flask import Flask, make_response, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful_swagger import swagger
from dotenv import dotenv_values
config = dotenv_values('.env')
app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='2.8')
jwt = JWTManager(app)



db = SQLAlchemy(app)
migrate = Migrate(app, db)

#app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:55664730@localhost:5432/quick_report'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jztcmnavqvekbf:4e05e1665e4573ddfca5cba53c4788910d5ff6ac306b8a696b15aaa6914c146c@ec2-54-220-170-192.eu-west-1.compute.amazonaws.com:5432/dc3fefsncq4lvc'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'holbieQuickreport'

app.config['JWT_SECRET_KEY'] = 'Qucikreportadmin'



app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


# Callback function to check if a JWT exists in the database blocklist
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header,jwt_payload):
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None


@app.before_first_request
def create_tables():
    db.create_all()


cors = CORS(app, resources={"/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.errorhandler(500)
def special_exception_handler(error):
    return make_response(jsonify({'error': "'Database connection failed'"}), 500)

from api.v1.views import company_route_all

# Public Route for now getting comapny and creating new one
api.add_resource(company_route_all, "/api/hidden")
from api.v1.views import Login, sign_up, Logout, TokenRefresh, ClientUserForm, CompanyAllClient, AdminUserID, CompanyAllRepport

# Authontication
api.add_resource(sign_up, "/api/signup")  # signup
api.add_resource(Login, "/api/login")  # Login
api.add_resource(Logout, "/api/logout")  # Logout
api.add_resource(TokenRefresh, "/api/refresh")  # Token refrecher
# Get Current Logged Client or update user inforamtion
api.add_resource(ClientUserForm, "/api/client")
# Company Action Web
# Get All Client that Belong to this Comapny
api.add_resource(CompanyAllClient, "/api/company/clients")
# Get Client that belong to this comapny by id
api.add_resource(AdminUserID, "/api/company/clients/<id>")
# Get All Report that bellong to current Company
api.add_resource(CompanyAllRepport, '/api/company/reports')
from api.v1.views import NewCar, GetUserCar, NewInsurance, GetClientCarId

# Cars and insurrance Endpoint
api.add_resource(NewInsurance, '/api/insurance/new')  # Create new insurance
api.add_resource(NewCar, '/api/car/new')  # Create new car
# All Car that belong to the current client
api.add_resource(GetUserCar, '/api/client/cars')
# Car by id that belong current Client
api.add_resource(GetClientCarId, '/api/client/cars/<id>')
from api.v1.views import ReportNew, Reportid, ReportPdf, Media, AllMedia

# Rapport Creation and Handling
# Create new Repport or Get All current Client Repport
api.add_resource(ReportNew, '/api/client/report')
# Get repport bellong to current client
api.add_resource(Reportid, '/api/client/report/<id>')
# Create a pdf file from reports
api.add_resource(ReportPdf, '/api/client/report/pdf/<a>')
# Get File image
api.add_resource(Media, "/api/client/report/media/<path:path>")
api.add_resource(AllMedia, "/api/client/report/media")  # List all file media
