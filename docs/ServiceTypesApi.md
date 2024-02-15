# swagger_client.ServiceTypesApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_type_get**](ServiceTypesApi.md#service_type_get) | **GET** /v1/ServiceTypes | Get a paged list of Service Types
[**service_type_get_0**](ServiceTypesApi.md#service_type_get_0) | **GET** /v1/ServiceType/id | Get a Service Type
[**service_type_post**](ServiceTypesApi.md#service_type_post) | **POST** /v1/ServiceType | Create a new service Type
[**service_type_put**](ServiceTypesApi.md#service_type_put) | **PUT** /v1/ServiceType | Update a service Type

# **service_type_get**
> ServiceTypesListResponseList service_type_get(site_id, request_complete_information, page=page, page_size=page_size)

Get a paged list of Service Types

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceTypesApi()
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of Service Types
    api_response = api_instance.service_type_get(site_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceTypesApi->service_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**ServiceTypesListResponseList**](ServiceTypesListResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_type_get_0**
> ServiceTypesListResponseList service_type_get_0(id, site_id, request_complete_information)

Get a Service Type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceTypesApi()
id = 56 # int | The Service Type id to retrieve
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a Service Type
    api_response = api_instance.service_type_get_0(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceTypesApi->service_type_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Service Type id to retrieve | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**ServiceTypesListResponseList**](ServiceTypesListResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_type_post**
> ServiceCreateUpdateResponseModel service_type_post(body)

Create a new service Type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceTypesApi()
body = swagger_client.CreateServiceTypeModel() # CreateServiceTypeModel | Details of new service Type

try:
    # Create a new service Type
    api_response = api_instance.service_type_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceTypesApi->service_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateServiceTypeModel**](CreateServiceTypeModel.md)| Details of new service Type | 

### Return type

[**ServiceCreateUpdateResponseModel**](ServiceCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_type_put**
> ServiceCreateUpdateResponseModel service_type_put(body)

Update a service Type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceTypesApi()
body = swagger_client.UpdateServiceTypeModel() # UpdateServiceTypeModel | Details of service Type

try:
    # Update a service Type
    api_response = api_instance.service_type_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceTypesApi->service_type_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateServiceTypeModel**](UpdateServiceTypeModel.md)| Details of service Type | 

### Return type

[**ServiceCreateUpdateResponseModel**](ServiceCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

