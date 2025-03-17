# PaginatedGebiedenbouwblokkenListPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from gebieden_api_client.models.paginated_gebiedenbouwblokken_list_page import PaginatedGebiedenbouwblokkenListPage

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGebiedenbouwblokkenListPage from a JSON string
paginated_gebiedenbouwblokken_list_page_instance = PaginatedGebiedenbouwblokkenListPage.from_json(json)
# print the JSON string representation of the object
print(PaginatedGebiedenbouwblokkenListPage.to_json())

# convert the object into a dict
paginated_gebiedenbouwblokken_list_page_dict = paginated_gebiedenbouwblokken_list_page_instance.to_dict()
# create an instance of PaginatedGebiedenbouwblokkenListPage from a dict
paginated_gebiedenbouwblokken_list_page_from_dict = PaginatedGebiedenbouwblokkenListPage.from_dict(paginated_gebiedenbouwblokken_list_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


