# PurchaseOrderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_id** | **int** | Part to be ordered. Part Id can be found in your Maxpanda Inventory Parts Index or Parts API | [optional] 
**bin_id** | **int** | Bin where Part is kept. Bin Id can be found in your Maxpanda Inventory Bin Index or Bin API | [optional] 
**unit_price** | **float** | Unit price of Ordered Item.Unit Price can be modified in case of Pending and Approved Purchase Orders only. | [optional] 
**ordered_qty** | **float** | Quantity of Items ordered. OrderedQty can be modified in case of Pending and Approved Purchase Orders only. | [optional] 
**received_qty** | **float** | Quantity Received. Quantity can be received only in case of OnOrdered Purchase Orders. | [optional] 
**update_bin_quantity_to_inventory** | **bool** | Bin Quantity Update. Update Bin Quantity to Inventory | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

