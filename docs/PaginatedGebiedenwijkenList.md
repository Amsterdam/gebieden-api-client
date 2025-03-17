# PaginatedGebiedenwijkenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PaginatedGebiedenbouwblokkenListPage**](PaginatedGebiedenbouwblokkenListPage.md) |  | [optional] 
**links** | [**PaginatedGebiedenbouwblokkenListLinks**](PaginatedGebiedenbouwblokkenListLinks.md) |  | [optional] 
**embedded** | [**PaginatedGebiedenwijkenListEmbedded**](PaginatedGebiedenwijkenListEmbedded.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenwijken_list import PaginatedGebiedenwijkenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenwijkenList from a JSON string
paginated_gebiedenwijken_list_instance = PaginatedGebiedenwijkenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenwijkenList.to_json())

# convert the object into a dict
paginated_gebiedenwijken_list_dict = paginated_gebiedenwijken_list_instance.to_dict()
# create an instance of PaginatedGebiedenwijkenList from a dict
paginated_gebiedenwijken_list_from_dict = PaginatedGebiedenwijkenList.from_dict(paginated_gebiedenwijken_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


