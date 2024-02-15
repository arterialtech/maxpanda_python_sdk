# UpdatePartModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Site Id of the Part. Site Id can be found in your Maxpanda Site Index or Site API | 
**part_id** | **int** | Id of the Part. Part Id can be found in your Maxpanda Inventory Part Index or Part API | 
**part_name** | **str** | Name of the Part | 
**part_number** | **str** | Number associated with Part | [optional] 
**part_status_id** | **int** | Status of the Part. Part Status Id can be found in your Maxpanda Company Part Status or Part Status API | 
**part_type_id** | **int** | Type of the Part. Part Type Id can be found in your Maxpanda Company Part Type or Part Type API | 
**part_category_id** | **int** | Category of the Part. Part Category Id can be found in your Maxpanda Company Part Category or Part Category API | [optional] 
**manufracturer** | **str** | Part Manufracturer details | [optional] 
**model_name** | **str** | Part ModelName | [optional] 
**upc** | **str** | UPC details | [optional] 
**preferred_supplier_id** | **int** | Preferred Supplier of the Part. Supplier Id can be found in your Maxpanda Vendor Index or Vendor API | [optional] 
**oem1** | **str** | OEM 1 details | [optional] 
**oem2** | **str** | OEM 2 details | [optional] 
**oem3** | **str** | OEM 3 details | [optional] 
**preferred_oem1_supplier_id** | **int** | Preferred Supplier 1 for the Part. Supplier Id can be found in your Maxpanda Vendor Index or Vendor API | [optional] 
**preferred_oem2_supplier_id** | **int** | Preferred Supplier 2 for the Part. Supplier Id can be found in your Maxpanda Vendor Index or Vendor API | [optional] 
**preferred_oem3_supplier_id** | **int** | Preferred Supplier for the Part. Supplier Id can be found in your Maxpanda Vendor Index or Vendor API | [optional] 
**supplier_info** | **str** | Information of Supplier of Part. | [optional] 
**increase_qty** | **float** | Increase Quantity of Parts | [optional] 
**decrease_qty** | **float** | Descrease Quantity of Parts | [optional] 
**part_cost** | **float** | Cost of the Part | [optional] 
**sales_price** | **float** | Minimum number of Parts | [optional] 
**minimum_level** | **float** | Minimum number of Parts | [optional] 
**maximum_level** | **float** | Maximum number of Parts | [optional] 
**notes** | **str** | Notes about Part | [optional] 
**installation_date** | **datetime** | Date of Installation of Part | [optional] 
**warranty_date** | **datetime** | Warranty Date of Part | [optional] 
**warranty_notes_labour** | **str** | Warranty Notes for Labour | [optional] 
**warranty_notes_parts** | **str** | Warranty Notes for Part | [optional] 
**storage_location** | **int** | Storage location of Part. Location Id can be found in your Maxpanda Location Index or Location API | [optional] 
**assigned_asset** | **list[int]** | Part assigned to Assets. Asset Id can be found in your Maxpanda Asset Index or Asset API | [optional] 
**bin_parts_ref** | [**list[BinPartsRef]**](BinPartsRef.md) | Part assigned to Bins. | [optional] 
**purchase_order_template_id** | **int** | Purchase Order of Part. Purchase Order Id can be found in your Maxpanda Accounting Purchase Order Index or Purchase Order API | [optional] 
**is_frozen** | **bool** |  | [optional] 
**customer_warranty_start_date** | **datetime** | Customer Warranty Start Date | [optional] 
**customer_warranty_end_date** | **datetime** | Customer Warranty End Date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

