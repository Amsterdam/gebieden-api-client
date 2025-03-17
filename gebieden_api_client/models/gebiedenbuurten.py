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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gebieden_api_client.models.gebieden_buurten_links import GebiedenBuurtenLinks
from gebieden_api_client.models.polygon import Polygon
from typing import Optional, Set
from typing_extensions import Self

class Gebiedenbuurten(BaseModel):
    """
    Amsterdam is opgedeeld in buurten ten behoeve van statistieken, een buurt is aaneengesloten gedeelte binnen een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen
    """ # noqa: E501
    links: GebiedenBuurtenLinks = Field(alias="_links")
    volgnummer: Annotated[int, Field(le=9223372036854775807, strict=True, ge=-9223372036854775808)] = Field(description="Uniek volgnummer van de toestand van het object")
    registratiedatum: Optional[datetime] = Field(default=None, description="Datum waarop het gegeven in de bron geregistreerd is")
    identificatie: Annotated[str, Field(strict=True, max_length=2147483647)] = Field(description="Unieke identificatie van het object")
    naam: Optional[Annotated[str, Field(strict=True, max_length=2147483647)]] = Field(default=None, description="De naam van het object")
    code: Optional[Annotated[str, Field(strict=True, max_length=2147483647)]] = Field(default=None, description="Volledige, samengestelde, code, bestaande uit stadsdeelcode en wijkcode")
    begin_geldigheid: Optional[datetime] = Field(default=None, description="De begindatum van de geldigheid van een bepaalde combinatie van gegevens over een buurt", alias="beginGeldigheid")
    eind_geldigheid: Optional[datetime] = Field(default=None, description="De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een buurt", alias="eindGeldigheid")
    documentdatum: Optional[date] = Field(default=None, description="De datum waarop het document is vastgesteld, op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden")
    documentnummer: Optional[Annotated[str, Field(strict=True, max_length=2147483647)]] = Field(default=None, description="De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden")
    cbs_code: Optional[Annotated[str, Field(strict=True, max_length=2147483647)]] = Field(default=None, description="De CBS-code van het object", alias="cbsCode")
    ligt_in_wijk_id: Optional[StrictStr] = Field(description="De wijk waar de buurt in ligt", alias="ligtInWijkId")
    ligt_in_ggpgebied_id: Optional[StrictStr] = Field(description="Het GGP gebied waar de buurt in ligt", alias="ligtInGgpgebiedId")
    ligt_in_ggwgebied_id: Optional[StrictStr] = Field(description="Het gebiedsgericht werken gebied waar de buurt in ligt", alias="ligtInGgwgebiedId")
    geometrie: Optional[Polygon] = None
    __properties: ClassVar[List[str]] = ["_links", "volgnummer", "registratiedatum", "identificatie", "naam", "code", "beginGeldigheid", "eindGeldigheid", "documentdatum", "documentnummer", "cbsCode", "ligtInWijkId", "ligtInGgpgebiedId", "ligtInGgwgebiedId", "geometrie"]

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
        """Create an instance of Gebiedenbuurten from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "ligt_in_wijk_id",
            "ligt_in_ggpgebied_id",
            "ligt_in_ggwgebied_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geometrie
        if self.geometrie:
            _dict['geometrie'] = self.geometrie.to_dict()
        # set to None if registratiedatum (nullable) is None
        # and model_fields_set contains the field
        if self.registratiedatum is None and "registratiedatum" in self.model_fields_set:
            _dict['registratiedatum'] = None

        # set to None if naam (nullable) is None
        # and model_fields_set contains the field
        if self.naam is None and "naam" in self.model_fields_set:
            _dict['naam'] = None

        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and "code" in self.model_fields_set:
            _dict['code'] = None

        # set to None if begin_geldigheid (nullable) is None
        # and model_fields_set contains the field
        if self.begin_geldigheid is None and "begin_geldigheid" in self.model_fields_set:
            _dict['beginGeldigheid'] = None

        # set to None if eind_geldigheid (nullable) is None
        # and model_fields_set contains the field
        if self.eind_geldigheid is None and "eind_geldigheid" in self.model_fields_set:
            _dict['eindGeldigheid'] = None

        # set to None if documentdatum (nullable) is None
        # and model_fields_set contains the field
        if self.documentdatum is None and "documentdatum" in self.model_fields_set:
            _dict['documentdatum'] = None

        # set to None if documentnummer (nullable) is None
        # and model_fields_set contains the field
        if self.documentnummer is None and "documentnummer" in self.model_fields_set:
            _dict['documentnummer'] = None

        # set to None if cbs_code (nullable) is None
        # and model_fields_set contains the field
        if self.cbs_code is None and "cbs_code" in self.model_fields_set:
            _dict['cbsCode'] = None

        # set to None if ligt_in_wijk_id (nullable) is None
        # and model_fields_set contains the field
        if self.ligt_in_wijk_id is None and "ligt_in_wijk_id" in self.model_fields_set:
            _dict['ligtInWijkId'] = None

        # set to None if ligt_in_ggpgebied_id (nullable) is None
        # and model_fields_set contains the field
        if self.ligt_in_ggpgebied_id is None and "ligt_in_ggpgebied_id" in self.model_fields_set:
            _dict['ligtInGgpgebiedId'] = None

        # set to None if ligt_in_ggwgebied_id (nullable) is None
        # and model_fields_set contains the field
        if self.ligt_in_ggwgebied_id is None and "ligt_in_ggwgebied_id" in self.model_fields_set:
            _dict['ligtInGgwgebiedId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Gebiedenbuurten from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": GebiedenBuurtenLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "volgnummer": obj.get("volgnummer"),
            "registratiedatum": obj.get("registratiedatum"),
            "identificatie": obj.get("identificatie"),
            "naam": obj.get("naam"),
            "code": obj.get("code"),
            "beginGeldigheid": obj.get("beginGeldigheid"),
            "eindGeldigheid": obj.get("eindGeldigheid"),
            "documentdatum": obj.get("documentdatum"),
            "documentnummer": obj.get("documentnummer"),
            "cbsCode": obj.get("cbsCode"),
            "ligtInWijkId": obj.get("ligtInWijkId"),
            "ligtInGgpgebiedId": obj.get("ligtInGgpgebiedId"),
            "ligtInGgwgebiedId": obj.get("ligtInGgwgebiedId"),
            "geometrie": Polygon.from_dict(obj["geometrie"]) if obj.get("geometrie") is not None else None
        })
        return _obj


