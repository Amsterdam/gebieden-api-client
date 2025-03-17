# PaginatedGebiedenstadsdelenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PaginatedGebiedenbouwblokkenListPage**](PaginatedGebiedenbouwblokkenListPage.md) |  | [optional] 
**links** | [**PaginatedGebiedenbouwblokkenListLinks**](PaginatedGebiedenbouwblokkenListLinks.md) |  | [optional] 
**embedded** | [**PaginatedGebiedenstadsdelenListEmbedded**](PaginatedGebiedenstadsdelenListEmbedded.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenstadsdelen_list import PaginatedGebiedenstadsdelenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenstadsdelenList from a JSON string
paginated_gebiedenstadsdelen_list_instance = PaginatedGebiedenstadsdelenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenstadsdelenList.to_json())

# convert the object into a dict
paginated_gebiedenstadsdelen_list_dict = paginated_gebiedenstadsdelen_list_instance.to_dict()
# create an instance of PaginatedGebiedenstadsdelenList from a dict
paginated_gebiedenstadsdelen_list_from_dict = PaginatedGebiedenstadsdelenList.from_dict(paginated_gebiedenstadsdelen_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


