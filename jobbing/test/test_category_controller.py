# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.category import Category  # noqa: E501
from jobbing.test import BaseTestCase


class TestCategoryController(BaseTestCase):
    """CategoryController integration test stubs"""

    def test_get_categories(self):
        """Test case for get_categories

        
        """
        response = self.client.open(
            '/categories',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_category_by_id(self):
        """Test case for get_category_by_id

        
        """
        response = self.client.open(
            '/categories/{categoryId}'.format(category_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
