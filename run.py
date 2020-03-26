""" The API entrypoint """

# Python imports
from os import getenv

# Local import
from app import app

if __name__ == '__main__':
    app.run(debug=getenv("APP_DEBUG"))
