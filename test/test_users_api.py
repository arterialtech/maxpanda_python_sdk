# coding: utf-8

"""
    Maxpanda API V1

    The Maxpanda API documentation for version 1  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import maxpanda_python_sdk
from maxpanda_python_sdk.api.users_api import UsersApi  # noqa: E501
from maxpanda_python_sdk.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_get_user_by_id(self):
        """Test case for user_get_user_by_id

        Get a specific User  # noqa: E501
        """
        pass

    def test_user_get_users(self):
        """Test case for user_get_users

        Get list of Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
