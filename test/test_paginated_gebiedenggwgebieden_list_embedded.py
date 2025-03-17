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

from gebieden_api_client.models.paginated_gebiedenggwgebieden_list_embedded import PaginatedGebiedenggwgebiedenListEmbedded

class TestPaginatedGebiedenggwgebiedenListEmbedded(unittest.TestCase):
    """PaginatedGebiedenggwgebiedenListEmbedded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedGebiedenggwgebiedenListEmbedded:
        """Test PaginatedGebiedenggwgebiedenListEmbedded
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedGebiedenggwgebiedenListEmbedded`
        """
        model = PaginatedGebiedenggwgebiedenListEmbedded()
        if include_optional:
            return PaginatedGebiedenggwgebiedenListEmbedded(
                ggwgebieden = [
                    gebieden_api_client.models.gebiedenggwgebieden.Gebiedenggwgebieden(
                        _links = null, 
                        identificatie = '', 
                        volgnummer = -9223372036854775808, 
                        registratiedatum = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        naam = '', 
                        code = '', 
                        begin_geldigheid = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        eind_geldigheid = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        documentdatum = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        documentnummer = '', 
                        ligt_in_stadsdeel_id = '', 
                        geometrie = gebieden_api_client.models.polygon.Polygon(), )
                    ]
            )
        else:
            return PaginatedGebiedenggwgebiedenListEmbedded(
        )
        """

    def testPaginatedGebiedenggwgebiedenListEmbedded(self):
        """Test PaginatedGebiedenggwgebiedenListEmbedded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
