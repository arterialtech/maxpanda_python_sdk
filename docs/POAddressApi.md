# maxpanda_python_sdk.POAddressApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_o_address_create**](POAddressApi.md#p_o_address_create) | **POST** /v1/Company/POAddress | Create a new Purchase Order Address
[**p_o_address_get**](POAddressApi.md#p_o_address_get) | **GET** /v1/Company/POAddress | Get Purchase Order Address
[**p_o_address_get_0**](POAddressApi.md#p_o_address_get_0) | **GET** /v1/Company/POAddress/id | Get a specific PO Address
[**p_o_address_put**](POAddressApi.md#p_o_address_put) | **PUT** /v1/Company/POAddress | Update an existing Purchase Order Address

# **p_o_address_create**
> POAddressAPIModel p_o_address_create(body)

Create a new Purchase Order Address

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.POAddressApi()
body = maxpanda_python_sdk.CreatePOAddress() # CreatePOAddress | Details of Purchase Order Address

try:
    # Create a new Purchase Order Address
    api_response = api_instance.p_o_address_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POAddressApi->p_o_address_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePOAddress**](CreatePOAddress.md)| Details of Purchase Order Address | 

### Return type

[**POAddressAPIModel**](POAddressAPIModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_o_address_get**
> POAddressModelAPI p_o_address_get(site_id, request_complete_information, page=page, page_size=page_size)

Get Purchase Order Address

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.POAddressApi()
site_id = 56 # int | 
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get Purchase Order Address
    api_response = api_instance.p_o_address_get(site_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POAddressApi->p_o_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**|  | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**POAddressModelAPI**](POAddressModelAPI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_o_address_get_0**
> POAddressModelAPI p_o_address_get_0(id, site_id, request_complete_information)

Get a specific PO Address

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.POAddressApi()
id = 56 # int | POAddress Id
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific PO Address
    api_response = api_instance.p_o_address_get_0(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POAddressApi->p_o_address_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| POAddress Id | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**POAddressModelAPI**](POAddressModelAPI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_o_address_put**
> POAddressAPIModel p_o_address_put(body)

Update an existing Purchase Order Address

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.POAddressApi()
body = maxpanda_python_sdk.UpdatePOAddress() # UpdatePOAddress | Details of Purchase Order Address

try:
    # Update an existing Purchase Order Address
    api_response = api_instance.p_o_address_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POAddressApi->p_o_address_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePOAddress**](UpdatePOAddress.md)| Details of Purchase Order Address | 

### Return type

[**POAddressAPIModel**](POAddressAPIModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

