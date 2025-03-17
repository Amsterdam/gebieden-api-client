# GebiedengrootstedelijkeProjecten

grootstedelijkeProjecten

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GebiedenGrootstedelijkeProjectenLinks**](GebiedenGrootstedelijkeProjectenLinks.md) |  | 
**id** | **int** |  | 
**geometrie** | [**MultiPolygon**](MultiPolygon.md) |  | 
**naam** | **str** |  | [optional] 
**type** | **str** | Categorie GSP, OD, PHS of PHSOD | [optional] 
**url** | **str** | URL naar bekendmaking | [optional] 
**typering** | **str** | Omschrijving type | [optional] 
**datum** | **str** |  | [optional] 
**legenda** | **str** |  | [optional] 

## Example

```python
from gebieden_api_client.models.gebiedengrootstedelijke_projecten import GebiedengrootstedelijkeProjecten

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedengrootstedelijkeProjecten from a JSON string
gebiedengrootstedelijke_projecten_instance = GebiedengrootstedelijkeProjecten.from_json(json)
# print the JSON string representation of the object
print(GebiedengrootstedelijkeProjecten.to_json())

# convert the object into a dict
gebiedengrootstedelijke_projecten_dict = gebiedengrootstedelijke_projecten_instance.to_dict()
# create an instance of GebiedengrootstedelijkeProjecten from a dict
gebiedengrootstedelijke_projecten_from_dict = GebiedengrootstedelijkeProjecten.from_dict(gebiedengrootstedelijke_projecten_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


