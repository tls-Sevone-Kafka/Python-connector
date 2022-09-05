# ThresholdDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | [Output Only] | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**device_id** | **int** | [Output Only] | [optional] 
**policy_id** | **int** | [Output Only] | [optional] 
**group_id** | **int** | [Output Only] | [optional] 
**severity** | **int** |  | [optional] 
**trigger_expression** | **str** | Specify the criteria under which a triggered alert is generated for the threshold. The criteria is defined in disjunctive normal form in which propositions are the id fields of ThresholdConditionDto(s) in the &#x27;triggerConditions&#x27; field. We use &#x27;|&#x27; to denote the &#x27;or&#x27; relation and &#x27;,&#x27; to denote the &#x27;and&#x27; relation. For example, suppose that there are three conditions with ids 1,2 and 3, a triggerExpression &#x27;1,2|3&#x27; means that when either condition 1 and condition 2 hold or condition 3 hold, the threshold alert is triggered. | [optional] 
**clear_expression** | **str** | Specify the criteria under which a cleared alert is generated for the threshold. The criteria is defined in disjunctive normal form in which propositions are the id fields of ThresholdConditionDto(s) in the &#x27;clearConditions&#x27; field. We use &#x27;|&#x27; to denote the &#x27;or&#x27; relation and &#x27;,&#x27; to denote the &#x27;and&#x27; relation. For example, suppose that there are three conditions with ids 1,2 and 3, a clearExpression may be &#x27;1,2|3&#x27; means that when either condition 1 and condition 2 hold or condition 3 hold, the threshold alert is cleared. | [optional] 
**user_enabled** | **int** |  | [optional] 
**policy_enabled** | **int** | [Output Only] | [optional] 
**mail_to** | **str** |  | [optional] 
**mail_once** | **bool** |  | [optional] 
**mail_period** | **int** |  | [optional] 
**last_updated** | **int** | Unix timestamp with milliseconds format | [optional] 
**use_default_traps** | **bool** |  | [optional] 
**use_device_traps** | **bool** |  | [optional] 
**use_custom_traps** | **bool** |  | [optional] 
**trigger_message** | **str** |  | [optional] 
**clear_message** | **str** |  | [optional] 
**append_condition_messages** | **bool** |  | [optional] 
**type** | **str** | [Output Only] | [optional] 
**peer_id** | **int** | [Output Only] | [optional] 
**flow_dto** | [**FlowDto**](FlowDto.md) |  | [optional] 
**trigger_conditions** | [**list[ThresholdConditionDto]**](ThresholdConditionDto.md) | Caveat: in order to do CRUD on trigger conditions of an existing threshold, use the /flow/{deviceId}/{thresholdId}/{triggerType}/conditions endpoints. The &#x27;PUT /flow/{deviceId}/{thresholdId}&#x27; endpoint does not update trigger conditions for an existing threshold | [optional] 
**clear_conditions** | [**list[ThresholdConditionDto]**](ThresholdConditionDto.md) | Caveat: in order to do CRUD on clear conditions of an existing threshold, use the /flow/{deviceId}/{thresholdId}/{triggerType}/conditions endpoints. The &#x27;PUT /flow/{deviceId}/{thresholdId}&#x27; endpoint does not update clear conditions for an existing threshold | [optional] 
**absolute_times** | [**list[ThresholdAbsoluteTimeDto]**](ThresholdAbsoluteTimeDto.md) |  | [optional] 
**relative_times** | [**list[ThresholdRelativeTimeDto]**](ThresholdRelativeTimeDto.md) |  | [optional] 
**trap_destinations** | [**list[ThresholdTrapDestinationDto]**](ThresholdTrapDestinationDto.md) |  | [optional] 
**device_group** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

