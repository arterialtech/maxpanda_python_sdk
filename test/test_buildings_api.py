# coding: utf-8

"""
    Maxpanda API V1

    The Maxpanda API documentation for version 1  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.buildings_api import BuildingsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBuildingsApi(unittest.TestCase):
    """BuildingsApi unit test stubs"""

    def setUp(self):
        self.api = BuildingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_buildings_create_building(self):
        """Test case for buildings_create_building

        Create a new Building  # noqa: E501
        """
        pass

    def test_buildings_get_building(self):
        """Test case for buildings_get_building

        Get a specific Building  # noqa: E501
        """
        pass

    def test_buildings_get_buildings(self):
        """Test case for buildings_get_buildings

        Get a paged list of buildings  # noqa: E501
        """
        pass

    def test_buildings_patch(self):
        """Test case for buildings_patch

        Update specific attributes of a given building  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()