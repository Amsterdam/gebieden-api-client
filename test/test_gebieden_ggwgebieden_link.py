# coding: utf-8

"""
    gebieden

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: datapunt@amsterdam.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gebieden_api_client.models.gebieden_ggwgebieden_link import GebiedenGgwgebiedenLink

class TestGebiedenGgwgebiedenLink(unittest.TestCase):
    """GebiedenGgwgebiedenLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GebiedenGgwgebiedenLink:
        """Test GebiedenGgwgebiedenLink
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GebiedenGgwgebiedenLink`
        """
        model = GebiedenGgwgebiedenLink()
        if include_optional:
            return GebiedenGgwgebiedenLink(
                href = '',
                title = '',
                identificatie = '',
                volgnummer = -9223372036854775808
            )
        else:
            return GebiedenGgwgebiedenLink(
                href = '',
                title = '',
                identificatie = '',
                volgnummer = -9223372036854775808,
        )
        """

    def testGebiedenGgwgebiedenLink(self):
        """Test GebiedenGgwgebiedenLink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
