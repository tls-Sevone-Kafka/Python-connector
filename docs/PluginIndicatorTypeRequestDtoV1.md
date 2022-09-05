# PluginIndicatorTypeRequestDtoV1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**plugin_object_type_id** | **int** |  | [optional] 
**is_enabled** | **bool** |  | 
**is_default** | **bool** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**allow_maximum_value** | **bool** |  | [optional] 
**data_units** | **str** |  | [optional] 
**display_units** | **str** |  | [optional] 
**synthetic_expression** | **str** |  | [optional] 
**synthetic_maximum_expression** | **str** |  | [optional] 
**extended_info** | **dict(str, dict(str, str))** | {number : {string: string}}, where the number value is pluginId surrounded with quotes and value is object retrieved from schema endpoint | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

