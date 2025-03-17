# GebiedenGrootstedelijkeProjectenLinks

The contents of the `grootstedelijkeProjecten._links` field. It contains all relationships with objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The schema field is exposed with every record | [readonly] 
**var_self** | [**GebiedengrootstedelijkeProjectenLink**](GebiedengrootstedelijkeProjectenLink.md) |  | 

## Example

```python
from gebieden_api_client.models.gebieden_grootstedelijke_projecten_links import GebiedenGrootstedelijkeProjectenLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenGrootstedelijkeProjectenLinks from a JSON string
gebieden_grootstedelijke_projecten_links_instance = GebiedenGrootstedelijkeProjectenLinks.from_json(json)
# print the JSON string representation of the object
print(GebiedenGrootstedelijkeProjectenLinks.to_json())

# convert the object into a dict
gebieden_grootstedelijke_projecten_links_dict = gebieden_grootstedelijke_projecten_links_instance.to_dict()
# create an instance of GebiedenGrootstedelijkeProjectenLinks from a dict
gebieden_grootstedelijke_projecten_links_from_dict = GebiedenGrootstedelijkeProjectenLinks.from_dict(gebieden_grootstedelijke_projecten_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


