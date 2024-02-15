# swagger_client.TaskPriorityApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_priorities_get**](TaskPriorityApi.md#task_priorities_get) | **GET** /v1/TaskPriorities | Get a paged list of Task Priority

# **task_priorities_get**
> TaskProrityResponseModel task_priorities_get(page=page, page_size=page_size)

Get a paged list of Task Priority

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaskPriorityApi()
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of Task Priority
    api_response = api_instance.task_priorities_get(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskPriorityApi->task_priorities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**TaskProrityResponseModel**](TaskProrityResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

