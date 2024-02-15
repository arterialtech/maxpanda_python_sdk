# UpdateAsset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **int** | Site Id of the Asset. Site Id can be found in your Maxpanda Site Index or Site API | 
**asset_id** | **int** | Id of the Asset. Asset Id can be found in your Maxpanda Asset Index or Assets API | 
**name** | **str** | Name of the Asset. | 
**description** | **str** | Description of Asset. | [optional] 
**model** | **str** | Model details of Asset | [optional] 
**asset_type_id** | **int** | Asset Type Id of the Asset. Asset Type Id can be found in your Maxpanda Company Asset Type Index or Asset Type Api | 
**asset_status_id** | **int** | Asset Status Id of the Asset. Asset Status Id can be found in your Maxpanda Company Asset Status Index or Asset Status Api | 
**asset_tag** | **str** | Tag details of the Asset. | [optional] 
**serial_number** | **str** | Serial Number of the Asset | [optional] 
**manufacturer** | **str** | Manufacturer details of the Asset. | [optional] 
**manufacturer_info** | **str** | Information of Manufacturer. | [optional] 
**preferred_vendor_id** | **int** | Id of Preferred Vendor for the Asset. Preferred Vendor Id can be found in your Maxpanda Vendor Index or Vendor Api | [optional] 
**vendor_info** | **str** | Information of Vendor. | [optional] 
**installation_date** | **datetime** | Installation date of Asset | [optional] 
**warranty_date** | **datetime** | Warrenty date of Asset | [optional] 
**warranty_notes_parts** | **str** | Warranty Notes for Parts | [optional] 
**warranty_notes_labor** | **str** | Warranty Notes for Labor | [optional] 
**add_cc** | **str** | Addition Email recievers | [optional] 
**notes** | **str** | Notes of the Asset | [optional] 
**ip_mac_address** | **str** | IP / Mac Address of the Asset | [optional] 
**is_mobile_asset** | **bool** | Assets which are movable or can be moved from one location to another are called Mobile Assets | [optional] 
**building_group_id** | **int** | Building group of the Asset. Building Group Id can be found in your Maxpanda company Building Group or Department Api | [optional] 
**building_id** | **int** | Building of the Asset. Building Id can be found in your Maxpanda Building index or Building Api | [optional] 
**location_id** | **int** | Location of the Asset. Location Id can be found in your Maxpanda Location index or Location Api | [optional] 
**assigned_user_id** | **int** | Currently assigned user of the Asset. User Id can be found in your Maxpanda User index or User Api | [optional] 
**purchase_cost** | **float** | Purchase cost of the Asset | [optional] 
**salvage_cost** | **float** | Salvage cost of the Asset | [optional] 
**useful_life_in_years** | **float** | Number of years this Asset can be used | [optional] 
**depreciation_rate** | **float** | Rate of Deprecation of the Asset | [optional] 
**parts_ids** | **list[int]** | Parts of the Asset. Parts Id can be found in your Maxpanda Inventory Part Index or Parts Api | [optional] 
**metering_ids** | **list[int]** | Metering type of the Asset. Metering Type Id can be found in your Maxpanda Company MeteringType or Metering Types Api | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

