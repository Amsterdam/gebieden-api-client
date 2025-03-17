# gebieden_api_client.BouwblokkenApi

All URIs are relative to *https://api.data.amsterdam.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gebieden_bouwblokken_list**](BouwblokkenApi.md#gebieden_bouwblokken_list) | **GET** /v1/gebieden/bouwblokken/ | 
[**gebieden_bouwblokken_retrieve**](BouwblokkenApi.md#gebieden_bouwblokken_retrieve) | **GET** /v1/gebieden/bouwblokken/{id}/ | 


# **gebieden_bouwblokken_list**
> PaginatedGebiedenbouwblokkenList gebieden_bouwblokken_list(accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, count=count, expand=expand, expand_scope=expand_scope, fields=fields, format=format, page_size=page_size, sort=sort, begin_geldigheid=begin_geldigheid, begin_geldigheid_gt=begin_geldigheid_gt, begin_geldigheid_gte=begin_geldigheid_gte, begin_geldigheid_in=begin_geldigheid_in, begin_geldigheid_isnull=begin_geldigheid_isnull, begin_geldigheid_lt=begin_geldigheid_lt, begin_geldigheid_lte=begin_geldigheid_lte, begin_geldigheid_not=begin_geldigheid_not, code=code, code_in=code_in, code_isempty=code_isempty, code_isnull=code_isnull, code_like=code_like, code_not=code_not, eind_geldigheid=eind_geldigheid, eind_geldigheid_gt=eind_geldigheid_gt, eind_geldigheid_gte=eind_geldigheid_gte, eind_geldigheid_in=eind_geldigheid_in, eind_geldigheid_isnull=eind_geldigheid_isnull, eind_geldigheid_lt=eind_geldigheid_lt, eind_geldigheid_lte=eind_geldigheid_lte, eind_geldigheid_not=eind_geldigheid_not, geldig_op=geldig_op, geldig_op_gt=geldig_op_gt, geldig_op_gte=geldig_op_gte, geldig_op_in=geldig_op_in, geldig_op_isnull=geldig_op_isnull, geldig_op_lt=geldig_op_lt, geldig_op_lte=geldig_op_lte, geldig_op_not=geldig_op_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, id=id, id_in=id_in, id_isempty=id_isempty, id_isnull=id_isnull, id_like=id_like, id_not=id_not, identificatie=identificatie, identificatie_in=identificatie_in, identificatie_isempty=identificatie_isempty, identificatie_isnull=identificatie_isnull, identificatie_like=identificatie_like, identificatie_not=identificatie_not, ligt_in_buurt_identificatie=ligt_in_buurt_identificatie, ligt_in_buurt_identificatie_in=ligt_in_buurt_identificatie_in, ligt_in_buurt_identificatie_isempty=ligt_in_buurt_identificatie_isempty, ligt_in_buurt_identificatie_isnull=ligt_in_buurt_identificatie_isnull, ligt_in_buurt_identificatie_like=ligt_in_buurt_identificatie_like, ligt_in_buurt_identificatie_not=ligt_in_buurt_identificatie_not, ligt_in_buurt_volgnummer=ligt_in_buurt_volgnummer, ligt_in_buurt_volgnummer_gt=ligt_in_buurt_volgnummer_gt, ligt_in_buurt_volgnummer_gte=ligt_in_buurt_volgnummer_gte, ligt_in_buurt_volgnummer_in=ligt_in_buurt_volgnummer_in, ligt_in_buurt_volgnummer_isnull=ligt_in_buurt_volgnummer_isnull, ligt_in_buurt_volgnummer_lt=ligt_in_buurt_volgnummer_lt, ligt_in_buurt_volgnummer_lte=ligt_in_buurt_volgnummer_lte, ligt_in_buurt_volgnummer_not=ligt_in_buurt_volgnummer_not, page=page, registratiedatum=registratiedatum, registratiedatum_gt=registratiedatum_gt, registratiedatum_gte=registratiedatum_gte, registratiedatum_in=registratiedatum_in, registratiedatum_isnull=registratiedatum_isnull, registratiedatum_lt=registratiedatum_lt, registratiedatum_lte=registratiedatum_lte, registratiedatum_not=registratiedatum_not, volgnummer=volgnummer, volgnummer_gt=volgnummer_gt, volgnummer_gte=volgnummer_gte, volgnummer_in=volgnummer_in, volgnummer_isnull=volgnummer_isnull, volgnummer_lt=volgnummer_lt, volgnummer_lte=volgnummer_lte, volgnummer_not=volgnummer_not)

Een bouwblok is het kleinst mogelijk afgrensbare gebied, in zijn geheel tot een buurt behorend, dat geheel of grotendeels door bestaande of aan te leggen wegen en/of waterlopen is of zal zijn ingesloten en waarop tenminste één gebouw met verblijfsobject staat op maaiveld niveau. Dus ondergrondse garages en metrostations krijgen géén bouwblok

### Example

* OAuth Authentication (oauth2):

```python
import gebieden_api_client
from gebieden_api_client.models.paginated_gebiedenbouwblokken_list import PaginatedGebiedenbouwblokkenList
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
    api_instance = gebieden_api_client.BouwblokkenApi(api_client)
    accept_crs = 'accept_crs_example' # str | Accept-Crs header for Geo queries (optional)
    content_crs = 'content_crs_example' # str | Content-Crs header for Geo queries (optional)
    x_api_key = 'x_api_key_example' # str | Api Key for statistical purposes, not for authentication (optional)
    count = True # bool | Include a count of the total result set and the number of pages.Only works for responses that return a page. (optional)
    expand = True # bool | Allow to expand relations. (optional)
    expand_scope = 'ligtInBuurt' # str | Comma separated list of named relations to expand. (optional)
    fields = 'fields_example' # str | Comma-separated list of fields to display (optional)
    format = 'format_example' # str | Select the export format (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    sort = 'sort_example' # str | Which field to use when ordering the results. (optional)
    begin_geldigheid = '2013-10-20T19:20:30+01:00' # datetime | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok (optional)
    begin_geldigheid_gt = '2013-10-20T19:20:30+01:00' # datetime | Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    begin_geldigheid_gte = '2013-10-20T19:20:30+01:00' # datetime | Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    begin_geldigheid_in = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    begin_geldigheid_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    begin_geldigheid_lt = '2013-10-20T19:20:30+01:00' # datetime | Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    begin_geldigheid_lte = '2013-10-20T19:20:30+01:00' # datetime | Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    begin_geldigheid_not = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    code = 'code_example' # str | Officiële code van het object (optional)
    code_in = ['code_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    code_isempty = True # bool | Whether the field is empty or not. (optional)
    code_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    code_like = 'code_like_example' # str | Matches text using wildcards (? and *). (optional)
    code_not = ['code_not_example'] # List[str] | Exclude matches; text (optional)
    eind_geldigheid = '2013-10-20T19:20:30+01:00' # datetime | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok (optional)
    eind_geldigheid_gt = '2013-10-20T19:20:30+01:00' # datetime | Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    eind_geldigheid_gte = '2013-10-20T19:20:30+01:00' # datetime | Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    eind_geldigheid_in = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    eind_geldigheid_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    eind_geldigheid_lt = '2013-10-20T19:20:30+01:00' # datetime | Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    eind_geldigheid_lte = '2013-10-20T19:20:30+01:00' # datetime | Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    eind_geldigheid_not = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    geldig_op = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_in = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_isnull = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_not = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geometrie = 'geometrie_example' # str | Geometrische beschrijving van een object (optional)
    geometrie_contains = 'geometrie_contains_example' # str | Use x,y or POINT(x y) (optional)
    geometrie_intersects = 'geometrie_intersects_example' # str | Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON (optional)
    geometrie_isnull = 'geometrie_isnull_example' # str | Whether the field has a NULL value or not. (optional)
    geometrie_not = 'geometrie_not_example' # str | GeoJSON | GEOMETRY(...) (optional)
    id = 'id_example' # str | Exact; text (optional)
    id_in = ['id_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    id_isempty = True # bool | Whether the field is empty or not. (optional)
    id_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    id_like = 'id_like_example' # str | Matches text using wildcards (? and *). (optional)
    id_not = ['id_not_example'] # List[str] | Exclude matches; text (optional)
    identificatie = 'identificatie_example' # str | Unieke identificatie van het object (optional)
    identificatie_in = ['identificatie_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    identificatie_isempty = True # bool | Whether the field is empty or not. (optional)
    identificatie_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    identificatie_like = 'identificatie_like_example' # str | Matches text using wildcards (? and *). (optional)
    identificatie_not = ['identificatie_not_example'] # List[str] | Exclude matches; text (optional)
    ligt_in_buurt_identificatie = 'ligt_in_buurt_identificatie_example' # str | Unieke identificatie van het object (optional)
    ligt_in_buurt_identificatie_in = ['ligt_in_buurt_identificatie_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    ligt_in_buurt_identificatie_isempty = True # bool | Whether the field is empty or not. (optional)
    ligt_in_buurt_identificatie_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    ligt_in_buurt_identificatie_like = 'ligt_in_buurt_identificatie_like_example' # str | Matches text using wildcards (? and *). (optional)
    ligt_in_buurt_identificatie_not = ['ligt_in_buurt_identificatie_not_example'] # List[str] | Exclude matches; text (optional)
    ligt_in_buurt_volgnummer = 56 # int | Uniek volgnummer van de toestand van het object (optional)
    ligt_in_buurt_volgnummer_gt = 56 # int | Greater than; number (optional)
    ligt_in_buurt_volgnummer_gte = 56 # int | Greater than or equal to; number (optional)
    ligt_in_buurt_volgnummer_in = [56] # List[int] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    ligt_in_buurt_volgnummer_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    ligt_in_buurt_volgnummer_lt = 56 # int | Less than; number (optional)
    ligt_in_buurt_volgnummer_lte = 56 # int | Less than or equal to; number (optional)
    ligt_in_buurt_volgnummer_not = [56] # List[int] | Exclude matches; number (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    registratiedatum = '2013-10-20T19:20:30+01:00' # datetime | Datum waarop het gegeven in de bron geregistreerd is (optional)
    registratiedatum_gt = '2013-10-20T19:20:30+01:00' # datetime | Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    registratiedatum_gte = '2013-10-20T19:20:30+01:00' # datetime | Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    registratiedatum_in = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    registratiedatum_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    registratiedatum_lt = '2013-10-20T19:20:30+01:00' # datetime | Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    registratiedatum_lte = '2013-10-20T19:20:30+01:00' # datetime | Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    registratiedatum_not = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    volgnummer = 56 # int | Uniek volgnummer van de toestand van het object (optional)
    volgnummer_gt = 56 # int | Greater than; number (optional)
    volgnummer_gte = 56 # int | Greater than or equal to; number (optional)
    volgnummer_in = [56] # List[int] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    volgnummer_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    volgnummer_lt = 56 # int | Less than; number (optional)
    volgnummer_lte = 56 # int | Less than or equal to; number (optional)
    volgnummer_not = [56] # List[int] | Exclude matches; number (optional)

    try:
        api_response = await api_instance.gebieden_bouwblokken_list(accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, count=count, expand=expand, expand_scope=expand_scope, fields=fields, format=format, page_size=page_size, sort=sort, begin_geldigheid=begin_geldigheid, begin_geldigheid_gt=begin_geldigheid_gt, begin_geldigheid_gte=begin_geldigheid_gte, begin_geldigheid_in=begin_geldigheid_in, begin_geldigheid_isnull=begin_geldigheid_isnull, begin_geldigheid_lt=begin_geldigheid_lt, begin_geldigheid_lte=begin_geldigheid_lte, begin_geldigheid_not=begin_geldigheid_not, code=code, code_in=code_in, code_isempty=code_isempty, code_isnull=code_isnull, code_like=code_like, code_not=code_not, eind_geldigheid=eind_geldigheid, eind_geldigheid_gt=eind_geldigheid_gt, eind_geldigheid_gte=eind_geldigheid_gte, eind_geldigheid_in=eind_geldigheid_in, eind_geldigheid_isnull=eind_geldigheid_isnull, eind_geldigheid_lt=eind_geldigheid_lt, eind_geldigheid_lte=eind_geldigheid_lte, eind_geldigheid_not=eind_geldigheid_not, geldig_op=geldig_op, geldig_op_gt=geldig_op_gt, geldig_op_gte=geldig_op_gte, geldig_op_in=geldig_op_in, geldig_op_isnull=geldig_op_isnull, geldig_op_lt=geldig_op_lt, geldig_op_lte=geldig_op_lte, geldig_op_not=geldig_op_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, id=id, id_in=id_in, id_isempty=id_isempty, id_isnull=id_isnull, id_like=id_like, id_not=id_not, identificatie=identificatie, identificatie_in=identificatie_in, identificatie_isempty=identificatie_isempty, identificatie_isnull=identificatie_isnull, identificatie_like=identificatie_like, identificatie_not=identificatie_not, ligt_in_buurt_identificatie=ligt_in_buurt_identificatie, ligt_in_buurt_identificatie_in=ligt_in_buurt_identificatie_in, ligt_in_buurt_identificatie_isempty=ligt_in_buurt_identificatie_isempty, ligt_in_buurt_identificatie_isnull=ligt_in_buurt_identificatie_isnull, ligt_in_buurt_identificatie_like=ligt_in_buurt_identificatie_like, ligt_in_buurt_identificatie_not=ligt_in_buurt_identificatie_not, ligt_in_buurt_volgnummer=ligt_in_buurt_volgnummer, ligt_in_buurt_volgnummer_gt=ligt_in_buurt_volgnummer_gt, ligt_in_buurt_volgnummer_gte=ligt_in_buurt_volgnummer_gte, ligt_in_buurt_volgnummer_in=ligt_in_buurt_volgnummer_in, ligt_in_buurt_volgnummer_isnull=ligt_in_buurt_volgnummer_isnull, ligt_in_buurt_volgnummer_lt=ligt_in_buurt_volgnummer_lt, ligt_in_buurt_volgnummer_lte=ligt_in_buurt_volgnummer_lte, ligt_in_buurt_volgnummer_not=ligt_in_buurt_volgnummer_not, page=page, registratiedatum=registratiedatum, registratiedatum_gt=registratiedatum_gt, registratiedatum_gte=registratiedatum_gte, registratiedatum_in=registratiedatum_in, registratiedatum_isnull=registratiedatum_isnull, registratiedatum_lt=registratiedatum_lt, registratiedatum_lte=registratiedatum_lte, registratiedatum_not=registratiedatum_not, volgnummer=volgnummer, volgnummer_gt=volgnummer_gt, volgnummer_gte=volgnummer_gte, volgnummer_in=volgnummer_in, volgnummer_isnull=volgnummer_isnull, volgnummer_lt=volgnummer_lt, volgnummer_lte=volgnummer_lte, volgnummer_not=volgnummer_not)
        print("The response of BouwblokkenApi->gebieden_bouwblokken_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BouwblokkenApi->gebieden_bouwblokken_list: %s\n" % e)
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
 **begin_geldigheid** | **datetime**| De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok | [optional] 
 **begin_geldigheid_gt** | **datetime**| Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **begin_geldigheid_gte** | **datetime**| Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **begin_geldigheid_in** | [**List[datetime]**](datetime.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **begin_geldigheid_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **begin_geldigheid_lt** | **datetime**| Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **begin_geldigheid_lte** | **datetime**| Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **begin_geldigheid_not** | [**List[datetime]**](datetime.md)| Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **code** | **str**| Officiële code van het object | [optional] 
 **code_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **code_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **code_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **code_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **code_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **eind_geldigheid** | **datetime**| De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok | [optional] 
 **eind_geldigheid_gt** | **datetime**| Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **eind_geldigheid_gte** | **datetime**| Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **eind_geldigheid_in** | [**List[datetime]**](datetime.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **eind_geldigheid_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **eind_geldigheid_lt** | **datetime**| Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **eind_geldigheid_lte** | **datetime**| Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **eind_geldigheid_not** | [**List[datetime]**](datetime.md)| Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **geldig_op** | **datetime**|  | [optional] 
 **geldig_op_gt** | **datetime**|  | [optional] 
 **geldig_op_gte** | **datetime**|  | [optional] 
 **geldig_op_in** | **datetime**|  | [optional] 
 **geldig_op_isnull** | **datetime**|  | [optional] 
 **geldig_op_lt** | **datetime**|  | [optional] 
 **geldig_op_lte** | **datetime**|  | [optional] 
 **geldig_op_not** | **datetime**|  | [optional] 
 **geometrie** | **str**| Geometrische beschrijving van een object | [optional] 
 **geometrie_contains** | **str**| Use x,y or POINT(x y) | [optional] 
 **geometrie_intersects** | **str**| Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON | [optional] 
 **geometrie_isnull** | **str**| Whether the field has a NULL value or not. | [optional] 
 **geometrie_not** | **str**| GeoJSON | GEOMETRY(...) | [optional] 
 **id** | **str**| Exact; text | [optional] 
 **id_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **id_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **id_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **id_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **id_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **identificatie** | **str**| Unieke identificatie van het object | [optional] 
 **identificatie_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **identificatie_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **identificatie_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **identificatie_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **identificatie_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **ligt_in_buurt_identificatie** | **str**| Unieke identificatie van het object | [optional] 
 **ligt_in_buurt_identificatie_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **ligt_in_buurt_identificatie_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **ligt_in_buurt_identificatie_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **ligt_in_buurt_identificatie_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **ligt_in_buurt_identificatie_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **ligt_in_buurt_volgnummer** | **int**| Uniek volgnummer van de toestand van het object | [optional] 
 **ligt_in_buurt_volgnummer_gt** | **int**| Greater than; number | [optional] 
 **ligt_in_buurt_volgnummer_gte** | **int**| Greater than or equal to; number | [optional] 
 **ligt_in_buurt_volgnummer_in** | [**List[int]**](int.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **ligt_in_buurt_volgnummer_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **ligt_in_buurt_volgnummer_lt** | **int**| Less than; number | [optional] 
 **ligt_in_buurt_volgnummer_lte** | **int**| Less than or equal to; number | [optional] 
 **ligt_in_buurt_volgnummer_not** | [**List[int]**](int.md)| Exclude matches; number | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **registratiedatum** | **datetime**| Datum waarop het gegeven in de bron geregistreerd is | [optional] 
 **registratiedatum_gt** | **datetime**| Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **registratiedatum_gte** | **datetime**| Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **registratiedatum_in** | [**List[datetime]**](datetime.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **registratiedatum_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **registratiedatum_lt** | **datetime**| Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **registratiedatum_lte** | **datetime**| Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **registratiedatum_not** | [**List[datetime]**](datetime.md)| Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **volgnummer** | **int**| Uniek volgnummer van de toestand van het object | [optional] 
 **volgnummer_gt** | **int**| Greater than; number | [optional] 
 **volgnummer_gte** | **int**| Greater than or equal to; number | [optional] 
 **volgnummer_in** | [**List[int]**](int.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **volgnummer_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **volgnummer_lt** | **int**| Less than; number | [optional] 
 **volgnummer_lte** | **int**| Less than or equal to; number | [optional] 
 **volgnummer_not** | [**List[int]**](int.md)| Exclude matches; number | [optional] 

### Return type

[**PaginatedGebiedenbouwblokkenList**](PaginatedGebiedenbouwblokkenList.md)

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

# **gebieden_bouwblokken_retrieve**
> Gebiedenbouwblokken gebieden_bouwblokken_retrieve(id, accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, expand=expand, expand_scope=expand_scope, fields=fields, format=format, sort=sort, begin_geldigheid=begin_geldigheid, begin_geldigheid_gt=begin_geldigheid_gt, begin_geldigheid_gte=begin_geldigheid_gte, begin_geldigheid_in=begin_geldigheid_in, begin_geldigheid_isnull=begin_geldigheid_isnull, begin_geldigheid_lt=begin_geldigheid_lt, begin_geldigheid_lte=begin_geldigheid_lte, begin_geldigheid_not=begin_geldigheid_not, code=code, code_in=code_in, code_isempty=code_isempty, code_isnull=code_isnull, code_like=code_like, code_not=code_not, eind_geldigheid=eind_geldigheid, eind_geldigheid_gt=eind_geldigheid_gt, eind_geldigheid_gte=eind_geldigheid_gte, eind_geldigheid_in=eind_geldigheid_in, eind_geldigheid_isnull=eind_geldigheid_isnull, eind_geldigheid_lt=eind_geldigheid_lt, eind_geldigheid_lte=eind_geldigheid_lte, eind_geldigheid_not=eind_geldigheid_not, geldig_op=geldig_op, geldig_op_gt=geldig_op_gt, geldig_op_gte=geldig_op_gte, geldig_op_in=geldig_op_in, geldig_op_isnull=geldig_op_isnull, geldig_op_lt=geldig_op_lt, geldig_op_lte=geldig_op_lte, geldig_op_not=geldig_op_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, id2=id2, id_in=id_in, id_isempty=id_isempty, id_isnull=id_isnull, id_like=id_like, id_not=id_not, identificatie=identificatie, identificatie_in=identificatie_in, identificatie_isempty=identificatie_isempty, identificatie_isnull=identificatie_isnull, identificatie_like=identificatie_like, identificatie_not=identificatie_not, ligt_in_buurt_identificatie=ligt_in_buurt_identificatie, ligt_in_buurt_identificatie_in=ligt_in_buurt_identificatie_in, ligt_in_buurt_identificatie_isempty=ligt_in_buurt_identificatie_isempty, ligt_in_buurt_identificatie_isnull=ligt_in_buurt_identificatie_isnull, ligt_in_buurt_identificatie_like=ligt_in_buurt_identificatie_like, ligt_in_buurt_identificatie_not=ligt_in_buurt_identificatie_not, ligt_in_buurt_volgnummer=ligt_in_buurt_volgnummer, ligt_in_buurt_volgnummer_gt=ligt_in_buurt_volgnummer_gt, ligt_in_buurt_volgnummer_gte=ligt_in_buurt_volgnummer_gte, ligt_in_buurt_volgnummer_in=ligt_in_buurt_volgnummer_in, ligt_in_buurt_volgnummer_isnull=ligt_in_buurt_volgnummer_isnull, ligt_in_buurt_volgnummer_lt=ligt_in_buurt_volgnummer_lt, ligt_in_buurt_volgnummer_lte=ligt_in_buurt_volgnummer_lte, ligt_in_buurt_volgnummer_not=ligt_in_buurt_volgnummer_not, registratiedatum=registratiedatum, registratiedatum_gt=registratiedatum_gt, registratiedatum_gte=registratiedatum_gte, registratiedatum_in=registratiedatum_in, registratiedatum_isnull=registratiedatum_isnull, registratiedatum_lt=registratiedatum_lt, registratiedatum_lte=registratiedatum_lte, registratiedatum_not=registratiedatum_not, volgnummer=volgnummer, volgnummer_gt=volgnummer_gt, volgnummer_gte=volgnummer_gte, volgnummer_in=volgnummer_in, volgnummer_isnull=volgnummer_isnull, volgnummer_lt=volgnummer_lt, volgnummer_lte=volgnummer_lte, volgnummer_not=volgnummer_not)

### Example

* OAuth Authentication (oauth2):

```python
import gebieden_api_client
from gebieden_api_client.models.gebiedenbouwblokken import Gebiedenbouwblokken
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
    api_instance = gebieden_api_client.BouwblokkenApi(api_client)
    id = 'id_example' # str | 
    accept_crs = 'accept_crs_example' # str | Accept-Crs header for Geo queries (optional)
    content_crs = 'content_crs_example' # str | Content-Crs header for Geo queries (optional)
    x_api_key = 'x_api_key_example' # str | Api Key for statistical purposes, not for authentication (optional)
    expand = True # bool | Allow to expand relations. (optional)
    expand_scope = 'ligtInBuurt' # str | Comma separated list of named relations to expand. (optional)
    fields = 'fields_example' # str | Comma-separated list of fields to display (optional)
    format = 'format_example' # str | Select the export format (optional)
    sort = 'sort_example' # str | Which field to use when ordering the results. (optional)
    begin_geldigheid = '2013-10-20T19:20:30+01:00' # datetime | De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok (optional)
    begin_geldigheid_gt = '2013-10-20T19:20:30+01:00' # datetime | Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    begin_geldigheid_gte = '2013-10-20T19:20:30+01:00' # datetime | Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    begin_geldigheid_in = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    begin_geldigheid_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    begin_geldigheid_lt = '2013-10-20T19:20:30+01:00' # datetime | Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    begin_geldigheid_lte = '2013-10-20T19:20:30+01:00' # datetime | Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    begin_geldigheid_not = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    code = 'code_example' # str | Officiële code van het object (optional)
    code_in = ['code_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    code_isempty = True # bool | Whether the field is empty or not. (optional)
    code_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    code_like = 'code_like_example' # str | Matches text using wildcards (? and *). (optional)
    code_not = ['code_not_example'] # List[str] | Exclude matches; text (optional)
    eind_geldigheid = '2013-10-20T19:20:30+01:00' # datetime | De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok (optional)
    eind_geldigheid_gt = '2013-10-20T19:20:30+01:00' # datetime | Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    eind_geldigheid_gte = '2013-10-20T19:20:30+01:00' # datetime | Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    eind_geldigheid_in = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    eind_geldigheid_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    eind_geldigheid_lt = '2013-10-20T19:20:30+01:00' # datetime | Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    eind_geldigheid_lte = '2013-10-20T19:20:30+01:00' # datetime | Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    eind_geldigheid_not = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    geldig_op = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_gt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_in = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_isnull = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_lt = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geldig_op_not = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    geometrie = 'geometrie_example' # str | Geometrische beschrijving van een object (optional)
    geometrie_contains = 'geometrie_contains_example' # str | Use x,y or POINT(x y) (optional)
    geometrie_intersects = 'geometrie_intersects_example' # str | Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON (optional)
    geometrie_isnull = 'geometrie_isnull_example' # str | Whether the field has a NULL value or not. (optional)
    geometrie_not = 'geometrie_not_example' # str | GeoJSON | GEOMETRY(...) (optional)
    id2 = 'id_example' # str | Exact; text (optional)
    id_in = ['id_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    id_isempty = True # bool | Whether the field is empty or not. (optional)
    id_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    id_like = 'id_like_example' # str | Matches text using wildcards (? and *). (optional)
    id_not = ['id_not_example'] # List[str] | Exclude matches; text (optional)
    identificatie = 'identificatie_example' # str | Unieke identificatie van het object (optional)
    identificatie_in = ['identificatie_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    identificatie_isempty = True # bool | Whether the field is empty or not. (optional)
    identificatie_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    identificatie_like = 'identificatie_like_example' # str | Matches text using wildcards (? and *). (optional)
    identificatie_not = ['identificatie_not_example'] # List[str] | Exclude matches; text (optional)
    ligt_in_buurt_identificatie = 'ligt_in_buurt_identificatie_example' # str | Unieke identificatie van het object (optional)
    ligt_in_buurt_identificatie_in = ['ligt_in_buurt_identificatie_in_example'] # List[str] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    ligt_in_buurt_identificatie_isempty = True # bool | Whether the field is empty or not. (optional)
    ligt_in_buurt_identificatie_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    ligt_in_buurt_identificatie_like = 'ligt_in_buurt_identificatie_like_example' # str | Matches text using wildcards (? and *). (optional)
    ligt_in_buurt_identificatie_not = ['ligt_in_buurt_identificatie_not_example'] # List[str] | Exclude matches; text (optional)
    ligt_in_buurt_volgnummer = 56 # int | Uniek volgnummer van de toestand van het object (optional)
    ligt_in_buurt_volgnummer_gt = 56 # int | Greater than; number (optional)
    ligt_in_buurt_volgnummer_gte = 56 # int | Greater than or equal to; number (optional)
    ligt_in_buurt_volgnummer_in = [56] # List[int] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    ligt_in_buurt_volgnummer_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    ligt_in_buurt_volgnummer_lt = 56 # int | Less than; number (optional)
    ligt_in_buurt_volgnummer_lte = 56 # int | Less than or equal to; number (optional)
    ligt_in_buurt_volgnummer_not = [56] # List[int] | Exclude matches; number (optional)
    registratiedatum = '2013-10-20T19:20:30+01:00' # datetime | Datum waarop het gegeven in de bron geregistreerd is (optional)
    registratiedatum_gt = '2013-10-20T19:20:30+01:00' # datetime | Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    registratiedatum_gte = '2013-10-20T19:20:30+01:00' # datetime | Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    registratiedatum_in = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    registratiedatum_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    registratiedatum_lt = '2013-10-20T19:20:30+01:00' # datetime | Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    registratiedatum_lte = '2013-10-20T19:20:30+01:00' # datetime | Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    registratiedatum_not = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] (optional)
    volgnummer = 56 # int | Uniek volgnummer van de toestand van het object (optional)
    volgnummer_gt = 56 # int | Greater than; number (optional)
    volgnummer_gte = 56 # int | Greater than or equal to; number (optional)
    volgnummer_in = [56] # List[int] | Matches any value from a comma-separated list: val1,val2,valN. (optional)
    volgnummer_isnull = True # bool | Whether the field has a NULL value or not. (optional)
    volgnummer_lt = 56 # int | Less than; number (optional)
    volgnummer_lte = 56 # int | Less than or equal to; number (optional)
    volgnummer_not = [56] # List[int] | Exclude matches; number (optional)

    try:
        api_response = await api_instance.gebieden_bouwblokken_retrieve(id, accept_crs=accept_crs, content_crs=content_crs, x_api_key=x_api_key, expand=expand, expand_scope=expand_scope, fields=fields, format=format, sort=sort, begin_geldigheid=begin_geldigheid, begin_geldigheid_gt=begin_geldigheid_gt, begin_geldigheid_gte=begin_geldigheid_gte, begin_geldigheid_in=begin_geldigheid_in, begin_geldigheid_isnull=begin_geldigheid_isnull, begin_geldigheid_lt=begin_geldigheid_lt, begin_geldigheid_lte=begin_geldigheid_lte, begin_geldigheid_not=begin_geldigheid_not, code=code, code_in=code_in, code_isempty=code_isempty, code_isnull=code_isnull, code_like=code_like, code_not=code_not, eind_geldigheid=eind_geldigheid, eind_geldigheid_gt=eind_geldigheid_gt, eind_geldigheid_gte=eind_geldigheid_gte, eind_geldigheid_in=eind_geldigheid_in, eind_geldigheid_isnull=eind_geldigheid_isnull, eind_geldigheid_lt=eind_geldigheid_lt, eind_geldigheid_lte=eind_geldigheid_lte, eind_geldigheid_not=eind_geldigheid_not, geldig_op=geldig_op, geldig_op_gt=geldig_op_gt, geldig_op_gte=geldig_op_gte, geldig_op_in=geldig_op_in, geldig_op_isnull=geldig_op_isnull, geldig_op_lt=geldig_op_lt, geldig_op_lte=geldig_op_lte, geldig_op_not=geldig_op_not, geometrie=geometrie, geometrie_contains=geometrie_contains, geometrie_intersects=geometrie_intersects, geometrie_isnull=geometrie_isnull, geometrie_not=geometrie_not, id2=id2, id_in=id_in, id_isempty=id_isempty, id_isnull=id_isnull, id_like=id_like, id_not=id_not, identificatie=identificatie, identificatie_in=identificatie_in, identificatie_isempty=identificatie_isempty, identificatie_isnull=identificatie_isnull, identificatie_like=identificatie_like, identificatie_not=identificatie_not, ligt_in_buurt_identificatie=ligt_in_buurt_identificatie, ligt_in_buurt_identificatie_in=ligt_in_buurt_identificatie_in, ligt_in_buurt_identificatie_isempty=ligt_in_buurt_identificatie_isempty, ligt_in_buurt_identificatie_isnull=ligt_in_buurt_identificatie_isnull, ligt_in_buurt_identificatie_like=ligt_in_buurt_identificatie_like, ligt_in_buurt_identificatie_not=ligt_in_buurt_identificatie_not, ligt_in_buurt_volgnummer=ligt_in_buurt_volgnummer, ligt_in_buurt_volgnummer_gt=ligt_in_buurt_volgnummer_gt, ligt_in_buurt_volgnummer_gte=ligt_in_buurt_volgnummer_gte, ligt_in_buurt_volgnummer_in=ligt_in_buurt_volgnummer_in, ligt_in_buurt_volgnummer_isnull=ligt_in_buurt_volgnummer_isnull, ligt_in_buurt_volgnummer_lt=ligt_in_buurt_volgnummer_lt, ligt_in_buurt_volgnummer_lte=ligt_in_buurt_volgnummer_lte, ligt_in_buurt_volgnummer_not=ligt_in_buurt_volgnummer_not, registratiedatum=registratiedatum, registratiedatum_gt=registratiedatum_gt, registratiedatum_gte=registratiedatum_gte, registratiedatum_in=registratiedatum_in, registratiedatum_isnull=registratiedatum_isnull, registratiedatum_lt=registratiedatum_lt, registratiedatum_lte=registratiedatum_lte, registratiedatum_not=registratiedatum_not, volgnummer=volgnummer, volgnummer_gt=volgnummer_gt, volgnummer_gte=volgnummer_gte, volgnummer_in=volgnummer_in, volgnummer_isnull=volgnummer_isnull, volgnummer_lt=volgnummer_lt, volgnummer_lte=volgnummer_lte, volgnummer_not=volgnummer_not)
        print("The response of BouwblokkenApi->gebieden_bouwblokken_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BouwblokkenApi->gebieden_bouwblokken_retrieve: %s\n" % e)
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
 **begin_geldigheid** | **datetime**| De ingangsdatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok | [optional] 
 **begin_geldigheid_gt** | **datetime**| Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **begin_geldigheid_gte** | **datetime**| Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **begin_geldigheid_in** | [**List[datetime]**](datetime.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **begin_geldigheid_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **begin_geldigheid_lt** | **datetime**| Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **begin_geldigheid_lte** | **datetime**| Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **begin_geldigheid_not** | [**List[datetime]**](datetime.md)| Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **code** | **str**| Officiële code van het object | [optional] 
 **code_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **code_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **code_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **code_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **code_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **eind_geldigheid** | **datetime**| De einddatum van de geldigheid van een bepaalde combinatie van gegevens over een bouwblok | [optional] 
 **eind_geldigheid_gt** | **datetime**| Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **eind_geldigheid_gte** | **datetime**| Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **eind_geldigheid_in** | [**List[datetime]**](datetime.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **eind_geldigheid_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **eind_geldigheid_lt** | **datetime**| Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **eind_geldigheid_lte** | **datetime**| Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **eind_geldigheid_not** | [**List[datetime]**](datetime.md)| Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **geldig_op** | **datetime**|  | [optional] 
 **geldig_op_gt** | **datetime**|  | [optional] 
 **geldig_op_gte** | **datetime**|  | [optional] 
 **geldig_op_in** | **datetime**|  | [optional] 
 **geldig_op_isnull** | **datetime**|  | [optional] 
 **geldig_op_lt** | **datetime**|  | [optional] 
 **geldig_op_lte** | **datetime**|  | [optional] 
 **geldig_op_not** | **datetime**|  | [optional] 
 **geometrie** | **str**| Geometrische beschrijving van een object | [optional] 
 **geometrie_contains** | **str**| Use x,y or POINT(x y) | [optional] 
 **geometrie_intersects** | **str**| Use WKT (POLYGON((x1 y1, x2 y2, ...))) or GeoJSON | [optional] 
 **geometrie_isnull** | **str**| Whether the field has a NULL value or not. | [optional] 
 **geometrie_not** | **str**| GeoJSON | GEOMETRY(...) | [optional] 
 **id2** | **str**| Exact; text | [optional] 
 **id_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **id_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **id_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **id_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **id_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **identificatie** | **str**| Unieke identificatie van het object | [optional] 
 **identificatie_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **identificatie_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **identificatie_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **identificatie_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **identificatie_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **ligt_in_buurt_identificatie** | **str**| Unieke identificatie van het object | [optional] 
 **ligt_in_buurt_identificatie_in** | [**List[str]**](str.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **ligt_in_buurt_identificatie_isempty** | **bool**| Whether the field is empty or not. | [optional] 
 **ligt_in_buurt_identificatie_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **ligt_in_buurt_identificatie_like** | **str**| Matches text using wildcards (? and *). | [optional] 
 **ligt_in_buurt_identificatie_not** | [**List[str]**](str.md)| Exclude matches; text | [optional] 
 **ligt_in_buurt_volgnummer** | **int**| Uniek volgnummer van de toestand van het object | [optional] 
 **ligt_in_buurt_volgnummer_gt** | **int**| Greater than; number | [optional] 
 **ligt_in_buurt_volgnummer_gte** | **int**| Greater than or equal to; number | [optional] 
 **ligt_in_buurt_volgnummer_in** | [**List[int]**](int.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **ligt_in_buurt_volgnummer_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **ligt_in_buurt_volgnummer_lt** | **int**| Less than; number | [optional] 
 **ligt_in_buurt_volgnummer_lte** | **int**| Less than or equal to; number | [optional] 
 **ligt_in_buurt_volgnummer_not** | [**List[int]**](int.md)| Exclude matches; number | [optional] 
 **registratiedatum** | **datetime**| Datum waarop het gegeven in de bron geregistreerd is | [optional] 
 **registratiedatum_gt** | **datetime**| Greater than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **registratiedatum_gte** | **datetime**| Greater than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **registratiedatum_in** | [**List[datetime]**](datetime.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **registratiedatum_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **registratiedatum_lt** | **datetime**| Less than; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **registratiedatum_lte** | **datetime**| Less than or equal to; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **registratiedatum_not** | [**List[datetime]**](datetime.md)| Exclude matches; use yyyy-mm-dd or yyyy-mm-ddThh:mm[:ss[.ms]] | [optional] 
 **volgnummer** | **int**| Uniek volgnummer van de toestand van het object | [optional] 
 **volgnummer_gt** | **int**| Greater than; number | [optional] 
 **volgnummer_gte** | **int**| Greater than or equal to; number | [optional] 
 **volgnummer_in** | [**List[int]**](int.md)| Matches any value from a comma-separated list: val1,val2,valN. | [optional] 
 **volgnummer_isnull** | **bool**| Whether the field has a NULL value or not. | [optional] 
 **volgnummer_lt** | **int**| Less than; number | [optional] 
 **volgnummer_lte** | **int**| Less than or equal to; number | [optional] 
 **volgnummer_not** | [**List[int]**](int.md)| Exclude matches; number | [optional] 

### Return type

[**Gebiedenbouwblokken**](Gebiedenbouwblokken.md)

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

