# swagger_client.ReportAttachmentsPerformanceMetricsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_performance_metrics_attachment**](ReportAttachmentsPerformanceMetricsApi.md#create_performance_metrics_attachment) | **POST** /api/v2/reports/{id}/attachments/performance-metrics | Create performance metrics attachment
[**create_performance_metrics_attachment1**](ReportAttachmentsPerformanceMetricsApi.md#create_performance_metrics_attachment1) | **POST** /api/v1/reports/{id}/attachments/performance-metrics | Create performance metrics attachment
[**get_performance_metrics_attachment**](ReportAttachmentsPerformanceMetricsApi.md#get_performance_metrics_attachment) | **GET** /api/v2/reports/attachments/performance-metrics/{id} | Get performance metrics attachment
[**get_performance_metrics_attachment_resources**](ReportAttachmentsPerformanceMetricsApi.md#get_performance_metrics_attachment_resources) | **GET** /api/v2/reports/attachments/performance-metrics/{id}/resources | Get resources
[**get_performance_metrics_attachment_resources1**](ReportAttachmentsPerformanceMetricsApi.md#get_performance_metrics_attachment_resources1) | **GET** /api/v1/reports/attachments/performance-metrics/{id}/resources | Get resources
[**get_performance_metrics_attachment_settings**](ReportAttachmentsPerformanceMetricsApi.md#get_performance_metrics_attachment_settings) | **GET** /api/v2/reports/attachments/performance-metrics/{id}/settings | Get attachment settings
[**get_performance_metrics_attachment_settings1**](ReportAttachmentsPerformanceMetricsApi.md#get_performance_metrics_attachment_settings1) | **GET** /api/v1/reports/attachments/performance-metrics/{id}/settings | Get attachment settings
[**get_performance_metrics_attachment_time_settings**](ReportAttachmentsPerformanceMetricsApi.md#get_performance_metrics_attachment_time_settings) | **GET** /api/v2/reports/attachments/performance-metrics/{id}/time | GET time ranges
[**get_performance_metrics_attachment_time_settings1**](ReportAttachmentsPerformanceMetricsApi.md#get_performance_metrics_attachment_time_settings1) | **GET** /api/v1/reports/attachments/performance-metrics/{id}/time | GET time ranges
[**get_performance_metrics_attachment_visualization_settings**](ReportAttachmentsPerformanceMetricsApi.md#get_performance_metrics_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/performance-metrics/{id}/visualizations | Get attachment visualization settings
[**get_performance_metrics_attachment_visualization_settings1**](ReportAttachmentsPerformanceMetricsApi.md#get_performance_metrics_attachment_visualization_settings1) | **GET** /api/v1/reports/attachments/performance-metrics/{id}/visualizations | Get attachment visualization settings
[**partially_update_performance_metrics_attachment_settings**](ReportAttachmentsPerformanceMetricsApi.md#partially_update_performance_metrics_attachment_settings) | **PATCH** /api/v2/reports/attachments/performance-metrics/{id}/settings | Partially update attachment settings
[**partially_update_performance_metrics_attachment_settings1**](ReportAttachmentsPerformanceMetricsApi.md#partially_update_performance_metrics_attachment_settings1) | **PATCH** /api/v1/reports/attachments/performance-metrics/{id}/settings | Partially update attachment settings
[**partially_update_performance_metrics_attachment_visualization_settings**](ReportAttachmentsPerformanceMetricsApi.md#partially_update_performance_metrics_attachment_visualization_settings) | **PATCH** /api/v2/reports/attachments/performance-metrics/{id}/visualizations | Partially update visualization settings
[**partially_update_performance_metrics_attachment_visualization_settings1**](ReportAttachmentsPerformanceMetricsApi.md#partially_update_performance_metrics_attachment_visualization_settings1) | **PATCH** /api/v1/reports/attachments/performance-metrics/{id}/visualizations | Partially update visualization settings
[**update_performance_metrics_attachment_resources**](ReportAttachmentsPerformanceMetricsApi.md#update_performance_metrics_attachment_resources) | **PUT** /api/v2/reports/attachments/performance-metrics/{id}/resources | Update resources
[**update_performance_metrics_attachment_resources1**](ReportAttachmentsPerformanceMetricsApi.md#update_performance_metrics_attachment_resources1) | **PUT** /api/v1/reports/attachments/performance-metrics/{id}/resources | Update resources
[**update_performance_metrics_attachment_settings**](ReportAttachmentsPerformanceMetricsApi.md#update_performance_metrics_attachment_settings) | **PUT** /api/v2/reports/attachments/performance-metrics/{id}/settings | Update attachment settings
[**update_performance_metrics_attachment_settings1**](ReportAttachmentsPerformanceMetricsApi.md#update_performance_metrics_attachment_settings1) | **PUT** /api/v1/reports/attachments/performance-metrics/{id}/settings | Update attachment settings
[**update_performance_metrics_attachment_time_settings**](ReportAttachmentsPerformanceMetricsApi.md#update_performance_metrics_attachment_time_settings) | **PUT** /api/v2/reports/attachments/performance-metrics/{id}/time | Update time ranges
[**update_performance_metrics_attachment_time_settings1**](ReportAttachmentsPerformanceMetricsApi.md#update_performance_metrics_attachment_time_settings1) | **PUT** /api/v1/reports/attachments/performance-metrics/{id}/time | Update time ranges
[**update_performance_metrics_attachment_visualization_settings**](ReportAttachmentsPerformanceMetricsApi.md#update_performance_metrics_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/performance-metrics/{id}/visualizations | Update visualization settings
[**update_performance_metrics_attachment_visualization_settings1**](ReportAttachmentsPerformanceMetricsApi.md#update_performance_metrics_attachment_visualization_settings1) | **PUT** /api/v1/reports/attachments/performance-metrics/{id}/visualizations | Update visualization settings

# **create_performance_metrics_attachment**
> PerformanceMetricsResponseDto create_performance_metrics_attachment(body, id)

Create performance metrics attachment

Create a new performance metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsRequestDto() # PerformanceMetricsRequestDto | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create performance metrics attachment
    api_response = api_instance.create_performance_metrics_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->create_performance_metrics_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsRequestDto**](PerformanceMetricsRequestDto.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**PerformanceMetricsResponseDto**](PerformanceMetricsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_performance_metrics_attachment1**
> PerformanceMetricsResponseDtoV1 create_performance_metrics_attachment1(body, id)

Create performance metrics attachment

Create a new performance metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsRequestDtoV1() # PerformanceMetricsRequestDtoV1 | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create performance metrics attachment
    api_response = api_instance.create_performance_metrics_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->create_performance_metrics_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsRequestDtoV1**](PerformanceMetricsRequestDtoV1.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**PerformanceMetricsResponseDtoV1**](PerformanceMetricsResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_metrics_attachment**
> PerformanceMetricsResponseDto get_performance_metrics_attachment(id)

Get performance metrics attachment

Get an existing performance metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
id = 789 # int | Performance metrics attachment id

try:
    # Get performance metrics attachment
    api_response = api_instance.get_performance_metrics_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->get_performance_metrics_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Performance metrics attachment id | 

### Return type

[**PerformanceMetricsResponseDto**](PerformanceMetricsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_metrics_attachment_resources**
> list[PerformanceMetricsResource] get_performance_metrics_attachment_resources(id)

Get resources

Get performance metrics resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_performance_metrics_attachment_resources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->get_performance_metrics_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**list[PerformanceMetricsResource]**](PerformanceMetricsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_metrics_attachment_resources1**
> PerformanceMetricsResourceV1 get_performance_metrics_attachment_resources1(id)

Get resources

Get performance metrics resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_performance_metrics_attachment_resources1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->get_performance_metrics_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsResourceV1**](PerformanceMetricsResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_metrics_attachment_settings**
> PerformanceMetricsSettings get_performance_metrics_attachment_settings(id)

Get attachment settings

Get performance metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_performance_metrics_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->get_performance_metrics_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsSettings**](PerformanceMetricsSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_metrics_attachment_settings1**
> PerformanceMetricsSettingsV1 get_performance_metrics_attachment_settings1(id)

Get attachment settings

Get performance metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_performance_metrics_attachment_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->get_performance_metrics_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsSettingsV1**](PerformanceMetricsSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_metrics_attachment_time_settings**
> TimeSetting get_performance_metrics_attachment_time_settings(id)

GET time ranges

Get performance metrics time ranges

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # GET time ranges
    api_response = api_instance.get_performance_metrics_attachment_time_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->get_performance_metrics_attachment_time_settings: %s\n" % e)
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

# **get_performance_metrics_attachment_time_settings1**
> TimeSettingV1 get_performance_metrics_attachment_time_settings1(id)

GET time ranges

Get performance metrics time ranges

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # GET time ranges
    api_response = api_instance.get_performance_metrics_attachment_time_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->get_performance_metrics_attachment_time_settings1: %s\n" % e)
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

# **get_performance_metrics_attachment_visualization_settings**
> PerformanceMetricsVisualization get_performance_metrics_attachment_visualization_settings(id)

Get attachment visualization settings

Get performance metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_performance_metrics_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->get_performance_metrics_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsVisualization**](PerformanceMetricsVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_metrics_attachment_visualization_settings1**
> PerformanceMetricsVisualizationV1 get_performance_metrics_attachment_visualization_settings1(id)

Get attachment visualization settings

Get performance metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_performance_metrics_attachment_visualization_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->get_performance_metrics_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsVisualizationV1**](PerformanceMetricsVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_performance_metrics_attachment_settings**
> PerformanceMetricsSettings partially_update_performance_metrics_attachment_settings(body, id)

Partially update attachment settings

Partially update performance metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsSettings() # PerformanceMetricsSettings | 
id = 789 # int | The id of the report attachment

try:
    # Partially update attachment settings
    api_response = api_instance.partially_update_performance_metrics_attachment_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->partially_update_performance_metrics_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsSettings**](PerformanceMetricsSettings.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsSettings**](PerformanceMetricsSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_performance_metrics_attachment_settings1**
> PerformanceMetricsSettingsV1 partially_update_performance_metrics_attachment_settings1(body, id)

Partially update attachment settings

Partially update performance metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsSettingsV1() # PerformanceMetricsSettingsV1 | 
id = 789 # int | The id of the report attachment

try:
    # Partially update attachment settings
    api_response = api_instance.partially_update_performance_metrics_attachment_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->partially_update_performance_metrics_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsSettingsV1**](PerformanceMetricsSettingsV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsSettingsV1**](PerformanceMetricsSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_performance_metrics_attachment_visualization_settings**
> PerformanceMetricsVisualization partially_update_performance_metrics_attachment_visualization_settings(body, id)

Partially update visualization settings

Partially update performance metrics visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsVisualization() # PerformanceMetricsVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_performance_metrics_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->partially_update_performance_metrics_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsVisualization**](PerformanceMetricsVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsVisualization**](PerformanceMetricsVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_performance_metrics_attachment_visualization_settings1**
> PerformanceMetricsVisualizationV1 partially_update_performance_metrics_attachment_visualization_settings1(body, id)

Partially update visualization settings

Partially update performance metrics visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsVisualizationV1() # PerformanceMetricsVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_performance_metrics_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->partially_update_performance_metrics_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsVisualizationV1**](PerformanceMetricsVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsVisualizationV1**](PerformanceMetricsVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_performance_metrics_attachment_resources**
> list[PerformanceMetricsResource] update_performance_metrics_attachment_resources(body, id)

Update resources

Update performance metrics resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = [swagger_client.PerformanceMetricsResource()] # list[PerformanceMetricsResource] | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_performance_metrics_attachment_resources(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->update_performance_metrics_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PerformanceMetricsResource]**](PerformanceMetricsResource.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**list[PerformanceMetricsResource]**](PerformanceMetricsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_performance_metrics_attachment_resources1**
> PerformanceMetricsResourceV1 update_performance_metrics_attachment_resources1(body, id)

Update resources

Update performance metrics resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsResourceV1() # PerformanceMetricsResourceV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_performance_metrics_attachment_resources1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->update_performance_metrics_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsResourceV1**](PerformanceMetricsResourceV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsResourceV1**](PerformanceMetricsResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_performance_metrics_attachment_settings**
> PerformanceMetricsSettings update_performance_metrics_attachment_settings(body, id)

Update attachment settings

Update performance metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsSettings() # PerformanceMetricsSettings | 
id = 789 # int | The id of the report attachment

try:
    # Update attachment settings
    api_response = api_instance.update_performance_metrics_attachment_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->update_performance_metrics_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsSettings**](PerformanceMetricsSettings.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsSettings**](PerformanceMetricsSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_performance_metrics_attachment_settings1**
> PerformanceMetricsSettingsV1 update_performance_metrics_attachment_settings1(body, id)

Update attachment settings

Update performance metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsSettingsV1() # PerformanceMetricsSettingsV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update attachment settings
    api_response = api_instance.update_performance_metrics_attachment_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->update_performance_metrics_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsSettingsV1**](PerformanceMetricsSettingsV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsSettingsV1**](PerformanceMetricsSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_performance_metrics_attachment_time_settings**
> TimeSetting update_performance_metrics_attachment_time_settings(body, id)

Update time ranges

Update performance metrics time ranges

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.TimeSetting() # TimeSetting | 
id = 789 # int | The id of the report attachment

try:
    # Update time ranges
    api_response = api_instance.update_performance_metrics_attachment_time_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->update_performance_metrics_attachment_time_settings: %s\n" % e)
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

# **update_performance_metrics_attachment_time_settings1**
> TimeSettingV1 update_performance_metrics_attachment_time_settings1(body, id)

Update time ranges

Update performance metrics time ranges

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.TimeSettingV1() # TimeSettingV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update time ranges
    api_response = api_instance.update_performance_metrics_attachment_time_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->update_performance_metrics_attachment_time_settings1: %s\n" % e)
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

# **update_performance_metrics_attachment_visualization_settings**
> PerformanceMetricsVisualization update_performance_metrics_attachment_visualization_settings(body, id)

Update visualization settings

Update performance metrics visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsVisualization() # PerformanceMetricsVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_performance_metrics_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->update_performance_metrics_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsVisualization**](PerformanceMetricsVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsVisualization**](PerformanceMetricsVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_performance_metrics_attachment_visualization_settings1**
> PerformanceMetricsVisualizationV1 update_performance_metrics_attachment_visualization_settings1(body, id)

Update visualization settings

Update performance metrics visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsPerformanceMetricsApi()
body = swagger_client.PerformanceMetricsVisualizationV1() # PerformanceMetricsVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_performance_metrics_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsPerformanceMetricsApi->update_performance_metrics_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PerformanceMetricsVisualizationV1**](PerformanceMetricsVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**PerformanceMetricsVisualizationV1**](PerformanceMetricsVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

