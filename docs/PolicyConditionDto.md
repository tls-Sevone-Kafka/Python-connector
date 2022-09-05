# PolicyConditionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | For POST /policies, id is compulsory in triggerConditions and clearConditions. | [optional] 
**policy_id** | **int** |  | [optional] 
**indicator_type_id** | **int** |  | [optional] 
**type** | **int** |  | [optional] 
**is_trigger** | **bool** | isTrigger is READ-ONLY in all endpoints except POST /policies/{policyId}/conditions | [optional] 
**value** | **float** |  | [optional] 
**unit** | **str** |  | [optional] 
**comparison** | **int** |  | [optional] 
**aggregation** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**sigma_direction** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

