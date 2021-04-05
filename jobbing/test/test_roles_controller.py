# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.role import Role  # noqa: E501
from jobbing.test import BaseTestCase


class TestRolesController(BaseTestCase):
    """RolesController integration test stubs"""

    def test_get_roles(self):
        """Test case for get_roles

        Lists all user roles
        """
        response = self.client.open(
            '/role',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
