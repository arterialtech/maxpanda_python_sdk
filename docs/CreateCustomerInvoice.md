# CreateCustomerInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Site Id of the Customer Invoice. Site Id can be found in your Maxpanda Site Index or Site API | 
**customer_id** | **int** | Id of the Customer. Customer Id can be found in your Maxpanda Customer Index or Customer API | 
**invoice_number** | **str** | Invoice Number of Customer Invoice | [optional] 
**archived** | **bool** |  | [optional] 
**invoice_date** | **datetime** | Date of Customer Invoice | 
**due_date** | **datetime** | Due date of Customer Invoice | [optional] 
**invoice_items** | [**list[CreateInvoiceItemModel]**](CreateInvoiceItemModel.md) | Details of Items of Customer Invoice | 
**invoice_taxes** | [**list[InvoiceTaxModel]**](InvoiceTaxModel.md) | Taxes applied on Customer Invoice | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

