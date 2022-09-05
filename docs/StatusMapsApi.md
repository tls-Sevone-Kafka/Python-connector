# swagger_client.StatusMapsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](StatusMapsApi.md#create_connection) | **POST** /api/v2/maps/{id}/connections | Create connection
[**create_connection1**](StatusMapsApi.md#create_connection1) | **POST** /api/v1/maps/{id}/connections | Create connection
[**create_node**](StatusMapsApi.md#create_node) | **POST** /api/v2/maps/{id}/nodes | Create node
[**create_node1**](StatusMapsApi.md#create_node1) | **POST** /api/v1/maps/{id}/nodes | Create node
[**create_status_map**](StatusMapsApi.md#create_status_map) | **POST** /api/v1/maps | Create status map
[**create_status_map1**](StatusMapsApi.md#create_status_map1) | **POST** /api/v2/maps | Create status map
[**delete_connection_by_id**](StatusMapsApi.md#delete_connection_by_id) | **DELETE** /api/v2/maps/{id}/connections/{connectionId} | Delete connection from status map
[**delete_connection_by_id1**](StatusMapsApi.md#delete_connection_by_id1) | **DELETE** /api/v1/maps/{id}/connections/{connectionId} | Delete connection from status map
[**delete_node_by_id**](StatusMapsApi.md#delete_node_by_id) | **DELETE** /api/v2/maps/{id}/nodes/{nodeId} | Delete node from status map
[**delete_node_by_id1**](StatusMapsApi.md#delete_node_by_id1) | **DELETE** /api/v1/maps/{id}/nodes/{nodeId} | Delete node from status map
[**delete_status_map_by_id**](StatusMapsApi.md#delete_status_map_by_id) | **DELETE** /api/v1/maps/{id} | Delete status map
[**delete_status_map_by_id1**](StatusMapsApi.md#delete_status_map_by_id1) | **DELETE** /api/v2/maps/{id} | Delete status map
[**get_connection_alerts**](StatusMapsApi.md#get_connection_alerts) | **GET** /api/v1/maps/{id}/connection/{connectionId}/alerts | Get alerts for connection
[**get_connection_alerts1**](StatusMapsApi.md#get_connection_alerts1) | **GET** /api/v2/maps/{id}/connection/{connectionId}/alerts | Get alerts for connection
[**get_connections**](StatusMapsApi.md#get_connections) | **GET** /api/v2/maps/{id}/connections | Get connections by status map Id
[**get_connections1**](StatusMapsApi.md#get_connections1) | **GET** /api/v1/maps/{id}/connections | Get connections by status map Id
[**get_node_alerts**](StatusMapsApi.md#get_node_alerts) | **GET** /api/v1/maps/{id}/node/{nodeId}/alerts | Get alerts for node
[**get_node_alerts1**](StatusMapsApi.md#get_node_alerts1) | **GET** /api/v2/maps/{id}/node/{nodeId}/alerts | Get alerts for node
[**get_status_map_by_id**](StatusMapsApi.md#get_status_map_by_id) | **GET** /api/v1/maps/{id} | Get status map by Id
[**get_status_map_by_id1**](StatusMapsApi.md#get_status_map_by_id1) | **GET** /api/v2/maps/{id} | Get status map by Id
[**get_status_map_nodes**](StatusMapsApi.md#get_status_map_nodes) | **GET** /api/v2/maps/{id}/nodes | Get all nodes for a specific status map
[**get_status_map_nodes1**](StatusMapsApi.md#get_status_map_nodes1) | **GET** /api/v1/maps/{id}/nodes | Get all nodes for a specific status map
[**get_status_maps**](StatusMapsApi.md#get_status_maps) | **GET** /api/v1/maps | Get all status maps
[**get_status_maps1**](StatusMapsApi.md#get_status_maps1) | **GET** /api/v2/maps | Get all status maps
[**partially_update_status_map_by_id**](StatusMapsApi.md#partially_update_status_map_by_id) | **PATCH** /api/v1/maps/{id} | Partially update status map
[**partially_update_status_map_by_id1**](StatusMapsApi.md#partially_update_status_map_by_id1) | **PATCH** /api/v2/maps/{id} | Partially update status map
[**update_connection_by_status_map_id**](StatusMapsApi.md#update_connection_by_status_map_id) | **PUT** /api/v2/maps/{id}/connections/{connectionId} | Update connection
[**update_connection_by_status_map_id1**](StatusMapsApi.md#update_connection_by_status_map_id1) | **PUT** /api/v1/maps/{id}/connections/{connectionId} | Update connection
[**update_node_by_id**](StatusMapsApi.md#update_node_by_id) | **PUT** /api/v2/maps/{id}/nodes/{nodeId} | Update node
[**update_node_by_id1**](StatusMapsApi.md#update_node_by_id1) | **PUT** /api/v1/maps/{id}/nodes/{nodeId} | Update node
[**update_status_map_by_id**](StatusMapsApi.md#update_status_map_by_id) | **PUT** /api/v1/maps/{id} | Update status map
[**update_status_map_by_id1**](StatusMapsApi.md#update_status_map_by_id1) | **PUT** /api/v2/maps/{id} | Update status map

# **create_connection**
> ConnectionDto create_connection(body, id)

Create connection

Creates a new connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.ConnectionRequestDto() # ConnectionRequestDto | 
id = 789 # int | The id of the map

try:
    # Create connection
    api_response = api_instance.create_connection(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionRequestDto**](ConnectionRequestDto.md)|  | 
 **id** | **int**| The id of the map | 

### Return type

[**ConnectionDto**](ConnectionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection1**
> ConnectionDto create_connection1(body, id)

Create connection

Creates a new connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.ConnectionRequestDto() # ConnectionRequestDto | 
id = 789 # int | The id of the map

try:
    # Create connection
    api_response = api_instance.create_connection1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->create_connection1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionRequestDto**](ConnectionRequestDto.md)|  | 
 **id** | **int**| The id of the map | 

### Return type

[**ConnectionDto**](ConnectionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node**
> NodeDto create_node(body, id)

Create node

Creates a new node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.NodeRequestDto() # NodeRequestDto | 
id = 789 # int | The id of the map

try:
    # Create node
    api_response = api_instance.create_node(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->create_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeRequestDto**](NodeRequestDto.md)|  | 
 **id** | **int**| The id of the map | 

### Return type

[**NodeDto**](NodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node1**
> NodeDto create_node1(body, id)

Create node

Creates a new node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.NodeRequestDto() # NodeRequestDto | 
id = 789 # int | The id of the map

try:
    # Create node
    api_response = api_instance.create_node1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->create_node1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeRequestDto**](NodeRequestDto.md)|  | 
 **id** | **int**| The id of the map | 

### Return type

[**NodeDto**](NodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_status_map**
> StatusMapDto create_status_map(body)

Create status map

Creates a new status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.StatusMapRequestDto() # StatusMapRequestDto | 

try:
    # Create status map
    api_response = api_instance.create_status_map(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->create_status_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapRequestDto**](StatusMapRequestDto.md)|  | 

### Return type

[**StatusMapDto**](StatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_status_map1**
> StatusMapDto create_status_map1(body)

Create status map

Creates a new status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.StatusMapRequestDto() # StatusMapRequestDto | 

try:
    # Create status map
    api_response = api_instance.create_status_map1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->create_status_map1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapRequestDto**](StatusMapRequestDto.md)|  | 

### Return type

[**StatusMapDto**](StatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_by_id**
> str delete_connection_by_id(id, connection_id)

Delete connection from status map

Deletes an existing connection from existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
connection_id = 789 # int | The id of the connection

try:
    # Delete connection from status map
    api_response = api_instance.delete_connection_by_id(id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->delete_connection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **connection_id** | **int**| The id of the connection | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_by_id1**
> str delete_connection_by_id1(id, connection_id)

Delete connection from status map

Deletes an existing connection from existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
connection_id = 789 # int | The id of the connection

try:
    # Delete connection from status map
    api_response = api_instance.delete_connection_by_id1(id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->delete_connection_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **connection_id** | **int**| The id of the connection | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_by_id**
> str delete_node_by_id(id, node_id)

Delete node from status map

Deletes an existing node from existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
node_id = 789 # int | The id of the node

try:
    # Delete node from status map
    api_response = api_instance.delete_node_by_id(id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->delete_node_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **node_id** | **int**| The id of the node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_by_id1**
> str delete_node_by_id1(id, node_id)

Delete node from status map

Deletes an existing node from existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
node_id = 789 # int | The id of the node

try:
    # Delete node from status map
    api_response = api_instance.delete_node_by_id1(id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->delete_node_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **node_id** | **int**| The id of the node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_status_map_by_id**
> str delete_status_map_by_id(id)

Delete status map

Deletes an existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map to be deleted

try:
    # Delete status map
    api_response = api_instance.delete_status_map_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->delete_status_map_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_status_map_by_id1**
> str delete_status_map_by_id1(id)

Delete status map

Deletes an existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map to be deleted

try:
    # Delete status map
    api_response = api_instance.delete_status_map_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->delete_status_map_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_alerts**
> list[NodeAlert] get_connection_alerts(id, connection_id)

Get alerts for connection

Get all alerts for a given connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
connection_id = 789 # int | The id of the connection

try:
    # Get alerts for connection
    api_response = api_instance.get_connection_alerts(id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_connection_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **connection_id** | **int**| The id of the connection | 

### Return type

[**list[NodeAlert]**](NodeAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_alerts1**
> list[NodeAlert] get_connection_alerts1(id, connection_id)

Get alerts for connection

Get all alerts for a given connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
connection_id = 789 # int | The id of the connection

try:
    # Get alerts for connection
    api_response = api_instance.get_connection_alerts1(id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_connection_alerts1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **connection_id** | **int**| The id of the connection | 

### Return type

[**list[NodeAlert]**](NodeAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections**
> PagerConnectionDto get_connections(id, options)

Get connections by status map Id

Gets all existing connections for status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the requested status map
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get connections by status map Id
    api_response = api_instance.get_connections(id, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested status map | 
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerConnectionDto**](PagerConnectionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections1**
> PagerConnectionDto get_connections1(id, options)

Get connections by status map Id

Gets all existing connections for status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the requested status map
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get connections by status map Id
    api_response = api_instance.get_connections1(id, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_connections1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested status map | 
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerConnectionDto**](PagerConnectionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_alerts**
> list[NodeAlert] get_node_alerts(id, node_id)

Get alerts for node

Get all alerts for a given node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
node_id = 789 # int | The id of the node

try:
    # Get alerts for node
    api_response = api_instance.get_node_alerts(id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_node_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **node_id** | **int**| The id of the node | 

### Return type

[**list[NodeAlert]**](NodeAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_alerts1**
> list[NodeAlert] get_node_alerts1(id, node_id)

Get alerts for node

Get all alerts for a given node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
node_id = 789 # int | The id of the node

try:
    # Get alerts for node
    api_response = api_instance.get_node_alerts1(id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_node_alerts1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **node_id** | **int**| The id of the node | 

### Return type

[**list[NodeAlert]**](NodeAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_map_by_id**
> StatusMapDto get_status_map_by_id(id, include_members=include_members)

Get status map by Id

Gets a single status map object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the requested status map
include_members = false # bool | Include status map nodes/connections (optional) (default to false)

try:
    # Get status map by Id
    api_response = api_instance.get_status_map_by_id(id, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_status_map_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested status map | 
 **include_members** | **bool**| Include status map nodes/connections | [optional] [default to false]

### Return type

[**StatusMapDto**](StatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_map_by_id1**
> StatusMapDto get_status_map_by_id1(id, include_members=include_members)

Get status map by Id

Gets a single status map object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the requested status map
include_members = false # bool | Include status map nodes/connections (optional) (default to false)

try:
    # Get status map by Id
    api_response = api_instance.get_status_map_by_id1(id, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_status_map_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested status map | 
 **include_members** | **bool**| Include status map nodes/connections | [optional] [default to false]

### Return type

[**StatusMapDto**](StatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_map_nodes**
> PagerNodeDto get_status_map_nodes(id, options)

Get all nodes for a specific status map

Endpoint for retrieving all nodes for a specific status map, supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all nodes for a specific status map
    api_response = api_instance.get_status_map_nodes(id, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_status_map_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerNodeDto**](PagerNodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_map_nodes1**
> PagerNodeDto get_status_map_nodes1(id, options)

Get all nodes for a specific status map

Endpoint for retrieving all nodes for a specific status map, supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
id = 789 # int | The id of the map
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all nodes for a specific status map
    api_response = api_instance.get_status_map_nodes1(id, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_status_map_nodes1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the map | 
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerNodeDto**](PagerNodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_maps**
> PagerStatusMapDto get_status_maps(options, include_members=include_members)

Get all status maps

Endpoint for retrieving all status maps that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
include_members = false # bool | Include status map nodes/connections (optional) (default to false)

try:
    # Get all status maps
    api_response = api_instance.get_status_maps(options, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_status_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **include_members** | **bool**| Include status map nodes/connections | [optional] [default to false]

### Return type

[**PagerStatusMapDto**](PagerStatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_maps1**
> PagerStatusMapDto get_status_maps1(options, include_members=include_members)

Get all status maps

Endpoint for retrieving all status maps that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
include_members = false # bool | Include status map nodes/connections (optional) (default to false)

try:
    # Get all status maps
    api_response = api_instance.get_status_maps1(options, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->get_status_maps1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **include_members** | **bool**| Include status map nodes/connections | [optional] [default to false]

### Return type

[**PagerStatusMapDto**](PagerStatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_status_map_by_id**
> StatusMapDto partially_update_status_map_by_id(body, id)

Partially update status map

Updates an existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.StatusMapRequestDto() # StatusMapRequestDto | 
id = 789 # int | The id of the map to be updated

try:
    # Partially update status map
    api_response = api_instance.partially_update_status_map_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->partially_update_status_map_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapRequestDto**](StatusMapRequestDto.md)|  | 
 **id** | **int**| The id of the map to be updated | 

### Return type

[**StatusMapDto**](StatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_status_map_by_id1**
> StatusMapDto partially_update_status_map_by_id1(body, id)

Partially update status map

Updates an existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.StatusMapRequestDto() # StatusMapRequestDto | 
id = 789 # int | The id of the map to be updated

try:
    # Partially update status map
    api_response = api_instance.partially_update_status_map_by_id1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->partially_update_status_map_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapRequestDto**](StatusMapRequestDto.md)|  | 
 **id** | **int**| The id of the map to be updated | 

### Return type

[**StatusMapDto**](StatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection_by_status_map_id**
> ConnectionDto update_connection_by_status_map_id(body, id, connection_id)

Update connection

Update connection belonging to a status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.ConnectionRequestDto() # ConnectionRequestDto | 
id = 789 # int | The id of the map
connection_id = 789 # int | The id of the connection

try:
    # Update connection
    api_response = api_instance.update_connection_by_status_map_id(body, id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->update_connection_by_status_map_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionRequestDto**](ConnectionRequestDto.md)|  | 
 **id** | **int**| The id of the map | 
 **connection_id** | **int**| The id of the connection | 

### Return type

[**ConnectionDto**](ConnectionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection_by_status_map_id1**
> ConnectionDto update_connection_by_status_map_id1(body, id, connection_id)

Update connection

Update connection belonging to a status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.ConnectionRequestDto() # ConnectionRequestDto | 
id = 789 # int | The id of the map
connection_id = 789 # int | The id of the connection

try:
    # Update connection
    api_response = api_instance.update_connection_by_status_map_id1(body, id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->update_connection_by_status_map_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionRequestDto**](ConnectionRequestDto.md)|  | 
 **id** | **int**| The id of the map | 
 **connection_id** | **int**| The id of the connection | 

### Return type

[**ConnectionDto**](ConnectionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_by_id**
> NodeDto update_node_by_id(body, id, node_id)

Update node

Update node belonging to a status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.NodeRequestDto() # NodeRequestDto | 
id = 789 # int | The id of the map
node_id = 789 # int | The id of the node

try:
    # Update node
    api_response = api_instance.update_node_by_id(body, id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->update_node_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeRequestDto**](NodeRequestDto.md)|  | 
 **id** | **int**| The id of the map | 
 **node_id** | **int**| The id of the node | 

### Return type

[**NodeDto**](NodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_by_id1**
> NodeDto update_node_by_id1(body, id, node_id)

Update node

Update node belonging to a status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.NodeRequestDto() # NodeRequestDto | 
id = 789 # int | The id of the map
node_id = 789 # int | The id of the node

try:
    # Update node
    api_response = api_instance.update_node_by_id1(body, id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->update_node_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeRequestDto**](NodeRequestDto.md)|  | 
 **id** | **int**| The id of the map | 
 **node_id** | **int**| The id of the node | 

### Return type

[**NodeDto**](NodeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status_map_by_id**
> StatusMapDto update_status_map_by_id(body, id)

Update status map

Updates an existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.StatusMapRequestDto() # StatusMapRequestDto | 
id = 789 # int | The id of the map to be updated

try:
    # Update status map
    api_response = api_instance.update_status_map_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->update_status_map_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapRequestDto**](StatusMapRequestDto.md)|  | 
 **id** | **int**| The id of the map to be updated | 

### Return type

[**StatusMapDto**](StatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status_map_by_id1**
> StatusMapDto update_status_map_by_id1(body, id)

Update status map

Updates an existing status map

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapsApi()
body = swagger_client.StatusMapRequestDto() # StatusMapRequestDto | 
id = 789 # int | The id of the map to be updated

try:
    # Update status map
    api_response = api_instance.update_status_map_by_id1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapsApi->update_status_map_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapRequestDto**](StatusMapRequestDto.md)|  | 
 **id** | **int**| The id of the map to be updated | 

### Return type

[**StatusMapDto**](StatusMapDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

