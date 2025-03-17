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

from gebieden_api_client.models.gebieden_stadsdelen_links import GebiedenStadsdelenLinks

class TestGebiedenStadsdelenLinks(unittest.TestCase):
    """GebiedenStadsdelenLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GebiedenStadsdelenLinks:
        """Test GebiedenStadsdelenLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GebiedenStadsdelenLinks`
        """
        model = GebiedenStadsdelenLinks()
        if include_optional:
            return GebiedenStadsdelenLinks(
                var_schema = '',
                var_self = gebieden_api_client.models.gebieden_stadsdelen_link.GebiedenStadsdelenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, ),
                ligt_in_gemeente = gebieden_api_client.models.brk2_gemeentes_raw_identifier.Brk2GemeentesRawIdentifier(
                    href = '', 
                    title = '', 
                    identificatie = '', )
            )
        else:
            return GebiedenStadsdelenLinks(
                var_schema = '',
                var_self = gebieden_api_client.models.gebieden_stadsdelen_link.GebiedenStadsdelenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, ),
                ligt_in_gemeente = gebieden_api_client.models.brk2_gemeentes_raw_identifier.Brk2GemeentesRawIdentifier(
                    href = '', 
                    title = '', 
                    identificatie = '', ),
        )
        """

    def testGebiedenStadsdelenLinks(self):
        """Test GebiedenStadsdelenLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
