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

from gebieden_api_client.models.paginated_gebiedenbuurten_list_embedded import PaginatedGebiedenbuurtenListEmbedded

class TestPaginatedGebiedenbuurtenListEmbedded(unittest.TestCase):
    """PaginatedGebiedenbuurtenListEmbedded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedGebiedenbuurtenListEmbedded:
        """Test PaginatedGebiedenbuurtenListEmbedded
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedGebiedenbuurtenListEmbedded`
        """
        model = PaginatedGebiedenbuurtenListEmbedded()
        if include_optional:
            return PaginatedGebiedenbuurtenListEmbedded(
                buurten = [
                    gebieden_api_client.models.gebiedenbuurten.Gebiedenbuurten(
                        _links = null, 
                        volgnummer = -9223372036854775808, 
                        registratiedatum = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        identificatie = '', 
                        naam = '', 
                        code = '', 
                        begin_geldigheid = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        eind_geldigheid = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        documentdatum = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        documentnummer = '', 
                        cbs_code = '', 
                        ligt_in_wijk_id = '', 
                        ligt_in_ggpgebied_id = '', 
                        ligt_in_ggwgebied_id = '', 
                        geometrie = gebieden_api_client.models.polygon.Polygon(), )
                    ]
            )
        else:
            return PaginatedGebiedenbuurtenListEmbedded(
        )
        """

    def testPaginatedGebiedenbuurtenListEmbedded(self):
        """Test PaginatedGebiedenbuurtenListEmbedded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
