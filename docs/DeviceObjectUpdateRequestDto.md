# DeviceObjectUpdateRequestDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**subtype_id** | **int** |  | [optional] 
**name** | **str** |  | 
**alternate_name** | **str** |  | [optional] 
**description** | **str** |  | 
**is_enabled** | **bool** | This field is deprecated and would be removed in a newer version of the API. Please use &#x27;enabled&#x27; field instead. When &#x27;enabled&#x27; is also sent, &#x27;isEnabled&#x27; will be ignored. | [optional] 
**enabled** | **str** |  | [optional] 
**is_visible** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] [default to False]
**poll_frequency** | **int** |  | 
**indicators** | [**list[IndicatorRequestDto]**](IndicatorRequestDto.md) |  | [optional] 
**extended_info** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

