# gebieden_api_client.GrootstedelijkeProjectenApi

All URIs are relative to *https://api.data.amsterdam.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gebieden_grootstedelijke_projecten_list**](GrootstedelijkeProjectenApi.md#gebieden_grootstedelijke_projecten_list) | **GET** /v1/gebieden/grootstedelijke_projecten/ | 
[**gebieden_grootstedelijke_projecten_retrieve**](GrootstedelijkeProjectenApi.md#gebieden_grootstedelijke_projecten_retrieve) | **GET** /v1/gebieden/grootstedelijke_projecten/{id}/ | 


# **gebieden_grootstedelijke_projecten_list**
> PaginatedGebiedengrootstedelijkeProjectenList gebieden_grootstedelijke_projecten_list(accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, count=count, expand=expand, expand_scope=expand_scope, fields=fields, format=format, page_size=page_size, sort=sort, datum=datum, datum_in=datum_in, datum_isempty=datum_isempty, datum_isnull=datum_isnull, datum_like=datum_like, datum_not=datum_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, id=id, id_gt=id_gt, id_gte=id_gte, id_in=id_in, id_isnull=id_isnull, id_lt=id_lt, id_lte=id_lte, id_not=id_not, legenda=legenda, legenda_in=legenda_in, legenda_isempty=legenda_isempty, legenda_isnull=legenda_isnull, legenda_like=legenda_like, legenda_not=legenda_not, naam=naam, naam_in=naam_in, naam_isempty=naam_isempty, naam_isnull=naam_isnull, naam_like=naam_like, naam_not=naam_not, page=page, type=type, type_in=type_in, type_isempty=type_isempty, type_isnull=type_isnull, type_like=type_like, type_not=type_not, typering=typering, typering_in=typering_in, typering_isempty=typering_isempty, typering_isnull=typering_isnull, typering_like=typering_like, typering_not=typering_not, url=url, url_in=url_in, url_isempty=url_isempty, url_isnull=url_isnull, url_like=url_like, url_not=url_not)

### Example

* OAuth Authentication (oauth2):

```python
import gebieden_api_client
from gebieden_api_client.models.paginated_gebiedengrootstedelijke_projecten_list import PaginatedGebiedengrootstedelijkeProjectenList
from gebieden_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.data.amsterdam.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = gebieden_api_client.Configuration(
    host = "https://api.data.amsterdam.nl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with gebieden_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gebieden_api_client.GrootstedelijkeProjectenApi(api_client)
    accept_crs = 'accept_crs_example' # str | Accept-Crs header for Geo queries (optional)
    content_crs = 'content_crs_example' # str | Content-Crs header for Geo queries (optional)
    x_api_key = 'x_api_key_example' # str | Api Key for statistical purposes, not for authentication (optional)
    count = True # bool | Include a count of the total result set and the number of pages.Only works for responses that return a page. (optional)
    expand = True # bool | Allow to expand relations. (optional)
    expand_scope = 'expand_scope_example' # str | Comma separated list of named relations to expand. (optional)
    fields = 'fields_example' # str | Comma-separated list of fields to display (optional)
    format = 'format_example' # str | Select the export format (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    sort = 'sort_example' # str | Which field to use when ordering the results. (optional)
    datum = 'datum_example' # str | Exact; text (optional)
    datum_in = ['datum_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    datum_isempty = True # bool | Whether the field is empty or not. (optional)
    datum_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    datum_like = 'datum_like_example' # str | Matches text using wildcards (? and *). (optional)
    datum_not = ['datum_not_example'] # List[str] | Exclude matches; text (optional)
    geometrie = 'geometrie_example' # str | GeoJSON | GEOMETRY(...) (optional)
    geometrie_contains = 'geometrie_contains_example' # str | Use x,y or POINT(x y) (optional)
    geometrie_intersects = 'geometrie_intersects_example' # str | Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON (optional)
    geometrie_isnull = 'geometrie_isnull_example' # str | Whether the field has a NULL value or not. (optional)
    geometrie_not = 'geometrie_not_example' # str | GeoJSON | GEOMETRY(...) (optional)
    id = 56 # int | Exact; number (optional)
    id_gt = 56 # int | Greater than; number (optional)
    id_gte = 56 # int | Greater than or equal to; number (optional)
    id_in = [56] # List[int] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    id_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    id_lt = 56 # int | Less than; number (optional)
    id_lte = 56 # int | Less than or equal to; number (optional)
    id_not = [56] # List[int] | Exclude matches; number (optional)
    legenda = 'legenda_example' # str | Exact; text (optional)
    legenda_in = ['legenda_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    legenda_isempty = True # bool | Whether the field is empty or not. (optional)
    legenda_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    legenda_like = 'legenda_like_example' # str | Matches text using wildcards (? and *). (optional)
    legenda_not = ['legenda_not_example'] # List[str] | Exclude matches; text (optional)
    naam = 'naam_example' # str | Exact; text (optional)
    naam_in = ['naam_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    naam_isempty = True # bool | Whether the field is empty or not. (optional)
    naam_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    naam_like = 'naam_like_example' # str | Matches text using wildcards (? and *). (optional)
    naam_not = ['naam_not_example'] # List[str] | Exclude matches; text (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    type = 'type_example' # str | Categorie GSP, OD, PHS of PHSOD (optional)
    type_in = ['type_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    type_isempty = True # bool | Whether the field is empty or not. (optional)
    type_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    type_like = 'type_like_example' # str | Matches text using wildcards (? and *). (optional)
    type_not = ['type_not_example'] # List[str] | Exclude matches; text (optional)
    typering = 'typering_example' # str | Omschrijving type (optional)
    typering_in = ['typering_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    typering_isempty = True # bool | Whether the field is empty or not. (optional)
    typering_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    typering_like = 'typering_like_example' # str | Matches text using wildcards (? and *). (optional)
    typering_not = ['typering_not_example'] # List[str] | Exclude matches; text (optional)
    url = 'url_example' # str | URL naar bekendmaking (optional)
    url_in = ['url_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    url_isempty = True # bool | Whether the field is empty or not. (optional)
    url_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    url_like = 'url_like_example' # str | Matches text using wildcards (? and *). (optional)
    url_not = ['url_not_example'] # List[str] | Exclude matches; URL (optional)

    try:
        api_response = await api_instance.gebieden_grootstedelijke_projecten_list(accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, count=count, expand=expand, expand_scope=expand_scope, fields=fields, format=format, page_size=page_size, sort=sort, datum=datum, datum_in=datum_in, datum_isempty=datum_isempty, datum_isnull=datum_isnull, datum_like=datum_like, datum_not=datum_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, id=id, id_gt=id_gt, id_gte=id_gte, id_in=id_in, id_isnull=id_isnull, id_lt=id_lt, id_lte=id_lte, id_not=id_not, legenda=legenda, legenda_in=legenda_in, legenda_isempty=legenda_isempty, legenda_isnull=legenda_isnull, legenda_like=legenda_like, legenda_not=legenda_not, naam=naam, naam_in=naam_in, naam_isempty=naam_isempty, naam_isnull=naam_isnull, naam_like=naam_like, naam_not=naam_not, page=page, type=type, type_in=type_in, type_isempty=type_isempty, type_isnull=type_isnull, type_like=type_like, type_not=type_not, typering=typering, typering_in=typering_in, typering_isempty=typering_isempty, typering_isnull=typering_isnull, typering_like=typering_like, typering_not=typering_not, url=url, url_in=url_in, url_isempty=url_isempty, url_isnull=url_isnull, url_like=url_like, url_not=url_not)
        print("The response of GrootstedelijkeProjectenApi->gebieden_grootstedelijke_projecten_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrootstedelijkeProjectenApi->gebieden_grootstedelijke_projecten_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_crs** | **str**| Accept-Crs header for Geo queries | [optional] 
 **content_crs** | **str**| Content-Crs header for Geo queries | [optional] 
 **x_api_key** | **str**| Api Key for statistical purposes, not for authentication | [optional] 
 **count** | **bool**| Include a count of the total result set and the number of pages.Only works for responses that return a page. | [optional] 
 **expand** | **bool**| Allow to expand relations. | [optional] 
 **expand_scope** | **str**| Comma separated list of named relations to expand. | [optional] 
 **fields** | **str**| Comma-separated list of fields to display | [optional] 
 **format** | **str**| Select the export format | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sort** | **str**| Which field to use when ordering the results. | [optional] 
 **datum** | **str**| Exact; text | [optional] 
 **datum_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **datum_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **datum_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **datum_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **datum_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **geometrie** | **str**| GeoJSON | GEOMETRY(...) | [optional] 
 **geometrie_contains** | **str**| Use x,y or POINT(x y) | [optional] 
 **geometrie_intersects** | **str**| Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON | [optional] 
 **geometrie_isnull** | **str**| Whether the field has a NULL value or not. | [optional] 
 **geometrie_not** | **str**| GeoJSON | GEOMETRY(...) | [optional] 
 **id** | **int**| Exact; number | [optional] 
 **id_gt** | **int**| Greater than; number | [optional] 
 **id_gte** | **int**| Greater than or equal to; number | [optional] 
 **id_in** | [**List[int]**](int.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **id_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **id_lt** | **int**| Less than; number | [optional] 
 **id_lte** | **int**| Less than or equal to; number | [optional] 
 **id_not** | [**List[int]**](int.md)| Exclude matches; number | [optional] 
 **legenda** | **str**| Exact; text | [optional] 
 **legenda_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **legenda_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **legenda_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **legenda_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **legenda_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **naam** | **str**| Exact; text | [optional] 
 **naam_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **naam_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **naam_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **naam_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **naam_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **type** | **str**| Categorie GSP, OD, PHS of PHSOD | [optional] 
 **type_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **type_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **type_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **type_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **type_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **typering** | **str**| Omschrijving type | [optional] 
 **typering_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **typering_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **typering_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **typering_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **typering_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **url** | **str**| URL naar bekendmaking | [optional] 
 **url_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **url_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **url_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **url_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **url_not** | [**List[str]**](str.md)| Exclude matches; URL | [optional] 

### Return type

[**PaginatedGebiedengrootstedelijkeProjectenList**](PaginatedGebiedengrootstedelijkeProjectenList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, text/csv, application/geo+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gebieden_grootstedelijke_projecten_retrieve**
> GebiedengrootstedelijkeProjecten gebieden_grootstedelijke_projecten_retrieve(id, accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, expand=expand, expand_scope=expand_scope, fields=fields, format=format, sort=sort, datum=datum, datum_in=datum_in, datum_isempty=datum_isempty, datum_isnull=datum_isnull, datum_like=datum_like, datum_not=datum_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, id2=id2, id_gt=id_gt, id_gte=id_gte, id_in=id_in, id_isnull=id_isnull, id_lt=id_lt, id_lte=id_lte, id_not=id_not, legenda=legenda, legenda_in=legenda_in, legenda_isempty=legenda_isempty, legenda_isnull=legenda_isnull, legenda_like=legenda_like, legenda_not=legenda_not, naam=naam, naam_in=naam_in, naam_isempty=naam_isempty, naam_isnull=naam_isnull, naam_like=naam_like, naam_not=naam_not, type=type, type_in=type_in, type_isempty=type_isempty, type_isnull=type_isnull, type_like=type_like, type_not=type_not, typering=typering, typering_in=typering_in, typering_isempty=typering_isempty, typering_isnull=typering_isnull, typering_like=typering_like, typering_not=typering_not, url=url, url_in=url_in, url_isempty=url_isempty, url_isnull=url_isnull, url_like=url_like, url_not=url_not)

### Example

* OAuth Authentication (oauth2):

```python
import gebieden_api_client
from gebieden_api_client.models.gebiedengrootstedelijke_projecten import GebiedengrootstedelijkeProjecten
from gebieden_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.data.amsterdam.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = gebieden_api_client.Configuration(
    host = "https://api.data.amsterdam.nl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with gebieden_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gebieden_api_client.GrootstedelijkeProjectenApi(api_client)
    id = 'id_example' # str | 
    accept_crs = 'accept_crs_example' # str | Accept-Crs header for Geo queries (optional)
    content_crs = 'content_crs_example' # str | Content-Crs header for Geo queries (optional)
    x_api_key = 'x_api_key_example' # str | Api Key for statistical purposes, not for authentication (optional)
    expand = True # bool | Allow to expand relations. (optional)
    expand_scope = 'expand_scope_example' # str | Comma separated list of named relations to expand. (optional)
    fields = 'fields_example' # str | Comma-separated list of fields to display (optional)
    format = 'format_example' # str | Select the export format (optional)
    sort = 'sort_example' # str | Which field to use when ordering the results. (optional)
    datum = 'datum_example' # str | Exact; text (optional)
    datum_in = ['datum_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    datum_isempty = True # bool | Whether the field is empty or not. (optional)
    datum_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    datum_like = 'datum_like_example' # str | Matches text using wildcards (? and *). (optional)
    datum_not = ['datum_not_example'] # List[str] | Exclude matches; text (optional)
    geometrie = 'geometrie_example' # str | GeoJSON | GEOMETRY(...) (optional)
    geometrie_contains = 'geometrie_contains_example' # str | Use x,y or POINT(x y) (optional)
    geometrie_intersects = 'geometrie_intersects_example' # str | Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON (optional)
    geometrie_isnull = 'geometrie_isnull_example' # str | Whether the field has a NULL value or not. (optional)
    geometrie_not = 'geometrie_not_example' # str | GeoJSON | GEOMETRY(...) (optional)
    id2 = 56 # int | Exact; number (optional)
    id_gt = 56 # int | Greater than; number (optional)
    id_gte = 56 # int | Greater than or equal to; number (optional)
    id_in = [56] # List[int] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    id_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    id_lt = 56 # int | Less than; number (optional)
    id_lte = 56 # int | Less than or equal to; number (optional)
    id_not = [56] # List[int] | Exclude matches; number (optional)
    legenda = 'legenda_example' # str | Exact; text (optional)
    legenda_in = ['legenda_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    legenda_isempty = True # bool | Whether the field is empty or not. (optional)
    legenda_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    legenda_like = 'legenda_like_example' # str | Matches text using wildcards (? and *). (optional)
    legenda_not = ['legenda_not_example'] # List[str] | Exclude matches; text (optional)
    naam = 'naam_example' # str | Exact; text (optional)
    naam_in = ['naam_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    naam_isempty = True # bool | Whether the field is empty or not. (optional)
    naam_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    naam_like = 'naam_like_example' # str | Matches text using wildcards (? and *). (optional)
    naam_not = ['naam_not_example'] # List[str] | Exclude matches; text (optional)
    type = 'type_example' # str | Categorie GSP, OD, PHS of PHSOD (optional)
    type_in = ['type_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    type_isempty = True # bool | Whether the field is empty or not. (optional)
    type_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    type_like = 'type_like_example' # str | Matches text using wildcards (? and *). (optional)
    type_not = ['type_not_example'] # List[str] | Exclude matches; text (optional)
    typering = 'typering_example' # str | Omschrijving type (optional)
    typering_in = ['typering_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    typering_isempty = True # bool | Whether the field is empty or not. (optional)
    typering_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    typering_like = 'typering_like_example' # str | Matches text using wildcards (? and *). (optional)
    typering_not = ['typering_not_example'] # List[str] | Exclude matches; text (optional)
    url = 'url_example' # str | URL naar bekendmaking (optional)
    url_in = ['url_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    url_isempty = True # bool | Whether the field is empty or not. (optional)
    url_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    url_like = 'url_like_example' # str | Matches text using wildcards (? and *). (optional)
    url_not = ['url_not_example'] # List[str] | Exclude matches; URL (optional)

    try:
        api_response = await api_instance.gebieden_grootstedelijke_projecten_retrieve(id, accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, expand=expand, expand_scope=expand_scope, fields=fields, format=format, sort=sort, datum=datum, datum_in=datum_in, datum_isempty=datum_isempty, datum_isnull=datum_isnull, datum_like=datum_like, datum_not=datum_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, id2=id2, id_gt=id_gt, id_gte=id_gte, id_in=id_in, id_isnull=id_isnull, id_lt=id_lt, id_lte=id_lte, id_not=id_not, legenda=legenda, legenda_in=legenda_in, legenda_isempty=legenda_isempty, legenda_isnull=legenda_isnull, legenda_like=legenda_like, legenda_not=legenda_not, naam=naam, naam_in=naam_in, naam_isempty=naam_isempty, naam_isnull=naam_isnull, naam_like=naam_like, naam_not=naam_not, type=type, type_in=type_in, type_isempty=type_isempty, type_isnull=type_isnull, type_like=type_like, type_not=type_not, typering=typering, typering_in=typering_in, typering_isempty=typering_isempty, typering_isnull=typering_isnull, typering_like=typering_like, typering_not=typering_not, url=url, url_in=url_in, url_isempty=url_isempty, url_isnull=url_isnull, url_like=url_like, url_not=url_not)
        print("The response of GrootstedelijkeProjectenApi->gebieden_grootstedelijke_projecten_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrootstedelijkeProjectenApi->gebieden_grootstedelijke_projecten_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **accept_crs** | **str**| Accept-Crs header for Geo queries | [optional] 
 **content_crs** | **str**| Content-Crs header for Geo queries | [optional] 
 **x_api_key** | **str**| Api Key for statistical purposes, not for authentication | [optional] 
 **expand** | **bool**| Allow to expand relations. | [optional] 
 **expand_scope** | **str**| Comma separated list of named relations to expand. | [optional] 
 **fields** | **str**| Comma-separated list of fields to display | [optional] 
 **format** | **str**| Select the export format | [optional] 
 **sort** | **str**| Which field to use when ordering the results. | [optional] 
 **datum** | **str**| Exact; text | [optional] 
 **datum_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **datum_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **datum_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **datum_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **datum_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **geometrie** | **str**| GeoJSON | GEOMETRY(...) | [optional] 
 **geometrie_contains** | **str**| Use x,y or POINT(x y) | [optional] 
 **geometrie_intersects** | **str**| Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON | [optional] 
 **geometrie_isnull** | **str**| Whether the field has a NULL value or not. | [optional] 
 **geometrie_not** | **str**| GeoJSON | GEOMETRY(...) | [optional] 
 **id2** | **int**| Exact; number | [optional] 
 **id_gt** | **int**| Greater than; number | [optional] 
 **id_gte** | **int**| Greater than or equal to; number | [optional] 
 **id_in** | [**List[int]**](int.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **id_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **id_lt** | **int**| Less than; number | [optional] 
 **id_lte** | **int**| Less than or equal to; number | [optional] 
 **id_not** | [**List[int]**](int.md)| Exclude matches; number | [optional] 
 **legenda** | **str**| Exact; text | [optional] 
 **legenda_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **legenda_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **legenda_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **legenda_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **legenda_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **naam** | **str**| Exact; text | [optional] 
 **naam_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **naam_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **naam_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **naam_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **naam_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **type** | **str**| Categorie GSP, OD, PHS of PHSOD | [optional] 
 **type_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **type_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **type_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **type_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **type_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **typering** | **str**| Omschrijving type | [optional] 
 **typering_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **typering_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **typering_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **typering_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **typering_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **url** | **str**| URL naar bekendmaking | [optional] 
 **url_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **url_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **url_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **url_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **url_not** | [**List[str]**](str.md)| Exclude matches; URL | [optional] 

### Return type

[**GebiedengrootstedelijkeProjecten**](GebiedengrootstedelijkeProjecten.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, text/csv, application/geo+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

