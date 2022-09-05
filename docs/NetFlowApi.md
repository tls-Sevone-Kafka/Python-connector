# swagger_client.NetFlowApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](NetFlowApi.md#create_application) | **POST** /api/v2/netflow/services | Create application
[**create_device_mappings**](NetFlowApi.md#create_device_mappings) | **POST** /api/v2/netflow/deviceMappings | Create device mapping
[**create_filter**](NetFlowApi.md#create_filter) | **POST** /api/v2/netflow/filters | Create Netflow filters
[**create_filter_entities**](NetFlowApi.md#create_filter_entities) | **POST** /api/v2/netflow/filters/{id}/rules | Create Netflow filters rules
[**create_mappings**](NetFlowApi.md#create_mappings) | **POST** /api/v2/netflow/objectMappings | Create object mapping
[**create_service_profile**](NetFlowApi.md#create_service_profile) | **POST** /api/v2/netflow/serviceProfiles | Create service profile
[**create_subnet**](NetFlowApi.md#create_subnet) | **POST** /api/v2/netflow/segments/{id}/subnets | Create subnet
[**create_subnet_category**](NetFlowApi.md#create_subnet_category) | **POST** /api/v2/netflow/segments | Create Network Segment
[**delet_subnet_by_id**](NetFlowApi.md#delet_subnet_by_id) | **DELETE** /api/v2/netflow/segments/subnets/{id} | Delete subnet
[**delet_subnet_category_by_id**](NetFlowApi.md#delet_subnet_category_by_id) | **DELETE** /api/v2/netflow/segments/{id} | Delete Network Segment
[**delete_application**](NetFlowApi.md#delete_application) | **DELETE** /api/v2/netflow/services/{id} | Delete application
[**delete_device_mapping_by_id**](NetFlowApi.md#delete_device_mapping_by_id) | **DELETE** /api/v2/netflow/deviceMappings/{mappingId} | Delete Device Mapping by Id
[**delete_filter**](NetFlowApi.md#delete_filter) | **DELETE** /api/v2/netflow/filters/{id} | Delete Netflow filter
[**delete_filter_entity**](NetFlowApi.md#delete_filter_entity) | **DELETE** /api/v2/netflow/filters/{id}/rules/{ruleId} | Delete Netflow filter rule
[**delete_interface**](NetFlowApi.md#delete_interface) | **DELETE** /api/v2/netflow/devices/{netflowDeviceId}/interfaces/{netFlowInterfaceId} | Delete interface by deviceId, interfaceId, direction.
[**delete_object_mapping_by_id**](NetFlowApi.md#delete_object_mapping_by_id) | **DELETE** /api/v2/netflow/objectMappings/{id} | Delete Object Mapping by Id
[**delete_service_profile**](NetFlowApi.md#delete_service_profile) | **DELETE** /api/v2/netflow/serviceProfiles/{id} | Delete service profile
[**filter_net_flow_device_interfaces**](NetFlowApi.md#filter_net_flow_device_interfaces) | **POST** /api/v2/netflow/devices/interfaces/filter | Get NetFlow device interfaces
[**filter_net_flow_devices**](NetFlowApi.md#filter_net_flow_devices) | **POST** /api/v2/netflow/devices/filter | Get all NetFlow devices
[**filter_netflow_fields**](NetFlowApi.md#filter_netflow_fields) | **POST** /api/v2/netflow/fields/filter | Filter netflow fields
[**filter_netflow_views**](NetFlowApi.md#filter_netflow_views) | **POST** /api/v2/netflow/views/filter | Filter views
[**filter_view_indicators**](NetFlowApi.md#filter_view_indicators) | **POST** /api/v2/netflow/views/{viewId}/fields/filter | Filter netflow view fields
[**get_device_mappings**](NetFlowApi.md#get_device_mappings) | **GET** /api/v2/netflow/deviceMappings | Get flow interface to device mappings
[**get_directions**](NetFlowApi.md#get_directions) | **GET** /api/v2/netflow/devices/{netflowDeviceId}/interfaces/{interfaceId}/directions | Get directions by NetFlow device id and interface id
[**get_filter_by_id**](NetFlowApi.md#get_filter_by_id) | **GET** /api/v2/netflow/filters/{id} | Get Netflow filters
[**get_filter_entities_by_id**](NetFlowApi.md#get_filter_entities_by_id) | **GET** /api/v2/netflow/filters/{id}/rules | Get Netflow filter rules
[**get_filters**](NetFlowApi.md#get_filters) | **GET** /api/v2/netflow/filters | Get Netflow filters
[**get_interfaces**](NetFlowApi.md#get_interfaces) | **GET** /api/v2/netflow/devices/{netflowDeviceId}/interfaces | Get interfaces by NetFlow device id
[**get_mapping_by_indicator**](NetFlowApi.md#get_mapping_by_indicator) | **POST** /api/v2/netflow/objectMappings/filterByIndicator | Get flow interface to device indicator mapping by indicators
[**get_mapping_by_interfaces**](NetFlowApi.md#get_mapping_by_interfaces) | **POST** /api/v2/netflow/objectMappings/filterByInterface | Get flow interface to device indicator mapping by interface
[**get_mappings**](NetFlowApi.md#get_mappings) | **GET** /api/v2/netflow/objectMappings | Get flow interface to device indicator mappings
[**get_net_flow_devices**](NetFlowApi.md#get_net_flow_devices) | **GET** /api/v2/netflow/devices | Get all NetFlow devices
[**get_net_flow_modes**](NetFlowApi.md#get_net_flow_modes) | **GET** /api/v2/netflow/settings | Get the status of NetFlow settings
[**get_netflow_categories**](NetFlowApi.md#get_netflow_categories) | **GET** /api/v2/netflow/views/categories | Get netflow view categories
[**get_netflow_fields**](NetFlowApi.md#get_netflow_fields) | **GET** /api/v2/netflow/fields | Get netflow fields
[**get_network_segments**](NetFlowApi.md#get_network_segments) | **GET** /api/v2/netflow/segments | Get Network Segments
[**get_protocols**](NetFlowApi.md#get_protocols) | **GET** /api/v2/netflow/protocols | Get protocols
[**get_report_columns**](NetFlowApi.md#get_report_columns) | **GET** /api/v2/netflow/views/{viewId}/reportColumns | 
[**get_service_profiles**](NetFlowApi.md#get_service_profiles) | **GET** /api/v2/netflow/serviceProfiles | Get service profiles
[**get_services_by_port**](NetFlowApi.md#get_services_by_port) | **GET** /api/v2/netflow/services | Get services by port
[**get_services_by_service_profile_id**](NetFlowApi.md#get_services_by_service_profile_id) | **GET** /api/v2/netflow/services/{serviceProfileId} | Get services by service profile Id
[**get_subnet_category_by_id**](NetFlowApi.md#get_subnet_category_by_id) | **GET** /api/v2/netflow/segments/{id} | Get Network Segment By Id
[**get_subnets**](NetFlowApi.md#get_subnets) | **GET** /api/v2/netflow/segments/subnets | Get subnets
[**get_subnets_by_category_id**](NetFlowApi.md#get_subnets_by_category_id) | **GET** /api/v2/netflow/segments/{id}/subnets | Get subnets
[**get_view_indicators**](NetFlowApi.md#get_view_indicators) | **GET** /api/v2/netflow/views/{viewId}/fields | Get the keys and metrics in a FlowFalcon view
[**get_views**](NetFlowApi.md#get_views) | **GET** /api/v2/netflow/views | Get views
[**update_application**](NetFlowApi.md#update_application) | **PATCH** /api/v2/netflow/services/{id} | Update application
[**update_device_mappings**](NetFlowApi.md#update_device_mappings) | **PATCH** /api/v2/netflow/deviceMappings/{mappingId} | Update device mapping
[**update_interface**](NetFlowApi.md#update_interface) | **PATCH** /api/v2/netflow/devices/{netflowDeviceId}/interfaces/{netFlowInterfaceId} | Update interface
[**update_service_profile**](NetFlowApi.md#update_service_profile) | **PATCH** /api/v2/netflow/serviceProfiles/{id} | Update service profile

# **create_application**
> NetFlowApplicationDto create_application(body)

Create application

Create application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowApplicationDto() # NetFlowApplicationDto | 

try:
    # Create application
    api_response = api_instance.create_application(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowApplicationDto**](NetFlowApplicationDto.md)|  | 

### Return type

[**NetFlowApplicationDto**](NetFlowApplicationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_mappings**
> NetFlowPluginMapDto create_device_mappings(body)

Create device mapping

Create device mapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowPluginMapDto() # NetFlowPluginMapDto | 

try:
    # Create device mapping
    api_response = api_instance.create_device_mappings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_device_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowPluginMapDto**](NetFlowPluginMapDto.md)|  | 

### Return type

[**NetFlowPluginMapDto**](NetFlowPluginMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_filter**
> NetFlowFilterDto create_filter(body)

Create Netflow filters

Create a netflow filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowFilterCreateDto() # NetFlowFilterCreateDto | 

try:
    # Create Netflow filters
    api_response = api_instance.create_filter(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowFilterCreateDto**](NetFlowFilterCreateDto.md)|  | 

### Return type

[**NetFlowFilterDto**](NetFlowFilterDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_filter_entities**
> NetFlowFilterEntityDto create_filter_entities(body, id)

Create Netflow filters rules

Create a netflow filter rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowFilterEntityCreateDto() # NetFlowFilterEntityCreateDto | 
id = 789 # int | Filter Id

try:
    # Create Netflow filters rules
    api_response = api_instance.create_filter_entities(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_filter_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowFilterEntityCreateDto**](NetFlowFilterEntityCreateDto.md)|  | 
 **id** | **int**| Filter Id | 

### Return type

[**NetFlowFilterEntityDto**](NetFlowFilterEntityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mappings**
> FlowDeviceMappingDto create_mappings(body)

Create object mapping

Create object mapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.FlowDeviceMappingDto() # FlowDeviceMappingDto | 

try:
    # Create object mapping
    api_response = api_instance.create_mappings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FlowDeviceMappingDto**](FlowDeviceMappingDto.md)|  | 

### Return type

[**FlowDeviceMappingDto**](FlowDeviceMappingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_profile**
> NetFlowServiceProfileDto create_service_profile(body)

Create service profile

Create service profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowServiceProfileDto() # NetFlowServiceProfileDto | 

try:
    # Create service profile
    api_response = api_instance.create_service_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_service_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowServiceProfileDto**](NetFlowServiceProfileDto.md)|  | 

### Return type

[**NetFlowServiceProfileDto**](NetFlowServiceProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subnet**
> NetFlowSubnetDto create_subnet(body, id)

Create subnet

Create a subnet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowSubnetCreateDto() # NetFlowSubnetCreateDto | 
id = 789 # int | Segment Id

try:
    # Create subnet
    api_response = api_instance.create_subnet(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowSubnetCreateDto**](NetFlowSubnetCreateDto.md)|  | 
 **id** | **int**| Segment Id | 

### Return type

[**NetFlowSubnetDto**](NetFlowSubnetDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subnet_category**
> NetFlowSubnetCategoryDto create_subnet_category(body)

Create Network Segment

Create a Network Segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowSubnetCategoryCreateDto() # NetFlowSubnetCategoryCreateDto | 

try:
    # Create Network Segment
    api_response = api_instance.create_subnet_category(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_subnet_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowSubnetCategoryCreateDto**](NetFlowSubnetCategoryCreateDto.md)|  | 

### Return type

[**NetFlowSubnetCategoryDto**](NetFlowSubnetCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delet_subnet_by_id**
> str delet_subnet_by_id(id)

Delete subnet

Deletes an existing subnet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the subnet to be deleted

try:
    # Delete subnet
    api_response = api_instance.delet_subnet_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delet_subnet_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the subnet to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delet_subnet_category_by_id**
> str delet_subnet_category_by_id(id)

Delete Network Segment

Deletes an existing Network Segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the segment to be deleted

try:
    # Delete Network Segment
    api_response = api_instance.delet_subnet_category_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delet_subnet_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the segment to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> NetFlowApplicationDto delete_application(id)

Delete application

Delete application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 56 # int | Application id

try:
    # Delete application
    api_response = api_instance.delete_application(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Application id | 

### Return type

[**NetFlowApplicationDto**](NetFlowApplicationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_mapping_by_id**
> str delete_device_mapping_by_id(mapping_id)

Delete Device Mapping by Id

Deletes an existing Device mapping 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
mapping_id = 789 # int | The id of the the device mapping to be deleted

try:
    # Delete Device Mapping by Id
    api_response = api_instance.delete_device_mapping_by_id(mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_device_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| The id of the the device mapping to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter**
> str delete_filter(id)

Delete Netflow filter

Deletes an existing netflow filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the filter to be deleted

try:
    # Delete Netflow filter
    api_response = api_instance.delete_filter(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the filter to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter_entity**
> str delete_filter_entity(id, rule_id)

Delete Netflow filter rule

Deletes an existing netflow filter rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the filter that has the rule
rule_id = 789 # int | The id of the filter rule to be deleted

try:
    # Delete Netflow filter rule
    api_response = api_instance.delete_filter_entity(id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_filter_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the filter that has the rule | 
 **rule_id** | **int**| The id of the filter rule to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_interface**
> str delete_interface(netflow_device_id, net_flow_interface_id, direction)

Delete interface by deviceId, interfaceId, direction.

Deletes an existing interface

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
netflow_device_id = 789 # int | netflowDeviceId
net_flow_interface_id = 789 # int | The id of the interface to be deleted
direction = 789 # int | direction. 1 for Incoming, 2 for Outgoing

try:
    # Delete interface by deviceId, interfaceId, direction.
    api_response = api_instance.delete_interface(netflow_device_id, net_flow_interface_id, direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netflow_device_id** | **int**| netflowDeviceId | 
 **net_flow_interface_id** | **int**| The id of the interface to be deleted | 
 **direction** | **int**| direction. 1 for Incoming, 2 for Outgoing | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_mapping_by_id**
> str delete_object_mapping_by_id(id)

Delete Object Mapping by Id

Deletes an existing Object mapping 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the the object mapping to be deleted

try:
    # Delete Object Mapping by Id
    api_response = api_instance.delete_object_mapping_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_object_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the the object mapping to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_profile**
> NetFlowServiceProfileDto delete_service_profile(id)

Delete service profile

Delete service profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 56 # int | Service profile id

try:
    # Delete service profile
    api_response = api_instance.delete_service_profile(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_service_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Service profile id | 

### Return type

[**NetFlowServiceProfileDto**](NetFlowServiceProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_net_flow_device_interfaces**
> PagerNetFlowInterfaceDto filter_net_flow_device_interfaces(body)

Get NetFlow device interfaces

Endpoint for retrieving all NetFlow device interfaces that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.InterfacesFilterBody() # InterfacesFilterBody | 

try:
    # Get NetFlow device interfaces
    api_response = api_instance.filter_net_flow_device_interfaces(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_net_flow_device_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterfacesFilterBody**](InterfacesFilterBody.md)|  | 

### Return type

[**PagerNetFlowInterfaceDto**](PagerNetFlowInterfaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_net_flow_devices**
> PagerNetFlowDeviceDto filter_net_flow_devices(body)

Get all NetFlow devices

Endpoint for retrieving all NetFlow devices that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.DevicesFilterBody() # DevicesFilterBody | 

try:
    # Get all NetFlow devices
    api_response = api_instance.filter_net_flow_devices(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_net_flow_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesFilterBody**](DevicesFilterBody.md)|  | 

### Return type

[**PagerNetFlowDeviceDto**](PagerNetFlowDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_netflow_fields**
> PagerNetFlowFieldDto filter_netflow_fields(body)

Filter netflow fields

Filter netflow fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.FieldsFilterBody1() # FieldsFilterBody1 | 

try:
    # Filter netflow fields
    api_response = api_instance.filter_netflow_fields(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_netflow_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FieldsFilterBody1**](FieldsFilterBody1.md)|  | 

### Return type

[**PagerNetFlowFieldDto**](PagerNetFlowFieldDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_netflow_views**
> PagerNetFlowAggregationTemplateDto filter_netflow_views(body)

Filter views

Filter netflow views

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.ViewsFilterBody() # ViewsFilterBody | 

try:
    # Filter views
    api_response = api_instance.filter_netflow_views(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_netflow_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ViewsFilterBody**](ViewsFilterBody.md)|  | 

### Return type

[**PagerNetFlowAggregationTemplateDto**](PagerNetFlowAggregationTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_view_indicators**
> PagerNetFlowFieldDto filter_view_indicators(body, view_id)

Filter netflow view fields

Filter netflow view fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.FieldsFilterBody() # FieldsFilterBody | 
view_id = 789 # int | 

try:
    # Filter netflow view fields
    api_response = api_instance.filter_view_indicators(body, view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_view_indicators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FieldsFilterBody**](FieldsFilterBody.md)|  | 
 **view_id** | **int**|  | 

### Return type

[**PagerNetFlowFieldDto**](PagerNetFlowFieldDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_mappings**
> PagerNetFlowPluginMapDto get_device_mappings(options, include_automatic=include_automatic)

Get flow interface to device mappings

Get flow interface to device mappings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
include_automatic = false # bool | Include automatic mappings (optional) (default to false)

try:
    # Get flow interface to device mappings
    api_response = api_instance.get_device_mappings(options, include_automatic=include_automatic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_device_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **include_automatic** | **bool**| Include automatic mappings | [optional] [default to false]

### Return type

[**PagerNetFlowPluginMapDto**](PagerNetFlowPluginMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directions**
> list[NetFlowDirectionDto] get_directions(netflow_device_id, interface_id)

Get directions by NetFlow device id and interface id

Get directions by NetFlow device id and interface id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
netflow_device_id = 789 # int | netflowDeviceId
interface_id = 789 # int | interfaceId

try:
    # Get directions by NetFlow device id and interface id
    api_response = api_instance.get_directions(netflow_device_id, interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_directions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netflow_device_id** | **int**| netflowDeviceId | 
 **interface_id** | **int**| interfaceId | 

### Return type

[**list[NetFlowDirectionDto]**](NetFlowDirectionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter_by_id**
> list[NetFlowFilterDto] get_filter_by_id(id)

Get Netflow filters

Get filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | Filter Id

try:
    # Get Netflow filters
    api_response = api_instance.get_filter_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_filter_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Filter Id | 

### Return type

[**list[NetFlowFilterDto]**](NetFlowFilterDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter_entities_by_id**
> list[NetFlowFilterEntityDto] get_filter_entities_by_id(id)

Get Netflow filter rules

Get filters rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | Filter Id

try:
    # Get Netflow filter rules
    api_response = api_instance.get_filter_entities_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_filter_entities_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Filter Id | 

### Return type

[**list[NetFlowFilterEntityDto]**](NetFlowFilterEntityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filters**
> list[NetFlowFilterDto] get_filters()

Get Netflow filters

Get filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get Netflow filters
    api_response = api_instance.get_filters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_filters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetFlowFilterDto]**](NetFlowFilterDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interfaces**
> list[NetFlowInterfaceDto] get_interfaces(netflow_device_id)

Get interfaces by NetFlow device id

Get interfaces by NetFlow device id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
netflow_device_id = 789 # int | netflowDeviceId

try:
    # Get interfaces by NetFlow device id
    api_response = api_instance.get_interfaces(netflow_device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netflow_device_id** | **int**| netflowDeviceId | 

### Return type

[**list[NetFlowInterfaceDto]**](NetFlowInterfaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_by_indicator**
> PagerFlowDeviceMappingDto get_mapping_by_indicator(body, include_automatic=include_automatic)

Get flow interface to device indicator mapping by indicators

Get flow interface to device indicator mapping by indicators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.ObjectMappingsFilterByIndicatorBody() # ObjectMappingsFilterByIndicatorBody | 
include_automatic = false # bool | Include automatic mappings (optional) (default to false)

try:
    # Get flow interface to device indicator mapping by indicators
    api_response = api_instance.get_mapping_by_indicator(body, include_automatic=include_automatic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_mapping_by_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectMappingsFilterByIndicatorBody**](ObjectMappingsFilterByIndicatorBody.md)|  | 
 **include_automatic** | **bool**| Include automatic mappings | [optional] [default to false]

### Return type

[**PagerFlowDeviceMappingDto**](PagerFlowDeviceMappingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_by_interfaces**
> PagerFlowDeviceMappingDto get_mapping_by_interfaces(body, include_automatic=include_automatic)

Get flow interface to device indicator mapping by interface

Get flow interface to device indicator mapping by interfaces

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.ObjectMappingsFilterByInterfaceBody() # ObjectMappingsFilterByInterfaceBody | 
include_automatic = false # bool | Include automatic mappings (optional) (default to false)

try:
    # Get flow interface to device indicator mapping by interface
    api_response = api_instance.get_mapping_by_interfaces(body, include_automatic=include_automatic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_mapping_by_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectMappingsFilterByInterfaceBody**](ObjectMappingsFilterByInterfaceBody.md)|  | 
 **include_automatic** | **bool**| Include automatic mappings | [optional] [default to false]

### Return type

[**PagerFlowDeviceMappingDto**](PagerFlowDeviceMappingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mappings**
> PagerFlowDeviceMappingDto get_mappings(options, include_automatic=include_automatic)

Get flow interface to device indicator mappings

Get flow interface to device indicator mappings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
include_automatic = false # bool | Include automatic mappings (optional) (default to false)

try:
    # Get flow interface to device indicator mappings
    api_response = api_instance.get_mappings(options, include_automatic=include_automatic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **include_automatic** | **bool**| Include automatic mappings | [optional] [default to false]

### Return type

[**PagerFlowDeviceMappingDto**](PagerFlowDeviceMappingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_net_flow_devices**
> PagerNetFlowDeviceDto get_net_flow_devices(options)

Get all NetFlow devices

Endpoint for retrieving all NetFlow devices with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all NetFlow devices
    api_response = api_instance.get_net_flow_devices(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_net_flow_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerNetFlowDeviceDto**](PagerNetFlowDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_net_flow_modes**
> NetFlowModesDto get_net_flow_modes()

Get the status of NetFlow settings

Endpoint for retrieving the status of NetFlow settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get the status of NetFlow settings
    api_response = api_instance.get_net_flow_modes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_net_flow_modes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetFlowModesDto**](NetFlowModesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_categories**
> PagerNetFlowViewCategoryDto get_netflow_categories(options)

Get netflow view categories

Get netflow view categories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get netflow view categories
    api_response = api_instance.get_netflow_categories(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_netflow_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerNetFlowViewCategoryDto**](PagerNetFlowViewCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_fields**
> PagerNetFlowFieldDto get_netflow_fields(options)

Get netflow fields

Get netflow fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get netflow fields
    api_response = api_instance.get_netflow_fields(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_netflow_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerNetFlowFieldDto**](PagerNetFlowFieldDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_segments**
> list[NetFlowSubnetCategoryDto] get_network_segments(name=name)

Get Network Segments

Get Networks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
name = 'name_example' # str | Name (optional)

try:
    # Get Network Segments
    api_response = api_instance.get_network_segments(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_network_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | [optional] 

### Return type

[**list[NetFlowSubnetCategoryDto]**](NetFlowSubnetCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protocols**
> list[NetFlowProtocolDto] get_protocols()

Get protocols

Get protocols

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get protocols
    api_response = api_instance.get_protocols()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_protocols: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetFlowProtocolDto]**](NetFlowProtocolDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_columns**
> list[NetflowReportingColumnDto] get_report_columns(view_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
view_id = 789 # int | viewId

try:
    api_response = api_instance.get_report_columns(view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_report_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| viewId | 

### Return type

[**list[NetflowReportingColumnDto]**](NetflowReportingColumnDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_profiles**
> list[NetFlowServiceProfileDto] get_service_profiles()

Get service profiles

Get all service profiles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get service profiles
    api_response = api_instance.get_service_profiles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_service_profiles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetFlowServiceProfileDto]**](NetFlowServiceProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_by_port**
> list[NetFlowApplicationDto] get_services_by_port(port=port, protocol=protocol)

Get services by port

Get applications by port

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
port = 56 # int | Port (optional)
protocol = 56 # int | Protocol (optional)

try:
    # Get services by port
    api_response = api_instance.get_services_by_port(port=port, protocol=protocol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_services_by_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **int**| Port | [optional] 
 **protocol** | **int**| Protocol | [optional] 

### Return type

[**list[NetFlowApplicationDto]**](NetFlowApplicationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_by_service_profile_id**
> list[NetFlowApplicationDto] get_services_by_service_profile_id(service_profile_id)

Get services by service profile Id

Get applications by service profile Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
service_profile_id = 56 # int | Service Profile id

try:
    # Get services by service profile Id
    api_response = api_instance.get_services_by_service_profile_id(service_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_services_by_service_profile_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_profile_id** | **int**| Service Profile id | 

### Return type

[**list[NetFlowApplicationDto]**](NetFlowApplicationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnet_category_by_id**
> NetFlowSubnetCategoryDto get_subnet_category_by_id(id)

Get Network Segment By Id

et Network Segment By Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | Segment Id

try:
    # Get Network Segment By Id
    api_response = api_instance.get_subnet_category_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_subnet_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Segment Id | 

### Return type

[**NetFlowSubnetCategoryDto**](NetFlowSubnetCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnets**
> list[NetFlowSubnetDto] get_subnets()

Get subnets

Get subnets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get subnets
    api_response = api_instance.get_subnets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_subnets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetFlowSubnetDto]**](NetFlowSubnetDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnets_by_category_id**
> list[NetFlowSubnetDto] get_subnets_by_category_id(id)

Get subnets

Get subnets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | Segment Id

try:
    # Get subnets
    api_response = api_instance.get_subnets_by_category_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_subnets_by_category_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Segment Id | 

### Return type

[**list[NetFlowSubnetDto]**](NetFlowSubnetDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_indicators**
> FlowFalconViewIndicatorsDto get_view_indicators(view_id, include_members=include_members)

Get the keys and metrics in a FlowFalcon view

Endpoint for retrieving the keys and metrics in a FlowFalcon view

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
view_id = 789 # int | viewId
include_members = false # bool | Include members, defaults to false (optional) (default to false)

try:
    # Get the keys and metrics in a FlowFalcon view
    api_response = api_instance.get_view_indicators(view_id, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_view_indicators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| viewId | 
 **include_members** | **bool**| Include members, defaults to false | [optional] [default to false]

### Return type

[**FlowFalconViewIndicatorsDto**](FlowFalconViewIndicatorsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_views**
> PagerNetFlowAggregationTemplateDto get_views(options)

Get views

Get views

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get views
    api_response = api_instance.get_views(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerNetFlowAggregationTemplateDto**](PagerNetFlowAggregationTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> NetFlowApplicationDto update_application(body, id)

Update application

Update application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowApplicationDto() # NetFlowApplicationDto | 
id = 56 # int | Application id

try:
    # Update application
    api_response = api_instance.update_application(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowApplicationDto**](NetFlowApplicationDto.md)|  | 
 **id** | **int**| Application id | 

### Return type

[**NetFlowApplicationDto**](NetFlowApplicationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_mappings**
> NetFlowPluginMapDto update_device_mappings(body, mapping_id)

Update device mapping

Update device mapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowPluginMapDto() # NetFlowPluginMapDto | 
mapping_id = 789 # int | The id of the the device mapping to be updated

try:
    # Update device mapping
    api_response = api_instance.update_device_mappings(body, mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->update_device_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowPluginMapDto**](NetFlowPluginMapDto.md)|  | 
 **mapping_id** | **int**| The id of the the device mapping to be updated | 

### Return type

[**NetFlowPluginMapDto**](NetFlowPluginMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_interface**
> NetFlowInterfaceDto update_interface(body, netflow_device_id, net_flow_interface_id)

Update interface

Update interface

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowInterfaceDto() # NetFlowInterfaceDto | 
netflow_device_id = 789 # int | netflowDeviceId
net_flow_interface_id = 789 # int | The id of the interface to be deleted

try:
    # Update interface
    api_response = api_instance.update_interface(body, netflow_device_id, net_flow_interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->update_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowInterfaceDto**](NetFlowInterfaceDto.md)|  | 
 **netflow_device_id** | **int**| netflowDeviceId | 
 **net_flow_interface_id** | **int**| The id of the interface to be deleted | 

### Return type

[**NetFlowInterfaceDto**](NetFlowInterfaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_profile**
> NetFlowServiceProfileDto update_service_profile(body, id)

Update service profile

Update service profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
body = swagger_client.NetFlowServiceProfileDto() # NetFlowServiceProfileDto | 
id = 56 # int | Service profile id

try:
    # Update service profile
    api_response = api_instance.update_service_profile(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->update_service_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetFlowServiceProfileDto**](NetFlowServiceProfileDto.md)|  | 
 **id** | **int**| Service profile id | 

### Return type

[**NetFlowServiceProfileDto**](NetFlowServiceProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

