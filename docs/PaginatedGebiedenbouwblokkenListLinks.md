# PaginatedGebiedenbouwblokkenListLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**PaginatedGebiedenbouwblokkenListLinksSelf**](PaginatedGebiedenbouwblokkenListLinksSelf.md) |  | [optional] 
**next** | [**PaginatedGebiedenbouwblokkenListLinksNext**](PaginatedGebiedenbouwblokkenListLinksNext.md) |  | [optional] 
**previous** | [**PaginatedGebiedenbouwblokkenListLinksPrevious**](PaginatedGebiedenbouwblokkenListLinksPrevious.md) |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenbouwblokken_list_links import PaginatedGebiedenbouwblokkenListLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenbouwblokkenListLinks from a JSON string
paginated_gebiedenbouwblokken_list_links_instance = PaginatedGebiedenbouwblokkenListLinks.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenbouwblokkenListLinks.to_json())

# convert the object into a dict
paginated_gebiedenbouwblokken_list_links_dict = paginated_gebiedenbouwblokken_list_links_instance.to_dict()
# create an instance of PaginatedGebiedenbouwblokkenListLinks from a dict
paginated_gebiedenbouwblokken_list_links_from_dict = PaginatedGebiedenbouwblokkenListLinks.from_dict(paginated_gebiedenbouwblokken_list_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


