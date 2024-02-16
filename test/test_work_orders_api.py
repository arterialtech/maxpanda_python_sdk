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
from maxpanda_python_sdk.api.work_orders_api import WorkOrdersApi  # noqa: E501
from maxpanda_python_sdk.rest import ApiException


class TestWorkOrdersApi(unittest.TestCase):
    """WorkOrdersApi unit test stubs"""

    def setUp(self):
        self.api = WorkOrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_work_orders_create_workorder(self):
        """Test case for work_orders_create_workorder

        Submit a workorder  # noqa: E501
        """
        pass

    def test_work_orders_delete_work_order_task(self):
        """Test case for work_orders_delete_work_order_task

        Delete Task of Workorder  # noqa: E501
        """
        pass

    def test_work_orders_get(self):
        """Test case for work_orders_get

        Get a list of work orders  # noqa: E501
        """
        pass

    def test_work_orders_get_0(self):
        """Test case for work_orders_get_0

        Get a specific work order  # noqa: E501
        """
        pass

    def test_work_orders_get_to_do(self):
        """Test case for work_orders_get_to_do

        Get Users To Do WorkOrder List  # noqa: E501
        """
        pass

    def test_work_orders_get_work_orders_by_status(self):
        """Test case for work_orders_get_work_orders_by_status

        Get Workorders by Status  # noqa: E501
        """
        pass

    def test_work_orders_get_work_orders_by_user(self):
        """Test case for work_orders_get_work_orders_by_user

        Get list of workorders created by an User  # noqa: E501
        """
        pass

    def test_work_orders_get_workorder_statuses(self):
        """Test case for work_orders_get_workorder_statuses

        Get a list of work orders statues  # noqa: E501
        """
        pass

    def test_work_orders_update_workorder(self):
        """Test case for work_orders_update_workorder

        Update a workorder  # noqa: E501
        """
        pass

    def test_work_orders_update_workorder_status(self):
        """Test case for work_orders_update_workorder_status

        Change status of workorder  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
