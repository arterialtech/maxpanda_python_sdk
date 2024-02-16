# maxpanda_python_sdk.CustomerApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_get**](CustomerApi.md#customer_get) | **GET** /v1/Customers | Get a paged list of Customers
[**customer_get_customer_by_id**](CustomerApi.md#customer_get_customer_by_id) | **GET** /v1/Customer/id | Get a specific customer
[**customer_post**](CustomerApi.md#customer_post) | **POST** /v1/Customer | Create a new customer
[**customer_put**](CustomerApi.md#customer_put) | **PUT** /v1/Customer | Update an existing customer.

# **customer_get**
> CustomerResponseModel customer_get(site_id, request_complete_information, page=page, page_size=page_size)

Get a paged list of Customers

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.CustomerApi()
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of Customers
    api_response = api_instance.customer_get(site_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**CustomerResponseModel**](CustomerResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_get_customer_by_id**
> CustomerResponseModel customer_get_customer_by_id(id, site_id, request_complete_information)

Get a specific customer

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.CustomerApi()
id = 56 # int | The customer id to retrieve
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific customer
    api_response = api_instance.customer_get_customer_by_id(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_get_customer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The customer id to retrieve | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**CustomerResponseModel**](CustomerResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_post**
> CustomerCreateUpdateResponseModel customer_post(body)

Create a new customer

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.CustomerApi()
body = maxpanda_python_sdk.CreateCustomerModel() # CreateCustomerModel | The Customer to be added

try:
    # Create a new customer
    api_response = api_instance.customer_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomerModel**](CreateCustomerModel.md)| The Customer to be added | 

### Return type

[**CustomerCreateUpdateResponseModel**](CustomerCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_put**
> CustomerCreateUpdateResponseModel customer_put(body)

Update an existing customer.

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.CustomerApi()
body = maxpanda_python_sdk.UpdateCustomerModel() # UpdateCustomerModel | The customer to be updated

try:
    # Update an existing customer.
    api_response = api_instance.customer_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCustomerModel**](UpdateCustomerModel.md)| The customer to be updated | 

### Return type

[**CustomerCreateUpdateResponseModel**](CustomerCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

