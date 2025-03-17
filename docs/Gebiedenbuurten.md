# Gebiedenbuurten

Amsterdam is opgedeeld in buurten ten behoeve van statistieken, een buurt is aaneengesloten gedeelte binnen een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GebiedenBuurtenLinks**](GebiedenBuurtenLinks.md) |  | 
**volgnummer** | **int** | Uniek volgnummer van de toestand van het object | 
**registratiedatum** | **datetime** | Datum waarop het gegeven in de bron geregistreerd is | [optional] 
**identificatie** | **str** | Unieke identificatie van het object | 
**naam** | **str** | De naam van het object | [optional] 
**code** | **str** | Volledige, samengestelde, code, bestaande uit stadsdeelcode en wijkcode | [optional] 
**begin_geldigheid** | **datetime** | De begindatum van de geldigheid van een bepaalde combinatie van gegevens over een buurt | [optional] 
**eind_geldigheid** | **datetime** | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een buurt | [optional] 
**documentdatum** | **date** | De datum waarop het document is vastgesteld, op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden | [optional] 
**documentnummer** | **str** | De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden | [optional] 
**cbs_code** | **str** | De CBS-code van het object | [optional] 
**ligt_in_wijk_id** | **str** | De wijk waar de buurt in ligt | [readonly] 
**ligt_in_ggpgebied_id** | **str** | Het GGP gebied waar de buurt in ligt | [readonly] 
**ligt_in_ggwgebied_id** | **str** | Het gebiedsgericht werken gebied waar de buurt in ligt | [readonly] 
**geometrie** | [**Polygon**](Polygon.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.gebiedenbuurten import Gebiedenbuurten

# TODO update the JSON string below
json = "{}"
# create an instance of Gebiedenbuurten from a JSON string
gebiedenbuurten_instance = Gebiedenbuurten.from_json(json)
# print the JSON string representation of the object
print(Gebiedenbuurten.to_json())

# convert the object into a dict
gebiedenbuurten_dict = gebiedenbuurten_instance.to_dict()
# create an instance of Gebiedenbuurten from a dict
gebiedenbuurten_from_dict = Gebiedenbuurten.from_dict(gebiedenbuurten_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


