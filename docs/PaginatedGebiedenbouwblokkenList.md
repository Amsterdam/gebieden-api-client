# PaginatedGebiedenbouwblokkenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PaginatedGebiedenbouwblokkenListPage**](PaginatedGebiedenbouwblokkenListPage.md) |  | [optional] 
**links** | [**PaginatedGebiedenbouwblokkenListLinks**](PaginatedGebiedenbouwblokkenListLinks.md) |  | [optional] 
**embedded** | [**PaginatedGebiedenbouwblokkenListEmbedded**](PaginatedGebiedenbouwblokkenListEmbedded.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenbouwblokken_list import PaginatedGebiedenbouwblokkenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenbouwblokkenList from a JSON string
paginated_gebiedenbouwblokken_list_instance = PaginatedGebiedenbouwblokkenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenbouwblokkenList.to_json())

# convert the object into a dict
paginated_gebiedenbouwblokken_list_dict = paginated_gebiedenbouwblokken_list_instance.to_dict()
# create an instance of PaginatedGebiedenbouwblokkenList from a dict
paginated_gebiedenbouwblokken_list_from_dict = PaginatedGebiedenbouwblokkenList.from_dict(paginated_gebiedenbouwblokken_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


