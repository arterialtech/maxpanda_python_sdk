# maxpanda-python-sdk
The Maxpanda API documentation for version 1

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://www.maxpanda.com/helpmemax/#api](https://www.maxpanda.com/helpmemax/#api)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import maxpanda_python_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import maxpanda_python_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = maxpanda_python_sdk.AssetStatusApi(maxpanda_python_sdk.ApiClient(configuration))
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields
page = 56 # int | Page number to start retrieving data (similar to List View pagification) (optional)
page_size = 56 # int | Number of records per page (max=100) (optional)

try:
    # Get a paged list of Asset Status
    api_response = api_instance.asset_statuses_get(request_complete_information, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetStatusApi->asset_statuses_get: %s\n" % e)

# Configure API key authorization: ApiKeyHeader
configuration = maxpanda_python_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = maxpanda_python_sdk.AssetStatusApi(maxpanda_python_sdk.ApiClient(configuration))
id = 56 # int | The Asset Status id to retrieve
request_complete_information = true # bool | True option provides all the data fields. False will only return required fields

try:
    # Get a specific Asset Status record
    api_response = api_instance.asset_statuses_get_0(id, request_complete_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetStatusApi->asset_statuses_get_0: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.maxpanda.com/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AssetStatusApi* | [**asset_statuses_get**](docs/AssetStatusApi.md#asset_statuses_get) | **GET** /v1/Company/AssetStatuses | Get a paged list of Asset Status
*AssetStatusApi* | [**asset_statuses_get_0**](docs/AssetStatusApi.md#asset_statuses_get_0) | **GET** /v1/Company/AssetStatuses/id | Get a specific Asset Status record
*AssetTypeApi* | [**asset_types_get**](docs/AssetTypeApi.md#asset_types_get) | **GET** /v1/Company/AssetTypes | Get a paged list of Asset Types
*AssetTypeApi* | [**asset_types_get_0**](docs/AssetTypeApi.md#asset_types_get_0) | **GET** /v1/Company/AssetTypes/id | Get a specific Asset Type type record
*AssetsApi* | [**assets_v1_create**](docs/AssetsApi.md#assets_v1_create) | **POST** /v1/Asset | Create an Asset
*AssetsApi* | [**assets_v1_get**](docs/AssetsApi.md#assets_v1_get) | **GET** /v1/Assets | Get a list of Assets
*AssetsApi* | [**assets_v1_get_0**](docs/AssetsApi.md#assets_v1_get_0) | **GET** /v1/Asset/id | Get a specific Asset
*AssetsApi* | [**assets_v1_update_asset**](docs/AssetsApi.md#assets_v1_update_asset) | **PUT** /v1/Asset | Update an Asset
*BinsApi* | [**bin_get**](docs/BinsApi.md#bin_get) | **GET** /v1/Bins | Get list of Bins
*BinsApi* | [**bin_get_0**](docs/BinsApi.md#bin_get_0) | **GET** /v1/Bins/id | Get a specific Bin
*BinsApi* | [**bin_post**](docs/BinsApi.md#bin_post) | **POST** /v1/Bins | Create a Bin
*BinsApi* | [**bin_put**](docs/BinsApi.md#bin_put) | **PUT** /v1/Bins | Update a Bin
*BuildingsApi* | [**buildings_create_building**](docs/BuildingsApi.md#buildings_create_building) | **POST** /v1/Building | Create a new Building
*BuildingsApi* | [**buildings_get_building**](docs/BuildingsApi.md#buildings_get_building) | **GET** /v1/Building/id | Get a specific Building
*BuildingsApi* | [**buildings_get_buildings**](docs/BuildingsApi.md#buildings_get_buildings) | **GET** /v1/Buildings | Get a paged list of buildings
*BuildingsApi* | [**buildings_patch**](docs/BuildingsApi.md#buildings_patch) | **PATCH** /v1/Building | Update specific attributes of a given building
*CustomerApi* | [**customer_get**](docs/CustomerApi.md#customer_get) | **GET** /v1/Customers | Get a paged list of Customers
*CustomerApi* | [**customer_get_customer_by_id**](docs/CustomerApi.md#customer_get_customer_by_id) | **GET** /v1/Customer/id | Get a specific customer
*CustomerApi* | [**customer_post**](docs/CustomerApi.md#customer_post) | **POST** /v1/Customer | Create a new customer
*CustomerApi* | [**customer_put**](docs/CustomerApi.md#customer_put) | **PUT** /v1/Customer | Update an existing customer.
*CustomerInvoicesApi* | [**customer_invoice_create_customer_invoice**](docs/CustomerInvoicesApi.md#customer_invoice_create_customer_invoice) | **POST** /v1/CustomerInvoice | Create a new customer invoice.
*CustomerInvoicesApi* | [**customer_invoice_edit_customer_invoice**](docs/CustomerInvoicesApi.md#customer_invoice_edit_customer_invoice) | **PUT** /v1/CustomerInvoice | Update Customer Invoice
*CustomerInvoicesApi* | [**customer_invoice_get**](docs/CustomerInvoicesApi.md#customer_invoice_get) | **GET** /v1/GetCustomerInvoices | Get list of Customer Invoices
*CustomerInvoicesApi* | [**customer_invoice_get_0**](docs/CustomerInvoicesApi.md#customer_invoice_get_0) | **GET** /v1/GetCustomerInvoice/id | Get a specific Customer Invoice
*DepartmentApi* | [**department_get**](docs/DepartmentApi.md#department_get) | **GET** /v1/Company/Departments | Get a paged list of departments
*DepartmentApi* | [**department_get_0**](docs/DepartmentApi.md#department_get_0) | **GET** /v1/Company/Department/id | Get a specific Department type record
*InvoiceItemTaxApi* | [**invoice_tax_get**](docs/InvoiceItemTaxApi.md#invoice_tax_get) | **GET** /v1/Company/InvoiceTaxes | Get a paged list of Invoice Taxes
*InvoiceItemTaxApi* | [**invoice_tax_get_0**](docs/InvoiceItemTaxApi.md#invoice_tax_get_0) | **GET** /v1/Company/InvoiceTax/id | Get a specific Invoice Tax record
*InvoiceItemTypeApi* | [**invoice_item_types_get**](docs/InvoiceItemTypeApi.md#invoice_item_types_get) | **GET** /v1/Company/InvoiceItemTypes | Get a paged list of Invoice Item Types
*InvoiceItemTypeApi* | [**invoice_item_types_get_0**](docs/InvoiceItemTypeApi.md#invoice_item_types_get_0) | **GET** /v1/Company/InvoiceItemType/id | Get a specific Invoice Item Type record
*LocationApi* | [**locations_create**](docs/LocationApi.md#locations_create) | **POST** /v1/Location | Create a location
*LocationApi* | [**locations_get**](docs/LocationApi.md#locations_get) | **GET** /v1/Locations | Get a list of locations
*LocationApi* | [**locations_get_0**](docs/LocationApi.md#locations_get_0) | **GET** /v1/Location/id | Get a specific location
*LocationApi* | [**locations_patch**](docs/LocationApi.md#locations_patch) | **PUT** /v1/Location | Update a location
*LocationTypeApi* | [**location_types_get**](docs/LocationTypeApi.md#location_types_get) | **GET** /v1/Company/LocationTypes | Get a paged list of Location Types
*LocationTypeApi* | [**location_types_get_0**](docs/LocationTypeApi.md#location_types_get_0) | **GET** /v1/Company/LocationTypes/id | Get a specific location type record
*MeteringTypeApi* | [**metering_types_get**](docs/MeteringTypeApi.md#metering_types_get) | **GET** /v1/Company/MeteringTypes | Get a paged list of Metering Types
*MeteringTypeApi* | [**metering_types_get_0**](docs/MeteringTypeApi.md#metering_types_get_0) | **GET** /v1/Company/MeteringTypes/id | Get a specific Metering Type record
*POAddressApi* | [**p_o_address_create**](docs/POAddressApi.md#p_o_address_create) | **POST** /v1/Company/POAddress | Create a new Purchase Order Address
*POAddressApi* | [**p_o_address_get**](docs/POAddressApi.md#p_o_address_get) | **GET** /v1/Company/POAddress | Get Purchase Order Address
*POAddressApi* | [**p_o_address_get_0**](docs/POAddressApi.md#p_o_address_get_0) | **GET** /v1/Company/POAddress/id | Get a specific PO Address
*POAddressApi* | [**p_o_address_put**](docs/POAddressApi.md#p_o_address_put) | **PUT** /v1/Company/POAddress | Update an existing Purchase Order Address
*POTemplatesApi* | [**p_o_template_get**](docs/POTemplatesApi.md#p_o_template_get) | **GET** /v1/PurchaseOrderTemplate | Get a paged list of Purchase Order Template
*POTemplatesApi* | [**p_o_template_get_0**](docs/POTemplatesApi.md#p_o_template_get_0) | **GET** /v1/PurchaseOrderTemplate/id | Get a specific Purchase Order Template
*PartCategoryApi* | [**part_category_create**](docs/PartCategoryApi.md#part_category_create) | **POST** /v1/Company/PartCategory | Create a new Part Category
*PartCategoryApi* | [**part_category_delete_part_category**](docs/PartCategoryApi.md#part_category_delete_part_category) | **DELETE** /v1/Company/PartCategory | Delete PartCategory of Part
*PartCategoryApi* | [**part_category_get**](docs/PartCategoryApi.md#part_category_get) | **GET** /v1/Company/PartCategory | Get a paged list of PartCategory
*PartCategoryApi* | [**part_category_get_0**](docs/PartCategoryApi.md#part_category_get_0) | **GET** /v1/Company/PartCategory/{id} | Get a specific Part Category record
*PartCategoryApi* | [**part_category_put**](docs/PartCategoryApi.md#part_category_put) | **PUT** /v1/Company/PartCategory | Update an existing Part Category
*PartStatusApi* | [**part_statuses_get**](docs/PartStatusApi.md#part_statuses_get) | **GET** /v1/Company/PartStatuses | Get a paged list of Parts Status
*PartStatusApi* | [**part_statuses_get_0**](docs/PartStatusApi.md#part_statuses_get_0) | **GET** /v1/Company/PartStatuses/{id} | Get a specific Part Status record
*PartsApi* | [**part_get**](docs/PartsApi.md#part_get) | **GET** /v1/Parts | Get a list of parts
*PartsApi* | [**part_get_0**](docs/PartsApi.md#part_get_0) | **GET** /v1/Part/id | Get a specific Part
*PartsApi* | [**part_get_part_types**](docs/PartsApi.md#part_get_part_types) | **GET** /v1/PartTypes | Get a list of Part Types
*PartsApi* | [**part_post**](docs/PartsApi.md#part_post) | **POST** /v1/Part | Create a new Part
*PartsApi* | [**part_put**](docs/PartsApi.md#part_put) | **PUT** /v1/Part | Update a Part
*PurchaseOrdersApi* | [**purchase_order_get**](docs/PurchaseOrdersApi.md#purchase_order_get) | **GET** /v1/PurchaseOrder | Get a paged list of Purchase Orders
*PurchaseOrdersApi* | [**purchase_order_get_0**](docs/PurchaseOrdersApi.md#purchase_order_get_0) | **GET** /v1/PurchaseOrder/id | Get a specific Purchase Order
*PurchaseOrdersApi* | [**purchase_order_get_po_status**](docs/PurchaseOrdersApi.md#purchase_order_get_po_status) | **GET** /v1/PurchaseOrderStatus | Get Purchase Order Statuses
*PurchaseOrdersApi* | [**purchase_order_post**](docs/PurchaseOrdersApi.md#purchase_order_post) | **POST** /v1/PurchaseOrder | Create a new Purchase Order
*PurchaseOrdersApi* | [**purchase_order_put**](docs/PurchaseOrdersApi.md#purchase_order_put) | **PUT** /v1/PurchaseOrder | Update a Purchase Order
*PurchaseOrdersApi* | [**purchase_order_put_0**](docs/PurchaseOrdersApi.md#purchase_order_put_0) | **PUT** /v1/UpdatePurchaseOrderStatus | Update Status of Purchase Order
*ServiceTypesApi* | [**service_type_get**](docs/ServiceTypesApi.md#service_type_get) | **GET** /v1/ServiceTypes | Get a paged list of Service Types
*ServiceTypesApi* | [**service_type_get_0**](docs/ServiceTypesApi.md#service_type_get_0) | **GET** /v1/ServiceType/id | Get a Service Type
*ServiceTypesApi* | [**service_type_post**](docs/ServiceTypesApi.md#service_type_post) | **POST** /v1/ServiceType | Create a new service Type
*ServiceTypesApi* | [**service_type_put**](docs/ServiceTypesApi.md#service_type_put) | **PUT** /v1/ServiceType | Update a service Type
*SitesApi* | [**sites_get**](docs/SitesApi.md#sites_get) | **GET** /v1/Sites | Get a list of sites
*SitesApi* | [**sites_get_0**](docs/SitesApi.md#sites_get_0) | **GET** /v1/Sites/id | Get a specific site
*TaskFieldsApi* | [**task_field_create**](docs/TaskFieldsApi.md#task_field_create) | **POST** /v1/TaskField | Create new Field for a Task
*TaskFieldsApi* | [**task_field_get**](docs/TaskFieldsApi.md#task_field_get) | **GET** /v1/TaskField | Get Fields associated with a Task
*TaskFieldsApi* | [**task_field_get_by_id**](docs/TaskFieldsApi.md#task_field_get_by_id) | **GET** /v1/TaskField/Id | Get Field associated with a Task
*TaskFieldsApi* | [**task_field_put**](docs/TaskFieldsApi.md#task_field_put) | **PUT** /v1/TaskField | Update Task Field
*TaskPriorityApi* | [**task_priorities_get**](docs/TaskPriorityApi.md#task_priorities_get) | **GET** /v1/TaskPriorities | Get a paged list of Task Priority
*TaskStatusApi* | [**task_statuses_get**](docs/TaskStatusApi.md#task_statuses_get) | **GET** /v1/TaskStatuses | Get a paged list of Task Statuses
*TasksApi* | [**task_get**](docs/TasksApi.md#task_get) | **GET** /v1/Tasks | Get a paged list of Task Statuses
*TasksApi* | [**task_get_0**](docs/TasksApi.md#task_get_0) | **GET** /v1/Tasks/id | Get a specific Task
*TasksApi* | [**task_post**](docs/TasksApi.md#task_post) | **POST** /v1/Task | Create a new Task
*TasksApi* | [**task_put**](docs/TasksApi.md#task_put) | **PUT** /v1/Task | Update an existing Task
*UsersApi* | [**user_get_user_by_id**](docs/UsersApi.md#user_get_user_by_id) | **GET** /v1/UserById/id | Get a specific User
*UsersApi* | [**user_get_users**](docs/UsersApi.md#user_get_users) | **GET** /v1/Users | Get list of Users
*VendorApi* | [**vendor_get_vendor_by_id**](docs/VendorApi.md#vendor_get_vendor_by_id) | **GET** /v1/Vendors/id | Get a specific Vendor
*VendorApi* | [**vendor_get_vendors**](docs/VendorApi.md#vendor_get_vendors) | **GET** /v1/Vendors | Get list of Vendors
*VendorApi* | [**vendor_post**](docs/VendorApi.md#vendor_post) | **POST** /v1/Vendor | Create a new Vendor
*VendorApi* | [**vendor_put**](docs/VendorApi.md#vendor_put) | **PUT** /v1/Vendor | Update an existing vendor.
*VendorInvoicesApi* | [**vendor_invoice_get**](docs/VendorInvoicesApi.md#vendor_invoice_get) | **GET** /v1/VendorInvoices | Get a paged list of Vendor Invoice
*VendorInvoicesApi* | [**vendor_invoice_get_0**](docs/VendorInvoicesApi.md#vendor_invoice_get_0) | **GET** /v1/VendorInvoice/id | Get a specific Vendor Invoice
*VendorInvoicesApi* | [**vendor_invoice_post**](docs/VendorInvoicesApi.md#vendor_invoice_post) | **POST** /v1/VendorInvoice | Create an Invoice
*VendorInvoicesApi* | [**vendor_invoice_put**](docs/VendorInvoicesApi.md#vendor_invoice_put) | **PUT** /v1/VendorInvoice | Update an Invoice
*WorkOrderCategoryApi* | [**work_order_categories_get**](docs/WorkOrderCategoryApi.md#work_order_categories_get) | **GET** /v1/Company/WorkorderCategories | Get a paged list of Workorder Categories
*WorkOrderCategoryApi* | [**work_order_categories_get_0**](docs/WorkOrderCategoryApi.md#work_order_categories_get_0) | **GET** /v1/Company/WorkorderCategory/id | Get a specific Workorder Category record
*WorkOrderPriorityApi* | [**work_order_priorities_get**](docs/WorkOrderPriorityApi.md#work_order_priorities_get) | **GET** /v1/Company/WorkOrderPriorities | Get a paged list of WorkOrder Priorities
*WorkOrderPriorityApi* | [**work_order_priorities_get_0**](docs/WorkOrderPriorityApi.md#work_order_priorities_get_0) | **GET** /v1/Company/WorkOrderPriority/id | Get a specific WorkOrder Priority record
*WorkOrdersApi* | [**work_orders_create_workorder**](docs/WorkOrdersApi.md#work_orders_create_workorder) | **POST** /v1/WorkOrder | Submit a workorder
*WorkOrdersApi* | [**work_orders_delete_work_order_task**](docs/WorkOrdersApi.md#work_orders_delete_work_order_task) | **DELETE** /v1/DeleteWorkOrderTask | Delete Task of Workorder
*WorkOrdersApi* | [**work_orders_get**](docs/WorkOrdersApi.md#work_orders_get) | **GET** /v1/WorkOrders | Get a list of work orders
*WorkOrdersApi* | [**work_orders_get_0**](docs/WorkOrdersApi.md#work_orders_get_0) | **GET** /v1/WorkOrders/id | Get a specific work order
*WorkOrdersApi* | [**work_orders_get_to_do**](docs/WorkOrdersApi.md#work_orders_get_to_do) | **GET** /v1/ToDo | Get Users To Do WorkOrder List
*WorkOrdersApi* | [**work_orders_get_work_orders_by_status**](docs/WorkOrdersApi.md#work_orders_get_work_orders_by_status) | **GET** /v1/WorkOrdersByWorkOrderStatus | Get Workorders by Status
*WorkOrdersApi* | [**work_orders_get_work_orders_by_user**](docs/WorkOrdersApi.md#work_orders_get_work_orders_by_user) | **GET** /v1/WorkordersByUser | Get list of workorders created by an User
*WorkOrdersApi* | [**work_orders_get_workorder_statuses**](docs/WorkOrdersApi.md#work_orders_get_workorder_statuses) | **GET** /v1/WorkOrderStatuses | Get a list of work orders statues
*WorkOrdersApi* | [**work_orders_update_workorder**](docs/WorkOrdersApi.md#work_orders_update_workorder) | **PUT** /v1/WorkOrder/id | Update a workorder
*WorkOrdersApi* | [**work_orders_update_workorder_status**](docs/WorkOrdersApi.md#work_orders_update_workorder_status) | **POST** /v1/ChangeWorkOrderStatus | Change status of workorder

## Documentation For Models

 - [APIAddressModel](docs/APIAddressModel.md)
 - [Address](docs/Address.md)
 - [AddressAPIModel](docs/AddressAPIModel.md)
 - [Asset](docs/Asset.md)
 - [AssetAuditModel](docs/AssetAuditModel.md)
 - [AssetCreateUpdateResponseModel](docs/AssetCreateUpdateResponseModel.md)
 - [AssetList](docs/AssetList.md)
 - [AssetRef](docs/AssetRef.md)
 - [AssetResponseModel](docs/AssetResponseModel.md)
 - [AssetStaffRef](docs/AssetStaffRef.md)
 - [AssetStatus](docs/AssetStatus.md)
 - [AssetStatusRef](docs/AssetStatusRef.md)
 - [AssetStatusResponseModel](docs/AssetStatusResponseModel.md)
 - [AssetType](docs/AssetType.md)
 - [AssetTypeRef](docs/AssetTypeRef.md)
 - [AssetTypeResponseModel](docs/AssetTypeResponseModel.md)
 - [Bin](docs/Bin.md)
 - [BinCreateUpdateResponseModel](docs/BinCreateUpdateResponseModel.md)
 - [BinPartsRef](docs/BinPartsRef.md)
 - [BinRef](docs/BinRef.md)
 - [BinResponseModel](docs/BinResponseModel.md)
 - [BuildingCreateModel](docs/BuildingCreateModel.md)
 - [BuildingCreateUpdateResponseModel](docs/BuildingCreateUpdateResponseModel.md)
 - [BuildingDetails](docs/BuildingDetails.md)
 - [BuildingList](docs/BuildingList.md)
 - [BuildingRef](docs/BuildingRef.md)
 - [BuildingResponseModel](docs/BuildingResponseModel.md)
 - [BuildingUpdateModel](docs/BuildingUpdateModel.md)
 - [CreateBinModel](docs/CreateBinModel.md)
 - [CreateCustomerInvoice](docs/CreateCustomerInvoice.md)
 - [CreateCustomerModel](docs/CreateCustomerModel.md)
 - [CreateInvoiceItemModel](docs/CreateInvoiceItemModel.md)
 - [CreateInvoiceModel](docs/CreateInvoiceModel.md)
 - [CreatePOAddress](docs/CreatePOAddress.md)
 - [CreatePartCategory](docs/CreatePartCategory.md)
 - [CreatePartModel](docs/CreatePartModel.md)
 - [CreatePurchaseOrder](docs/CreatePurchaseOrder.md)
 - [CreateServiceTypeModel](docs/CreateServiceTypeModel.md)
 - [CreateTaskField](docs/CreateTaskField.md)
 - [CreateTaskModel](docs/CreateTaskModel.md)
 - [CreateTaskTemplateField](docs/CreateTaskTemplateField.md)
 - [CreateUpdateAssetModel](docs/CreateUpdateAssetModel.md)
 - [CreateUpdateBinModel](docs/CreateUpdateBinModel.md)
 - [CreateUpdateBuildingModel](docs/CreateUpdateBuildingModel.md)
 - [CreateUpdateCustomerModel](docs/CreateUpdateCustomerModel.md)
 - [CreateUpdateInvoiceModel](docs/CreateUpdateInvoiceModel.md)
 - [CreateUpdateLocationModel](docs/CreateUpdateLocationModel.md)
 - [CreateUpdatePOModel](docs/CreateUpdatePOModel.md)
 - [CreateUpdatePartCategory](docs/CreateUpdatePartCategory.md)
 - [CreateUpdatePartCategoryModel](docs/CreateUpdatePartCategoryModel.md)
 - [CreateUpdatePartModel](docs/CreateUpdatePartModel.md)
 - [CreateUpdateServiceTypeModel](docs/CreateUpdateServiceTypeModel.md)
 - [CreateUpdateTaskFieldModel](docs/CreateUpdateTaskFieldModel.md)
 - [CreateUpdateTaskModel](docs/CreateUpdateTaskModel.md)
 - [CreateUpdateVendorModel](docs/CreateUpdateVendorModel.md)
 - [CreateUpdateWorkorderModel](docs/CreateUpdateWorkorderModel.md)
 - [CreateVendorModel](docs/CreateVendorModel.md)
 - [Customer](docs/Customer.md)
 - [CustomerCreateUpdateResponseModel](docs/CustomerCreateUpdateResponseModel.md)
 - [CustomerRef](docs/CustomerRef.md)
 - [CustomerResponseModel](docs/CustomerResponseModel.md)
 - [Department](docs/Department.md)
 - [DepartmentRef](docs/DepartmentRef.md)
 - [DepartmentResponseModel](docs/DepartmentResponseModel.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceCreateUpdateResponseModel](docs/InvoiceCreateUpdateResponseModel.md)
 - [InvoiceItemModel](docs/InvoiceItemModel.md)
 - [InvoiceItemType](docs/InvoiceItemType.md)
 - [InvoiceItemTypeRef](docs/InvoiceItemTypeRef.md)
 - [InvoiceItemTypeResponseModel](docs/InvoiceItemTypeResponseModel.md)
 - [InvoiceRef](docs/InvoiceRef.md)
 - [InvoiceResponseModel](docs/InvoiceResponseModel.md)
 - [InvoiceTax](docs/InvoiceTax.md)
 - [InvoiceTaxModel](docs/InvoiceTaxModel.md)
 - [InvoiceTaxRef](docs/InvoiceTaxRef.md)
 - [InvoiceTaxResponseModel](docs/InvoiceTaxResponseModel.md)
 - [Location](docs/Location.md)
 - [LocationCreateUpdateResponseModel](docs/LocationCreateUpdateResponseModel.md)
 - [LocationRef](docs/LocationRef.md)
 - [LocationResponseModel](docs/LocationResponseModel.md)
 - [LocationType](docs/LocationType.md)
 - [LocationTypeResponseModel](docs/LocationTypeResponseModel.md)
 - [LocationUpdateModel](docs/LocationUpdateModel.md)
 - [MerteringRef](docs/MerteringRef.md)
 - [MeteringType](docs/MeteringType.md)
 - [MeteringTypeResponseModel](docs/MeteringTypeResponseModel.md)
 - [POAddress](docs/POAddress.md)
 - [POAddressAPIModel](docs/POAddressAPIModel.md)
 - [POAddressModelAPI](docs/POAddressModelAPI.md)
 - [POCreateUpdateResponseModel](docs/POCreateUpdateResponseModel.md)
 - [POStatusRef](docs/POStatusRef.md)
 - [POTemplate](docs/POTemplate.md)
 - [POTemplateRef](docs/POTemplateRef.md)
 - [POTemplateResponseModel](docs/POTemplateResponseModel.md)
 - [PageResult](docs/PageResult.md)
 - [PagedResults](docs/PagedResults.md)
 - [Part](docs/Part.md)
 - [PartCategory](docs/PartCategory.md)
 - [PartCategoryRef](docs/PartCategoryRef.md)
 - [PartCategoryResponseModel](docs/PartCategoryResponseModel.md)
 - [PartCreateUpdateResponseModel](docs/PartCreateUpdateResponseModel.md)
 - [PartRef](docs/PartRef.md)
 - [PartResponseModel](docs/PartResponseModel.md)
 - [PartStatus](docs/PartStatus.md)
 - [PartStatusRef](docs/PartStatusRef.md)
 - [PartStatusResponseModel](docs/PartStatusResponseModel.md)
 - [PartType](docs/PartType.md)
 - [PartTypeRef](docs/PartTypeRef.md)
 - [PartTypeResponseModel](docs/PartTypeResponseModel.md)
 - [PurchaseOrder](docs/PurchaseOrder.md)
 - [PurchaseOrderItem](docs/PurchaseOrderItem.md)
 - [PurchaseOrderItemDetails](docs/PurchaseOrderItemDetails.md)
 - [PurchaseOrderResponseModel](docs/PurchaseOrderResponseModel.md)
 - [ServiceCreateUpdateResponseModel](docs/ServiceCreateUpdateResponseModel.md)
 - [ServiceTypesList](docs/ServiceTypesList.md)
 - [ServiceTypesListResponseList](docs/ServiceTypesListResponseList.md)
 - [SiteList](docs/SiteList.md)
 - [SiteRef](docs/SiteRef.md)
 - [SiteResponseModel](docs/SiteResponseModel.md)
 - [StaffRef](docs/StaffRef.md)
 - [Task](docs/Task.md)
 - [TaskCreateUpdateResponseModel](docs/TaskCreateUpdateResponseModel.md)
 - [TaskFieldCreateUpdateResponseModel](docs/TaskFieldCreateUpdateResponseModel.md)
 - [TaskFieldRef](docs/TaskFieldRef.md)
 - [TaskPriority](docs/TaskPriority.md)
 - [TaskPriorityDetails](docs/TaskPriorityDetails.md)
 - [TaskPriorityRef](docs/TaskPriorityRef.md)
 - [TaskProrityResponseModel](docs/TaskProrityResponseModel.md)
 - [TaskRef](docs/TaskRef.md)
 - [TaskReponseModel](docs/TaskReponseModel.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [TaskStatusAPIListModel](docs/TaskStatusAPIListModel.md)
 - [TaskStatusResponseModel](docs/TaskStatusResponseModel.md)
 - [TaskTemplateField](docs/TaskTemplateField.md)
 - [TaskTemplateFieldResponseModel](docs/TaskTemplateFieldResponseModel.md)
 - [UpdateAsset](docs/UpdateAsset.md)
 - [UpdateBinModel](docs/UpdateBinModel.md)
 - [UpdateCustomerInvoice](docs/UpdateCustomerInvoice.md)
 - [UpdateCustomerModel](docs/UpdateCustomerModel.md)
 - [UpdateInvoiceModel](docs/UpdateInvoiceModel.md)
 - [UpdatePOAddress](docs/UpdatePOAddress.md)
 - [UpdatePartCategory](docs/UpdatePartCategory.md)
 - [UpdatePartModel](docs/UpdatePartModel.md)
 - [UpdatePurchaseOrder](docs/UpdatePurchaseOrder.md)
 - [UpdateServiceTypeModel](docs/UpdateServiceTypeModel.md)
 - [UpdateTaskField](docs/UpdateTaskField.md)
 - [UpdateTaskModel](docs/UpdateTaskModel.md)
 - [UpdateTaskTemplateField](docs/UpdateTaskTemplateField.md)
 - [UpdateVendorModel](docs/UpdateVendorModel.md)
 - [UpdateWorkorder](docs/UpdateWorkorder.md)
 - [UserDetail](docs/UserDetail.md)
 - [UserListResponseModel](docs/UserListResponseModel.md)
 - [UserRef](docs/UserRef.md)
 - [UsersList](docs/UsersList.md)
 - [VendorCreateUpdateResponseModel](docs/VendorCreateUpdateResponseModel.md)
 - [VendorDetail](docs/VendorDetail.md)
 - [VendorDetailsRef](docs/VendorDetailsRef.md)
 - [VendorRef](docs/VendorRef.md)
 - [VendorsListModel](docs/VendorsListModel.md)
 - [VendorsListResponseModel](docs/VendorsListResponseModel.md)
 - [WOPartRef](docs/WOPartRef.md)
 - [WOTaskDetailRef](docs/WOTaskDetailRef.md)
 - [WOTaskFieldDetail](docs/WOTaskFieldDetail.md)
 - [WorkOrderAudit](docs/WorkOrderAudit.md)
 - [WorkOrderCategory](docs/WorkOrderCategory.md)
 - [WorkOrderCategoryResponseModel](docs/WorkOrderCategoryResponseModel.md)
 - [WorkOrderCreateUpdateResponseModel](docs/WorkOrderCreateUpdateResponseModel.md)
 - [WorkOrderList](docs/WorkOrderList.md)
 - [WorkOrderPartsRef](docs/WorkOrderPartsRef.md)
 - [WorkOrderPriorityResponseModel](docs/WorkOrderPriorityResponseModel.md)
 - [WorkOrderResourceActiveHoursWeeklyModel](docs/WorkOrderResourceActiveHoursWeeklyModel.md)
 - [Workorder](docs/Workorder.md)
 - [WorkorderCategoryRef](docs/WorkorderCategoryRef.md)
 - [WorkorderListResponseList](docs/WorkorderListResponseList.md)
 - [WorkorderPriorityRef](docs/WorkorderPriorityRef.md)
 - [WorkorderRef](docs/WorkorderRef.md)
 - [WorkorderStaffsRef](docs/WorkorderStaffsRef.md)
 - [WorkorderStatus](docs/WorkorderStatus.md)
 - [WorkorderTypeRef](docs/WorkorderTypeRef.md)

## Documentation For Authorization


## ApiKeyHeader

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author


