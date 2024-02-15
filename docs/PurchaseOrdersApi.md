# swagger_client.PurchaseOrdersApi

All URIs are relative to *https://api.maxpanda.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_order_get**](PurchaseOrdersApi.md#purchase_order_get) | **GET** /v1/PurchaseOrder | Get a paged list of Purchase Orders
[**purchase_order_get_0**](PurchaseOrdersApi.md#purchase_order_get_0) | **GET** /v1/PurchaseOrder/id | Get a specific Purchase Order
[**purchase_order_get_po_status**](PurchaseOrdersApi.md#purchase_order_get_po_status) | **GET** /v1/PurchaseOrderStatus | Get Purchase Order Statuses
[**purchase_order_post**](PurchaseOrdersApi.md#purchase_order_post) | **POST** /v1/PurchaseOrder | Create a new Purchase Order
[**purchase_order_put**](PurchaseOrdersApi.md#purchase_order_put) | **PUT** /v1/PurchaseOrder | Update a Purchase Order
[**purchase_order_put_0**](PurchaseOrdersApi.md#purchase_order_put_0) | **PUT** /v1/UpdatePurchaseOrderStatus | Update Status of Purchase Order

# **purchase_order_get**
> PurchaseOrderResponseModel purchase_order_get(site_id, request_complete_information, page=page, page_size=page_size)

Get a paged list of Purchase Orders

The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PurchaseOrdersApi()
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of Purchase Orders
    api_response = api_instance.purchase_order_get(site_id, request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->purchase_order_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 
 **page** | **int**| Page number to start retrieving data (similar to List View pagification) | [optional] 
 **page_size** | **int**| Number of records per page (max&#x3D;100) | [optional] 

### Return type

[**PurchaseOrderResponseModel**](PurchaseOrderResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_get_0**
> PurchaseOrderResponseModel purchase_order_get_0(id, site_id, request_complete_information)

Get a specific Purchase Order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PurchaseOrdersApi()
id = 56 # int | The Purchase Order id to retrieve
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Purchase Order
    api_response = api_instance.purchase_order_get_0(id, site_id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->purchase_order_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Purchase Order id to retrieve | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **request_complete_information** | **bool**| True option provides all the data fields. False will only return required fields | 

### Return type

[**PurchaseOrderResponseModel**](PurchaseOrderResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_get_po_status**
> PageResult purchase_order_get_po_status()

Get Purchase Order Statuses

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PurchaseOrdersApi()

try:
    # Get Purchase Order Statuses
    api_response = api_instance.purchase_order_get_po_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->purchase_order_get_po_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PageResult**](PageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_post**
> POCreateUpdateResponseModel purchase_order_post(body)

Create a new Purchase Order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PurchaseOrdersApi()
body = swagger_client.CreatePurchaseOrder() # CreatePurchaseOrder | Details of new Purchase Order

try:
    # Create a new Purchase Order
    api_response = api_instance.purchase_order_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->purchase_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePurchaseOrder**](CreatePurchaseOrder.md)| Details of new Purchase Order | 

### Return type

[**POCreateUpdateResponseModel**](POCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_put**
> POCreateUpdateResponseModel purchase_order_put(body)

Update a Purchase Order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PurchaseOrdersApi()
body = swagger_client.UpdatePurchaseOrder() # UpdatePurchaseOrder | Details of Purchase Order

try:
    # Update a Purchase Order
    api_response = api_instance.purchase_order_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->purchase_order_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePurchaseOrder**](UpdatePurchaseOrder.md)| Details of Purchase Order | 

### Return type

[**POCreateUpdateResponseModel**](POCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_put_0**
> POCreateUpdateResponseModel purchase_order_put_0(purchase_order_id, site_id, new_status)

Update Status of Purchase Order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PurchaseOrdersApi()
purchase_order_id = 56 # int | Purchase Order Id
site_id = 56 # int | Site ID can be found in your Maxpanda Site index or Sites API
new_status = 56 # int | Status ID can be found in Purchase Order Status API

try:
    # Update Status of Purchase Order
    api_response = api_instance.purchase_order_put_0(purchase_order_id, site_id, new_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->purchase_order_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order_id** | **int**| Purchase Order Id | 
 **site_id** | **int**| Site ID can be found in your Maxpanda Site index or Sites API | 
 **new_status** | **int**| Status ID can be found in Purchase Order Status API | 

### Return type

[**POCreateUpdateResponseModel**](POCreateUpdateResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

