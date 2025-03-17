# GebiedenBuurtenLinks

The contents of the `buurten._links` field. It contains all relationships with objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The schema field is exposed with every record | [readonly] 
**var_self** | [**GebiedenBuurtenLink**](GebiedenBuurtenLink.md) |  | 
**ligt_in_wijk** | [**GebiedenWijkenLink**](GebiedenWijkenLink.md) |  | 
**ligt_in_ggpgebied** | [**GebiedenGgpgebiedenLink**](GebiedenGgpgebiedenLink.md) |  | 
**ligt_in_ggwgebied** | [**GebiedenGgwgebiedenLink**](GebiedenGgwgebiedenLink.md) |  | 

## Example

```python
from gebieden_api_client.models.gebieden_buurten_links import GebiedenBuurtenLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenBuurtenLinks from a JSON string
gebieden_buurten_links_instance = GebiedenBuurtenLinks.from_json(json)
# print the JSON string representation of the object
print(GebiedenBuurtenLinks.to_json())

# convert the object into a dict
gebieden_buurten_links_dict = gebieden_buurten_links_instance.to_dict()
# create an instance of GebiedenBuurtenLinks from a dict
gebieden_buurten_links_from_dict = GebiedenBuurtenLinks.from_dict(gebieden_buurten_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


