# maxpanda_python_sdk.CustomerInvoicesApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_invoice_create_customer_invoice**](CustomerInvoicesApi.md#customer_invoice_create_customer_invoice) | **POST** /v1/CustomerInvoice | Create a new customer invoice.
[**customer_invoice_edit_customer_invoice**](CustomerInvoicesApi.md#customer_invoice_edit_customer_invoice) | **PUT** /v1/CustomerInvoice | Update Customer Invoice
[**customer_invoice_get**](CustomerInvoicesApi.md#customer_invoice_get) | **GET** /v1/GetCustomerInvoices | Get list of Customer Invoices
[**customer_invoice_get_0**](CustomerInvoicesApi.md#customer_invoice_get_0) | **GET** /v1/GetCustomerInvoice/id | Get a specific Customer Invoice

# **customer_invoice_create_customer_invoice**
> InvoiceCreateUpdateResponseModel customer_invoice_create_customer_invoice(body)

Create a new customer invoice.

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
api_instance = maxpanda_python_sdk.CustomerInvoicesApi(maxpanda_python_sdk.ApiClient(configuration))
body = maxpanda_python_sdk.CreateCustomerInvoice() # CreateCustomerInvoice | The Customer invoice to be added

try:
    # Create a new customer invoice.
    api_response = api_instance.customer_invoice_create_customer_invoice(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoicesApi->customer_invoice_create_customer_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomerInvoice**](CreateCustomerInvoice.md)| The Customer invoice to be added | 

### Return type

[**InvoiceCreateUpdateResponseModel**](InvoiceCreateUpdateResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_invoice_edit_customer_invoice**
> InvoiceCreateUpdateResponseModel customer_invoice_edit_customer_invoice(body)

Update Customer Invoice

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
api_instance = maxpanda_python_sdk.CustomerInvoicesApi(maxpanda_python_sdk.ApiClient(configuration))
body = maxpanda_python_sdk.UpdateCustomerInvoice() # UpdateCustomerInvoice | 

try:
    # Update Customer Invoice
    api_response = api_instance.customer_invoice_edit_customer_invoice(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoicesApi->customer_invoice_edit_customer_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCustomerInvoice**](UpdateCustomerInvoice.md)|  | 

### Return type

[**InvoiceCreateUpdateResponseModel**](InvoiceCreateUpdateResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_invoice_get**
> InvoiceResponseModel customer_invoice_get(request_complete_information, page=page, page_size=page_size)

Get list of Customer Invoices

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
api_instance = maxpanda_python_sdk.CustomerInvoicesApi(maxpanda_python_sdk.ApiClient(configuration))
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get list of Customer Invoices
    api_response = api_instance.customer_invoice_get(request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoicesApi->customer_invoice_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**InvoiceResponseModel**](InvoiceResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_invoice_get_0**
> InvoiceResponseModel customer_invoice_get_0(id, request_complete_information)

Get a specific Customer Invoice

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
api_instance = maxpanda_python_sdk.CustomerInvoicesApi(maxpanda_python_sdk.ApiClient(configuration))
id = 56 # int | Invoice ID can be found in your Maxpanda Customer Invoice index or Customer Invoice API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Customer Invoice
    api_response = api_instance.customer_invoice_get_0(id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerInvoicesApi->customer_invoice_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invoice ID can be found in your Maxpanda Customer Invoice index or Customer Invoice API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**InvoiceResponseModel**](InvoiceResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

