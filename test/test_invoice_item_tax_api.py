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
from maxpanda_python_sdk.api.invoice_item_tax_api import InvoiceItemTaxApi  # noqa: E501
from maxpanda_python_sdk.rest import ApiException


class TestInvoiceItemTaxApi(unittest.TestCase):
    """InvoiceItemTaxApi unit test stubs"""

    def setUp(self):
        self.api = InvoiceItemTaxApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_invoice_tax_get(self):
        """Test case for invoice_tax_get

        Get a paged list of Invoice Taxes  # noqa: E501
        """
        pass

    def test_invoice_tax_get_0(self):
        """Test case for invoice_tax_get_0

        Get a specific Invoice Tax record  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
