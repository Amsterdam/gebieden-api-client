# PaginatedGebiedengrootstedelijkeProjectenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PaginatedGebiedenbouwblokkenListPage**](PaginatedGebiedenbouwblokkenListPage.md) |  | [optional] 
**links** | [**PaginatedGebiedenbouwblokkenListLinks**](PaginatedGebiedenbouwblokkenListLinks.md) |  | [optional] 
**embedded** | [**PaginatedGebiedengrootstedelijkeProjectenListEmbedded**](PaginatedGebiedengrootstedelijkeProjectenListEmbedded.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedengrootstedelijke_projecten_list import PaginatedGebiedengrootstedelijkeProjectenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedengrootstedelijkeProjectenList from a JSON string
paginated_gebiedengrootstedelijke_projecten_list_instance = PaginatedGebiedengrootstedelijkeProjectenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedengrootstedelijkeProjectenList.to_json())

# convert the object into a dict
paginated_gebiedengrootstedelijke_projecten_list_dict = paginated_gebiedengrootstedelijke_projecten_list_instance.to_dict()
# create an instance of PaginatedGebiedengrootstedelijkeProjectenList from a dict
paginated_gebiedengrootstedelijke_projecten_list_from_dict = PaginatedGebiedengrootstedelijkeProjectenList.from_dict(paginated_gebiedengrootstedelijke_projecten_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


