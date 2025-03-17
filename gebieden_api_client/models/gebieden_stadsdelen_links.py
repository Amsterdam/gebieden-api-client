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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from gebieden_api_client.models.brk2_gemeentes_raw_identifier import Brk2GemeentesRawIdentifier
from gebieden_api_client.models.gebieden_stadsdelen_link import GebiedenStadsdelenLink
from typing import Optional, Set
from typing_extensions import Self

class GebiedenStadsdelenLinks(BaseModel):
    """
    The contents of the `stadsdelen._links` field. It contains all relationships with objects.
    """ # noqa: E501
    var_schema: StrictStr = Field(description="The schema field is exposed with every record", alias="schema")
    var_self: GebiedenStadsdelenLink = Field(alias="self")
    ligt_in_gemeente: Brk2GemeentesRawIdentifier = Field(alias="ligtInGemeente")
    __properties: ClassVar[List[str]] = ["schema", "self", "ligtInGemeente"]

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
        """Create an instance of GebiedenStadsdelenLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "var_schema",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_self
        if self.var_self:
            _dict['self'] = self.var_self.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ligt_in_gemeente
        if self.ligt_in_gemeente:
            _dict['ligtInGemeente'] = self.ligt_in_gemeente.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GebiedenStadsdelenLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": obj.get("schema"),
            "self": GebiedenStadsdelenLink.from_dict(obj["self"]) if obj.get("self") is not None else None,
            "ligtInGemeente": Brk2GemeentesRawIdentifier.from_dict(obj["ligtInGemeente"]) if obj.get("ligtInGemeente") is not None else None
        })
        return _obj


