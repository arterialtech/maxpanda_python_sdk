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
from swagger_client.api.task_priority_api import TaskPriorityApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTaskPriorityApi(unittest.TestCase):
    """TaskPriorityApi unit test stubs"""

    def setUp(self):
        self.api = TaskPriorityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_task_priorities_get(self):
        """Test case for task_priorities_get

        Get a paged list of Task Priority  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()