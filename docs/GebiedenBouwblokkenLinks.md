# GebiedenBouwblokkenLinks

The contents of the `bouwblokken._links` field. It contains all relationships with objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The schema field is exposed with every record | [readonly] 
**var_self** | [**GebiedenBouwblokkenLink**](GebiedenBouwblokkenLink.md) |  | 
**ligt_in_buurt** | [**GebiedenBuurtenLink**](GebiedenBuurtenLink.md) |  | 

## Example

```python
from gebieden_api_client.models.gebieden_bouwblokken_links import GebiedenBouwblokkenLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenBouwblokkenLinks from a JSON string
gebieden_bouwblokken_links_instance = GebiedenBouwblokkenLinks.from_json(json)
# print the JSON string representation of the object
print(GebiedenBouwblokkenLinks.to_json())

# convert the object into a dict
gebieden_bouwblokken_links_dict = gebieden_bouwblokken_links_instance.to_dict()
# create an instance of GebiedenBouwblokkenLinks from a dict
gebieden_bouwblokken_links_from_dict = GebiedenBouwblokkenLinks.from_dict(gebieden_bouwblokken_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


