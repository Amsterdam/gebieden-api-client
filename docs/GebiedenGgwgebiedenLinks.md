# GebiedenGgwgebiedenLinks

The contents of the `ggwgebieden._links` field. It contains all relationships with objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The schema field is exposed with every record | [readonly] 
**var_self** | [**GebiedenGgwgebiedenLink**](GebiedenGgwgebiedenLink.md) |  | 
**ligt_in_stadsdeel** | [**GebiedenStadsdelenLink**](GebiedenStadsdelenLink.md) |  | 
**bestaat_uit_buurten** | [**List[GebiedenggwgebiedenBestaatUitBuurtenM2M]**](GebiedenggwgebiedenBestaatUitBuurtenM2M.md) |  | 

## Example

```python
from gebieden_api_client.models.gebieden_ggwgebieden_links import GebiedenGgwgebiedenLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenGgwgebiedenLinks from a JSON string
gebieden_ggwgebieden_links_instance = GebiedenGgwgebiedenLinks.from_json(json)
# print the JSON string representation of the object
print(GebiedenGgwgebiedenLinks.to_json())

# convert the object into a dict
gebieden_ggwgebieden_links_dict = gebieden_ggwgebieden_links_instance.to_dict()
# create an instance of GebiedenGgwgebiedenLinks from a dict
gebieden_ggwgebieden_links_from_dict = GebiedenGgwgebiedenLinks.from_dict(gebieden_ggwgebieden_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


