# coding: utf-8

"""
    Jellyfish Media Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import jellyfish_openapi_client
from jellyfish_openapi_client.models.add_component_request import AddComponentRequest  # noqa: E501
from jellyfish_openapi_client.rest import ApiException

class TestAddComponentRequest(unittest.TestCase):
    """AddComponentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddComponentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddComponentRequest`
        """
        model = jellyfish_openapi_client.models.add_component_request.AddComponentRequest()  # noqa: E501
        if include_optional :
            return AddComponentRequest(
                options = jellyfish_openapi_client.models.component_options.ComponentOptions(), 
                type = 'hls'
            )
        else :
            return AddComponentRequest(
                options = jellyfish_openapi_client.models.component_options.ComponentOptions(),
                type = 'hls',
        )
        """

    def testAddComponentRequest(self):
        """Test AddComponentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()