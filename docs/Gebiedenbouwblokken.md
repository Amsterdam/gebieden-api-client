# Gebiedenbouwblokken

Een bouwblok is het kleinst mogelijk afgrensbare gebied, in zijn geheel tot een buurt behorend, dat geheel of grotendeels door bestaande of aan te leggen wegen en/of waterlopen is of zal zijn ingesloten en waarop tenminste één gebouw met verblijfsobject staat op maaiveld niveau. Dus ondergrondse garages en metrostations krijgen géén bouwblok

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GebiedenBouwblokkenLinks**](GebiedenBouwblokkenLinks.md) |  | 
**identificatie** | **str** | Unieke identificatie van het object | 
**volgnummer** | **int** | Uniek volgnummer van de toestand van het object | 
**registratiedatum** | **datetime** | Datum waarop het gegeven in de bron geregistreerd is | [optional] 
**code** | **str** | Officiële code van het object | [optional] 
**begin_geldigheid** | **datetime** | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok | [optional] 
**eind_geldigheid** | **datetime** | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok | [optional] 
**ligt_in_buurt_id** | **str** | De buurt waar het bouwblok in ligt | [readonly] 
**geometrie** | [**Polygon**](Polygon.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.gebiedenbouwblokken import Gebiedenbouwblokken

# TODO update the JSON string below
json = "{}"
# create an instance of Gebiedenbouwblokken from a JSON string
gebiedenbouwblokken_instance = Gebiedenbouwblokken.from_json(json)
# print the JSON string representation of the object
print(Gebiedenbouwblokken.to_json())

# convert the object into a dict
gebiedenbouwblokken_dict = gebiedenbouwblokken_instance.to_dict()
# create an instance of Gebiedenbouwblokken from a dict
gebiedenbouwblokken_from_dict = Gebiedenbouwblokken.from_dict(gebiedenbouwblokken_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


