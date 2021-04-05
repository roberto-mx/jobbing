# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.service_provided import ServiceProvided  # noqa: E501
from jobbing.test import BaseTestCase


class TestServicesProvidedController(BaseTestCase):
    """ServicesProvidedController integration test stubs"""

    def test_get_service_provided_by_client_id(self):
        """Test case for get_service_provided_by_client_id

        
        """
        response = self.client.open(
            '/client/{clientId}/services_contracted'.format(client_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_service_provided_by_id(self):
        """Test case for get_service_provided_by_id

        
        """
        response = self.client.open(
            '/services_provided/{serviceProvidedId}'.format(service_provided_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_service_provided_by_provider_id(self):
        """Test case for get_service_provided_by_provider_id

        
        """
        response = self.client.open(
            '/provider/{providerId}/services_provided'.format(provider_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_service_provided(self):
        """Test case for save_service_provided

        
        """
        body = ServiceProvided()
        response = self.client.open(
            '/services_provided',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
