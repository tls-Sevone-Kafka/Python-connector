# ThresholdConditionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | This field is [OUTPUT ONLY] in all cases except the following one: when a threshold is created, it is required to assign a value to it as a placeholder so that triggerExpression/clearExpression can refer to the condition. Once the threshold is created, both this field and triggerExpression/clearExpression are populated with the real id. | [optional] 
**threshold_id** | **int** | [Output Only] | [optional] 
**policy_id** | **int** | [Output Only] | [optional] 
**policy_condition_id** | **int** | [Output Only] | [optional] 
**device_id** | **int** |  | [optional] 
**plugin_id** | **int** |  | [optional] 
**object_id** | **int** |  | [optional] 
**poll_id** | **int** |  | [optional] 
**type** | **int** |  | [optional] 
**value** | **float** |  | [optional] 
**unit** | **str** |  | [optional] 
**comparison** | **int** |  | [optional] 
**aggregation** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**sigma_direction** | **int** |  | [optional] 
**value2** | **float** |  | [optional] 
**flow_dto** | [**ThresholdConditionFlowfalconDto**](ThresholdConditionFlowfalconDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

