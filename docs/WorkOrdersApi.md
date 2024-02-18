# maxpanda_python_sdk.WorkOrdersApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**work_orders_create_workorder**](WorkOrdersApi.md#work_orders_create_workorder) | **POST** /v1/WorkOrder | Submit a workorder
[**work_orders_delete_work_order_task**](WorkOrdersApi.md#work_orders_delete_work_order_task) | **DELETE** /v1/DeleteWorkOrderTask | Delete Task of Workorder
[**work_orders_get**](WorkOrdersApi.md#work_orders_get) | **GET** /v1/WorkOrders | Get a list of work orders
[**work_orders_get_0**](WorkOrdersApi.md#work_orders_get_0) | **GET** /v1/WorkOrders/id | Get a specific work order
[**work_orders_get_to_do**](WorkOrdersApi.md#work_orders_get_to_do) | **GET** /v1/ToDo | Get Users To Do WorkOrder List
[**work_orders_get_work_orders_by_status**](WorkOrdersApi.md#work_orders_get_work_orders_by_status) | **GET** /v1/WorkOrdersByWorkOrderStatus | Get Workorders by Status
[**work_orders_get_work_orders_by_user**](WorkOrdersApi.md#work_orders_get_work_orders_by_user) | **GET** /v1/WorkordersByUser | Get list of workorders created by an User
[**work_orders_get_workorder_statuses**](WorkOrdersApi.md#work_orders_get_workorder_statuses) | **GET** /v1/WorkOrderStatuses | Get a list of work orders statues
[**work_orders_update_workorder**](WorkOrdersApi.md#work_orders_update_workorder) | **PUT** /v1/WorkOrder/id | Update a workorder
[**work_orders_update_workorder_status**](WorkOrdersApi.md#work_orders_update_workorder_status) | **POST** /v1/ChangeWorkOrderStatus | Change status of workorder

# **work_orders_create_workorder**
> WorkOrderCreateUpdateResponseModel work_orders_create_workorder(body)

Submit a workorder

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
body = maxpanda_python_sdk.Workorder() # Workorder | Workorder details to be submitted

try:
    # Submit a workorder
    api_response = api_instance.work_orders_create_workorder(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_create_workorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Workorder**](Workorder.md)| Workorder details to be submitted | 

### Return type

[**WorkOrderCreateUpdateResponseModel**](WorkOrderCreateUpdateResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_orders_delete_work_order_task**
> PageResult work_orders_delete_work_order_task(work_order_id, work_order_task_id, id_company)

Delete Task of Workorder

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
work_order_id = 56 # int | Id of workorder
work_order_task_id = 56 # int | Task Id of workorder
id_company = 56 # int | Company Id

try:
    # Delete Task of Workorder
    api_response = api_instance.work_orders_delete_work_order_task(work_order_id, work_order_task_id, id_company)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_delete_work_order_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_order_id** | **int**| Id of workorder | 
 **work_order_task_id** | **int**| Task Id of workorder | 
 **id_company** | **int**| Company Id | 

### Return type

[**PageResult**](PageResult.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_orders_get**
> WorkorderListResponseList work_orders_get(site_id, last_week_active_hours, request_complete_information, page=page, page_size=page_size)

Get a list of work orders

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
last_week_active_hours = true # bool | Show staff's last week active hours
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a list of work orders
    api_response = api_instance.work_orders_get(site_id, last_week_active_hours, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **last_week_active_hours** | **bool**| Show staff&#x27;s last week active hours | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**WorkorderListResponseList**](WorkorderListResponseList.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_orders_get_0**
> WorkorderListResponseList work_orders_get_0(id, site_id, request_complete_information)

Get a specific work order

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
id = 56 # int | Workorder Id
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific work order
    api_response = api_instance.work_orders_get_0(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Workorder Id | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**WorkorderListResponseList**](WorkorderListResponseList.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_orders_get_to_do**
> WorkorderListResponseList work_orders_get_to_do(request_complete_information, site_id=site_id, page=page, page_size=page_size)

Get Users To Do WorkOrder List

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API (optional)
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get Users To Do WorkOrder List
    api_response = api_instance.work_orders_get_to_do(request_complete_information, site_id=site_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_get_to_do: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | [optional] 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**WorkorderListResponseList**](WorkorderListResponseList.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_orders_get_work_orders_by_status**
> WorkorderListResponseList work_orders_get_work_orders_by_status(site_id, request_complete_information, status, page=page, page_size=page_size)

Get Workorders by Status

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
status = 56 # int | Status ID can be found in your WorkOrderStatuses API
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get Workorders by Status
    api_response = api_instance.work_orders_get_work_orders_by_status(site_id, request_complete_information, status, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_get_work_orders_by_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **status** | **int**| Status ID can be found in your WorkOrderStatuses API | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**WorkorderListResponseList**](WorkorderListResponseList.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_orders_get_work_orders_by_user**
> PagedResults work_orders_get_work_orders_by_user(site_id, user_id, page=page, page_size=page_size)

Get list of workorders created by an User

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
user_id = 56 # int | User ID can be found in your Maxpanda Users index or User API
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get list of workorders created by an User
    api_response = api_instance.work_orders_get_work_orders_by_user(site_id, user_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_get_work_orders_by_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **user_id** | **int**| User ID can be found in your Maxpanda Users index or User API | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**PagedResults**](PagedResults.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_orders_get_workorder_statuses**
> PagedResults work_orders_get_workorder_statuses(page=page, page_size=page_size)

Get a list of work orders statues

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a list of work orders statues
    api_response = api_instance.work_orders_get_workorder_statuses(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_get_workorder_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**PagedResults**](PagedResults.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_orders_update_workorder**
> WorkOrderCreateUpdateResponseModel work_orders_update_workorder(body)

Update a workorder

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
body = maxpanda_python_sdk.UpdateWorkorder() # UpdateWorkorder | Workorder details to be updated

try:
    # Update a workorder
    api_response = api_instance.work_orders_update_workorder(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_update_workorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWorkorder**](UpdateWorkorder.md)| Workorder details to be updated | 

### Return type

[**WorkOrderCreateUpdateResponseModel**](WorkOrderCreateUpdateResponseModel.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **work_orders_update_workorder_status**
> PageResult work_orders_update_workorder_status(site_id, workorder_id, new_status)

Change status of workorder

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
api_instance = maxpanda_python_sdk.WorkOrdersApi(maxpanda_python_sdk.ApiClient(configuration))
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
workorder_id = 56 # int | Id of workorder
new_status = 56 # int | New status of workorder

try:
    # Change status of workorder
    api_response = api_instance.work_orders_update_workorder_status(site_id, workorder_id, new_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkOrdersApi->work_orders_update_workorder_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **workorder_id** | **int**| Id of workorder | 
 **new_status** | **int**| New status of workorder | 

### Return type

[**PageResult**](PageResult.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

