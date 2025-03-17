# GebiedenWijkenLinks

The contents of the `wijken._links` field. It contains all relationships with objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The schema field is exposed with every record | [readonly] 
**var_self** | [**GebiedenWijkenLink**](GebiedenWijkenLink.md) |  | 
**ligt_in_stadsdeel** | [**GebiedenStadsdelenLink**](GebiedenStadsdelenLink.md) |  | 
**ligt_in_ggwgebied** | [**GebiedenGgwgebiedenLink**](GebiedenGgwgebiedenLink.md) |  | 

## Example

```python
from gebieden_api_client.models.gebieden_wijken_links import GebiedenWijkenLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenWijkenLinks from a JSON string
gebieden_wijken_links_instance = GebiedenWijkenLinks.from_json(json)
# print the JSON string representation of the object
print(GebiedenWijkenLinks.to_json())

# convert the object into a dict
gebieden_wijken_links_dict = gebieden_wijken_links_instance.to_dict()
# create an instance of GebiedenWijkenLinks from a dict
gebieden_wijken_links_from_dict = GebiedenWijkenLinks.from_dict(gebieden_wijken_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


