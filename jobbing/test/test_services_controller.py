# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.service import Service  # noqa: E501
from jobbing.test import BaseTestCase


class TestServicesController(BaseTestCase):
    """ServicesController integration test stubs"""

    def test_get_catalog_entry_by_id(self):
        """Test case for get_catalog_entry_by_id

        
        """
        response = self.client.open(
            '/services/{serviceId}'.format(service_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_services_by_catalog_id(self):
        """Test case for get_services_by_catalog_id

        
        """
        response = self.client.open(
            '/catalog/{catalogId}/entries'.format(catalog_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_service(self):
        """Test case for save_service

        
        """
        body = Service()
        response = self.client.open(
            '/services',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
