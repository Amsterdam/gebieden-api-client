# PaginatedGebiedenggpgebiedenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PaginatedGebiedenbouwblokkenListPage**](PaginatedGebiedenbouwblokkenListPage.md) |  | [optional] 
**links** | [**PaginatedGebiedenbouwblokkenListLinks**](PaginatedGebiedenbouwblokkenListLinks.md) |  | [optional] 
**embedded** | [**PaginatedGebiedenggpgebiedenListEmbedded**](PaginatedGebiedenggpgebiedenListEmbedded.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenggpgebieden_list import PaginatedGebiedenggpgebiedenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenggpgebiedenList from a JSON string
paginated_gebiedenggpgebieden_list_instance = PaginatedGebiedenggpgebiedenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenggpgebiedenList.to_json())

# convert the object into a dict
paginated_gebiedenggpgebieden_list_dict = paginated_gebiedenggpgebieden_list_instance.to_dict()
# create an instance of PaginatedGebiedenggpgebiedenList from a dict
paginated_gebiedenggpgebieden_list_from_dict = PaginatedGebiedenggpgebiedenList.from_dict(paginated_gebiedenggpgebieden_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


