# maxpanda_python_sdk.TaskPriorityApi

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
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeader
configuration = maxpanda_python_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = maxpanda_python_sdk.TaskPriorityApi(maxpanda_python_sdk.ApiClient(configuration))
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

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

