# coding: utf-8

"""
    gebieden

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: datapunt@amsterdam.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from gebieden_api_client.models.paginated_gebiedenbouwblokken_list_links import PaginatedGebiedenbouwblokkenListLinks
from gebieden_api_client.models.paginated_gebiedenbouwblokken_list_page import PaginatedGebiedenbouwblokkenListPage
from gebieden_api_client.models.paginated_gebiedenstadsdelen_list_embedded import PaginatedGebiedenstadsdelenListEmbedded
from typing import Optional, Set
from typing_extensions import Self

class PaginatedGebiedenstadsdelenList(BaseModel):
    """
    PaginatedGebiedenstadsdelenList
    """ # noqa: E501
    page: Optional[PaginatedGebiedenbouwblokkenListPage] = None
    links: Optional[PaginatedGebiedenbouwblokkenListLinks] = Field(default=None, alias="_links")
    embedded: Optional[PaginatedGebiedenstadsdelenListEmbedded] = Field(default=None, alias="_embedded")
    __properties: ClassVar[List[str]] = ["page", "_links", "_embedded"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PaginatedGebiedenstadsdelenList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of page
        if self.page:
            _dict['page'] = self.page.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of embedded
        if self.embedded:
            _dict['_embedded'] = self.embedded.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaginatedGebiedenstadsdelenList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page": PaginatedGebiedenbouwblokkenListPage.from_dict(obj["page"]) if obj.get("page") is not None else None,
            "_links": PaginatedGebiedenbouwblokkenListLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "_embedded": PaginatedGebiedenstadsdelenListEmbedded.from_dict(obj["_embedded"]) if obj.get("_embedded") is not None else None
        })
        return _obj


