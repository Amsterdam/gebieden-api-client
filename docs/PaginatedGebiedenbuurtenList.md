# PaginatedGebiedenbuurtenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PaginatedGebiedenbouwblokkenListPage**](PaginatedGebiedenbouwblokkenListPage.md) |  | [optional] 
**links** | [**PaginatedGebiedenbouwblokkenListLinks**](PaginatedGebiedenbouwblokkenListLinks.md) |  | [optional] 
**embedded** | [**PaginatedGebiedenbuurtenListEmbedded**](PaginatedGebiedenbuurtenListEmbedded.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenbuurten_list import PaginatedGebiedenbuurtenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenbuurtenList from a JSON string
paginated_gebiedenbuurten_list_instance = PaginatedGebiedenbuurtenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenbuurtenList.to_json())

# convert the object into a dict
paginated_gebiedenbuurten_list_dict = paginated_gebiedenbuurten_list_instance.to_dict()
# create an instance of PaginatedGebiedenbuurtenList from a dict
paginated_gebiedenbuurten_list_from_dict = PaginatedGebiedenbuurtenList.from_dict(paginated_gebiedenbuurten_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


