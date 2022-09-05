# DeviceObjectDtoNoMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**plugin_id** | **int** |  | [optional] 
**plugin_object_type_id** | **int** |  | [optional] 
**subtype_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**alternate_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **str** |  | [optional] 
**is_enabled** | **bool** | This field is deprecated and would be removed in a newer version of the API. Please use &#x27;enabled&#x27; field instead. | [optional] 
**is_visible** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**date_added** | **int** | Unix timestamp with milliseconds proximity | [optional] 
**indicators** | [**list[IndicatorDtoNoMetadata]**](IndicatorDtoNoMetadata.md) |  | [optional] 
**extended_info** | **dict(str, str)** |  | [optional] 
**disabled_by_ddq** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

