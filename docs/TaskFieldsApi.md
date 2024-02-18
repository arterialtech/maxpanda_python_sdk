# maxpanda_python_sdk.TaskFieldsApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**task_field_create**](TaskFieldsApi.md#task_field_create) | **POST** /v1/TaskField | Create new Field for a Task
[**task_field_get**](TaskFieldsApi.md#task_field_get) | **GET** /v1/TaskField | Get Fields associated with a Task
[**task_field_get_by_id**](TaskFieldsApi.md#task_field_get_by_id) | **GET** /v1/TaskField/Id | Get Field associated with a Task
[**task_field_put**](TaskFieldsApi.md#task_field_put) | **PUT** /v1/TaskField | Update Task Field

# **task_field_create**
> TaskFieldCreateUpdateResponseModel task_field_create(body)

Create new Field for a Task

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
api_instance = maxpanda_python_sdk.TaskFieldsApi(maxpanda_python_sdk.ApiClient(configuration))
body = maxpanda_python_sdk.CreateTaskTemplateField() # CreateTaskTemplateField | Details of Field

try:
    # Create new Field for a Task
    api_response = api_instance.task_field_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskFieldsApi->task_field_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTaskTemplateField**](CreateTaskTemplateField.md)| Details of Field | 

### Return type

[**TaskFieldCreateUpdateResponseModel**](TaskFieldCreateUpdateResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_field_get**
> TaskTemplateFieldResponseModel task_field_get(task_id, request_complete_information, page=page, page_size=page_size)

Get Fields associated with a Task

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
api_instance = maxpanda_python_sdk.TaskFieldsApi(maxpanda_python_sdk.ApiClient(configuration))
task_id = 56 # int | Task Id can be from Task Index or Task API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get Fields associated with a Task
    api_response = api_instance.task_field_get(task_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskFieldsApi->task_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task Id can be from Task Index or Task API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**TaskTemplateFieldResponseModel**](TaskTemplateFieldResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_field_get_by_id**
> TaskTemplateFieldResponseModel task_field_get_by_id(id, request_complete_information)

Get Field associated with a Task

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
api_instance = maxpanda_python_sdk.TaskFieldsApi(maxpanda_python_sdk.ApiClient(configuration))
id = 56 # int | Field Id of Task
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get Field associated with a Task
    api_response = api_instance.task_field_get_by_id(id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskFieldsApi->task_field_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Field Id of Task | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**TaskTemplateFieldResponseModel**](TaskTemplateFieldResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **task_field_put**
> TaskFieldCreateUpdateResponseModel task_field_put(body)

Update Task Field

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
api_instance = maxpanda_python_sdk.TaskFieldsApi(maxpanda_python_sdk.ApiClient(configuration))
body = maxpanda_python_sdk.UpdateTaskTemplateField() # UpdateTaskTemplateField | Details of Task Field

try:
    # Update Task Field
    api_response = api_instance.task_field_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskFieldsApi->task_field_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTaskTemplateField**](UpdateTaskTemplateField.md)| Details of Task Field | 

### Return type

[**TaskFieldCreateUpdateResponseModel**](TaskFieldCreateUpdateResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

