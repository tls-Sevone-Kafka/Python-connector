# coding: utf-8

"""
    SevOne API Documentation

    Supported endpoints by the new RESTful API  # noqa: E501

    OpenAPI spec version: 2.1.42, Hash: 719f8be
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.background_tasks_api import BackgroundTasksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBackgroundTasksApi(unittest.TestCase):
    """BackgroundTasksApi unit test stubs"""

    def setUp(self):
        self.api = BackgroundTasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_background_task(self):
        """Test case for create_background_task

        Create new background task  # noqa: E501
        """
        pass

    def test_get_background_task(self):
        """Test case for get_background_task

        Get background task status / response  # noqa: E501
        """
        pass

    def test_get_background_tasks(self):
        """Test case for get_background_tasks

        List background tasks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
