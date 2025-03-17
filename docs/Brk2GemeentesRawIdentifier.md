# Brk2GemeentesRawIdentifier

The identifier of the relationship to gemeentes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [readonly] 
**title** | **str** |  | 
**identificatie** | **str** |  | 

## Example

```python
from gebieden_api_client.models.brk2_gemeentes_raw_identifier import Brk2GemeentesRawIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of Brk2GemeentesRawIdentifier from a JSON string
brk2_gemeentes_raw_identifier_instance = Brk2GemeentesRawIdentifier.from_json(json)
# print the JSON string representation of the object
print(Brk2GemeentesRawIdentifier.to_json())

# convert the object into a dict
brk2_gemeentes_raw_identifier_dict = brk2_gemeentes_raw_identifier_instance.to_dict()
# create an instance of Brk2GemeentesRawIdentifier from a dict
brk2_gemeentes_raw_identifier_from_dict = Brk2GemeentesRawIdentifier.from_dict(brk2_gemeentes_raw_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


