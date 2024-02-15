# swagger_client.VendorInvoicesApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendor_invoice_get**](VendorInvoicesApi.md#vendor_invoice_get) | **GET** /v1/VendorInvoices | Get a paged list of Vendor Invoice
[**vendor_invoice_get_0**](VendorInvoicesApi.md#vendor_invoice_get_0) | **GET** /v1/VendorInvoice/id | Get a specific Vendor Invoice
[**vendor_invoice_post**](VendorInvoicesApi.md#vendor_invoice_post) | **POST** /v1/VendorInvoice | Create an Invoice
[**vendor_invoice_put**](VendorInvoicesApi.md#vendor_invoice_put) | **PUT** /v1/VendorInvoice | Update an Invoice

# **vendor_invoice_get**
> InvoiceResponseModel vendor_invoice_get(site_id, request_complete_information, page=page, page_size=page_size)

Get a paged list of Vendor Invoice

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorInvoicesApi()
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of Vendor Invoice
    api_response = api_instance.vendor_invoice_get(site_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorInvoicesApi->vendor_invoice_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**InvoiceResponseModel**](InvoiceResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_invoice_get_0**
> InvoiceResponseModel vendor_invoice_get_0(id, site_id, request_complete_information)

Get a specific Vendor Invoice

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorInvoicesApi()
id = 56 # int | The Vendor Invoice id to retrieve
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Vendor Invoice
    api_response = api_instance.vendor_invoice_get_0(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorInvoicesApi->vendor_invoice_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Vendor Invoice id to retrieve | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**InvoiceResponseModel**](InvoiceResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_invoice_post**
> InvoiceCreateUpdateResponseModel vendor_invoice_post(body)

Create an Invoice

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorInvoicesApi()
body = swagger_client.CreateInvoiceModel() # CreateInvoiceModel | Details of the new invoice

try:
    # Create an Invoice
    api_response = api_instance.vendor_invoice_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorInvoicesApi->vendor_invoice_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInvoiceModel**](CreateInvoiceModel.md)| Details of the new invoice | 

### Return type

[**InvoiceCreateUpdateResponseModel**](InvoiceCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_invoice_put**
> InvoiceCreateUpdateResponseModel vendor_invoice_put(body)

Update an Invoice

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorInvoicesApi()
body = swagger_client.UpdateInvoiceModel() # UpdateInvoiceModel | Details of the Invoice

try:
    # Update an Invoice
    api_response = api_instance.vendor_invoice_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorInvoicesApi->vendor_invoice_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInvoiceModel**](UpdateInvoiceModel.md)| Details of the Invoice | 

### Return type

[**InvoiceCreateUpdateResponseModel**](InvoiceCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

