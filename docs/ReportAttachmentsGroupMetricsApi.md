# swagger_client.ReportAttachmentsGroupMetricsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_metrics_attachment**](ReportAttachmentsGroupMetricsApi.md#create_group_metrics_attachment) | **POST** /api/v2/reports/{id}/attachments/group-metrics | Create group metrics report attachment
[**create_group_metrics_attachment1**](ReportAttachmentsGroupMetricsApi.md#create_group_metrics_attachment1) | **POST** /api/v1/reports/{id}/attachments/group-metrics | Create group metrics report attachment
[**get_group_metrics_attachment**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment) | **GET** /api/v2/reports/attachments/group-metrics/{id} | Get group metrics attachment
[**get_group_metrics_attachment1**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment1) | **GET** /api/v2/reports/attachments/group-metrics/{id}/resources | Get group metrics report attachment
[**get_group_metrics_attachment2**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment2) | **GET** /api/v1/reports/attachments/group-metrics/{id}/resources | Get group metrics report attachment
[**get_group_metrics_attachment_settings**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_settings) | **GET** /api/v2/reports/attachments/group-metrics/{id}/settings | Get group metrics report attachment
[**get_group_metrics_attachment_settings1**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_settings1) | **GET** /api/v1/reports/attachments/group-metrics/{id}/settings | Get group metrics report attachment
[**get_group_metrics_attachment_time_settings**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_time_settings) | **GET** /api/v2/reports/attachments/group-metrics/{id}/time | Get group metrics report attachment
[**get_group_metrics_attachment_time_settings1**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_time_settings1) | **GET** /api/v1/reports/attachments/group-metrics/{id}/time | Get group metrics report attachment
[**get_group_metrics_attachment_visualization**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_visualization) | **GET** /api/v2/reports/attachments/group-metrics/{id}/visualization | Get group metrics report attachment
[**get_group_metrics_attachment_visualization1**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_visualization1) | **GET** /api/v1/reports/attachments/group-metrics/{id}/visualization | Get group metrics report attachment
[**update_group_metrics_attachment**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment) | **PUT** /api/v2/reports/attachments/group-metrics/{id}/resources | Update group metrics report attachment
[**update_group_metrics_attachment1**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment1) | **PUT** /api/v1/reports/attachments/group-metrics/{id}/resources | Update group metrics report attachment
[**update_group_metrics_attachment_settings**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_settings) | **PUT** /api/v2/reports/attachments/group-metrics/{id}/settings | Update group metrics report attachment
[**update_group_metrics_attachment_settings1**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_settings1) | **PUT** /api/v1/reports/attachments/group-metrics/{id}/settings | Update group metrics report attachment
[**update_group_metrics_attachment_time_settings**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_time_settings) | **PUT** /api/v2/reports/attachments/group-metrics/{id}/time | Update group metrics report attachment
[**update_group_metrics_attachment_time_settings1**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_time_settings1) | **PUT** /api/v1/reports/attachments/group-metrics/{id}/time | Update group metrics report attachment
[**update_group_metrics_attachment_visualization**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_visualization) | **PUT** /api/v2/reports/attachments/group-metrics/{id}/visualization | Update group metrics report attachment
[**update_group_metrics_attachment_visualization1**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_visualization1) | **PUT** /api/v1/reports/attachments/group-metrics/{id}/visualization | Update group metrics report attachment

# **create_group_metrics_attachment**
> GroupMetricsResponseDto create_group_metrics_attachment(body, id)

Create group metrics report attachment

Creates a new group metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.GroupMetricsRequestDto() # GroupMetricsRequestDto | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create group metrics report attachment
    api_response = api_instance.create_group_metrics_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->create_group_metrics_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupMetricsRequestDto**](GroupMetricsRequestDto.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**GroupMetricsResponseDto**](GroupMetricsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_metrics_attachment1**
> GroupMetricsResponseDtoV1 create_group_metrics_attachment1(body, id)

Create group metrics report attachment

Creates a new group metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.GroupMetricsRequestDtoV1() # GroupMetricsRequestDtoV1 | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create group metrics report attachment
    api_response = api_instance.create_group_metrics_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->create_group_metrics_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupMetricsRequestDtoV1**](GroupMetricsRequestDtoV1.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**GroupMetricsResponseDtoV1**](GroupMetricsResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment**
> GroupMetricsResponseDto get_group_metrics_attachment(id)

Get group metrics attachment

Get an existing group metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | Group metrics attachment id

try:
    # Get group metrics attachment
    api_response = api_instance.get_group_metrics_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group metrics attachment id | 

### Return type

[**GroupMetricsResponseDto**](GroupMetricsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment1**
> GroupMetricsResource get_group_metrics_attachment1(id)

Get group metrics report attachment

Get group metrics attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsResource**](GroupMetricsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment2**
> GroupMetricsResourceV1 get_group_metrics_attachment2(id)

Get group metrics report attachment

Get group metrics attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment2(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsResourceV1**](GroupMetricsResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_settings**
> GroupMetricsSettingsDto get_group_metrics_attachment_settings(id)

Get group metrics report attachment

Get group metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsSettingsDto**](GroupMetricsSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_settings1**
> GroupMetricsSettingsDtoV1 get_group_metrics_attachment_settings1(id)

Get group metrics report attachment

Get group metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsSettingsDtoV1**](GroupMetricsSettingsDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_time_settings**
> TimeSetting get_group_metrics_attachment_time_settings(id)

Get group metrics report attachment

Get group metrics attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_time_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_time_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TimeSetting**](TimeSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_time_settings1**
> TimeSettingV1 get_group_metrics_attachment_time_settings1(id)

Get group metrics report attachment

Get group metrics attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_time_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_time_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TimeSettingV1**](TimeSettingV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_visualization**
> GroupMetricsVisualization get_group_metrics_attachment_visualization(id)

Get group metrics report attachment

Get group metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_visualization(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsVisualization**](GroupMetricsVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_visualization1**
> GroupMetricsVisualizationV1 get_group_metrics_attachment_visualization1(id)

Get group metrics report attachment

Get group metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_visualization1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_visualization1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsVisualizationV1**](GroupMetricsVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment**
> GroupMetricsResource update_group_metrics_attachment(body, id)

Update group metrics report attachment

Update group metrics attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.GroupMetricsResource() # GroupMetricsResource | 
id = 789 # int | The id of the report attachment

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupMetricsResource**](GroupMetricsResource.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsResource**](GroupMetricsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment1**
> GroupMetricsResourceV1 update_group_metrics_attachment1(body, id)

Update group metrics report attachment

Update group metrics attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.GroupMetricsResourceV1() # GroupMetricsResourceV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupMetricsResourceV1**](GroupMetricsResourceV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsResourceV1**](GroupMetricsResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_settings**
> GroupMetricsSettingsDto update_group_metrics_attachment_settings(body, id)

Update group metrics report attachment

Update group metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.GroupMetricsSettingsDto() # GroupMetricsSettingsDto | 
id = 789 # int | The id of the report attachment

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupMetricsSettingsDto**](GroupMetricsSettingsDto.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsSettingsDto**](GroupMetricsSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_settings1**
> GroupMetricsSettingsDtoV1 update_group_metrics_attachment_settings1(body, id)

Update group metrics report attachment

Update group metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.GroupMetricsSettingsDtoV1() # GroupMetricsSettingsDtoV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupMetricsSettingsDtoV1**](GroupMetricsSettingsDtoV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsSettingsDtoV1**](GroupMetricsSettingsDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_time_settings**
> TimeSetting update_group_metrics_attachment_time_settings(body, id)

Update group metrics report attachment

Update group metrics attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.TimeSetting() # TimeSetting | 
id = 789 # int | The id of the report attachment

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_time_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_time_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSetting**](TimeSetting.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**TimeSetting**](TimeSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_time_settings1**
> TimeSettingV1 update_group_metrics_attachment_time_settings1(body, id)

Update group metrics report attachment

Update group metrics attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.TimeSettingV1() # TimeSettingV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_time_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_time_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSettingV1**](TimeSettingV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**TimeSettingV1**](TimeSettingV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_visualization**
> GroupMetricsVisualization update_group_metrics_attachment_visualization(body, id)

Update group metrics report attachment

Update group metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.GroupMetricsVisualization() # GroupMetricsVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_visualization(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupMetricsVisualization**](GroupMetricsVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsVisualization**](GroupMetricsVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_visualization1**
> GroupMetricsVisualizationV1 update_group_metrics_attachment_visualization1(body, id)

Update group metrics report attachment

Update group metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
body = swagger_client.GroupMetricsVisualizationV1() # GroupMetricsVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_visualization1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_visualization1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupMetricsVisualizationV1**](GroupMetricsVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsVisualizationV1**](GroupMetricsVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

