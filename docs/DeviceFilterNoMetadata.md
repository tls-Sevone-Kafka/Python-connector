# DeviceFilterNoMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **list[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**names** | **list[str]** |  | [optional] 
**alternate_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**ip_addresses** | **list[str]** |  | [optional] 
**peer_ids** | **list[int]** |  | [optional] 
**timezone** | **str** |  | [optional] 
**workhours_group_id** | **int** |  | [optional] 
**snmp_version** | **int** |  | [optional] 
**poll_frequency** | **int** |  | [optional] 
**disable_polling** | **bool** |  | [optional] 
**disable_concurrent_polling** | **bool** |  | [optional] 
**disable_thresholding** | **bool** |  | [optional] 
**in_device_group_ids** | **list[int]** |  | [optional] 
**not_in_device_group_ids** | **list[int]** |  | [optional] 
**plugin_manager_id** | **int** |  | [optional] 
**allow_delete** | **bool** |  | [optional] 
**num_elements** | **int** |  | [optional] 
**is_queued_for_deletion** | **bool** |  | [optional] 
**metadata** | **dict(str, str)** | Key-value pair, the key is namespaceName.attributeName, e.g. {system}.sysName | [optional] 
**plugins** | [**list[PluginFilterDtoNoMetadata]**](PluginFilterDtoNoMetadata.md) |  | [optional] 
**new** | **bool** |  | [optional] 
**deleted** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

