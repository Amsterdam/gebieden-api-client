# GebiedenGgwgebiedenLink

The identifier of the relationship to ggwgebieden.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [readonly] 
**title** | **str** |  | 
**identificatie** | **str** | Unieke identificatie van het object | 
**volgnummer** | **int** | Uniek volgnummer van de toestand van het object | 

## Example

```python
from gebieden_api_client.models.gebieden_ggwgebieden_link import GebiedenGgwgebiedenLink

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenGgwgebiedenLink from a JSON string
gebieden_ggwgebieden_link_instance = GebiedenGgwgebiedenLink.from_json(json)
# print the JSON string representation of the object
print(GebiedenGgwgebiedenLink.to_json())

# convert the object into a dict
gebieden_ggwgebieden_link_dict = gebieden_ggwgebieden_link_instance.to_dict()
# create an instance of GebiedenGgwgebiedenLink from a dict
gebieden_ggwgebieden_link_from_dict = GebiedenGgwgebiedenLink.from_dict(gebieden_ggwgebieden_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


