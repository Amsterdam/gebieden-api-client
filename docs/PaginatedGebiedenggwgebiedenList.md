# PaginatedGebiedenggwgebiedenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PaginatedGebiedenbouwblokkenListPage**](PaginatedGebiedenbouwblokkenListPage.md) |  | [optional] 
**links** | [**PaginatedGebiedenbouwblokkenListLinks**](PaginatedGebiedenbouwblokkenListLinks.md) |  | [optional] 
**embedded** | [**PaginatedGebiedenggwgebiedenListEmbedded**](PaginatedGebiedenggwgebiedenListEmbedded.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenggwgebieden_list import PaginatedGebiedenggwgebiedenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenggwgebiedenList from a JSON string
paginated_gebiedenggwgebieden_list_instance = PaginatedGebiedenggwgebiedenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenggwgebiedenList.to_json())

# convert the object into a dict
paginated_gebiedenggwgebieden_list_dict = paginated_gebiedenggwgebieden_list_instance.to_dict()
# create an instance of PaginatedGebiedenggwgebiedenList from a dict
paginated_gebiedenggwgebieden_list_from_dict = PaginatedGebiedenggwgebiedenList.from_dict(paginated_gebiedenggwgebieden_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


