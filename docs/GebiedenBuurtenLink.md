# GebiedenBuurtenLink

The identifier of the relationship to buurten.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [readonly] 
**title** | **str** |  | 
**identificatie** | **str** | Unieke identificatie van het object | 
**volgnummer** | **int** | Uniek volgnummer van de toestand van het object | 

## Example

```python
from gebieden_api_client.models.gebieden_buurten_link import GebiedenBuurtenLink

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenBuurtenLink from a JSON string
gebieden_buurten_link_instance = GebiedenBuurtenLink.from_json(json)
# print the JSON string representation of the object
print(GebiedenBuurtenLink.to_json())

# convert the object into a dict
gebieden_buurten_link_dict = gebieden_buurten_link_instance.to_dict()
# create an instance of GebiedenBuurtenLink from a dict
gebieden_buurten_link_from_dict = GebiedenBuurtenLink.from_dict(gebieden_buurten_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


