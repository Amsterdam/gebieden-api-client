# GebiedenGgpgebiedenLinks

The contents of the `ggpgebieden._links` field. It contains all relationships with objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The schema field is exposed with every record | [readonly] 
**var_self** | [**GebiedenGgpgebiedenLink**](GebiedenGgpgebiedenLink.md) |  | 
**ligt_in_stadsdeel** | [**GebiedenStadsdelenLink**](GebiedenStadsdelenLink.md) |  | 
**bestaat_uit_buurten** | [**List[GebiedenggpgebiedenBestaatUitBuurtenM2M]**](GebiedenggpgebiedenBestaatUitBuurtenM2M.md) |  | 

## Example

```python
from gebieden_api_client.models.gebieden_ggpgebieden_links import GebiedenGgpgebiedenLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenGgpgebiedenLinks from a JSON string
gebieden_ggpgebieden_links_instance = GebiedenGgpgebiedenLinks.from_json(json)
# print the JSON string representation of the object
print(GebiedenGgpgebiedenLinks.to_json())

# convert the object into a dict
gebieden_ggpgebieden_links_dict = gebieden_ggpgebieden_links_instance.to_dict()
# create an instance of GebiedenGgpgebiedenLinks from a dict
gebieden_ggpgebieden_links_from_dict = GebiedenGgpgebiedenLinks.from_dict(gebieden_ggpgebieden_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


