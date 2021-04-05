# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.album import Album  # noqa: E501
from jobbing.test import BaseTestCase


class TestAlbumsController(BaseTestCase):
    """AlbumsController integration test stubs"""

    def test_get_album_by_id(self):
        """Test case for get_album_by_id

        
        """
        response = self.client.open(
            '/albums/{albumId}'.format(album_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_albums(self):
        """Test case for get_albums

        
        """
        response = self.client.open(
            '/albums',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_album_profile(self):
        """Test case for save_album_profile

        
        """
        body = Album()
        response = self.client.open(
            '/albums',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
