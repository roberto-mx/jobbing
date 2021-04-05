# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.user_profile import UserProfile  # noqa: E501
from jobbing.test import BaseTestCase


class TestProvidersController(BaseTestCase):
    """ProvidersController integration test stubs"""

    def test_get_provider_by_id(self):
        """Test case for get_provider_by_id

        
        """
        response = self.client.open(
            '/providers/{userProfileId}'.format(user_profile_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_providers_by_skill_id(self):
        """Test case for get_providers_by_skill_id

        
        """
        response = self.client.open(
            '/providers/{skillId}/skills'.format(skill_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
