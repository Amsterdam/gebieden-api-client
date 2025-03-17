# Gebiedenstedelijkgebiedprojectofbelangen

Stedelijke gebieden, projecten en belangen zijn projectgebieden binnen de gemeente Amsterdam, waar de voorbereiding van bestemmingsplannen door het college van burgemeester en wethouders of de burgemeester ter hand worden genomen

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GebiedenStedelijkgebiedprojectofbelangenLinks**](GebiedenStedelijkgebiedprojectofbelangenLinks.md) |  | 
**identificatie** | **str** | Unieke identificatie van het object | 
**geometrie** | [**MultiPolygon**](MultiPolygon.md) |  | 
**naam** | **str** | De naam van het object | [optional] 
**categorie_code** | **str** |  | [optional] 
**categorie_omschrijving** | **str** |  | [optional] 
**url** | **str** | URL naar bekendmaking | [optional] 
**datum** | **date** | Wordt nog aangevuld | [optional] 
**datum_actueel_tot** | **datetime** | Einddatum van de cyclus, eventueel in combinatie met het kenmerk Status | [optional] 
**legenda** | **str** | Wordt nog aangevuld | [optional] 

## Example

```python
from gebieden_api_client.models.gebiedenstedelijkgebiedprojectofbelangen import Gebiedenstedelijkgebiedprojectofbelangen

# TODO update the JSON string below
json = "{}"
# create an instance of Gebiedenstedelijkgebiedprojectofbelangen from a JSON string
gebiedenstedelijkgebiedprojectofbelangen_instance = Gebiedenstedelijkgebiedprojectofbelangen.from_json(json)
# print the JSON string representation of the object
print(Gebiedenstedelijkgebiedprojectofbelangen.to_json())

# convert the object into a dict
gebiedenstedelijkgebiedprojectofbelangen_dict = gebiedenstedelijkgebiedprojectofbelangen_instance.to_dict()
# create an instance of Gebiedenstedelijkgebiedprojectofbelangen from a dict
gebiedenstedelijkgebiedprojectofbelangen_from_dict = Gebiedenstedelijkgebiedprojectofbelangen.from_dict(gebiedenstedelijkgebiedprojectofbelangen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


