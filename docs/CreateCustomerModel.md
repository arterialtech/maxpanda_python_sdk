# CreateCustomerModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sites_id** | **list[int]** | Site Ids of the Customer. Site Id can be found in your Maxpanda Site Index or Site API | 
**first_name** | **str** | First Name of the Customer | 
**last_name** | **str** | Last Name of the Customer | 
**email** | **str** | Email address of the Customer | 
**account_number** | **str** | Account # of the Customer | [optional] 
**contract_date** | **datetime** | Contract Date of the Customer | [optional] 
**min_weekly_hours** | **float** | Min Weekly Hours of the Customer | [optional] 
**max_weekly_hours** | **float** | Max Weekly Hours of the Customer | [optional] 
**total_hours** | **float** | Total Hours of the Customer | [optional] 
**company_name** | **str** | Phone number of customer. | [optional] 
**phone_number** | **str** | Phone Number of the Customer | [optional] 
**mobile_number** | **str** | Mobile Number of the Customer | [optional] 
**fax** | **str** | Fax Number of the Customer | [optional] 
**other** | **str** | Othe details of the Customer | [optional] 
**web_site** | **str** | Website address of the Customer | [optional] 
**notes** | **str** | Notes about the Customer | [optional] 
**billing_address** | [**APIAddressModel**](APIAddressModel.md) |  | [optional] 
**shipping_address_same_as_billing** | **bool** | Use Customers Billing address as Shipping Address | [optional] 
**shipping_address** | [**APIAddressModel**](APIAddressModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

