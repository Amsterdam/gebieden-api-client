# GebiedenggwgebiedenBestaatUitBuurtenM2M

The M2M table for `Ggwgebieden.bestaatUitBuurten` that links to `Buurten`

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
from gebieden_api_client.models.gebiedenggwgebieden_bestaat_uit_buurten_m2_m import GebiedenggwgebiedenBestaatUitBuurtenM2M

# TODO update the JSON string below
json = "{}"
# create an instance of GebiedenggwgebiedenBestaatUitBuurtenM2M from a JSON string
gebiedenggwgebieden_bestaat_uit_buurten_m2_m_instance = GebiedenggwgebiedenBestaatUitBuurtenM2M.from_json(json)
# print the JSON string representation of the object
print(GebiedenggwgebiedenBestaatUitBuurtenM2M.to_json())

# convert the object into a dict
gebiedenggwgebieden_bestaat_uit_buurten_m2_m_dict = gebiedenggwgebieden_bestaat_uit_buurten_m2_m_instance.to_dict()
# create an instance of GebiedenggwgebiedenBestaatUitBuurtenM2M from a dict
gebiedenggwgebieden_bestaat_uit_buurten_m2_m_from_dict = GebiedenggwgebiedenBestaatUitBuurtenM2M.from_dict(gebiedenggwgebieden_bestaat_uit_buurten_m2_m_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


