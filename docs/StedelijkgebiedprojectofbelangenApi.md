# gebieden_api_client.StedelijkgebiedprojectofbelangenApi

All URIs are relative to *https://api.data.amsterdam.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gebieden_stedelijkgebiedprojectofbelangen_list**](StedelijkgebiedprojectofbelangenApi.md#gebieden_stedelijkgebiedprojectofbelangen_list) | **GET** /v1/gebieden/stedelijkgebiedprojectofbelangen/ | 
[**gebieden_stedelijkgebiedprojectofbelangen_retrieve**](StedelijkgebiedprojectofbelangenApi.md#gebieden_stedelijkgebiedprojectofbelangen_retrieve) | **GET** /v1/gebieden/stedelijkgebiedprojectofbelangen/{identificatie}/ | 


# **gebieden_stedelijkgebiedprojectofbelangen_list**
> PaginatedGebiedenstedelijkgebiedprojectofbelangenList gebieden_stedelijkgebiedprojectofbelangen_list(accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, count=count, expand=expand, expand_scope=expand_scope, fields=fields, format=format, page_size=page_size, sort=sort, datum=datum, datum_actueel_tot=datum_actueel_tot, datum_actueel_tot_gt=datum_actueel_tot_gt, datum_actueel_tot_gte=datum_actueel_tot_gte, datum_actueel_tot_in=datum_actueel_tot_in, datum_actueel_tot_isnull=datum_actueel_tot_isnull, datum_actueel_tot_lt=datum_actueel_tot_lt, datum_actueel_tot_lte=datum_actueel_tot_lte, datum_actueel_tot_not=datum_actueel_tot_not, datum_gt=datum_gt, datum_gte=datum_gte, datum_in=datum_in, datum_isnull=datum_isnull, datum_lt=datum_lt, datum_lte=datum_lte, datum_not=datum_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, identificatie=identificatie, identificatie_in=identificatie_in, identificatie_isempty=identificatie_isempty, identificatie_isnull=identificatie_isnull, identificatie_like=identificatie_like, identificatie_not=identificatie_not, legenda=legenda, legenda_in=legenda_in, legenda_isempty=legenda_isempty, legenda_isnull=legenda_isnull, legenda_like=legenda_like, legenda_not=legenda_not, naam=naam, naam_in=naam_in, naam_isempty=naam_isempty, naam_isnull=naam_isnull, naam_like=naam_like, naam_not=naam_not, page=page, url=url, url_in=url_in, url_isempty=url_isempty, url_isnull=url_isnull, url_like=url_like, url_not=url_not)

Stedelijke gebieden, projecten en belangen zijn projectgebieden binnen de gemeente Amsterdam, waar de voorbereiding van bestemmingsplannen door het college van burgemeester en wethouders of de burgemeester ter hand worden genomen

### Example

* OAuth Authentication (oauth2):

```python
import gebieden_api_client
from gebieden_api_client.models.paginated_gebiedenstedelijkgebiedprojectofbelangen_list import PaginatedGebiedenstedelijkgebiedprojectofbelangenList
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
    api_instance = gebieden_api_client.StedelijkgebiedprojectofbelangenApi(api_client)
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
    datum = '2013-10-20' # date | Wordt nog aangevuld (optional)
    datum_actueel_tot = '2013-10-20T19:20:30+01:00' # datetime | Einddatum van de cyclus, eventueel in combinatie met het kenmerk Status (optional)
    datum_actueel_tot_gt = '2013-10-20T19:20:30+01:00' # datetime | Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_actueel_tot_gte = '2013-10-20T19:20:30+01:00' # datetime | Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_actueel_tot_in = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    datum_actueel_tot_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    datum_actueel_tot_lt = '2013-10-20T19:20:30+01:00' # datetime | Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_actueel_tot_lte = '2013-10-20T19:20:30+01:00' # datetime | Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_actueel_tot_not = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_gt = '2013-10-20' # date | Greater than; use yyyy-mm-dd (optional)
    datum_gte = '2013-10-20' # date | Greater than or equal to; use yyyy-mm-dd (optional)
    datum_in = ['2013-10-20'] # List[date] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    datum_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    datum_lt = '2013-10-20' # date | Less than; use yyyy-mm-dd (optional)
    datum_lte = '2013-10-20' # date | Less than or equal to; use yyyy-mm-dd (optional)
    datum_not = ['2013-10-20'] # List[date] | Exclude matches; use yyyy-mm-dd (optional)
    geometrie = 'geometrie_example' # str | Geometrische beschrijving van een object (optional)
    geometrie_contains = 'geometrie_contains_example' # str | Use x,y or POINT(x y) (optional)
    geometrie_intersects = 'geometrie_intersects_example' # str | Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON (optional)
    geometrie_isnull = 'geometrie_isnull_example' # str | Whether the field has a NULL value or not. (optional)
    geometrie_not = 'geometrie_not_example' # str | GeoJSON | GEOMETRY(...) (optional)
    identificatie = 'identificatie_example' # str | Unieke identificatie van het object (optional)
    identificatie_in = ['identificatie_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    identificatie_isempty = True # bool | Whether the field is empty or not. (optional)
    identificatie_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    identificatie_like = 'identificatie_like_example' # str | Matches text using wildcards (? and *). (optional)
    identificatie_not = ['identificatie_not_example'] # List[str] | Exclude matches; text (optional)
    legenda = 'legenda_example' # str | Wordt nog aangevuld (optional)
    legenda_in = ['legenda_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    legenda_isempty = True # bool | Whether the field is empty or not. (optional)
    legenda_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    legenda_like = 'legenda_like_example' # str | Matches text using wildcards (? and *). (optional)
    legenda_not = ['legenda_not_example'] # List[str] | Exclude matches; text (optional)
    naam = 'naam_example' # str | De naam van het object (optional)
    naam_in = ['naam_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    naam_isempty = True # bool | Whether the field is empty or not. (optional)
    naam_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    naam_like = 'naam_like_example' # str | Matches text using wildcards (? and *). (optional)
    naam_not = ['naam_not_example'] # List[str] | Exclude matches; text (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    url = 'url_example' # str | URL naar bekendmaking (optional)
    url_in = ['url_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    url_isempty = True # bool | Whether the field is empty or not. (optional)
    url_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    url_like = 'url_like_example' # str | Matches text using wildcards (? and *). (optional)
    url_not = ['url_not_example'] # List[str] | Exclude matches; URL (optional)

    try:
        api_response = await api_instance.gebieden_stedelijkgebiedprojectofbelangen_list(accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, count=count, expand=expand, expand_scope=expand_scope, fields=fields, format=format, page_size=page_size, sort=sort, datum=datum, datum_actueel_tot=datum_actueel_tot, datum_actueel_tot_gt=datum_actueel_tot_gt, datum_actueel_tot_gte=datum_actueel_tot_gte, datum_actueel_tot_in=datum_actueel_tot_in, datum_actueel_tot_isnull=datum_actueel_tot_isnull, datum_actueel_tot_lt=datum_actueel_tot_lt, datum_actueel_tot_lte=datum_actueel_tot_lte, datum_actueel_tot_not=datum_actueel_tot_not, datum_gt=datum_gt, datum_gte=datum_gte, datum_in=datum_in, datum_isnull=datum_isnull, datum_lt=datum_lt, datum_lte=datum_lte, datum_not=datum_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, identificatie=identificatie, identificatie_in=identificatie_in, identificatie_isempty=identificatie_isempty, identificatie_isnull=identificatie_isnull, identificatie_like=identificatie_like, identificatie_not=identificatie_not, legenda=legenda, legenda_in=legenda_in, legenda_isempty=legenda_isempty, legenda_isnull=legenda_isnull, legenda_like=legenda_like, legenda_not=legenda_not, naam=naam, naam_in=naam_in, naam_isempty=naam_isempty, naam_isnull=naam_isnull, naam_like=naam_like, naam_not=naam_not, page=page, url=url, url_in=url_in, url_isempty=url_isempty, url_isnull=url_isnull, url_like=url_like, url_not=url_not)
        print("The response of StedelijkgebiedprojectofbelangenApi->gebieden_stedelijkgebiedprojectofbelangen_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StedelijkgebiedprojectofbelangenApi->gebieden_stedelijkgebiedprojectofbelangen_list: %s\n" % e)
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
 **datum** | **date**| Wordt nog aangevuld | [optional] 
 **datum_actueel_tot** | **datetime**| Einddatum van de cyclus, eventueel in combinatie met het kenmerk Status | [optional] 
 **datum_actueel_tot_gt** | **datetime**| Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_actueel_tot_gte** | **datetime**| Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_actueel_tot_in** | [**List[datetime]**](datetime.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **datum_actueel_tot_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **datum_actueel_tot_lt** | **datetime**| Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_actueel_tot_lte** | **datetime**| Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_actueel_tot_not** | [**List[datetime]**](datetime.md)| Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_gt** | **date**| Greater than; use yyyy-mm-dd | [optional] 
 **datum_gte** | **date**| Greater than or equal to; use yyyy-mm-dd | [optional] 
 **datum_in** | [**List[date]**](date.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **datum_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **datum_lt** | **date**| Less than; use yyyy-mm-dd | [optional] 
 **datum_lte** | **date**| Less than or equal to; use yyyy-mm-dd | [optional] 
 **datum_not** | [**List[date]**](date.md)| Exclude matches; use yyyy-mm-dd | [optional] 
 **geometrie** | **str**| Geometrische beschrijving van een object | [optional] 
 **geometrie_contains** | **str**| Use x,y or POINT(x y) | [optional] 
 **geometrie_intersects** | **str**| Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON | [optional] 
 **geometrie_isnull** | **str**| Whether the field has a NULL value or not. | [optional] 
 **geometrie_not** | **str**| GeoJSON | GEOMETRY(...) | [optional] 
 **identificatie** | **str**| Unieke identificatie van het object | [optional] 
 **identificatie_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **identificatie_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **identificatie_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **identificatie_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **identificatie_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **legenda** | **str**| Wordt nog aangevuld | [optional] 
 **legenda_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **legenda_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **legenda_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **legenda_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **legenda_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **naam** | **str**| De naam van het object | [optional] 
 **naam_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **naam_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **naam_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **naam_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **naam_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **url** | **str**| URL naar bekendmaking | [optional] 
 **url_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **url_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **url_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **url_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **url_not** | [**List[str]**](str.md)| Exclude matches; URL | [optional] 

### Return type

[**PaginatedGebiedenstedelijkgebiedprojectofbelangenList**](PaginatedGebiedenstedelijkgebiedprojectofbelangenList.md)

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

# **gebieden_stedelijkgebiedprojectofbelangen_retrieve**
> Gebiedenstedelijkgebiedprojectofbelangen gebieden_stedelijkgebiedprojectofbelangen_retrieve(identificatie, accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, expand=expand, expand_scope=expand_scope, fields=fields, format=format, sort=sort, datum=datum, datum_actueel_tot=datum_actueel_tot, datum_actueel_tot_gt=datum_actueel_tot_gt, datum_actueel_tot_gte=datum_actueel_tot_gte, datum_actueel_tot_in=datum_actueel_tot_in, datum_actueel_tot_isnull=datum_actueel_tot_isnull, datum_actueel_tot_lt=datum_actueel_tot_lt, datum_actueel_tot_lte=datum_actueel_tot_lte, datum_actueel_tot_not=datum_actueel_tot_not, datum_gt=datum_gt, datum_gte=datum_gte, datum_in=datum_in, datum_isnull=datum_isnull, datum_lt=datum_lt, datum_lte=datum_lte, datum_not=datum_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, identificatie2=identificatie2, identificatie_in=identificatie_in, identificatie_isempty=identificatie_isempty, identificatie_isnull=identificatie_isnull, identificatie_like=identificatie_like, identificatie_not=identificatie_not, legenda=legenda, legenda_in=legenda_in, legenda_isempty=legenda_isempty, legenda_isnull=legenda_isnull, legenda_like=legenda_like, legenda_not=legenda_not, naam=naam, naam_in=naam_in, naam_isempty=naam_isempty, naam_isnull=naam_isnull, naam_like=naam_like, naam_not=naam_not, url=url, url_in=url_in, url_isempty=url_isempty, url_isnull=url_isnull, url_like=url_like, url_not=url_not)

### Example

* OAuth Authentication (oauth2):

```python
import gebieden_api_client
from gebieden_api_client.models.gebiedenstedelijkgebiedprojectofbelangen import Gebiedenstedelijkgebiedprojectofbelangen
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
    api_instance = gebieden_api_client.StedelijkgebiedprojectofbelangenApi(api_client)
    identificatie = 'identificatie_example' # str | 
    accept_crs = 'accept_crs_example' # str | Accept-Crs header for Geo queries (optional)
    content_crs = 'content_crs_example' # str | Content-Crs header for Geo queries (optional)
    x_api_key = 'x_api_key_example' # str | Api Key for statistical purposes, not for authentication (optional)
    expand = True # bool | Allow to expand relations. (optional)
    expand_scope = 'expand_scope_example' # str | Comma separated list of named relations to expand. (optional)
    fields = 'fields_example' # str | Comma-separated list of fields to display (optional)
    format = 'format_example' # str | Select the export format (optional)
    sort = 'sort_example' # str | Which field to use when ordering the results. (optional)
    datum = '2013-10-20' # date | Wordt nog aangevuld (optional)
    datum_actueel_tot = '2013-10-20T19:20:30+01:00' # datetime | Einddatum van de cyclus, eventueel in combinatie met het kenmerk Status (optional)
    datum_actueel_tot_gt = '2013-10-20T19:20:30+01:00' # datetime | Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_actueel_tot_gte = '2013-10-20T19:20:30+01:00' # datetime | Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_actueel_tot_in = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    datum_actueel_tot_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    datum_actueel_tot_lt = '2013-10-20T19:20:30+01:00' # datetime | Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_actueel_tot_lte = '2013-10-20T19:20:30+01:00' # datetime | Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_actueel_tot_not = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    datum_gt = '2013-10-20' # date | Greater than; use yyyy-mm-dd (optional)
    datum_gte = '2013-10-20' # date | Greater than or equal to; use yyyy-mm-dd (optional)
    datum_in = ['2013-10-20'] # List[date] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    datum_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    datum_lt = '2013-10-20' # date | Less than; use yyyy-mm-dd (optional)
    datum_lte = '2013-10-20' # date | Less than or equal to; use yyyy-mm-dd (optional)
    datum_not = ['2013-10-20'] # List[date] | Exclude matches; use yyyy-mm-dd (optional)
    geometrie = 'geometrie_example' # str | Geometrische beschrijving van een object (optional)
    geometrie_contains = 'geometrie_contains_example' # str | Use x,y or POINT(x y) (optional)
    geometrie_intersects = 'geometrie_intersects_example' # str | Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON (optional)
    geometrie_isnull = 'geometrie_isnull_example' # str | Whether the field has a NULL value or not. (optional)
    geometrie_not = 'geometrie_not_example' # str | GeoJSON | GEOMETRY(...) (optional)
    identificatie2 = 'identificatie_example' # str | Unieke identificatie van het object (optional)
    identificatie_in = ['identificatie_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    identificatie_isempty = True # bool | Whether the field is empty or not. (optional)
    identificatie_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    identificatie_like = 'identificatie_like_example' # str | Matches text using wildcards (? and *). (optional)
    identificatie_not = ['identificatie_not_example'] # List[str] | Exclude matches; text (optional)
    legenda = 'legenda_example' # str | Wordt nog aangevuld (optional)
    legenda_in = ['legenda_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    legenda_isempty = True # bool | Whether the field is empty or not. (optional)
    legenda_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    legenda_like = 'legenda_like_example' # str | Matches text using wildcards (? and *). (optional)
    legenda_not = ['legenda_not_example'] # List[str] | Exclude matches; text (optional)
    naam = 'naam_example' # str | De naam van het object (optional)
    naam_in = ['naam_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    naam_isempty = True # bool | Whether the field is empty or not. (optional)
    naam_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    naam_like = 'naam_like_example' # str | Matches text using wildcards (? and *). (optional)
    naam_not = ['naam_not_example'] # List[str] | Exclude matches; text (optional)
    url = 'url_example' # str | URL naar bekendmaking (optional)
    url_in = ['url_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    url_isempty = True # bool | Whether the field is empty or not. (optional)
    url_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    url_like = 'url_like_example' # str | Matches text using wildcards (? and *). (optional)
    url_not = ['url_not_example'] # List[str] | Exclude matches; URL (optional)

    try:
        api_response = await api_instance.gebieden_stedelijkgebiedprojectofbelangen_retrieve(identificatie, accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, expand=expand, expand_scope=expand_scope, fields=fields, format=format, sort=sort, datum=datum, datum_actueel_tot=datum_actueel_tot, datum_actueel_tot_gt=datum_actueel_tot_gt, datum_actueel_tot_gte=datum_actueel_tot_gte, datum_actueel_tot_in=datum_actueel_tot_in, datum_actueel_tot_isnull=datum_actueel_tot_isnull, datum_actueel_tot_lt=datum_actueel_tot_lt, datum_actueel_tot_lte=datum_actueel_tot_lte, datum_actueel_tot_not=datum_actueel_tot_not, datum_gt=datum_gt, datum_gte=datum_gte, datum_in=datum_in, datum_isnull=datum_isnull, datum_lt=datum_lt, datum_lte=datum_lte, datum_not=datum_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, identificatie2=identificatie2, identificatie_in=identificatie_in, identificatie_isempty=identificatie_isempty, identificatie_isnull=identificatie_isnull, identificatie_like=identificatie_like, identificatie_not=identificatie_not, legenda=legenda, legenda_in=legenda_in, legenda_isempty=legenda_isempty, legenda_isnull=legenda_isnull, legenda_like=legenda_like, legenda_not=legenda_not, naam=naam, naam_in=naam_in, naam_isempty=naam_isempty, naam_isnull=naam_isnull, naam_like=naam_like, naam_not=naam_not, url=url, url_in=url_in, url_isempty=url_isempty, url_isnull=url_isnull, url_like=url_like, url_not=url_not)
        print("The response of StedelijkgebiedprojectofbelangenApi->gebieden_stedelijkgebiedprojectofbelangen_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StedelijkgebiedprojectofbelangenApi->gebieden_stedelijkgebiedprojectofbelangen_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificatie** | **str**|  | 
 **accept_crs** | **str**| Accept-Crs header for Geo queries | [optional] 
 **content_crs** | **str**| Content-Crs header for Geo queries | [optional] 
 **x_api_key** | **str**| Api Key for statistical purposes, not for authentication | [optional] 
 **expand** | **bool**| Allow to expand relations. | [optional] 
 **expand_scope** | **str**| Comma separated list of named relations to expand. | [optional] 
 **fields** | **str**| Comma-separated list of fields to display | [optional] 
 **format** | **str**| Select the export format | [optional] 
 **sort** | **str**| Which field to use when ordering the results. | [optional] 
 **datum** | **date**| Wordt nog aangevuld | [optional] 
 **datum_actueel_tot** | **datetime**| Einddatum van de cyclus, eventueel in combinatie met het kenmerk Status | [optional] 
 **datum_actueel_tot_gt** | **datetime**| Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_actueel_tot_gte** | **datetime**| Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_actueel_tot_in** | [**List[datetime]**](datetime.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **datum_actueel_tot_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **datum_actueel_tot_lt** | **datetime**| Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_actueel_tot_lte** | **datetime**| Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_actueel_tot_not** | [**List[datetime]**](datetime.md)| Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **datum_gt** | **date**| Greater than; use yyyy-mm-dd | [optional] 
 **datum_gte** | **date**| Greater than or equal to; use yyyy-mm-dd | [optional] 
 **datum_in** | [**List[date]**](date.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **datum_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **datum_lt** | **date**| Less than; use yyyy-mm-dd | [optional] 
 **datum_lte** | **date**| Less than or equal to; use yyyy-mm-dd | [optional] 
 **datum_not** | [**List[date]**](date.md)| Exclude matches; use yyyy-mm-dd | [optional] 
 **geometrie** | **str**| Geometrische beschrijving van een object | [optional] 
 **geometrie_contains** | **str**| Use x,y or POINT(x y) | [optional] 
 **geometrie_intersects** | **str**| Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON | [optional] 
 **geometrie_isnull** | **str**| Whether the field has a NULL value or not. | [optional] 
 **geometrie_not** | **str**| GeoJSON | GEOMETRY(...) | [optional] 
 **identificatie2** | **str**| Unieke identificatie van het object | [optional] 
 **identificatie_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **identificatie_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **identificatie_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **identificatie_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **identificatie_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **legenda** | **str**| Wordt nog aangevuld | [optional] 
 **legenda_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **legenda_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **legenda_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **legenda_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **legenda_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **naam** | **str**| De naam van het object | [optional] 
 **naam_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **naam_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **naam_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **naam_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **naam_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **url** | **str**| URL naar bekendmaking | [optional] 
 **url_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **url_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **url_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **url_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **url_not** | [**List[str]**](str.md)| Exclude matches; URL | [optional] 

### Return type

[**Gebiedenstedelijkgebiedprojectofbelangen**](Gebiedenstedelijkgebiedprojectofbelangen.md)

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

