# maxpanda_python_sdk.InvoiceItemTaxApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoice_tax_get**](InvoiceItemTaxApi.md#invoice_tax_get) | **GET** /v1/Company/InvoiceTaxes | Get a paged list of Invoice Taxes
[**invoice_tax_get_0**](InvoiceItemTaxApi.md#invoice_tax_get_0) | **GET** /v1/Company/InvoiceTax/id | Get a specific Invoice Tax record

# **invoice_tax_get**
> InvoiceTaxResponseModel invoice_tax_get(request_complete_information, page=page, page_size=page_size)

Get a paged list of Invoice Taxes

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.InvoiceItemTaxApi()
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of Invoice Taxes
    api_response = api_instance.invoice_tax_get(request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceItemTaxApi->invoice_tax_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**InvoiceTaxResponseModel**](InvoiceTaxResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_tax_get_0**
> InvoiceTaxResponseModel invoice_tax_get_0(id, request_complete_information)

Get a specific Invoice Tax record

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.InvoiceItemTaxApi()
id = 56 # int | The Invoice Tax Id to retrieve
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Invoice Tax record
    api_response = api_instance.invoice_tax_get_0(id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceItemTaxApi->invoice_tax_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Invoice Tax Id to retrieve | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**InvoiceTaxResponseModel**](InvoiceTaxResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

