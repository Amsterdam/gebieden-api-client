# PaginatedGebiedenbuurtenListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buurten** | [**List[Gebiedenbuurten]**](Gebiedenbuurten.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenbuurten_list_embedded import PaginatedGebiedenbuurtenListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenbuurtenListEmbedded from a JSON string
paginated_gebiedenbuurten_list_embedded_instance = PaginatedGebiedenbuurtenListEmbedded.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenbuurtenListEmbedded.to_json())

# convert the object into a dict
paginated_gebiedenbuurten_list_embedded_dict = paginated_gebiedenbuurten_list_embedded_instance.to_dict()
# create an instance of PaginatedGebiedenbuurtenListEmbedded from a dict
paginated_gebiedenbuurten_list_embedded_from_dict = PaginatedGebiedenbuurtenListEmbedded.from_dict(paginated_gebiedenbuurten_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


