# maxpanda_python_sdk.AssetsApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_create**](AssetsApi.md#assets_v1_create) | **POST** /v1/Asset | Create an Asset
[**assets_v1_get**](AssetsApi.md#assets_v1_get) | **GET** /v1/Assets | Get a list of Assets
[**assets_v1_get_0**](AssetsApi.md#assets_v1_get_0) | **GET** /v1/Asset/id | Get a specific Asset
[**assets_v1_update_asset**](AssetsApi.md#assets_v1_update_asset) | **PUT** /v1/Asset | Update an Asset

# **assets_v1_create**
> AssetCreateUpdateResponseModel assets_v1_create(body)

Create an Asset

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.AssetsApi()
body = maxpanda_python_sdk.Asset() # Asset | Details of the new Asset

try:
    # Create an Asset
    api_response = api_instance.assets_v1_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_v1_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Asset**](Asset.md)| Details of the new Asset | 

### Return type

[**AssetCreateUpdateResponseModel**](AssetCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_get**
> AssetResponseModel assets_v1_get(site_id, request_complete_information, page=page, page_size=page_size)

Get a list of Assets

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.AssetsApi()
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a list of Assets
    api_response = api_instance.assets_v1_get(site_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_v1_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**AssetResponseModel**](AssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_get_0**
> AssetResponseModel assets_v1_get_0(id, site_id, request_complete_information)

Get a specific Asset

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.AssetsApi()
id = 56 # int | The asset id to retrieve
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Asset
    api_response = api_instance.assets_v1_get_0(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_v1_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The asset id to retrieve | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**AssetResponseModel**](AssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_update_asset**
> AssetCreateUpdateResponseModel assets_v1_update_asset(body)

Update an Asset

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.AssetsApi()
body = maxpanda_python_sdk.UpdateAsset() # UpdateAsset | Details of the Asset

try:
    # Update an Asset
    api_response = api_instance.assets_v1_update_asset(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_v1_update_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAsset**](UpdateAsset.md)| Details of the Asset | 

### Return type

[**AssetCreateUpdateResponseModel**](AssetCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

