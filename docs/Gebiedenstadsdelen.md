# Gebiedenstadsdelen

Door de Amsterdamse gemeenteraad vastgestelde begrenzing van een stadsdeel, ressorterend onder een stadsgebied- of stadsdeelbestuur

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GebiedenStadsdelenLinks**](GebiedenStadsdelenLinks.md) |  | 
**identificatie** | **str** | Unieke identificatie van het object | 
**volgnummer** | **int** | Uniek volgnummer van de toestand van het object | 
**registratiedatum** | **datetime** | De datum waarop een gegeven in de bron is geregistreerd | [optional] 
**naam** | **str** | De naam van het object | [optional] 
**code** | **str** | Volledige, samengestelde, code, bestaande uit stadsdeelcode en wijkcode | [optional] 
**begin_geldigheid** | **datetime** | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een stadsdeel | [optional] 
**eind_geldigheid** | **datetime** | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een stadsdeel | [optional] 
**documentdatum** | **date** | De datum waarop het document is vastgesteld, op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden | [optional] 
**documentnummer** | **str** | De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van het object heeft plaatsgevonden | [optional] 
**ligt_in_gemeente_id** | **str** | De gemeente waar het stadsdeel in ligt | [readonly] 
**geometrie** | [**Polygon**](Polygon.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.gebiedenstadsdelen import Gebiedenstadsdelen

# TODO update the JSON string below
json = "{}"
# create an instance of Gebiedenstadsdelen from a JSON string
gebiedenstadsdelen_instance = Gebiedenstadsdelen.from_json(json)
# print the JSON string representation of the object
print(Gebiedenstadsdelen.to_json())

# convert the object into a dict
gebiedenstadsdelen_dict = gebiedenstadsdelen_instance.to_dict()
# create an instance of Gebiedenstadsdelen from a dict
gebiedenstadsdelen_from_dict = Gebiedenstadsdelen.from_dict(gebiedenstadsdelen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


