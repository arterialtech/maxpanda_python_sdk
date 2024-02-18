# maxpanda_python_sdk.WorkOrderPriorityApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**work_order_priorities_get**](WorkOrderPriorityApi.md#work_order_priorities_get) | **GET** /v1/Company/WorkOrderPriorities | Get a paged list of WorkOrder Priorities
[**work_order_priorities_get_0**](WorkOrderPriorityApi.md#work_order_priorities_get_0) | **GET** /v1/Company/WorkOrderPriority/id | Get a specific WorkOrder Priority record

# **work_order_priorities_get**
> WorkOrderPriorityResponseModel work_order_priorities_get(request_complete_information, page=page, page_size=page_size)

Get a paged list of WorkOrder Priorities

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
api_instance = maxpanda_python_sdk.WorkOrderPriorityApi(maxpanda_python_sdk.ApiClient(configuration))
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of WorkOrder Priorities
    api_response = api_instance.work_order_priorities_get(request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrderPriorityApi->work_order_priorities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**WorkOrderPriorityResponseModel**](WorkOrderPriorityResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_order_priorities_get_0**
> WorkOrderPriorityResponseModel work_order_priorities_get_0(id, request_complete_information)

Get a specific WorkOrder Priority record

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
api_instance = maxpanda_python_sdk.WorkOrderPriorityApi(maxpanda_python_sdk.ApiClient(configuration))
id = 56 # int | The WorkOrder Priority id to retrieve
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific WorkOrder Priority record
    api_response = api_instance.work_order_priorities_get_0(id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrderPriorityApi->work_order_priorities_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The WorkOrder Priority id to retrieve | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**WorkOrderPriorityResponseModel**](WorkOrderPriorityResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

