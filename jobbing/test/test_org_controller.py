# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.org import Org  # noqa: E501
from jobbing.test import BaseTestCase


class TestOrgController(BaseTestCase):
    """OrgController integration test stubs"""

    def test_get_org_by_id(self):
        """Test case for get_org_by_id

        
        """
        response = self.client.open(
            '/org/{orgId}'.format(org_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_org(self):
        """Test case for save_org

        
        """
        body = Org()
        response = self.client.open(
            '/org',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
