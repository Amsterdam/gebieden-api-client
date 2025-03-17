# GebiedenStedelijkgebiedprojectofbelangenLinks

The contents of the `stedelijkgebiedprojectofbelangen._links` field. It contains all relationships with objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The schema field is exposed with every record | [readonly] 
**var_self** | [**GebiedenstedelijkgebiedprojectofbelangenLink**](GebiedenstedelijkgebiedprojectofbelangenLink.md) |  | 

## Example

```python
from gebieden_api_client.models.gebieden_stedelijkgebiedprojectofbelangen_links import GebiedenStedelijkgebiedprojectofbelangenLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenStedelijkgebiedprojectofbelangenLinks from a JSON string
gebieden_stedelijkgebiedprojectofbelangen_links_instance = GebiedenStedelijkgebiedprojectofbelangenLinks.from_json(json)
# print the JSON string representation of the object
print(GebiedenStedelijkgebiedprojectofbelangenLinks.to_json())

# convert the object into a dict
gebieden_stedelijkgebiedprojectofbelangen_links_dict = gebieden_stedelijkgebiedprojectofbelangen_links_instance.to_dict()
# create an instance of GebiedenStedelijkgebiedprojectofbelangenLinks from a dict
gebieden_stedelijkgebiedprojectofbelangen_links_from_dict = GebiedenStedelijkgebiedprojectofbelangenLinks.from_dict(gebieden_stedelijkgebiedprojectofbelangen_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


