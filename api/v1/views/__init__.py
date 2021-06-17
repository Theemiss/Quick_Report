
from api.v1.views.user import Login, sign_up, TokenRefresh, Logout, ClientUserForm
from api.v1.views.company import company_route_all, CompanyAllClient, AdminUserID, CompanyAllRepport, CompanySingleRapport
from api.v1.views.car import NewCar, NewInsurance, GetUserCar, GetClientCarId
from api.v1.views.ClientRapport import ReportNew, Reportid, ReportPdf, Media, AllMedia, MatcherA, MatcherB
from api.v1.views.dashboard import FetchCar,Dashboard,GetBReport,AllClientCar