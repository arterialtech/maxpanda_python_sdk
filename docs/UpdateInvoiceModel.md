# UpdateInvoiceModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **int** | Vendor ID can be found in your Maxpanda Vendor index or Vendor API | 
**invoice_id** | **int** | Site ID can be found in your Maxpanda Site index or Vendor API | 
**sites** | **list[int]** |  | [optional] 
**invoice_number** | **str** | Invoice Number of Invoice | 
**invoice_date** | **datetime** | Date on which Invoice was Raised | 
**due_date** | **datetime** | Due date of Invoice | [optional] 
**description** | **str** | Description of Invoice | [optional] 
**invoice_items** | [**list[InvoiceItemModel]**](InvoiceItemModel.md) |  | [optional] 
**invoice_taxes** | [**list[InvoiceTaxModel]**](InvoiceTaxModel.md) | Taxes applied on Invoice | 
**current_site** | **int** | Users current site | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

