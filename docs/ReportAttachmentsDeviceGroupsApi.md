# swagger_client.ReportAttachmentsDeviceGroupsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_groups_attachment**](ReportAttachmentsDeviceGroupsApi.md#create_device_groups_attachment) | **POST** /api/v2/reports/{id}/attachments/devicegroups | Create device groups attachment
[**create_device_groups_attachment1**](ReportAttachmentsDeviceGroupsApi.md#create_device_groups_attachment1) | **POST** /api/v1/reports/{id}/attachments/devicegroups | Create device groups attachment
[**get_device_group_attachment**](ReportAttachmentsDeviceGroupsApi.md#get_device_group_attachment) | **GET** /api/v2/reports/attachments/devicegroups/{id} | Get device group attachment
[**get_device_groups_attachment**](ReportAttachmentsDeviceGroupsApi.md#get_device_groups_attachment) | **GET** /api/v2/reports/attachments/devicegroups/{id}/resources | Get resources for device groups report attachment
[**get_device_groups_attachment1**](ReportAttachmentsDeviceGroupsApi.md#get_device_groups_attachment1) | **GET** /api/v1/reports/attachments/devicegroups/{id}/resources | Get resources for device groups report attachment
[**get_device_groups_attachment_visualization**](ReportAttachmentsDeviceGroupsApi.md#get_device_groups_attachment_visualization) | **GET** /api/v2/reports/attachments/devicegroups/{id}/visualizations | Get visualization
[**get_device_groups_attachment_visualization1**](ReportAttachmentsDeviceGroupsApi.md#get_device_groups_attachment_visualization1) | **GET** /api/v1/reports/attachments/devicegroups/{id}/visualizations | Get visualization
[**update_device_groups_attachment**](ReportAttachmentsDeviceGroupsApi.md#update_device_groups_attachment) | **PUT** /api/v2/reports/attachments/devicegroups/{id}/resources | Update resources
[**update_device_groups_attachment1**](ReportAttachmentsDeviceGroupsApi.md#update_device_groups_attachment1) | **PUT** /api/v1/reports/attachments/devicegroups/{id}/resources | Update resources
[**update_device_groups_attachment_visualization**](ReportAttachmentsDeviceGroupsApi.md#update_device_groups_attachment_visualization) | **PUT** /api/v2/reports/attachments/devicegroups/{id}/visualizations | Update visualization
[**update_device_groups_attachment_visualization1**](ReportAttachmentsDeviceGroupsApi.md#update_device_groups_attachment_visualization1) | **PUT** /api/v1/reports/attachments/devicegroups/{id}/visualizations | Update visualization

# **create_device_groups_attachment**
> DeviceGroupsResponseDto create_device_groups_attachment(body, id)

Create device groups attachment

Create a new device groups attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
body = swagger_client.DeviceGroupsRequestDto() # DeviceGroupsRequestDto | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create device groups attachment
    api_response = api_instance.create_device_groups_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->create_device_groups_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroupsRequestDto**](DeviceGroupsRequestDto.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**DeviceGroupsResponseDto**](DeviceGroupsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_groups_attachment1**
> DeviceGroupsResponseDtoV1 create_device_groups_attachment1(body, id)

Create device groups attachment

Create a new device groups attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
body = swagger_client.DeviceGroupsRequestDtoV1() # DeviceGroupsRequestDtoV1 | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create device groups attachment
    api_response = api_instance.create_device_groups_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->create_device_groups_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroupsRequestDtoV1**](DeviceGroupsRequestDtoV1.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**DeviceGroupsResponseDtoV1**](DeviceGroupsResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_attachment**
> DeviceGroupsResponseDto get_device_group_attachment(id)

Get device group attachment

Get an existing devicegroup attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
id = 789 # int | Device group attachment id

try:
    # Get device group attachment
    api_response = api_instance.get_device_group_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->get_device_group_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device group attachment id | 

### Return type

[**DeviceGroupsResponseDto**](DeviceGroupsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups_attachment**
> DeviceGroupsResource get_device_groups_attachment(id)

Get resources for device groups report attachment

Get resources for device groups attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources for device groups report attachment
    api_response = api_instance.get_device_groups_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->get_device_groups_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**DeviceGroupsResource**](DeviceGroupsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups_attachment1**
> DeviceGroupsResourceV1 get_device_groups_attachment1(id)

Get resources for device groups report attachment

Get resources for device groups attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources for device groups report attachment
    api_response = api_instance.get_device_groups_attachment1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->get_device_groups_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**DeviceGroupsResourceV1**](DeviceGroupsResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups_attachment_visualization**
> DeviceGroupsVisualization get_device_groups_attachment_visualization(id)

Get visualization

Get visualization for device groups attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
id = 789 # int | The id of device groups attachment

try:
    # Get visualization
    api_response = api_instance.get_device_groups_attachment_visualization(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->get_device_groups_attachment_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of device groups attachment | 

### Return type

[**DeviceGroupsVisualization**](DeviceGroupsVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups_attachment_visualization1**
> DeviceGroupsVisualizationV1 get_device_groups_attachment_visualization1(id)

Get visualization

Get visualization for device groups attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
id = 789 # int | The id of device groups attachment

try:
    # Get visualization
    api_response = api_instance.get_device_groups_attachment_visualization1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->get_device_groups_attachment_visualization1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of device groups attachment | 

### Return type

[**DeviceGroupsVisualizationV1**](DeviceGroupsVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_groups_attachment**
> DeviceGroupsResource update_device_groups_attachment(body, id)

Update resources

Update resources of device groups report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
body = swagger_client.DeviceGroupsResource() # DeviceGroupsResource | 
id = 789 # int | The id of device groups attachment

try:
    # Update resources
    api_response = api_instance.update_device_groups_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->update_device_groups_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroupsResource**](DeviceGroupsResource.md)|  | 
 **id** | **int**| The id of device groups attachment | 

### Return type

[**DeviceGroupsResource**](DeviceGroupsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_groups_attachment1**
> DeviceGroupsResourceV1 update_device_groups_attachment1(body, id)

Update resources

Update resources of device groups report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
body = swagger_client.DeviceGroupsResourceV1() # DeviceGroupsResourceV1 | 
id = 789 # int | The id of device groups attachment

try:
    # Update resources
    api_response = api_instance.update_device_groups_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->update_device_groups_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroupsResourceV1**](DeviceGroupsResourceV1.md)|  | 
 **id** | **int**| The id of device groups attachment | 

### Return type

[**DeviceGroupsResourceV1**](DeviceGroupsResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_groups_attachment_visualization**
> DeviceGroupsVisualization update_device_groups_attachment_visualization(body, id)

Update visualization

Update visualization for device groups attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
body = swagger_client.DeviceGroupsVisualization() # DeviceGroupsVisualization | 
id = 789 # int | The id of device groups attachment

try:
    # Update visualization
    api_response = api_instance.update_device_groups_attachment_visualization(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->update_device_groups_attachment_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroupsVisualization**](DeviceGroupsVisualization.md)|  | 
 **id** | **int**| The id of device groups attachment | 

### Return type

[**DeviceGroupsVisualization**](DeviceGroupsVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_groups_attachment_visualization1**
> DeviceGroupsVisualizationV1 update_device_groups_attachment_visualization1(body, id)

Update visualization

Update visualization for device groups attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDeviceGroupsApi()
body = swagger_client.DeviceGroupsVisualizationV1() # DeviceGroupsVisualizationV1 | 
id = 789 # int | The id of device groups attachment

try:
    # Update visualization
    api_response = api_instance.update_device_groups_attachment_visualization1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDeviceGroupsApi->update_device_groups_attachment_visualization1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroupsVisualizationV1**](DeviceGroupsVisualizationV1.md)|  | 
 **id** | **int**| The id of device groups attachment | 

### Return type

[**DeviceGroupsVisualizationV1**](DeviceGroupsVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

