# swagger_client.ThresholdsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_threshold**](ThresholdsApi.md#create_threshold) | **POST** /api/v2/thresholds/flow/{deviceId} | Create threshold
[**create_threshold_condition**](ThresholdsApi.md#create_threshold_condition) | **POST** /api/v2/thresholds/flow/{deviceId}/{thresholdId}/{triggerType}/conditions | add a condition to a threshold
[**delete_threshold_by_id**](ThresholdsApi.md#delete_threshold_by_id) | **DELETE** /api/v2/thresholds/flow/{deviceId}/{thresholdId} | Delete threshold by Id
[**delete_threshold_condition_by_id**](ThresholdsApi.md#delete_threshold_condition_by_id) | **DELETE** /api/v2/thresholds/flow/{deviceId}/{thresholdId}/{triggerType}/conditions/{conditionId} | delete a condition of a threshold
[**get_threshold_by_id**](ThresholdsApi.md#get_threshold_by_id) | **GET** /api/v2/thresholds/flow/{deviceId}/{thresholdId} | Get a threshold by id
[**get_thresholds**](ThresholdsApi.md#get_thresholds) | **GET** /api/v2/thresholds | Get thresholds
[**update_threshold**](ThresholdsApi.md#update_threshold) | **PUT** /api/v2/thresholds/flow/{deviceId}/{thresholdId} | Update threshold by ID
[**update_threshold_condition_by_id**](ThresholdsApi.md#update_threshold_condition_by_id) | **PUT** /api/v2/thresholds/flow/{deviceId}/{thresholdId}/{triggerType}/conditions/{conditionId} | update a condition of a threshold

# **create_threshold**
> ThresholdDto create_threshold(body, device_id)

Create threshold

Create threshold

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThresholdsApi()
body = swagger_client.ThresholdDto() # ThresholdDto | 
device_id = 789 # int | The flow device id

try:
    # Create threshold
    api_response = api_instance.create_threshold(body, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdsApi->create_threshold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThresholdDto**](ThresholdDto.md)|  | 
 **device_id** | **int**| The flow device id | 

### Return type

[**ThresholdDto**](ThresholdDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threshold_condition**
> ThresholdConditionDto create_threshold_condition(body, device_id, threshold_id, trigger_type)

add a condition to a threshold

add a threshold condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThresholdsApi()
body = swagger_client.ThresholdConditionDto() # ThresholdConditionDto | 
device_id = 789 # int | 
threshold_id = 789 # int | 
trigger_type = 'trigger_type_example' # str | 

try:
    # add a condition to a threshold
    api_response = api_instance.create_threshold_condition(body, device_id, threshold_id, trigger_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdsApi->create_threshold_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThresholdConditionDto**](ThresholdConditionDto.md)|  | 
 **device_id** | **int**|  | 
 **threshold_id** | **int**|  | 
 **trigger_type** | **str**|  | 

### Return type

[**ThresholdConditionDto**](ThresholdConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threshold_by_id**
> str delete_threshold_by_id(device_id, threshold_id)

Delete threshold by Id

Delete a threshold

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThresholdsApi()
device_id = 789 # int | The flow device id
threshold_id = 789 # int | The threshold id

try:
    # Delete threshold by Id
    api_response = api_instance.delete_threshold_by_id(device_id, threshold_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdsApi->delete_threshold_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The flow device id | 
 **threshold_id** | **int**| The threshold id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threshold_condition_by_id**
> str delete_threshold_condition_by_id(device_id, threshold_id, trigger_type, condition_id)

delete a condition of a threshold

delete a threshold condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThresholdsApi()
device_id = 789 # int | 
threshold_id = 789 # int | 
trigger_type = 'trigger_type_example' # str | 
condition_id = 789 # int | 

try:
    # delete a condition of a threshold
    api_response = api_instance.delete_threshold_condition_by_id(device_id, threshold_id, trigger_type, condition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdsApi->delete_threshold_condition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **threshold_id** | **int**|  | 
 **trigger_type** | **str**|  | 
 **condition_id** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_threshold_by_id**
> ThresholdDto get_threshold_by_id(device_id, threshold_id)

Get a threshold by id

Get threshold

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThresholdsApi()
device_id = 789 # int | The flow device id
threshold_id = 789 # int | The threshold id

try:
    # Get a threshold by id
    api_response = api_instance.get_threshold_by_id(device_id, threshold_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdsApi->get_threshold_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The flow device id | 
 **threshold_id** | **int**| The threshold id | 

### Return type

[**ThresholdDto**](ThresholdDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thresholds**
> PagerThresholdDto get_thresholds(type=type, page=page, size=size, include_count=include_count)

Get thresholds

Get thresholds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThresholdsApi()
type = 'type_example' # str | Threshold type filter. If not set, both other and flow thresholds are returned (optional)
page = 0 # int |  (optional) (default to 0)
size = 20 # int |  (optional) (default to 20)
include_count = true # bool |  (optional) (default to true)

try:
    # Get thresholds
    api_response = api_instance.get_thresholds(type=type, page=page, size=size, include_count=include_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdsApi->get_thresholds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Threshold type filter. If not set, both other and flow thresholds are returned | [optional] 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 20]
 **include_count** | **bool**|  | [optional] [default to true]

### Return type

[**PagerThresholdDto**](PagerThresholdDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threshold**
> ThresholdDto update_threshold(body, device_id, threshold_id)

Update threshold by ID

Update threshold

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThresholdsApi()
body = swagger_client.ThresholdDto() # ThresholdDto | 
device_id = 789 # int | The flow device id
threshold_id = 789 # int | The threshold id to be updated

try:
    # Update threshold by ID
    api_response = api_instance.update_threshold(body, device_id, threshold_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdsApi->update_threshold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThresholdDto**](ThresholdDto.md)|  | 
 **device_id** | **int**| The flow device id | 
 **threshold_id** | **int**| The threshold id to be updated | 

### Return type

[**ThresholdDto**](ThresholdDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threshold_condition_by_id**
> ThresholdConditionDto update_threshold_condition_by_id(body, device_id, threshold_id, trigger_type, condition_id)

update a condition of a threshold

update a threshold condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThresholdsApi()
body = swagger_client.ThresholdConditionDto() # ThresholdConditionDto | 
device_id = 789 # int | 
threshold_id = 789 # int | 
trigger_type = 'trigger_type_example' # str | 
condition_id = 789 # int | 

try:
    # update a condition of a threshold
    api_response = api_instance.update_threshold_condition_by_id(body, device_id, threshold_id, trigger_type, condition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThresholdsApi->update_threshold_condition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThresholdConditionDto**](ThresholdConditionDto.md)|  | 
 **device_id** | **int**|  | 
 **threshold_id** | **int**|  | 
 **trigger_type** | **str**|  | 
 **condition_id** | **int**|  | 

### Return type

[**ThresholdConditionDto**](ThresholdConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

