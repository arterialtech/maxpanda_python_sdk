# maxpanda_python_sdk.InvoiceItemTypeApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoice_item_types_get**](InvoiceItemTypeApi.md#invoice_item_types_get) | **GET** /v1/Company/InvoiceItemTypes | Get a paged list of Invoice Item Types
[**invoice_item_types_get_0**](InvoiceItemTypeApi.md#invoice_item_types_get_0) | **GET** /v1/Company/InvoiceItemType/id | Get a specific Invoice Item Type record

# **invoice_item_types_get**
> InvoiceItemTypeResponseModel invoice_item_types_get(request_complete_information, page=page, page_size=page_size)

Get a paged list of Invoice Item Types

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records

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
api_instance = maxpanda_python_sdk.InvoiceItemTypeApi(maxpanda_python_sdk.ApiClient(configuration))
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of Invoice Item Types
    api_response = api_instance.invoice_item_types_get(request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceItemTypeApi->invoice_item_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**InvoiceItemTypeResponseModel**](InvoiceItemTypeResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_item_types_get_0**
> InvoiceItemTypeResponseModel invoice_item_types_get_0(id, request_complete_information)

Get a specific Invoice Item Type record

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
api_instance = maxpanda_python_sdk.InvoiceItemTypeApi(maxpanda_python_sdk.ApiClient(configuration))
id = 56 # int | TheInvoice Item Type id to retrieve
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Invoice Item Type record
    api_response = api_instance.invoice_item_types_get_0(id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceItemTypeApi->invoice_item_types_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TheInvoice Item Type id to retrieve | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**InvoiceItemTypeResponseModel**](InvoiceItemTypeResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

