# swagger_client.TopologyApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_constraint**](TopologyApi.md#create_constraint) | **POST** /api/v2/topology/constraints | Create constraint
[**create_topology_link**](TopologyApi.md#create_topology_link) | **POST** /api/v2/topology/links | Create topology link
[**delete_constraint_by_id**](TopologyApi.md#delete_constraint_by_id) | **DELETE** /api/v2/topology/constraints/{id} | Delete constraint
[**delete_topology_full_link**](TopologyApi.md#delete_topology_full_link) | **DELETE** /api/v2/topology/links/{connectionId} | Delete topology full link
[**delete_topology_half_link**](TopologyApi.md#delete_topology_half_link) | **DELETE** /api/v2/topology/links/{connectionId}/halflinks/{deviceId} | Delete topology link
[**filter_topology_links**](TopologyApi.md#filter_topology_links) | **POST** /api/v2/topology/filter | Filter topology links
[**get_constraint**](TopologyApi.md#get_constraint) | **GET** /api/v2/topology/constraints/{id} | Get constraint
[**get_constraints**](TopologyApi.md#get_constraints) | **GET** /api/v2/topology/constraints | Get constraints
[**get_topology_full_link**](TopologyApi.md#get_topology_full_link) | **GET** /api/v2/topology/links/{connectionId} | Get topology full link
[**get_topology_full_link_by_device_id**](TopologyApi.md#get_topology_full_link_by_device_id) | **GET** /api/v2/topology/devices/{deviceId}/links | Get topology full link by device id
[**update_constraint_by_id**](TopologyApi.md#update_constraint_by_id) | **PUT** /api/v2/topology/constraints/{id} | Update constraint

# **create_constraint**
> ConstraintDto create_constraint(body)

Create constraint

Create the relationship constraint for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
body = swagger_client.ConstraintDto() # ConstraintDto | 

try:
    # Create constraint
    api_response = api_instance.create_constraint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->create_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConstraintDto**](ConstraintDto.md)|  | 

### Return type

[**ConstraintDto**](ConstraintDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_topology_link**
> CreateLinkData create_topology_link(body)

Create topology link

Create topology link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
body = swagger_client.CreateLinkData() # CreateLinkData | 

try:
    # Create topology link
    api_response = api_instance.create_topology_link(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->create_topology_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLinkData**](CreateLinkData.md)|  | 

### Return type

[**CreateLinkData**](CreateLinkData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_constraint_by_id**
> str delete_constraint_by_id(id)

Delete constraint

Deletes the relationship constraint for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
id = 789 # int | The id of the Constraint to be deleted

try:
    # Delete constraint
    api_response = api_instance.delete_constraint_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_constraint_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the Constraint to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology_full_link**
> str delete_topology_full_link(connection_id)

Delete topology full link

Delete topology full link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
connection_id = 789 # int | connectionId

try:
    # Delete topology full link
    api_response = api_instance.delete_topology_full_link(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_topology_full_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| connectionId | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology_half_link**
> str delete_topology_half_link(connection_id, device_id)

Delete topology link

Delete topology half link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
connection_id = 789 # int | connectionId
device_id = 789 # int | deviceId

try:
    # Delete topology link
    api_response = api_instance.delete_topology_half_link(connection_id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_topology_half_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| connectionId | 
 **device_id** | **int**| deviceId | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_topology_links**
> PagerLinkData filter_topology_links(body)

Filter topology links

Endpoint for filtering topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
body = swagger_client.TopologyFilterBody() # TopologyFilterBody | 

try:
    # Filter topology links
    api_response = api_instance.filter_topology_links(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->filter_topology_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TopologyFilterBody**](TopologyFilterBody.md)|  | 

### Return type

[**PagerLinkData**](PagerLinkData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constraint**
> ConstraintDto get_constraint(id)

Get constraint

Get the relationship constraint for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
id = 789 # int | Constraint Id

try:
    # Get constraint
    api_response = api_instance.get_constraint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Constraint Id | 

### Return type

[**ConstraintDto**](ConstraintDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constraints**
> PagerConstraintDto get_constraints(options)

Get constraints

Get the relationship constraints for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get constraints
    api_response = api_instance.get_constraints(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_constraints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerConstraintDto**](PagerConstraintDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_full_link**
> list[LinkData] get_topology_full_link(connection_id)

Get topology full link

Get topology full link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
connection_id = 789 # int | connectionId

try:
    # Get topology full link
    api_response = api_instance.get_topology_full_link(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_topology_full_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| connectionId | 

### Return type

[**list[LinkData]**](LinkData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_full_link_by_device_id**
> list[LinkData] get_topology_full_link_by_device_id(device_id)

Get topology full link by device id

Get topology full link by device id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
device_id = 789 # int | deviceId

try:
    # Get topology full link by device id
    api_response = api_instance.get_topology_full_link_by_device_id(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_topology_full_link_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| deviceId | 

### Return type

[**list[LinkData]**](LinkData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_constraint_by_id**
> ConstraintDto update_constraint_by_id(body, id)

Update constraint

Update the relationship constraint for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
body = swagger_client.ConstraintDto() # ConstraintDto | 
id = 789 # int | The id of the Constraint to be updated

try:
    # Update constraint
    api_response = api_instance.update_constraint_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->update_constraint_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConstraintDto**](ConstraintDto.md)|  | 
 **id** | **int**| The id of the Constraint to be updated | 

### Return type

[**ConstraintDto**](ConstraintDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

