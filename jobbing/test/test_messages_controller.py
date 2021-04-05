# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.message import Message  # noqa: E501
from jobbing.test import BaseTestCase


class TestMessagesController(BaseTestCase):
    """MessagesController integration test stubs"""

    def test_get_message_by_id(self):
        """Test case for get_message_by_id

        
        """
        response = self.client.open(
            '/messages/{messageId}'.format(message_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_message_by_provider_id(self):
        """Test case for get_message_by_provider_id

        
        """
        response = self.client.open(
            '/providers/{providerId}/messages'.format(provider_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_message(self):
        """Test case for save_message

        
        """
        body = Message()
        response = self.client.open(
            '/messages',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
