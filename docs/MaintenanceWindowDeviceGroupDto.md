# MaintenanceWindowDeviceGroupDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [default to 'Maintenance window UUID -- omit to auto-generate for POST or leave unchanged for PUT']
**name** | **str** |  | [default to 'Name of maintenance window -- must be unique']
**notes** | **str** |  | [optional] [default to 'Free form notes']
**maintenance_type** | **str** |  | [optional] [default to 'Type of maintenance window']
**schedule_instance** | [**ScheduleInstanceDto**](ScheduleInstanceDto.md) |  | 
**actions** | **str** |  | [optional] [default to 'List of actions for this maintenance window -- SUPPRESS_ALERT_NOTIFICATIONS (SevOne will not send notification emails or traps for alerts occurring during this maintenance window), CATEGORIZE_ALERTS (Prepend 'Maintenance Window' to alerts overlapping this maintenance window and downgrade severity levels higher than Info), EXCLUDE_DATA_FROM_BASELINES (Exclude data during the maintenance window from baseline calculations), EXCLUDE_DATA_FROM_AGGREGATION (Exclude data during the maintenance window from aggregation calculations)']
**mapped_entities** | [**list[MappedDeviceGroupEntityDto]**](MappedDeviceGroupEntityDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

