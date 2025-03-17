# Gebiedenwijken

Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GebiedenWijkenLinks**](GebiedenWijkenLinks.md) |  | 
**identificatie** | **str** | Unieke identificatie van het object | 
**volgnummer** | **int** | Uniek volgnummer van de toestand van het object | 
**registratiedatum** | **datetime** | Datum waarop het gegeven in de bron geregistreerd is | [optional] 
**naam** | **str** | De naam van het object | [optional] 
**code** | **str** | Volledige, samengestelde, code, bestaande uit stadsdeelcode en wijkcode | [optional] 
**begin_geldigheid** | **datetime** | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een wijk | [optional] 
**eind_geldigheid** | **datetime** | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een wijk | [optional] 
**documentdatum** | **date** | De datum waarop het document is vastgesteld, op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden | [optional] 
**documentnummer** | **str** | De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden | [optional] 
**cbs_code** | **str** | Code zoals geleverd wordt door het CBS | [optional] 
**ligt_in_stadsdeel_id** | **str** | Het stadsdeel waar de wijk in ligt | [readonly] 
**ligt_in_ggwgebied_id** | **str** | Het gebiedsgericht werken gebied waar de wijk in ligt | [readonly] 
**geometrie** | [**Polygon**](Polygon.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.gebiedenwijken import Gebiedenwijken

# TODO update the JSON string below
json = "{}"
# create an instance of Gebiedenwijken from a JSON string
gebiedenwijken_instance = Gebiedenwijken.from_json(json)
# print the JSON string representation of the object
print(Gebiedenwijken.to_json())

# convert the object into a dict
gebiedenwijken_dict = gebiedenwijken_instance.to_dict()
# create an instance of Gebiedenwijken from a dict
gebiedenwijken_from_dict = Gebiedenwijken.from_dict(gebiedenwijken_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


