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

from gebieden_api_client.models.paginated_gebiedenstedelijkgebiedprojectofbelangen_list_embedded import PaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded

class TestPaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded(unittest.TestCase):
    """PaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded:
        """Test PaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded`
        """
        model = PaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded()
        if include_optional:
            return PaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded(
                stedelijkgebiedprojectofbelangen = [
                    gebieden_api_client.models.gebiedenstedelijkgebiedprojectofbelangen.Gebiedenstedelijkgebiedprojectofbelangen(
                        _links = null, 
                        identificatie = '', 
                        geometrie = gebieden_api_client.models.multi_polygon.MultiPolygon(), 
                        naam = '', 
                        categorie_code = '', 
                        categorie_omschrijving = '', 
                        url = '', 
                        datum = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        datum_actueel_tot = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        legenda = '', )
                    ]
            )
        else:
            return PaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded(
        )
        """

    def testPaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded(self):
        """Test PaginatedGebiedenstedelijkgebiedprojectofbelangenListEmbedded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
