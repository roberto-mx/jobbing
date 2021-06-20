# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.country import Country  # noqa: E501
from jobbing.models.municipality import Municipality  # noqa: E501
from jobbing.models.neighbourhood import Neighbourhood  # noqa: E501
from jobbing.models.notification_type import NotificationType  # noqa: E501
from jobbing.models.state import State  # noqa: E501
from jobbing.test import BaseTestCase


class TestCatalogsController(BaseTestCase):
    """CatalogsController integration test stubs"""

    def test_get_countries(self):
        """Test case for get_countries

        
        """
        response = self.client.open(
            '/countries',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_country_by_id(self):
        """Test case for get_country_by_id

        
        """
        response = self.client.open(
            '/countries/{countryId}'.format(country_id='country_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_municipalities_by_state_id(self):
        """Test case for get_municipalities_by_state_id

        
        """
        response = self.client.open(
            '/states/{stateId}/municipalities'.format(state_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_municipality_by_id(self):
        """Test case for get_municipality_by_id

        
        """
        response = self.client.open(
            '/municipalities/{municipalityId}'.format(municipality_id='municipality_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_neighbourhood_by_id(self):
        """Test case for get_eighbourhood_by_id

        
        """
        response = self.client.open(
            '/eighbourhood/{neighbourhoodId}'.format(eighbourhood_id='eighbourhood_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_neighbourhoods_by_municipality(self):
        """Test case for get_neighbourhoods_by_municipality

        
        """
        response = self.client.open(
            '/municipalities/{municipalityId}/neighbourhoods'.format(municipality_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_notification_type_by_id(self):
        """Test case for get_notification_type_by_id

        
        """
        response = self.client.open(
            '/notification_types/{notificactionTypeId}'.format(notificaction_type_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_notification_types(self):
        """Test case for get_notification_types

        
        """
        response = self.client.open(
            '/notification_types',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_state_by_id(self):
        """Test case for get_state_by_id

        
        """
        response = self.client.open(
            '/states/{stateId}'.format(state_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_states_by_country_id(self):
        """Test case for get_states_by_country_id

        
        """
        response = self.client.open(
            '/countries/{countryId}/states'.format(country_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
