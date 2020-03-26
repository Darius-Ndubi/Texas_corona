
""" Module for Corona Views in two texas counties """

# Python modules
import requests

# Third part imports
from flask_restplus import Resource, Namespace


corona_status = Namespace('status')

@corona_status.route('/<county_name>')
class CoronaOnCounty(Resource):

    def get(self, county_name):
        ''' Endpoint to fetch number of cases per county '''
        request_data = {
            'country_code': 'US',
            'province': 'Texas',
            'county': county_name,
            'timelines': 'true'
        }

        data = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations?source=csbs', params=request_data)

        # num_cases = data.json()['latest']['confirmed']

        response_message = {
            'county': county_name,
            'confirmed_cases': data.json()['latest']['confirmed']
        }

        return response_message

@corona_status.route('/per_capita/<county_name>')
class CoronaPerCapita(Resource):

    def num_of_cases(self, county_name):
        ''' method to fetch number of cases per capita '''
        request_data = {
            'country_code': 'US',
            'province': 'Texas',
            'county': county_name,
            'timelines': 'true'
            }

        data = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations?source=csbs', params=request_data)

        num_cases = data.json()['latest']['confirmed']

        infected_per_capita = (100*num_cases) / 1000.0

        return infected_per_capita

    def get(self, county_name):
        ''' Method to retrieve number of cases per capita for
            Travis and Harris Counties '''

        county_name = county_name.capitalize()

        if county_name == 'Harris':

            num_cases = self.num_of_cases(county_name)

            return {
                'County': 'Harris',
                'per_capita': num_cases
            }
        elif county_name == 'Travis':

            num_cases = self.num_of_cases(county_name)

            return {
                'County': 'Travis',
                'per_capita': num_cases
            }
