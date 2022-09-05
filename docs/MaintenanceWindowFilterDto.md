# MaintenanceWindowFilterDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [default to 'Match maintenance windows whose name contains this substring']
**device_ids** | **list[int]** |  | [optional] 
**actions** | **str** |  | [optional] [default to 'Match maintenance window with any of these actions -- SUPPRESS_ALERT_NOTIFICATIONS (SevOne will not send notification emails or traps for alerts occurring during this maintenance window), CATEGORIZE_ALERTS (Prepend 'Maintenance Window' to alerts overlapping this maintenance window and downgrade severity levels higher than Info), EXCLUDE_DATA_FROM_BASELINES (Exclude data during the maintenance window from baseline calculations), EXCLUDE_DATA_FROM_AGGREGATION (Exclude data during the maintenance window from aggregation calculations)']
**is_retroactive** | **bool** |  | [optional] [default to False]
**end_date_before** | **str** |  | [optional] [default to 'Match maintenance windows ending before this time']
**end_date_after** | **str** |  | [optional] [default to 'Match maintenance windows ending after this time']
**begin_date_before** | **str** |  | [optional] [default to 'Match maintenance windows beginning before this time']
**begin_date_after** | **str** |  | [optional] [default to 'Match maintenance windows beginning after this time']
**create_date_before** | **str** |  | [optional] [default to 'Match maintenance windows created before this time']
**create_date_after** | **str** |  | [optional] [default to 'Match maintenance windows created after this time']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

