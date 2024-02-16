# maxpanda_python_sdk.TaskStatusApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_statuses_get**](TaskStatusApi.md#task_statuses_get) | **GET** /v1/TaskStatuses | Get a paged list of Task Statuses

# **task_statuses_get**
> TaskStatusResponseModel task_statuses_get(page=page, page_size=page_size)

Get a paged list of Task Statuses

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.TaskStatusApi()
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of Task Statuses
    api_response = api_instance.task_statuses_get(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskStatusApi->task_statuses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**TaskStatusResponseModel**](TaskStatusResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

