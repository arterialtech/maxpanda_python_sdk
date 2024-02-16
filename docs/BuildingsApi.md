# maxpanda_python_sdk.BuildingsApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buildings_create_building**](BuildingsApi.md#buildings_create_building) | **POST** /v1/Building | Create a new Building
[**buildings_get_building**](BuildingsApi.md#buildings_get_building) | **GET** /v1/Building/id | Get a specific Building
[**buildings_get_buildings**](BuildingsApi.md#buildings_get_buildings) | **GET** /v1/Buildings | Get a paged list of buildings
[**buildings_patch**](BuildingsApi.md#buildings_patch) | **PATCH** /v1/Building | Update specific attributes of a given building

# **buildings_create_building**
> BuildingCreateUpdateResponseModel buildings_create_building(body)

Create a new Building

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.BuildingsApi()
body = maxpanda_python_sdk.BuildingCreateModel() # BuildingCreateModel | Details of the new Building

try:
    # Create a new Building
    api_response = api_instance.buildings_create_building(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildingsApi->buildings_create_building: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BuildingCreateModel**](BuildingCreateModel.md)| Details of the new Building | 

### Return type

[**BuildingCreateUpdateResponseModel**](BuildingCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buildings_get_building**
> BuildingResponseModel buildings_get_building(id, site_id, request_complete_information)

Get a specific Building

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.BuildingsApi()
id = 56 # int | The building id to retrieve
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Building
    api_response = api_instance.buildings_get_building(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildingsApi->buildings_get_building: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The building id to retrieve | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**BuildingResponseModel**](BuildingResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buildings_get_buildings**
> BuildingResponseModel buildings_get_buildings(site_id, request_complete_information, page=page, page_size=page_size)

Get a paged list of buildings

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.BuildingsApi()
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of buildings
    api_response = api_instance.buildings_get_buildings(site_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildingsApi->buildings_get_buildings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**BuildingResponseModel**](BuildingResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buildings_patch**
> BuildingCreateUpdateResponseModel buildings_patch(body)

Update specific attributes of a given building

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.BuildingsApi()
body = maxpanda_python_sdk.BuildingUpdateModel() # BuildingUpdateModel | Building details can be found in Building API

try:
    # Update specific attributes of a given building
    api_response = api_instance.buildings_patch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildingsApi->buildings_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BuildingUpdateModel**](BuildingUpdateModel.md)| Building details can be found in Building API | 

### Return type

[**BuildingCreateUpdateResponseModel**](BuildingCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

