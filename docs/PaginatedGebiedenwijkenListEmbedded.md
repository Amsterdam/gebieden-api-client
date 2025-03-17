# PaginatedGebiedenwijkenListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wijken** | [**List[Gebiedenwijken]**](Gebiedenwijken.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenwijken_list_embedded import PaginatedGebiedenwijkenListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenwijkenListEmbedded from a JSON string
paginated_gebiedenwijken_list_embedded_instance = PaginatedGebiedenwijkenListEmbedded.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenwijkenListEmbedded.to_json())

# convert the object into a dict
paginated_gebiedenwijken_list_embedded_dict = paginated_gebiedenwijken_list_embedded_instance.to_dict()
# create an instance of PaginatedGebiedenwijkenListEmbedded from a dict
paginated_gebiedenwijken_list_embedded_from_dict = PaginatedGebiedenwijkenListEmbedded.from_dict(paginated_gebiedenwijken_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


