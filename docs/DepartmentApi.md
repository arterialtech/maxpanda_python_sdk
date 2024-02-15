# swagger_client.DepartmentApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**department_get**](DepartmentApi.md#department_get) | **GET** /v1/Company/Departments | Get a paged list of departments
[**department_get_0**](DepartmentApi.md#department_get_0) | **GET** /v1/Company/Department/id | Get a specific Department type record

# **department_get**
> DepartmentResponseModel department_get(request_complete_information, page=page, page_size=page_size)

Get a paged list of departments

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DepartmentApi()
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of departments
    api_response = api_instance.department_get(request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentApi->department_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**DepartmentResponseModel**](DepartmentResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **department_get_0**
> DepartmentResponseModel department_get_0(id, request_complete_information)

Get a specific Department type record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DepartmentApi()
id = 56 # int | Id of the Building Group to retrieve
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Department type record
    api_response = api_instance.department_get_0(id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepartmentApi->department_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the Building Group to retrieve | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**DepartmentResponseModel**](DepartmentResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

