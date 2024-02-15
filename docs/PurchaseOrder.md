# PurchaseOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_ref** | [**SiteRef**](SiteRef.md) |  | [optional] 
**title** | **str** |  | [optional] 
**purchase_order_id** | **int** |  | [optional] 
**vendor_ref** | [**VendorRef**](VendorRef.md) |  | [optional] 
**status_ref** | [**POStatusRef**](POStatusRef.md) |  | [optional] 
**account** | **str** |  | [optional] 
**shipping_address** | [**POAddress**](POAddress.md) |  | [optional] 
**request_approver_ref** | [**list[UserRef]**](UserRef.md) |  | [optional] 
**created_by_user_ref** | [**UserRef**](UserRef.md) |  | [optional] 
**updated_by_user_ref** | [**UserRef**](UserRef.md) |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**ordered** | **datetime** |  | [optional] 
**received** | **datetime** |  | [optional] 
**all_item_paid** | **str** |  | [optional] 
**vendor_confirmed** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**private_notes** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**purchase_order_item_ref** | [**list[PurchaseOrderItemDetails]**](PurchaseOrderItemDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

