# PolicyDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | [Output Only] | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_device_group** | **bool** | Determines whether policy is associated with deviceGroup or objectGroup. | [optional] 
**group_id** | **int** | Deprecated. Use groupIdList instead. | [optional] 
**group_id_list** | **list[int]** | A list of group IDs associated with the policy. If groupIdList and groupId are both set, groupId is ignored. | [optional] 
**is_member_of_any** | **bool** |  | [optional] 
**plugin_id** | **int** |  | [optional] 
**object_type_id** | **int** |  | [optional] 
**object_sub_type_id** | **int** |  | [optional] 
**severity** | **int** |  | [optional] 
**trigger_expression** | **str** | Specify the criteria under which a triggered alert is generated for the policy. The criteria is defined in disjunctive normal form in which propositions are the id fields of PolicyConditionDto(s) in the &#x27;triggerConditions&#x27; field. We use &#x27;|&#x27; to denote the &#x27;or&#x27; relation and &#x27;,&#x27; to denote the &#x27;and&#x27; relation. For example, suppose that there are three conditions with ids 1,2 and 3, a triggerExpression &#x27;1,2|3&#x27; means that when either condition 1 and condition 2 hold or condition 3 hold, the policy alert is triggered. Index of triggerConditions starts from 1 | [optional] 
**clear_expression** | **str** | Specify the criteria under which a cleared alert is generated for the policy. The criteria is defined in disjunctive normal form in which propositions are the id fields of PolicyConditionDto(s) in the &#x27;clearConditions&#x27; field. We use &#x27;|&#x27; to denote the &#x27;or&#x27; relation and &#x27;,&#x27; to denote the &#x27;and&#x27; relation. For example, suppose that there are three conditions with ids 1,2 and 3, a clearExpression may be &#x27;1,2|3&#x27; means that when either condition 1 and condition 2 hold or condition 3 hold, the policy alert is cleared. Index of clearConditions starts from 1 | [optional] 
**user_enabled** | **int** |  | [optional] 
**mail_to** | **str** |  | [optional] 
**mail_once** | **bool** |  | [optional] 
**mail_period** | **int** |  | [optional] 
**last_updated** | **int** |  | [optional] 
**use_default_traps** | **bool** |  | [optional] 
**use_device_traps** | **bool** |  | [optional] 
**use_custom_traps** | **bool** |  | [optional] 
**trigger_message** | **str** |  | [optional] 
**clear_message** | **str** |  | [optional] 
**append_condition_messages** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**flow** | [**PolicyFlowDto**](PolicyFlowDto.md) |  | [optional] 
**trigger_conditions** | [**list[PolicyConditionDto]**](PolicyConditionDto.md) | For POST, Array of Policy conditions where isTrigger will be true. In triggerExpression, use array index reference as an ID of triggerCondition to make expression where ID of 1st triggerCondition is 1. For PUT, we don&#x27;t allow user to specify this field. | [optional] 
**clear_conditions** | [**list[PolicyConditionDto]**](PolicyConditionDto.md) | For POST, Array of Policy conditions where isTrigger will be false. In clearExpression, use array index reference as an ID of clearCondition to make expression where ID of 1st clearCondition is 1. For PUT, we don&#x27;t allow user to specify this field. | [optional] 
**folder_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

