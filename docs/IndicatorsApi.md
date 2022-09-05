# swagger_client.IndicatorsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_indicator_data**](IndicatorsApi.md#create_device_indicator_data) | **POST** /api/v2/device-indicators/data | Create device indicator data
[**create_device_indicator_data1**](IndicatorsApi.md#create_device_indicator_data1) | **POST** /api/v1/device-indicators/data | Create device indicator data
[**get_indicator**](IndicatorsApi.md#get_indicator) | **GET** /api/v2/devices/{deviceId}/objects/{objectId}/indicators/{indicatorId} | Get indicator by deviceId, objectId and indicatorId
[**get_indicator1**](IndicatorsApi.md#get_indicator1) | **GET** /api/v1/devices/{deviceId}/objects/{objectId}/indicators/{indicatorId} | Get indicator by deviceId, objectId and indicatorId
[**get_indicator_data**](IndicatorsApi.md#get_indicator_data) | **GET** /api/v2/devices/{deviceId}/objects/{objectId}/indicators/{indicatorId}/data | Get indicator data by deviceId, objectId and indicatorId
[**get_indicator_data1**](IndicatorsApi.md#get_indicator_data1) | **GET** /api/v1/devices/{deviceId}/objects/{objectId}/indicators/{indicatorId}/data | Get indicator data by deviceId, objectId and indicatorId
[**get_indicators**](IndicatorsApi.md#get_indicators) | **GET** /api/v2/devices/{deviceId}/objects/{objectId}/indicators | Get indicators by deviceId and objectId
[**get_indicators1**](IndicatorsApi.md#get_indicators1) | **GET** /api/v1/devices/{deviceId}/objects/{objectId}/indicators | Get indicators by deviceId and objectId
[**get_last_seen_timestamp_for_indicators**](IndicatorsApi.md#get_last_seen_timestamp_for_indicators) | **POST** /api/v2/device-indicators/last-seen | Get the timestamp of the most recent data point for indicators

# **create_device_indicator_data**
> str create_device_indicator_data(body)

Create device indicator data

Creates a new device indicator data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
body = [swagger_client.ObjectDataDto()] # list[ObjectDataDto] | 

try:
    # Create device indicator data
    api_response = api_instance.create_device_indicator_data(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->create_device_indicator_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ObjectDataDto]**](ObjectDataDto.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_indicator_data1**
> str create_device_indicator_data1(body)

Create device indicator data

Creates a new device indicator data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
body = [swagger_client.ObjectDataDto()] # list[ObjectDataDto] | 

try:
    # Create device indicator data
    api_response = api_instance.create_device_indicator_data1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->create_device_indicator_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ObjectDataDto]**](ObjectDataDto.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator**
> IndicatorDtoIncludeMetadata get_indicator(device_id, object_id, indicator_id, include_extended_info=include_extended_info)

Get indicator by deviceId, objectId and indicatorId

Endpoint for retrieving a single indicator for given deviceId, objectId and indicatorId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
indicator_id = 789 # int | The Id of the indicator
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get indicator by deviceId, objectId and indicatorId
    api_response = api_instance.get_indicator(device_id, object_id, indicator_id, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **indicator_id** | **int**| The Id of the indicator | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**IndicatorDtoIncludeMetadata**](IndicatorDtoIncludeMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator1**
> IndicatorDtoNoMetadata get_indicator1(device_id, object_id, indicator_id, include_extended_info=include_extended_info)

Get indicator by deviceId, objectId and indicatorId

Endpoint for retrieving a single indicator for given deviceId, objectId and indicatorId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
indicator_id = 789 # int | The Id of the indicator
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get indicator by deviceId, objectId and indicatorId
    api_response = api_instance.get_indicator1(device_id, object_id, indicator_id, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicator1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **indicator_id** | **int**| The Id of the indicator | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**IndicatorDtoNoMetadata**](IndicatorDtoNoMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator_data**
> list[DataPointDto] get_indicator_data(device_id, object_id, indicator_id, start_time, end_time, raw_data=raw_data)

Get indicator data by deviceId, objectId and indicatorId

Endpoint for retrieving indicators data for a given indicatorId and period of time

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
indicator_id = 789 # int | The Id of the indicator
start_time = 789 # int | Start time for the data, unix timestamp with milliseconds proximity
end_time = 789 # int | End time for the data, unix timestamp with milliseconds proximity
raw_data = false # bool | Determines whether to return raw data (optional) (default to false)

try:
    # Get indicator data by deviceId, objectId and indicatorId
    api_response = api_instance.get_indicator_data(device_id, object_id, indicator_id, start_time, end_time, raw_data=raw_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicator_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **indicator_id** | **int**| The Id of the indicator | 
 **start_time** | **int**| Start time for the data, unix timestamp with milliseconds proximity | 
 **end_time** | **int**| End time for the data, unix timestamp with milliseconds proximity | 
 **raw_data** | **bool**| Determines whether to return raw data | [optional] [default to false]

### Return type

[**list[DataPointDto]**](DataPointDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator_data1**
> list[DataPointDto] get_indicator_data1(device_id, object_id, indicator_id, start_time, end_time)

Get indicator data by deviceId, objectId and indicatorId

Endpoint for retrieving indicators data for a given indicatorId and period of time

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
indicator_id = 789 # int | The Id of the indicator
start_time = 789 # int | Start time for the data, unix timestamp with milliseconds proximity
end_time = 789 # int | End time for the data, unix timestamp with milliseconds proximity

try:
    # Get indicator data by deviceId, objectId and indicatorId
    api_response = api_instance.get_indicator_data1(device_id, object_id, indicator_id, start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicator_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **indicator_id** | **int**| The Id of the indicator | 
 **start_time** | **int**| Start time for the data, unix timestamp with milliseconds proximity | 
 **end_time** | **int**| End time for the data, unix timestamp with milliseconds proximity | 

### Return type

[**list[DataPointDto]**](DataPointDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicators**
> PagerIndicatorDtoIncludeMetadata get_indicators(device_id, object_id, options, include_extended_info=include_extended_info, include_indicator_metadata=include_indicator_metadata)

Get indicators by deviceId and objectId

Endpoint for retrieving all indicators for a given deviceId and objectId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
options = swagger_client.PageAndSortOptionsIncludeMetadata() # PageAndSortOptionsIncludeMetadata | 
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)
include_indicator_metadata = false # bool | Determines whether to include indicator metadata (optional) (default to false)

try:
    # Get indicators by deviceId and objectId
    api_response = api_instance.get_indicators(device_id, object_id, options, include_extended_info=include_extended_info, include_indicator_metadata=include_indicator_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **options** | [**PageAndSortOptionsIncludeMetadata**](.md)|  | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]
 **include_indicator_metadata** | **bool**| Determines whether to include indicator metadata | [optional] [default to false]

### Return type

[**PagerIndicatorDtoIncludeMetadata**](PagerIndicatorDtoIncludeMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicators1**
> PagerIndicatorDtoNoMetadata get_indicators1(device_id, object_id, page=page, size=size, include_extended_info=include_extended_info)

Get indicators by deviceId and objectId

Endpoint for retrieving all indicators for a given deviceId and objectId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get indicators by deviceId and objectId
    api_response = api_instance.get_indicators1(device_id, object_id, page=page, size=size, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicators1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerIndicatorDtoNoMetadata**](PagerIndicatorDtoNoMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_seen_timestamp_for_indicators**
> LastSeenResponseDto get_last_seen_timestamp_for_indicators(body)

Get the timestamp of the most recent data point for indicators

Endpoint for retrieving the timestamp of the most recent data point for indicators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
body = swagger_client.LastSeenRequestDto() # LastSeenRequestDto | 

try:
    # Get the timestamp of the most recent data point for indicators
    api_response = api_instance.get_last_seen_timestamp_for_indicators(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_last_seen_timestamp_for_indicators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LastSeenRequestDto**](LastSeenRequestDto.md)|  | 

### Return type

[**LastSeenResponseDto**](LastSeenResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

