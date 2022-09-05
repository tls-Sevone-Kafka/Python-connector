# swagger_client.DevicesApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_device_rules**](DevicesApi.md#apply_device_rules) | **POST** /api/v2/devices/{id}/rules/apply | Apply the rules for the specified device
[**create_device**](DevicesApi.md#create_device) | **POST** /api/v2/devices | Create device
[**create_device1**](DevicesApi.md#create_device1) | **POST** /api/v1/devices | Create device
[**create_device_data**](DevicesApi.md#create_device_data) | **POST** /api/v2/devices/data | Create device data
[**delete_device_by_id**](DevicesApi.md#delete_device_by_id) | **DELETE** /api/v2/devices/{id} | Delete device
[**delete_device_by_id1**](DevicesApi.md#delete_device_by_id1) | **DELETE** /api/v1/devices/{id} | Delete device
[**filter_device**](DevicesApi.md#filter_device) | **POST** /api/v2/devices/filter | Filter devices
[**filter_device1**](DevicesApi.md#filter_device1) | **POST** /api/v1/devices/filter | Filter devices
[**get_device_by_id**](DevicesApi.md#get_device_by_id) | **GET** /api/v2/devices/{id} | Get device by Id
[**get_device_by_id1**](DevicesApi.md#get_device_by_id1) | **GET** /api/v1/devices/{id} | Get device by Id
[**get_devices**](DevicesApi.md#get_devices) | **GET** /api/v2/devices | Get all devices
[**get_devices1**](DevicesApi.md#get_devices1) | **GET** /api/v1/devices | Get all devices
[**partially_update_device_by_id**](DevicesApi.md#partially_update_device_by_id) | **PATCH** /api/v2/devices/{id} | Partially update device
[**partially_update_device_by_id1**](DevicesApi.md#partially_update_device_by_id1) | **PATCH** /api/v1/devices/{id} | Partially update device
[**partially_update_devices**](DevicesApi.md#partially_update_devices) | **PATCH** /api/v2/devices/bulkUpdateDevices | Updates devices basic info
[**undelete_device_by_id**](DevicesApi.md#undelete_device_by_id) | **POST** /api/v2/devices/{id}/undelete | Undelete device
[**undelete_device_by_id1**](DevicesApi.md#undelete_device_by_id1) | **POST** /api/v1/devices/{id}/undelete | Undelete device
[**update_device_by_id**](DevicesApi.md#update_device_by_id) | **PUT** /api/v2/devices/{id} | Update device
[**update_device_by_id1**](DevicesApi.md#update_device_by_id1) | **PUT** /api/v1/devices/{id} | Update device

# **apply_device_rules**
> str apply_device_rules(id)

Apply the rules for the specified device

Applies device group and object group rules for the specified device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device

try:
    # Apply the rules for the specified device
    api_response = api_instance.apply_device_rules(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->apply_device_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device**
> DeviceDto create_device(body)

Create device

Creates a new device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.CreateDeviceRequestDto() # CreateDeviceRequestDto | 

try:
    # Create device
    api_response = api_instance.create_device(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDeviceRequestDto**](CreateDeviceRequestDto.md)|  | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device1**
> DeviceDto create_device1(body)

Create device

Creates a new device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.CreateDeviceRequestDto() # CreateDeviceRequestDto | 

try:
    # Create device
    api_response = api_instance.create_device1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDeviceRequestDto**](CreateDeviceRequestDto.md)|  | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_data**
> str create_device_data(body)

Create device data

Creates new device data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.DeviceDescription() # DeviceDescription | 

try:
    # Create device data
    api_response = api_instance.create_device_data(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceDescription**](DeviceDescription.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_by_id**
> str delete_device_by_id(id, force_delete=force_delete)

Delete device

Moves device to the deletion queue. If `days_to_delay` in cluster setting is set to 0, device will be deleted immediately in the next discovery.  Set forceDelete flag to true to force delete device instead of moving it in the queue.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be deleted
force_delete = false # bool | Determines whether to force delete device or not (put device in deletion queue).  If `days_to_delay` in cluster setting is set to 0, device will be deleted immediately in the next discovery. (optional) (default to false)

try:
    # Delete device
    api_response = api_instance.delete_device_by_id(id, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be deleted | 
 **force_delete** | **bool**| Determines whether to force delete device or not (put device in deletion queue).  If &#x60;days_to_delay&#x60; in cluster setting is set to 0, device will be deleted immediately in the next discovery. | [optional] [default to false]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_by_id1**
> str delete_device_by_id1(id, force_delete=force_delete)

Delete device

Moves device to the deletion queue. If `days_to_delay` in cluster setting is set to 0, device will be deleted immediately in the next discovery.  Set forceDelete flag to true to force delete device instead of moving it in the queue.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be deleted
force_delete = false # bool | Determines whether to force delete device or not (put device in deletion queue).  If `days_to_delay` in cluster setting is set to 0, device will be deleted immediately in the next discovery. (optional) (default to false)

try:
    # Delete device
    api_response = api_instance.delete_device_by_id1(id, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be deleted | 
 **force_delete** | **bool**| Determines whether to force delete device or not (put device in deletion queue).  If &#x60;days_to_delay&#x60; in cluster setting is set to 0, device will be deleted immediately in the next discovery. | [optional] [default to false]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_device**
> PagerDeviceDtoNoMetadata filter_device(body, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only)

Filter devices

Find all devices that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.DevicesFilterBody1() # DevicesFilterBody1 | 
include_objects = false # bool | Determines whether to include objects (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)
include_extended_info = false # bool | Determines whether to include extendedInfo or not (optional) (default to false)
local_only = true # bool | Determines whether to execute distributed request or not (optional) (default to true)

try:
    # Filter devices
    api_response = api_instance.filter_device(body, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->filter_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesFilterBody1**](DevicesFilterBody1.md)|  | 
 **include_objects** | **bool**| Determines whether to include objects | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to false]
 **local_only** | **bool**| Determines whether to execute distributed request or not | [optional] [default to true]

### Return type

[**PagerDeviceDtoNoMetadata**](PagerDeviceDtoNoMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_device1**
> PagerDeviceDtoNoMetadata filter_device1(body, page=page, size=size, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only)

Filter devices

Find all devices that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.DeviceFilterV1NoMetadata() # DeviceFilterV1NoMetadata | 
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_objects = false # bool | Determines whether to include objects (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)
include_extended_info = false # bool | Determines whether to include extendedInfo or not (optional) (default to false)
local_only = true # bool | Determines whether to execute distributed request or not (optional) (default to true)

try:
    # Filter devices
    api_response = api_instance.filter_device1(body, page=page, size=size, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->filter_device1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceFilterV1NoMetadata**](DeviceFilterV1NoMetadata.md)|  | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_objects** | **bool**| Determines whether to include objects | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to false]
 **local_only** | **bool**| Determines whether to execute distributed request or not | [optional] [default to true]

### Return type

[**PagerDeviceDtoNoMetadata**](PagerDeviceDtoNoMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id**
> DeviceDtoNoMetadata get_device_by_id(id, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info)

Get device by Id

Gets a single device object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the requested device
include_objects = false # bool | Determines whether to include objects of the device (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators and objects (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not. Note that encrypted fields/credentials like username, password related to device for the plugin will not be returned (optional) (default to true)

try:
    # Get device by Id
    api_response = api_instance.get_device_by_id(id, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device | 
 **include_objects** | **bool**| Determines whether to include objects of the device | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators and objects | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not. Note that encrypted fields/credentials like username, password related to device for the plugin will not be returned | [optional] [default to true]

### Return type

[**DeviceDtoNoMetadata**](DeviceDtoNoMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id1**
> DeviceDtoNoMetadata get_device_by_id1(id, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info)

Get device by Id

Gets a single device object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the requested device
include_objects = false # bool | Determines whether to include objects of the device (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators and objects (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get device by Id
    api_response = api_instance.get_device_by_id1(id, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device | 
 **include_objects** | **bool**| Determines whether to include objects of the device | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators and objects | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**DeviceDtoNoMetadata**](DeviceDtoNoMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> PagerDeviceDto get_devices(options)

Get all devices

Endpoint for retrieving all devices that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all devices
    api_response = api_instance.get_devices(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerDeviceDto**](PagerDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices1**
> PagerDeviceDto get_devices1(page=page, size=size)

Get all devices

Endpoint for retrieving all devices that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)

try:
    # Get all devices
    api_response = api_instance.get_devices1(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]

### Return type

[**PagerDeviceDto**](PagerDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_device_by_id**
> DeviceDto partially_update_device_by_id(body, id)

Partially update device

Partial update an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.DeviceUpdateRequestDto() # DeviceUpdateRequestDto | 
id = 789 # int | The id of the device to be updated

try:
    # Partially update device
    api_response = api_instance.partially_update_device_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->partially_update_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceUpdateRequestDto**](DeviceUpdateRequestDto.md)|  | 
 **id** | **int**| The id of the device to be updated | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_device_by_id1**
> DeviceDto partially_update_device_by_id1(body, id)

Partially update device

Partial update an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.DeviceUpdateRequestDto() # DeviceUpdateRequestDto | 
id = 789 # int | The id of the device to be updated

try:
    # Partially update device
    api_response = api_instance.partially_update_device_by_id1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->partially_update_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceUpdateRequestDto**](DeviceUpdateRequestDto.md)|  | 
 **id** | **int**| The id of the device to be updated | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_devices**
> list[DeviceDto] partially_update_devices(body)

Updates devices basic info

Partially updates basic info of the existing devices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = [swagger_client.DeviceBulkUpdateRequestDto()] # list[DeviceBulkUpdateRequestDto] | 

try:
    # Updates devices basic info
    api_response = api_instance.partially_update_devices(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->partially_update_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DeviceBulkUpdateRequestDto]**](DeviceBulkUpdateRequestDto.md)|  | 

### Return type

[**list[DeviceDto]**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_device_by_id**
> str undelete_device_by_id(id)

Undelete device

Removes device from deletion queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be updated

try:
    # Undelete device
    api_response = api_instance.undelete_device_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->undelete_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be updated | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_device_by_id1**
> str undelete_device_by_id1(id)

Undelete device

Removes device from deletion queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be updated

try:
    # Undelete device
    api_response = api_instance.undelete_device_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->undelete_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be updated | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_by_id**
> DeviceDto update_device_by_id(body, id)

Update device

Updates an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.DeviceUpdateRequestDto() # DeviceUpdateRequestDto | 
id = 789 # int | The id of the device to be updated

try:
    # Update device
    api_response = api_instance.update_device_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceUpdateRequestDto**](DeviceUpdateRequestDto.md)|  | 
 **id** | **int**| The id of the device to be updated | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_by_id1**
> DeviceDto update_device_by_id1(body, id)

Update device

Updates an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.DeviceUpdateRequestDto() # DeviceUpdateRequestDto | 
id = 789 # int | The id of the device to be updated

try:
    # Update device
    api_response = api_instance.update_device_by_id1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceUpdateRequestDto**](DeviceUpdateRequestDto.md)|  | 
 **id** | **int**| The id of the device to be updated | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

