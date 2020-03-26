""" Module to initialize flask """

# Third Party imports
from flask import Flask
from flask_restplus import Api

app = Flask(__name__)

API = Api(
    app,
    version='1.0',
    title='Corona Texas',
    description='Get corona data in Texas County'
)


from app.view.corona_texas_view import corona_status as status
API.add_namespace(status, path='/api/v1')
