# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.notification import Notification  # noqa: E501
from jobbing.test import BaseTestCase


class TestNotificationsController(BaseTestCase):
    """NotificationsController integration test stubs"""

    def test_get_notifications_by_media(self):
        """Test case for get_notifications_by_media

        
        """
        response = self.client.open(
            '/media/{mediaId}/notifications'.format(media_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_notificationy_by_id(self):
        """Test case for get_notificationy_by_id

        
        """
        response = self.client.open(
            '/notifications/{notificationId}'.format(notification_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_notifications(self):
        """Test case for save_notifications

        
        """
        body = Notification()
        response = self.client.open(
            '/notifications',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
