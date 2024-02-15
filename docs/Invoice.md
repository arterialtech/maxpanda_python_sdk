# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **int** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**vendor_ref** | [**VendorRef**](VendorRef.md) |  | [optional] 
**invoice_date** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**total_amount** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**invoice_type_ref** | [**list[InvoiceItemTypeRef]**](InvoiceItemTypeRef.md) |  | [optional] 
**invoice_tax_ref** | [**list[InvoiceTaxRef]**](InvoiceTaxRef.md) |  | [optional] 
**workorder_ref** | [**list[WorkorderRef]**](WorkorderRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

