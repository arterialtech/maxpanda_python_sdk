# Workorder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Site Id of the WorkOrder. Site Id can be found in your Maxpanda Site Index or Site API | 
**title** | **str** | Name or Title of the WorkOrder | 
**referenced_id** | **str** | Reference Id of the WorkOrder | [optional] 
**workorder_category_id** | **int** | Category Id of the WorkOrder. Category Id can be found in your Maxpanda Company WorkOrderCategory or WorkOrderCategory API | 
**workorder_priority_id** | **int** | Priority Id of the WorkOrder. Priotiy Id can be found in your Maxpanda Company WorkOrderPriority or WorkOrderPriority API | 
**short_description** | **str** | Short Description about the WorkOrder | [optional] 
**notes** | **str** | Notes for the Staff | [optional] 
**private_notes** | **str** | Private Notes | [optional] 
**comments** | **str** | Comments | [optional] 
**primary_contact** | **str** | Primary Contact Number | [optional] 
**alternate_contact** | **str** | Alternate Contact Number | [optional] 
**add_cc** | **str** | Add external Email Recipients | [optional] 
**enter_work_area** | **bool** | Allow to enter in Work Area. Enter boolean value. | 
**all_day_event** | **bool** | Is this an All day event | [optional] 
**start_date** | **datetime** | Date on which WorkOrder was Started | 
**due_date** | **datetime** | Due Date of WorkOrder | [optional] 
**completed_date** | **datetime** | Date on which WorkOrder was Completed | [optional] 
**closed_date** | **datetime** | Date on which WorkOrder was Closed | [optional] 
**customer_id** | **int** | Customer Id of the WorkOrder. Customer Id can be found in your Maxpanda Customer Index or Customer API | [optional] 
**building_group_id** | **int** | Building Group Id of the WorkOrder. Building Group Id can be found in your Maxpanda Company Building Group or Department API | [optional] 
**building_id** | **int** | Building Id of the WorkOrder. Building Id can be found in your Maxpanda Building Index or Buildings API | [optional] 
**locations_id** | **list[int]** | Location Id of the WorkOrder. Location Id can be found in your Maxpanda Location Index or Locations API | [optional] 
**assets_id** | **list[int]** | Asset Id of the WorkOrder. Asset Id can be found in your Maxpanda Asset Index or Assets API | [optional] 
**vendor_id** | **list[int]** | Vendor Id of the WorkOrder. Vendor Id can be found in your Maxpanda Vendor Index or Vendors API | [optional] 
**tasks_id** | **list[int]** | Task Id of the WorkOrder. Task Id can be found in your Maxpanda Task Index or Task API | [optional] 
**staffs_id** | **list[int]** | Staff Id of the WorkOrder. Staff Id can be found in your Maxpanda Users Index or Users API | [optional] 
**customer_invoices_id** | **list[int]** | Customer Invoice Id of the WorkOrder. Customer Invoice Id can be found in your Maxpanda Customer Invoice Index or Customer Invoices API | [optional] 
**vendor_invoices_id** | **list[int]** | Vendor Invoices Id of the WorkOrder. Vendor Invoices Id can be found in your Maxpanda Inventory Invoices Index or Vendor Invoices API | [optional] 
**work_order_part_refs** | [**list[WorkOrderPartsRef]**](WorkOrderPartsRef.md) | Part Id of the WorkOrder. Part Id can be found in your Maxpanda Part Index or Parts API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

