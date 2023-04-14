# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import graph_api
from graph_api.models.relations_entity import RelationsEntity  # noqa: E501
from graph_api.rest import ApiException

class TestRelationsEntity(unittest.TestCase):
    """RelationsEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RelationsEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelationsEntity`
        """
        model = graph_api.models.relations_entity.RelationsEntity()  # noqa: E501
        if include_optional :
            return RelationsEntity(
                happened_after = None, 
                led_to = None, 
                affected = None, 
                includes = None, 
                occurred_in = None, 
                has_relationship = None, 
                participated_in = None, 
                contains = None
            )
        else :
            return RelationsEntity(
                happened_after = None,
                led_to = None,
                affected = None,
                includes = None,
                occurred_in = None,
                has_relationship = None,
                participated_in = None,
                contains = None,
        )
        """

    def testRelationsEntity(self):
        """Test RelationsEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
