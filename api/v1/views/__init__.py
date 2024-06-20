from flask import Blueprint

# Create the blueprint object
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views after blueprint creation to avoid circular import issues
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.application import *
from api.v1.views.delivery import *
from api.v1.views.order import *

# Note: The following import of app_views is not needed here as it's already defined above
# from api.v1.views import app_views

# Ensure all views are imported and registered with the blueprint
