# maxpanda_python_sdk.PartCategoryApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**part_category_create**](PartCategoryApi.md#part_category_create) | **POST** /v1/Company/PartCategory | Create a new Part Category
[**part_category_delete_part_category**](PartCategoryApi.md#part_category_delete_part_category) | **DELETE** /v1/Company/PartCategory | Delete PartCategory of Part
[**part_category_get**](PartCategoryApi.md#part_category_get) | **GET** /v1/Company/PartCategory | Get a paged list of PartCategory
[**part_category_get_0**](PartCategoryApi.md#part_category_get_0) | **GET** /v1/Company/PartCategory/{id} | Get a specific Part Category record
[**part_category_put**](PartCategoryApi.md#part_category_put) | **PUT** /v1/Company/PartCategory | Update an existing Part Category

# **part_category_create**
> CreateUpdatePartCategory part_category_create(body)

Create a new Part Category

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.PartCategoryApi()
body = maxpanda_python_sdk.CreatePartCategory() # CreatePartCategory | Details of Part Category

try:
    # Create a new Part Category
    api_response = api_instance.part_category_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartCategoryApi->part_category_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePartCategory**](CreatePartCategory.md)| Details of Part Category | 

### Return type

[**CreateUpdatePartCategory**](CreateUpdatePartCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **part_category_delete_part_category**
> PageResult part_category_delete_part_category(part_category_id)

Delete PartCategory of Part

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.PartCategoryApi()
part_category_id = 56 # int | Id of PartCategory

try:
    # Delete PartCategory of Part
    api_response = api_instance.part_category_delete_part_category(part_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartCategoryApi->part_category_delete_part_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_category_id** | **int**| Id of PartCategory | 

### Return type

[**PageResult**](PageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **part_category_get**
> PartCategoryResponseModel part_category_get(request_complete_information, page=page, page_size=page_size)

Get a paged list of PartCategory

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.PartCategoryApi()
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of PartCategory
    api_response = api_instance.part_category_get(request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartCategoryApi->part_category_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**PartCategoryResponseModel**](PartCategoryResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **part_category_get_0**
> PartCategoryResponseModel part_category_get_0(id, request_complete_information)

Get a specific Part Category record

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.PartCategoryApi()
id = 56 # int | The Part category id to retrieve
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Part Category record
    api_response = api_instance.part_category_get_0(id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartCategoryApi->part_category_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Part category id to retrieve | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**PartCategoryResponseModel**](PartCategoryResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **part_category_put**
> CreateUpdatePartCategory part_category_put(body)

Update an existing Part Category

### Example
```python
from __future__ import print_function
import time
import maxpanda_python_sdk
from maxpanda_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = maxpanda_python_sdk.PartCategoryApi()
body = maxpanda_python_sdk.UpdatePartCategory() # UpdatePartCategory | Details of Part Category

try:
    # Update an existing Part Category
    api_response = api_instance.part_category_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartCategoryApi->part_category_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePartCategory**](UpdatePartCategory.md)| Details of Part Category | 

### Return type

[**CreateUpdatePartCategory**](CreateUpdatePartCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

