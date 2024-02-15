# swagger_client.LocationApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_create**](LocationApi.md#locations_create) | **POST** /v1/Location | Create a location
[**locations_get**](LocationApi.md#locations_get) | **GET** /v1/Locations | Get a list of locations
[**locations_get_0**](LocationApi.md#locations_get_0) | **GET** /v1/Location/id | Get a specific location
[**locations_patch**](LocationApi.md#locations_patch) | **PUT** /v1/Location | Update a location

# **locations_create**
> LocationCreateUpdateResponseModel locations_create(body)

Create a location

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationApi()
body = swagger_client.Location() # Location | Details of the new location

try:
    # Create a location
    api_response = api_instance.locations_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->locations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Location**](Location.md)| Details of the new location | 

### Return type

[**LocationCreateUpdateResponseModel**](LocationCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_get**
> LocationResponseModel locations_get(site_id, request_complete_information, page=page, page_size=page_size)

Get a list of locations

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationApi()
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a list of locations
    api_response = api_instance.locations_get(site_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->locations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**LocationResponseModel**](LocationResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_get_0**
> LocationResponseModel locations_get_0(id, site_id, request_complete_information)

Get a specific location

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationApi()
id = 56 # int | The location id to retrieve
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific location
    api_response = api_instance.locations_get_0(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->locations_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The location id to retrieve | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**LocationResponseModel**](LocationResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_patch**
> LocationCreateUpdateResponseModel locations_patch(body)

Update a location

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationApi()
body = swagger_client.LocationUpdateModel() # LocationUpdateModel | Details of the new location

try:
    # Update a location
    api_response = api_instance.locations_patch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->locations_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationUpdateModel**](LocationUpdateModel.md)| Details of the new location | 

### Return type

[**LocationCreateUpdateResponseModel**](LocationCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

