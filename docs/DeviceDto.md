# DeviceDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**is_new** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**alternate_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**manual_ip** | **bool** |  | [optional] 
**peer_id** | **int** |  | [optional] 
**poll_frequency** | **int** |  | [optional] 
**date_added** | **int** | Unix timestamp with milliseconds proximity | [optional] 
**last_discovery** | **int** | Unix timestamp with milliseconds proximity | [optional] 
**allow_delete** | **bool** |  | [optional] 
**disable_polling** | **bool** |  | [optional] 
**disable_concurrent_polling** | **bool** |  | [optional] 
**disable_thresholding** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 
**workhours_group_id** | **int** |  | [optional] 
**num_elements** | **int** |  | [optional] 
**plugin_info** | [**dict(str, PluginInfoResponse)**](PluginInfoResponse.md) |  | [optional] 
**objects** | [**list[DeviceObjectDto]**](DeviceObjectDto.md) |  | [optional] 
**plugin_manager_id** | **int** |  | [optional] 
**is_queued_for_deletion** | **bool** |  | [optional] 
**queued_user** | **int** |  | [optional] 
**queued_time** | **int** |  | [optional] 
**ips_update_time** | **float** |  | [optional] 
**ips15min** | **float** |  | [optional] 
**ips1hour** | **float** |  | [optional] 
**ips2hour** | **float** |  | [optional] 
**ips6hour** | **float** |  | [optional] 
**ips24hour** | **float** |  | [optional] 
**ips7day** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

