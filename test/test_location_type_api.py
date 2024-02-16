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
from maxpanda_python_sdk.api.location_type_api import LocationTypeApi  # noqa: E501
from maxpanda_python_sdk.rest import ApiException


class TestLocationTypeApi(unittest.TestCase):
    """LocationTypeApi unit test stubs"""

    def setUp(self):
        self.api = LocationTypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_location_types_get(self):
        """Test case for location_types_get

        Get a paged list of Location Types  # noqa: E501
        """
        pass

    def test_location_types_get_0(self):
        """Test case for location_types_get_0

        Get a specific location type record  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
