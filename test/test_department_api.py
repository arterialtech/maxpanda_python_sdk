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
from maxpanda_python_sdk.api.department_api import DepartmentApi  # noqa: E501
from maxpanda_python_sdk.rest import ApiException


class TestDepartmentApi(unittest.TestCase):
    """DepartmentApi unit test stubs"""

    def setUp(self):
        self.api = DepartmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_department_get(self):
        """Test case for department_get

        Get a paged list of departments  # noqa: E501
        """
        pass

    def test_department_get_0(self):
        """Test case for department_get_0

        Get a specific Department type record  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
