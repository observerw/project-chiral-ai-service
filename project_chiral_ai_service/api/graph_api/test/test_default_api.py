# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import graph_api
from graph_api.api.default_api import DefaultApi  # noqa: E501
from graph_api.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = graph_api.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_node(self):
        """Test case for create_node

        """
        pass

    def test_create_relation(self):
        """Test case for create_relation

        """
        pass

    def test_get_relations(self):
        """Test case for get_relations

        """
        pass

    def test_get_test(self):
        """Test case for get_test

        """
        pass

    def test_remove_node(self):
        """Test case for remove_node

        """
        pass

    def test_remove_relation(self):
        """Test case for remove_relation

        """
        pass


if __name__ == '__main__':
    unittest.main()
