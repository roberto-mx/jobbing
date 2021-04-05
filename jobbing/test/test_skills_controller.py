# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jobbing.models.skill import Skill  # noqa: E501
from jobbing.test import BaseTestCase


class TestSkillsController(BaseTestCase):
    """SkillsController integration test stubs"""

    def test_get_skill_by_id(self):
        """Test case for get_skill_by_id

        
        """
        response = self.client.open(
            '/skills/{skillId}'.format(skill_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
