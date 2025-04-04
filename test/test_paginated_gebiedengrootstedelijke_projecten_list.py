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

from gebieden_api_client.models.paginated_gebiedengrootstedelijke_projecten_list import PaginatedGebiedengrootstedelijkeProjectenList

class TestPaginatedGebiedengrootstedelijkeProjectenList(unittest.TestCase):
    """PaginatedGebiedengrootstedelijkeProjectenList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedGebiedengrootstedelijkeProjectenList:
        """Test PaginatedGebiedengrootstedelijkeProjectenList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedGebiedengrootstedelijkeProjectenList`
        """
        model = PaginatedGebiedengrootstedelijkeProjectenList()
        if include_optional:
            return PaginatedGebiedengrootstedelijkeProjectenList(
                page = gebieden_api_client.models.paginated_gebiedenbouwblokken_list_page.PaginatedGebiedenbouwblokkenList_page(
                    number = 3, 
                    size = 20, 
                    total_elements = 5, 
                    total_pages = 3, ),
                links = gebieden_api_client.models.paginated_gebiedenbouwblokken_list__links.PaginatedGebiedenbouwblokkenList__links(
                    self = gebieden_api_client.models.paginated_gebiedenbouwblokken_list__links_self.PaginatedGebiedenbouwblokkenList__links_self(
                        href = 'https://api.data.amsterdam.nl/v1/.../resource/?page=3', ), 
                    next = gebieden_api_client.models.paginated_gebiedenbouwblokken_list__links_next.PaginatedGebiedenbouwblokkenList__links_next(
                        href = 'https://api.data.amsterdam.nl/v1/.../resource/?page=4', ), 
                    previous = gebieden_api_client.models.paginated_gebiedenbouwblokken_list__links_previous.PaginatedGebiedenbouwblokkenList__links_previous(
                        href = 'https://api.data.amsterdam.nl/v1/.../resource/?page=2', ), ),
                embedded = gebieden_api_client.models.paginated_gebiedengrootstedelijke_projecten_list__embedded.PaginatedGebiedengrootstedelijke_projectenList__embedded(
                    grootstedelijke_projecten = [
                        gebieden_api_client.models.gebiedengrootstedelijke_projecten.Gebiedengrootstedelijke_projecten(
                            _links = null, 
                            id = -9223372036854775808, 
                            geometrie = gebieden_api_client.models.multi_polygon.MultiPolygon(), 
                            naam = '', 
                            type = '', 
                            url = '', 
                            typering = '', 
                            datum = '', 
                            legenda = '', )
                        ], )
            )
        else:
            return PaginatedGebiedengrootstedelijkeProjectenList(
        )
        """

    def testPaginatedGebiedengrootstedelijkeProjectenList(self):
        """Test PaginatedGebiedengrootstedelijkeProjectenList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
