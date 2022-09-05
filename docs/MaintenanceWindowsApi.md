# swagger_client.MaintenanceWindowsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_maintenance_window**](MaintenanceWindowsApi.md#create_maintenance_window) | **POST** /api/v2/maintenancewindows | Create maintenance window associated with devices
[**create_maintenance_window1**](MaintenanceWindowsApi.md#create_maintenance_window1) | **POST** /api/v2/maintenancewindows/device-group | Create maintenance window associated to device groups
[**delete_maintenance_window_by_id**](MaintenanceWindowsApi.md#delete_maintenance_window_by_id) | **DELETE** /api/v2/maintenancewindows/{id} | Delete maintenance window
[**filter_maintenance_windows**](MaintenanceWindowsApi.md#filter_maintenance_windows) | **POST** /api/v2/maintenancewindows/filterall | Get filtered list of maintenance windows of any entity type
[**filter_maintenance_windows1**](MaintenanceWindowsApi.md#filter_maintenance_windows1) | **POST** /api/v2/maintenancewindows/filter | Get filtered list of device maintenance windows
[**get_maintenance_window_by_id**](MaintenanceWindowsApi.md#get_maintenance_window_by_id) | **GET** /api/v2/maintenancewindows/{id} | Get maintenance window
[**get_maintenance_windows**](MaintenanceWindowsApi.md#get_maintenance_windows) | **GET** /api/v2/maintenancewindows | Get list of maintenance windows
[**update_group_maintenance_window**](MaintenanceWindowsApi.md#update_group_maintenance_window) | **PUT** /api/v2/maintenancewindows/device-group/{id} | 
[**update_maintenance_window_by_id**](MaintenanceWindowsApi.md#update_maintenance_window_by_id) | **PUT** /api/v2/maintenancewindows/{id} | Update maintenance window associated with devices

# **create_maintenance_window**
> MaintenanceWindowDeviceDto create_maintenance_window(body, date_format=date_format, no_validation=no_validation)

Create maintenance window associated with devices

Creates a new maintenance window associated with a list of device IDs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaintenanceWindowsApi()
body = swagger_client.MaintenanceWindowDeviceDto() # MaintenanceWindowDeviceDto | 
date_format = 'UNIX_TIMESTAMP_MILLISECONDS' # str | The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS (optional) (default to UNIX_TIMESTAMP_MILLISECONDS)
no_validation = false # bool |  (optional) (default to false)

try:
    # Create maintenance window associated with devices
    api_response = api_instance.create_maintenance_window(body, date_format=date_format, no_validation=no_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowsApi->create_maintenance_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceWindowDeviceDto**](MaintenanceWindowDeviceDto.md)|  | 
 **date_format** | **str**| The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS | [optional] [default to UNIX_TIMESTAMP_MILLISECONDS]
 **no_validation** | **bool**|  | [optional] [default to false]

### Return type

[**MaintenanceWindowDeviceDto**](MaintenanceWindowDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_maintenance_window1**
> MaintenanceWindowDeviceGroupDto create_maintenance_window1(body, date_format=date_format, no_validation=no_validation)

Create maintenance window associated to device groups

Creates a new maintenance window associated with Device Groups with their IDs. Normally you should not provide Maintenance Window ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaintenanceWindowsApi()
body = swagger_client.MaintenanceWindowDeviceGroupDto() # MaintenanceWindowDeviceGroupDto | 
date_format = 'UNIX_TIMESTAMP_MILLISECONDS' # str | The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS (optional) (default to UNIX_TIMESTAMP_MILLISECONDS)
no_validation = false # bool |  (optional) (default to false)

try:
    # Create maintenance window associated to device groups
    api_response = api_instance.create_maintenance_window1(body, date_format=date_format, no_validation=no_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowsApi->create_maintenance_window1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceWindowDeviceGroupDto**](MaintenanceWindowDeviceGroupDto.md)|  | 
 **date_format** | **str**| The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS | [optional] [default to UNIX_TIMESTAMP_MILLISECONDS]
 **no_validation** | **bool**|  | [optional] [default to false]

### Return type

[**MaintenanceWindowDeviceGroupDto**](MaintenanceWindowDeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_maintenance_window_by_id**
> str delete_maintenance_window_by_id(id, no_validation=no_validation)

Delete maintenance window

Deletes an existing maintenance window given its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaintenanceWindowsApi()
id = 'id_example' # str | The ID of the maintenance window to be deleted
no_validation = false # bool |  (optional) (default to false)

try:
    # Delete maintenance window
    api_response = api_instance.delete_maintenance_window_by_id(id, no_validation=no_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowsApi->delete_maintenance_window_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the maintenance window to be deleted | 
 **no_validation** | **bool**|  | [optional] [default to false]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_maintenance_windows**
> PagerMaintenanceWindowRetrievalDto filter_maintenance_windows(body, date_format=date_format, page=page, size=size, sort_by=sort_by, sort=sort, dir=dir)

Get filtered list of maintenance windows of any entity type

Endpoint for retrieving filtered maintenance windows of any entity type that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaintenanceWindowsApi()
body = swagger_client.MaintenanceWindowFilterDto() # MaintenanceWindowFilterDto | 
date_format = 'UNIX_TIMESTAMP_MILLISECONDS' # str | The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS (optional) (default to UNIX_TIMESTAMP_MILLISECONDS)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 50 # int | The size of the requested page, defaults to 50 (optional) (default to 50)
sort_by = 'sort_by_example' # str | Sort string of format \"property1,-property2,...\", where minus is for descending. Sortable properties: name, notes, maintenanceType, createDateTime, beginDateTime (default), endDateTime. (optional)
sort = 'sort_example' # str |  (optional)
dir = 'dir_example' # str |  (optional)

try:
    # Get filtered list of maintenance windows of any entity type
    api_response = api_instance.filter_maintenance_windows(body, date_format=date_format, page=page, size=size, sort_by=sort_by, sort=sort, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowsApi->filter_maintenance_windows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceWindowFilterDto**](MaintenanceWindowFilterDto.md)|  | 
 **date_format** | **str**| The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS | [optional] [default to UNIX_TIMESTAMP_MILLISECONDS]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 50 | [optional] [default to 50]
 **sort_by** | **str**| Sort string of format \&quot;property1,-property2,...\&quot;, where minus is for descending. Sortable properties: name, notes, maintenanceType, createDateTime, beginDateTime (default), endDateTime. | [optional] 
 **sort** | **str**|  | [optional] 
 **dir** | **str**|  | [optional] 

### Return type

[**PagerMaintenanceWindowRetrievalDto**](PagerMaintenanceWindowRetrievalDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_maintenance_windows1**
> PagerMaintenanceWindowDeviceDto filter_maintenance_windows1(body, date_format=date_format, page=page, size=size, sort_by=sort_by, sort=sort, dir=dir)

Get filtered list of device maintenance windows

Endpoint for retrieving filtered device maintenance windows that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaintenanceWindowsApi()
body = swagger_client.MaintenanceWindowFilterDto() # MaintenanceWindowFilterDto | 
date_format = 'UNIX_TIMESTAMP_MILLISECONDS' # str | The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS (optional) (default to UNIX_TIMESTAMP_MILLISECONDS)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 50 # int | The size of the requested page, defaults to 50 (optional) (default to 50)
sort_by = 'sort_by_example' # str | Sort string of format \"property1,-property2,...\", where minus is for descending. Sortable properties: name, notes, maintenanceType, createDateTime, beginDateTime (default), endDateTime. (optional)
sort = 'sort_example' # str |  (optional)
dir = 'dir_example' # str |  (optional)

try:
    # Get filtered list of device maintenance windows
    api_response = api_instance.filter_maintenance_windows1(body, date_format=date_format, page=page, size=size, sort_by=sort_by, sort=sort, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowsApi->filter_maintenance_windows1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceWindowFilterDto**](MaintenanceWindowFilterDto.md)|  | 
 **date_format** | **str**| The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS | [optional] [default to UNIX_TIMESTAMP_MILLISECONDS]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 50 | [optional] [default to 50]
 **sort_by** | **str**| Sort string of format \&quot;property1,-property2,...\&quot;, where minus is for descending. Sortable properties: name, notes, maintenanceType, createDateTime, beginDateTime (default), endDateTime. | [optional] 
 **sort** | **str**|  | [optional] 
 **dir** | **str**|  | [optional] 

### Return type

[**PagerMaintenanceWindowDeviceDto**](PagerMaintenanceWindowDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_window_by_id**
> str get_maintenance_window_by_id(id, date_format=date_format)

Get maintenance window

Gets a specific maintenance window by ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaintenanceWindowsApi()
id = 'id_example' # str | The ID of the maintenance window
date_format = 'UNIX_TIMESTAMP_MILLISECONDS' # str | The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS (optional) (default to UNIX_TIMESTAMP_MILLISECONDS)

try:
    # Get maintenance window
    api_response = api_instance.get_maintenance_window_by_id(id, date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowsApi->get_maintenance_window_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the maintenance window | 
 **date_format** | **str**| The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS | [optional] [default to UNIX_TIMESTAMP_MILLISECONDS]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_windows**
> PagerMaintenanceWindowDeviceDto get_maintenance_windows(date_format=date_format, page=page, size=size, sort_by=sort_by, sort=sort, dir=dir)

Get list of maintenance windows

Endpoint for retrieving maintenance windows that supports filtering and pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaintenanceWindowsApi()
date_format = 'UNIX_TIMESTAMP_MILLISECONDS' # str | The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS (optional) (default to UNIX_TIMESTAMP_MILLISECONDS)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 50 # int | The size of the requested page, defaults to 50 (optional) (default to 50)
sort_by = 'sort_by_example' # str | Sort string of format \"property1,-property2,...\", where minus is for descending. Sortable properties: name, notes, maintenanceType, createDateTime, beginDateTime (default), endDateTime. (optional)
sort = 'sort_example' # str |  (optional)
dir = 'dir_example' # str |  (optional)

try:
    # Get list of maintenance windows
    api_response = api_instance.get_maintenance_windows(date_format=date_format, page=page, size=size, sort_by=sort_by, sort=sort, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowsApi->get_maintenance_windows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**| The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS | [optional] [default to UNIX_TIMESTAMP_MILLISECONDS]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 50 | [optional] [default to 50]
 **sort_by** | **str**| Sort string of format \&quot;property1,-property2,...\&quot;, where minus is for descending. Sortable properties: name, notes, maintenanceType, createDateTime, beginDateTime (default), endDateTime. | [optional] 
 **sort** | **str**|  | [optional] 
 **dir** | **str**|  | [optional] 

### Return type

[**PagerMaintenanceWindowDeviceDto**](PagerMaintenanceWindowDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_maintenance_window**
> str update_group_maintenance_window(body, id, date_format=date_format)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaintenanceWindowsApi()
body = swagger_client.MaintenanceWindowDeviceGroupDto() # MaintenanceWindowDeviceGroupDto | 
id = 'id_example' # str | The id of the maintenance window to be updated
date_format = 'UNIX_TIMESTAMP_MILLISECONDS' # str | The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS (optional) (default to UNIX_TIMESTAMP_MILLISECONDS)

try:
    api_response = api_instance.update_group_maintenance_window(body, id, date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowsApi->update_group_maintenance_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceWindowDeviceGroupDto**](MaintenanceWindowDeviceGroupDto.md)|  | 
 **id** | **str**| The id of the maintenance window to be updated | 
 **date_format** | **str**| The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS | [optional] [default to UNIX_TIMESTAMP_MILLISECONDS]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_maintenance_window_by_id**
> str update_maintenance_window_by_id(body, id, date_format=date_format)

Update maintenance window associated with devices

Updates all fields of an existing maintenance window

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MaintenanceWindowsApi()
body = swagger_client.MaintenanceWindowDeviceDto() # MaintenanceWindowDeviceDto | 
id = 'id_example' # str | The id of the maintenance window to be updated
date_format = 'UNIX_TIMESTAMP_MILLISECONDS' # str | The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS (optional) (default to UNIX_TIMESTAMP_MILLISECONDS)

try:
    # Update maintenance window associated with devices
    api_response = api_instance.update_maintenance_window_by_id(body, id, date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowsApi->update_maintenance_window_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceWindowDeviceDto**](MaintenanceWindowDeviceDto.md)|  | 
 **id** | **str**| The id of the maintenance window to be updated | 
 **date_format** | **str**| The date format for begin and end dates: UNIX_TIMESTAMP_SECONDS, UNIX_TIMESTAMP_MILLISECONDS, ISO8601_SECONDS, ISO8601_MILLISECONDS | [optional] [default to UNIX_TIMESTAMP_MILLISECONDS]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

