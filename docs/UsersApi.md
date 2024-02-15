# swagger_client.UsersApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get_user_by_id**](UsersApi.md#user_get_user_by_id) | **GET** /v1/UserById/id | Get a specific User
[**user_get_users**](UsersApi.md#user_get_users) | **GET** /v1/Users | Get list of Users

# **user_get_user_by_id**
> UserListResponseModel user_get_user_by_id(id, site_id, request_complete_information)

Get a specific User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 56 # int | The User id to retrieve
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific User
    api_response = api_instance.user_get_user_by_id(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The User id to retrieve | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**UserListResponseModel**](UserListResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_users**
> UserListResponseModel user_get_users(site_id, request_complete_information, disabled, page=page, page_size=page_size)

Get list of Users

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
disabled = true # bool | True option provides all the Users. False will provide only Enabled Users
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get list of Users
    api_response = api_instance.user_get_users(site_id, request_complete_information, disabled, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **disabled** | **bool**| True option provides all the Users. False will provide only Enabled Users | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**UserListResponseModel**](UserListResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

