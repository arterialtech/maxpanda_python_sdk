# Customer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_ref** | [**list[SiteRef]**](SiteRef.md) | Site to which access is allowed for customer. | [optional] 
**customer_id** | **int** | Customer&#x27;s id. | [optional] 
**first_name** | **str** | First Name of the customer. | 
**last_name** | **str** | Last Name of the customer. | 
**company_name** | **str** | Name of the company to which customer belongs to. | [optional] 
**email** | **str** | Email address of customer. | 
**account_number** | **str** | Account # of the Customer | [optional] 
**contract_date** | **datetime** | Contract Date of the Customer | [optional] 
**min_weekly_hours** | **float** | Min Weekly Hours of the Customer | [optional] 
**max_weekly_hours** | **float** | Max Weekly Hours of the Customer | [optional] 
**total_hours** | **float** | Total Hours of the Customer | [optional] 
**phone** | **str** | Phone number of customer. | [optional] 
**mobile** | **str** | Mobile number of customer. | [optional] 
**notes** | **str** | Notes. | [optional] 
**billing_address** | [**Address**](Address.md) |  | [optional] 
**shipping_address** | [**Address**](Address.md) |  | [optional] 
**shipping_address_same_as_billing** | **bool** | If customer wants to have same address for Billing as well as Shipping. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

