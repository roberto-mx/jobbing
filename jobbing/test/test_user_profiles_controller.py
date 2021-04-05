# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.address import Address  # noqa: E501
from jobbing.models.user_profile import UserProfile  # noqa: E501
from jobbing.test import BaseTestCase


class TestUserProfilesController(BaseTestCase):
    """UserProfilesController integration test stubs"""

    def test_avatar_put(self):
        """Test case for avatar_put

        Upload an avatar
        """
        body = Object()
        response = self.client.open(
            '/avatar',
            method='PUT',
            data=json.dumps(body),
            content_type='image/png')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_addres_by_user_id(self):
        """Test case for get_addres_by_user_id

        
        """
        response = self.client.open(
            '/address/{userId}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_profile_by_id(self):
        """Test case for get_user_profile_by_id

        
        """
        response = self.client.open(
            '/userProfile/{uid}'.format(uid='uid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_address_profile(self):
        """Test case for save_address_profile

        
        """
        body = UserProfile()
        response = self.client.open(
            '/address',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_user_profile(self):
        """Test case for save_user_profile

        
        """
        body = UserProfile()
        response = self.client.open(
            '/userProfile',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_addres_by_user_id(self):
        """Test case for update_addres_by_user_id

        
        """
        response = self.client.open(
            '/address/{userId}'.format(user_id=56),
            method='PATCH')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user_profile_by_id(self):
        """Test case for update_user_profile_by_id

        
        """
        response = self.client.open(
            '/userProfile/{uid}'.format(uid='uid_example'),
            method='PATCH')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
