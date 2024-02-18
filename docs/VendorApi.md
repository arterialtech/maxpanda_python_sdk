# maxpanda_python_sdk.VendorApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendor_get_vendor_by_id**](VendorApi.md#vendor_get_vendor_by_id) | **GET** /v1/Vendors/id | Get a specific Vendor
[**vendor_get_vendors**](VendorApi.md#vendor_get_vendors) | **GET** /v1/Vendors | Get list of Vendors
[**vendor_post**](VendorApi.md#vendor_post) | **POST** /v1/Vendor | Create a new Vendor
[**vendor_put**](VendorApi.md#vendor_put) | **PUT** /v1/Vendor | Update an existing vendor.

# **vendor_get_vendor_by_id**
> VendorsListResponseModel vendor_get_vendor_by_id(id, site_id, request_complete_information)

Get a specific Vendor

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
api_instance = maxpanda_python_sdk.VendorApi(maxpanda_python_sdk.ApiClient(configuration))
id = 56 # int | Vendor ID can be found in your Maxpanda Vendor index or Vendor API
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Vendor
    api_response = api_instance.vendor_get_vendor_by_id(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->vendor_get_vendor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Vendor ID can be found in your Maxpanda Vendor index or Vendor API | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**VendorsListResponseModel**](VendorsListResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_get_vendors**
> VendorsListResponseModel vendor_get_vendors(site_id, request_complete_information, page=page, page_size=page_size)

Get list of Vendors

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
api_instance = maxpanda_python_sdk.VendorApi(maxpanda_python_sdk.ApiClient(configuration))
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get list of Vendors
    api_response = api_instance.vendor_get_vendors(site_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->vendor_get_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**VendorsListResponseModel**](VendorsListResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_post**
> VendorCreateUpdateResponseModel vendor_post(body)

Create a new Vendor

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
api_instance = maxpanda_python_sdk.VendorApi(maxpanda_python_sdk.ApiClient(configuration))
body = maxpanda_python_sdk.CreateVendorModel() # CreateVendorModel | The Vendor to be added

try:
    # Create a new Vendor
    api_response = api_instance.vendor_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->vendor_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVendorModel**](CreateVendorModel.md)| The Vendor to be added | 

### Return type

[**VendorCreateUpdateResponseModel**](VendorCreateUpdateResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_put**
> VendorCreateUpdateResponseModel vendor_put(body)

Update an existing vendor.

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
api_instance = maxpanda_python_sdk.VendorApi(maxpanda_python_sdk.ApiClient(configuration))
body = maxpanda_python_sdk.UpdateVendorModel() # UpdateVendorModel | The Vendor to be updated

try:
    # Update an existing vendor.
    api_response = api_instance.vendor_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->vendor_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateVendorModel**](UpdateVendorModel.md)| The Vendor to be updated | 

### Return type

[**VendorCreateUpdateResponseModel**](VendorCreateUpdateResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

