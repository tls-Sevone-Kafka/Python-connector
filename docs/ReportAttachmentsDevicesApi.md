# swagger_client.ReportAttachmentsDevicesApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_attachment**](ReportAttachmentsDevicesApi.md#create_device_attachment) | **POST** /api/v2/reports/{id}/attachments/devices | Create devices attachment
[**create_device_attachment1**](ReportAttachmentsDevicesApi.md#create_device_attachment1) | **POST** /api/v1/reports/{id}/attachments/devices | Create devices attachment
[**get_device_attachment**](ReportAttachmentsDevicesApi.md#get_device_attachment) | **GET** /api/v2/reports/attachments/devices/{id} | Get device attachment
[**get_device_attachment1**](ReportAttachmentsDevicesApi.md#get_device_attachment1) | **GET** /api/v2/reports/attachments/devices/{id}/resources | Get devices report attachment
[**get_device_attachment2**](ReportAttachmentsDevicesApi.md#get_device_attachment2) | **GET** /api/v1/reports/attachments/devices/{id}/resources | Get devices report attachment
[**get_device_attachment_filter_schema**](ReportAttachmentsDevicesApi.md#get_device_attachment_filter_schema) | **GET** /api/v2/reports/attachments/devices/filters/schema | Gets the filters schema
[**get_device_attachment_filter_schema1**](ReportAttachmentsDevicesApi.md#get_device_attachment_filter_schema1) | **GET** /api/v1/reports/attachments/devices/filters/schema | Gets the filters schema
[**get_device_attachment_filters**](ReportAttachmentsDevicesApi.md#get_device_attachment_filters) | **GET** /api/v2/reports/attachments/devices/{id}/filters | Get filters
[**get_device_attachment_filters1**](ReportAttachmentsDevicesApi.md#get_device_attachment_filters1) | **GET** /api/v1/reports/attachments/devices/{id}/filters | Get filters
[**get_device_attachment_settings**](ReportAttachmentsDevicesApi.md#get_device_attachment_settings) | **GET** /api/v2/reports/attachments/devices/{id}/settings | Get devices report attachment
[**get_device_attachment_settings1**](ReportAttachmentsDevicesApi.md#get_device_attachment_settings1) | **GET** /api/v1/reports/attachments/devices/{id}/settings | Get devices report attachment
[**get_device_attachment_visualization**](ReportAttachmentsDevicesApi.md#get_device_attachment_visualization) | **GET** /api/v2/reports/attachments/devices/{id}/visualizations | Get devices report attachment
[**get_device_attachment_visualization1**](ReportAttachmentsDevicesApi.md#get_device_attachment_visualization1) | **GET** /api/v1/reports/attachments/devices/{id}/visualizations | Get devices report attachment
[**update_device_attachment**](ReportAttachmentsDevicesApi.md#update_device_attachment) | **PUT** /api/v2/reports/attachments/devices/{id}/resources | Update devices report attachment
[**update_device_attachment1**](ReportAttachmentsDevicesApi.md#update_device_attachment1) | **PUT** /api/v1/reports/attachments/devices/{id}/resources | Update devices report attachment
[**update_device_attachment_filters**](ReportAttachmentsDevicesApi.md#update_device_attachment_filters) | **PUT** /api/v2/reports/attachments/devices/{id}/filters | Update filters
[**update_device_attachment_filters1**](ReportAttachmentsDevicesApi.md#update_device_attachment_filters1) | **PUT** /api/v1/reports/attachments/devices/{id}/filters | Update filters
[**update_device_attachment_settings**](ReportAttachmentsDevicesApi.md#update_device_attachment_settings) | **PUT** /api/v2/reports/attachments/devices/{id}/settings | Update devices report attachment
[**update_device_attachment_settings1**](ReportAttachmentsDevicesApi.md#update_device_attachment_settings1) | **PUT** /api/v1/reports/attachments/devices/{id}/settings | Update devices report attachment
[**update_device_attachment_visualization**](ReportAttachmentsDevicesApi.md#update_device_attachment_visualization) | **PUT** /api/v2/reports/attachments/devices/{id}/visualizations | Update devices report attachment
[**update_device_attachment_visualization1**](ReportAttachmentsDevicesApi.md#update_device_attachment_visualization1) | **PUT** /api/v1/reports/attachments/devices/{id}/visualizations | Update devices report attachment

# **create_device_attachment**
> DevicesResponseDto create_device_attachment(body, id)

Create devices attachment

Create a new devices attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.DevicesRequestDto() # DevicesRequestDto | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create devices attachment
    api_response = api_instance.create_device_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->create_device_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesRequestDto**](DevicesRequestDto.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**DevicesResponseDto**](DevicesResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_attachment1**
> DevicesResponseDtoV1 create_device_attachment1(body, id)

Create devices attachment

Create a new devices attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.DevicesRequestDtoV1() # DevicesRequestDtoV1 | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create devices attachment
    api_response = api_instance.create_device_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->create_device_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesRequestDtoV1**](DevicesRequestDtoV1.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**DevicesResponseDtoV1**](DevicesResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment**
> DevicesResponseDto get_device_attachment(id)

Get device attachment

Get an existing device attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
id = 789 # int | Device attachment id

try:
    # Get device attachment
    api_response = api_instance.get_device_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device attachment id | 

### Return type

[**DevicesResponseDto**](DevicesResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment1**
> DevicesResource get_device_attachment1(id)

Get devices report attachment

Get resources for devices attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
id = 789 # int | The id of devices report attachment

try:
    # Get devices report attachment
    api_response = api_instance.get_device_attachment1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesResource**](DevicesResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment2**
> DevicesResourceV1 get_device_attachment2(id)

Get devices report attachment

Get resources for devices attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
id = 789 # int | The id of devices report attachment

try:
    # Get devices report attachment
    api_response = api_instance.get_device_attachment2(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesResourceV1**](DevicesResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment_filter_schema**
> DeviceAttachmentFiltersSchema get_device_attachment_filter_schema()

Gets the filters schema

Gets the filters schema containing available filter fields and values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()

try:
    # Gets the filters schema
    api_response = api_instance.get_device_attachment_filter_schema()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment_filter_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceAttachmentFiltersSchema**](DeviceAttachmentFiltersSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment_filter_schema1**
> DeviceAttachmentFiltersSchema get_device_attachment_filter_schema1()

Gets the filters schema

Gets the filters schema containing available filter fields and values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()

try:
    # Gets the filters schema
    api_response = api_instance.get_device_attachment_filter_schema1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment_filter_schema1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceAttachmentFiltersSchema**](DeviceAttachmentFiltersSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment_filters**
> AttachmentFilters get_device_attachment_filters(id)

Get filters

Get the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
id = 789 # int | The id of the report attachment

try:
    # Get filters
    api_response = api_instance.get_device_attachment_filters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AttachmentFilters**](AttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment_filters1**
> AttachmentFilters get_device_attachment_filters1(id)

Get filters

Get the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
id = 789 # int | The id of the report attachment

try:
    # Get filters
    api_response = api_instance.get_device_attachment_filters1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment_filters1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AttachmentFilters**](AttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment_settings**
> DevicesSettings get_device_attachment_settings(id)

Get devices report attachment

Get devices attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
id = 789 # int | The id of devices report attachment

try:
    # Get devices report attachment
    api_response = api_instance.get_device_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesSettings**](DevicesSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment_settings1**
> DevicesSettingsV1 get_device_attachment_settings1(id)

Get devices report attachment

Get devices attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
id = 789 # int | The id of devices report attachment

try:
    # Get devices report attachment
    api_response = api_instance.get_device_attachment_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesSettingsV1**](DevicesSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment_visualization**
> DevicesVisualization get_device_attachment_visualization(id)

Get devices report attachment

Get devices attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
id = 789 # int | The id of devices report attachment

try:
    # Get devices report attachment
    api_response = api_instance.get_device_attachment_visualization(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesVisualization**](DevicesVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_attachment_visualization1**
> DevicesVisualizationV1 get_device_attachment_visualization1(id)

Get devices report attachment

Get devices attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
id = 789 # int | The id of devices report attachment

try:
    # Get devices report attachment
    api_response = api_instance.get_device_attachment_visualization1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->get_device_attachment_visualization1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesVisualizationV1**](DevicesVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_attachment**
> DevicesResource update_device_attachment(body, id)

Update devices report attachment

Update devices attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.DevicesResource() # DevicesResource | 
id = 789 # int | The id of devices report attachment

try:
    # Update devices report attachment
    api_response = api_instance.update_device_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->update_device_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesResource**](DevicesResource.md)|  | 
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesResource**](DevicesResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_attachment1**
> DevicesResourceV1 update_device_attachment1(body, id)

Update devices report attachment

Update devices attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.DevicesResourceV1() # DevicesResourceV1 | 
id = 789 # int | The id of devices report attachment

try:
    # Update devices report attachment
    api_response = api_instance.update_device_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->update_device_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesResourceV1**](DevicesResourceV1.md)|  | 
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesResourceV1**](DevicesResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_attachment_filters**
> AttachmentFilters update_device_attachment_filters(body, id)

Update filters

Updates the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.AttachmentFilters() # AttachmentFilters | 
id = 789 # int | The id of the report attachment

try:
    # Update filters
    api_response = api_instance.update_device_attachment_filters(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->update_device_attachment_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttachmentFilters**](AttachmentFilters.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AttachmentFilters**](AttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_attachment_filters1**
> AttachmentFilters update_device_attachment_filters1(body, id)

Update filters

Updates the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.AttachmentFilters() # AttachmentFilters | 
id = 789 # int | The id of the report attachment

try:
    # Update filters
    api_response = api_instance.update_device_attachment_filters1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->update_device_attachment_filters1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttachmentFilters**](AttachmentFilters.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AttachmentFilters**](AttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_attachment_settings**
> DevicesSettings update_device_attachment_settings(body, id)

Update devices report attachment

Update device attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.DevicesSettings() # DevicesSettings | 
id = 789 # int | The id of devices report attachment

try:
    # Update devices report attachment
    api_response = api_instance.update_device_attachment_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->update_device_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesSettings**](DevicesSettings.md)|  | 
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesSettings**](DevicesSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_attachment_settings1**
> DevicesSettingsV1 update_device_attachment_settings1(body, id)

Update devices report attachment

Update device attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.DevicesSettingsV1() # DevicesSettingsV1 | 
id = 789 # int | The id of devices report attachment

try:
    # Update devices report attachment
    api_response = api_instance.update_device_attachment_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->update_device_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesSettingsV1**](DevicesSettingsV1.md)|  | 
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesSettingsV1**](DevicesSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_attachment_visualization**
> DevicesVisualization update_device_attachment_visualization(body, id)

Update devices report attachment

Update devices attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.DevicesVisualization() # DevicesVisualization | 
id = 789 # int | The id of devices report attachment

try:
    # Update devices report attachment
    api_response = api_instance.update_device_attachment_visualization(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->update_device_attachment_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesVisualization**](DevicesVisualization.md)|  | 
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesVisualization**](DevicesVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_attachment_visualization1**
> DevicesVisualizationV1 update_device_attachment_visualization1(body, id)

Update devices report attachment

Update devices attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsDevicesApi()
body = swagger_client.DevicesVisualizationV1() # DevicesVisualizationV1 | 
id = 789 # int | The id of devices report attachment

try:
    # Update devices report attachment
    api_response = api_instance.update_device_attachment_visualization1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsDevicesApi->update_device_attachment_visualization1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesVisualizationV1**](DevicesVisualizationV1.md)|  | 
 **id** | **int**| The id of devices report attachment | 

### Return type

[**DevicesVisualizationV1**](DevicesVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

