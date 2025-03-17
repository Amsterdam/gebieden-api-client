# Gebiedenggwgebieden

Gebiedsgericht werken is een manier om breed samenwerken in de stad te verbeteren tussen  gemeente, bewoners, ondernemers, (lokale) partners en maatschappelijke organisaties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GebiedenGgwgebiedenLinks**](GebiedenGgwgebiedenLinks.md) |  | 
**identificatie** | **str** | Unieke identificatie van het object | 
**volgnummer** | **int** | Uniek volgnummer van de toestand van het object | 
**registratiedatum** | **datetime** | De datum waarop een gegeven in de bron is geregistreerd | [optional] 
**naam** | **str** | De naam van het object | [optional] 
**code** | **str** | Officiële code van het object | [optional] 
**begin_geldigheid** | **datetime** | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een gebied | [optional] 
**eind_geldigheid** | **datetime** | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een gebied | [optional] 
**documentdatum** | **date** | De datum waarop het document is vastgesteld, op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden | [optional] 
**documentnummer** | **str** | Unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden | [optional] 
**ligt_in_stadsdeel_id** | **str** | Het stadsdeel waar het gebied in ligt | [readonly] 
**geometrie** | [**Polygon**](Polygon.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.gebiedenggwgebieden import Gebiedenggwgebieden

# TODO update the JSON string below
json = "{}"
# create an instance of Gebiedenggwgebieden from a JSON string
gebiedenggwgebieden_instance = Gebiedenggwgebieden.from_json(json)
# print the JSON string representation of the object
print(Gebiedenggwgebieden.to_json())

# convert the object into a dict
gebiedenggwgebieden_dict = gebiedenggwgebieden_instance.to_dict()
# create an instance of Gebiedenggwgebieden from a dict
gebiedenggwgebieden_from_dict = Gebiedenggwgebieden.from_dict(gebiedenggwgebieden_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


