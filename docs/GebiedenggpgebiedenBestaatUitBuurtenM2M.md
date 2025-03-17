# GebiedenggpgebiedenBestaatUitBuurtenM2M

The M2M table for `Ggpgebieden.bestaatUitBuurten` that links to `Buurten`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [readonly] 
**title** | **str** |  | [readonly] 
**identificatie** | **str** |  | [optional] 
**volgnummer** | **int** |  | [optional] 
**begin_geldigheid** | **datetime** |  | [optional] 
**eind_geldigheid** | **datetime** |  | [optional] 

## Example

```python
from gebieden_api_client.models.gebiedenggpgebieden_bestaat_uit_buurten_m2_m import GebiedenggpgebiedenBestaatUitBuurtenM2M

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenggpgebiedenBestaatUitBuurtenM2M from a JSON string
gebiedenggpgebieden_bestaat_uit_buurten_m2_m_instance = GebiedenggpgebiedenBestaatUitBuurtenM2M.from_json(json)
# print the JSON string representation of the object
print(GebiedenggpgebiedenBestaatUitBuurtenM2M.to_json())

# convert the object into a dict
gebiedenggpgebieden_bestaat_uit_buurten_m2_m_dict = gebiedenggpgebieden_bestaat_uit_buurten_m2_m_instance.to_dict()
# create an instance of GebiedenggpgebiedenBestaatUitBuurtenM2M from a dict
gebiedenggpgebieden_bestaat_uit_buurten_m2_m_from_dict = GebiedenggpgebiedenBestaatUitBuurtenM2M.from_dict(gebiedenggpgebieden_bestaat_uit_buurten_m2_m_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


