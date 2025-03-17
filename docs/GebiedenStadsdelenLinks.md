# GebiedenStadsdelenLinks

The contents of the `stadsdelen._links` field. It contains all relationships with objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The schema field is exposed with every record | [readonly] 
**var_self** | [**GebiedenStadsdelenLink**](GebiedenStadsdelenLink.md) |  | 
**ligt_in_gemeente** | [**Brk2GemeentesRawIdentifier**](Brk2GemeentesRawIdentifier.md) |  | 

## Example

```python
from gebieden_api_client.models.gebieden_stadsdelen_links import GebiedenStadsdelenLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenStadsdelenLinks from a JSON string
gebieden_stadsdelen_links_instance = GebiedenStadsdelenLinks.from_json(json)
# print the JSON string representation of the object
print(GebiedenStadsdelenLinks.to_json())

# convert the object into a dict
gebieden_stadsdelen_links_dict = gebieden_stadsdelen_links_instance.to_dict()
# create an instance of GebiedenStadsdelenLinks from a dict
gebieden_stadsdelen_links_from_dict = GebiedenStadsdelenLinks.from_dict(gebieden_stadsdelen_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


