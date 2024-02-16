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
from maxpanda_python_sdk.api.asset_type_api import AssetTypeApi  # noqa: E501
from maxpanda_python_sdk.rest import ApiException


class TestAssetTypeApi(unittest.TestCase):
    """AssetTypeApi unit test stubs"""

    def setUp(self):
        self.api = AssetTypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_asset_types_get(self):
        """Test case for asset_types_get

        Get a paged list of Asset Types  # noqa: E501
        """
        pass

    def test_asset_types_get_0(self):
        """Test case for asset_types_get_0

        Get a specific Asset Type type record  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
