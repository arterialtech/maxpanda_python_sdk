# UpdatePurchaseOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Site Id of the Purchase Order. Site Id can be found in your Maxpanda Site Index or Site API | 
**purchase_order_id** | **int** | Id of the Purchase Order. Purchase Order Id can be found in your Maxpanda Accounting PO Index or Purchase Order API | 
**vendor_id** | **int** | Vendor Id of the Purchase Order. Vendor Id can be found in your Maxpanda Vendor Index or Vednor API | 
**title** | **str** | Title of Purchase Order | 
**account** | **str** | Account details | [optional] 
**shipping_address_id** | **int** | Shipping Address Id of the Purchase Order. Shipping Id can be found in your Maxpanda Company PO Address or PO Address API | 
**request_approvers_id** | **list[int]** | Approvers Id of the Purchase Order. User Id can be found in your Maxpanda User Index or User API | 
**received** | **datetime** | Date of Item Receiving | [optional] 
**ordered** | **datetime** | Date of Item Order | [optional] 
**notes** | **str** | Notes about Purchase Order | [optional] 
**private_notes** | **str** | Private Notes about Purchase Order | [optional] 
**comment** | **str** | Comment | [optional] 
**status** | **int** | Status of Purchase Order. Purchase Order Status can be found in Purchase Order Status API | 
**sort_order** | **int** | Order of sorting | [optional] 
**purchase_order_items** | [**list[PurchaseOrderItem]**](PurchaseOrderItem.md) | Parts ordered in Purchase Order. | [optional] 
**all_items_paid** | **bool** | Set Trus if All Items are Paid else set False | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

