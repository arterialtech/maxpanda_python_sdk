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
from maxpanda_python_sdk.api.purchase_orders_api import PurchaseOrdersApi  # noqa: E501
from maxpanda_python_sdk.rest import ApiException


class TestPurchaseOrdersApi(unittest.TestCase):
    """PurchaseOrdersApi unit test stubs"""

    def setUp(self):
        self.api = PurchaseOrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_purchase_order_get(self):
        """Test case for purchase_order_get

        Get a paged list of Purchase Orders  # noqa: E501
        """
        pass

    def test_purchase_order_get_0(self):
        """Test case for purchase_order_get_0

        Get a specific Purchase Order  # noqa: E501
        """
        pass

    def test_purchase_order_get_po_status(self):
        """Test case for purchase_order_get_po_status

        Get Purchase Order Statuses  # noqa: E501
        """
        pass

    def test_purchase_order_post(self):
        """Test case for purchase_order_post

        Create a new Purchase Order  # noqa: E501
        """
        pass

    def test_purchase_order_put(self):
        """Test case for purchase_order_put

        Update a Purchase Order  # noqa: E501
        """
        pass

    def test_purchase_order_put_0(self):
        """Test case for purchase_order_put_0

        Update Status of Purchase Order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
