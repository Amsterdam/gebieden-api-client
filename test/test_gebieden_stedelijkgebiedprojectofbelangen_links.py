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

from gebieden_api_client.models.gebieden_stedelijkgebiedprojectofbelangen_links import GebiedenStedelijkgebiedprojectofbelangenLinks

class TestGebiedenStedelijkgebiedprojectofbelangenLinks(unittest.TestCase):
    """GebiedenStedelijkgebiedprojectofbelangenLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GebiedenStedelijkgebiedprojectofbelangenLinks:
        """Test GebiedenStedelijkgebiedprojectofbelangenLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GebiedenStedelijkgebiedprojectofbelangenLinks`
        """
        model = GebiedenStedelijkgebiedprojectofbelangenLinks()
        if include_optional:
            return GebiedenStedelijkgebiedprojectofbelangenLinks(
                var_schema = '',
                var_self = gebieden_api_client.models.gebiedenstedelijkgebiedprojectofbelangen_link.GebiedenstedelijkgebiedprojectofbelangenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', )
            )
        else:
            return GebiedenStedelijkgebiedprojectofbelangenLinks(
                var_schema = '',
                var_self = gebieden_api_client.models.gebiedenstedelijkgebiedprojectofbelangen_link.GebiedenstedelijkgebiedprojectofbelangenLink(
                    href = '', 
                    title = '', 
                    identificatie = '', ),
        )
        """

    def testGebiedenStedelijkgebiedprojectofbelangenLinks(self):
        """Test GebiedenStedelijkgebiedprojectofbelangenLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
