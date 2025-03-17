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

from gebieden_api_client.models.gebieden_buurten_links import GebiedenBuurtenLinks

class TestGebiedenBuurtenLinks(unittest.TestCase):
    """GebiedenBuurtenLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GebiedenBuurtenLinks:
        """Test GebiedenBuurtenLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GebiedenBuurtenLinks`
        """
        model = GebiedenBuurtenLinks()
        if include_optional:
            return GebiedenBuurtenLinks(
                var_schema = '',
                var_self = gebieden_api_client.models.gebieden_buurten_link.GebiedenBuurtenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, ),
                ligt_in_wijk = gebieden_api_client.models.gebieden_wijken_link.GebiedenWijkenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, ),
                ligt_in_ggpgebied = gebieden_api_client.models.gebieden_ggpgebieden_link.GebiedenGgpgebiedenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, ),
                ligt_in_ggwgebied = gebieden_api_client.models.gebieden_ggwgebieden_link.GebiedenGgwgebiedenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, )
            )
        else:
            return GebiedenBuurtenLinks(
                var_schema = '',
                var_self = gebieden_api_client.models.gebieden_buurten_link.GebiedenBuurtenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, ),
                ligt_in_wijk = gebieden_api_client.models.gebieden_wijken_link.GebiedenWijkenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, ),
                ligt_in_ggpgebied = gebieden_api_client.models.gebieden_ggpgebieden_link.GebiedenGgpgebiedenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, ),
                ligt_in_ggwgebied = gebieden_api_client.models.gebieden_ggwgebieden_link.GebiedenGgwgebiedenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', 
                    volgnummer = -9223372036854775808, ),
        )
        """

    def testGebiedenBuurtenLinks(self):
        """Test GebiedenBuurtenLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
