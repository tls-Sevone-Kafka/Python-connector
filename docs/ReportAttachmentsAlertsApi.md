# swagger_client.ReportAttachmentsAlertsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_attachment**](ReportAttachmentsAlertsApi.md#create_alert_attachment) | **POST** /api/v2/reports/{id}/attachments/alerts | Create alert report attachment
[**create_alert_attachment1**](ReportAttachmentsAlertsApi.md#create_alert_attachment1) | **POST** /api/v1/reports/{id}/attachments/alerts | Create alert report attachment
[**get_alert_attachment**](ReportAttachmentsAlertsApi.md#get_alert_attachment) | **GET** /api/v2/reports/attachments/alerts/{id} | Get alert attachment
[**get_alert_attachment_aggregation**](ReportAttachmentsAlertsApi.md#get_alert_attachment_aggregation) | **GET** /api/v2/reports/attachments/alerts/{id}/aggregation | Get attachment aggregation
[**get_alert_attachment_aggregation1**](ReportAttachmentsAlertsApi.md#get_alert_attachment_aggregation1) | **GET** /api/v1/reports/attachments/alerts/{id}/aggregation | Get attachment aggregation
[**get_alert_attachment_filter_schema**](ReportAttachmentsAlertsApi.md#get_alert_attachment_filter_schema) | **GET** /api/v2/reports/attachments/alerts/filters/schema | Gets the filters schema
[**get_alert_attachment_filter_schema1**](ReportAttachmentsAlertsApi.md#get_alert_attachment_filter_schema1) | **GET** /api/v1/reports/attachments/alerts/filters/schema | Gets the filters schema
[**get_alert_attachment_filters**](ReportAttachmentsAlertsApi.md#get_alert_attachment_filters) | **GET** /api/v2/reports/attachments/alerts/{id}/filters | Get filters
[**get_alert_attachment_filters1**](ReportAttachmentsAlertsApi.md#get_alert_attachment_filters1) | **GET** /api/v1/reports/attachments/alerts/{id}/filters | Get filters
[**get_alert_attachment_resource**](ReportAttachmentsAlertsApi.md#get_alert_attachment_resource) | **GET** /api/v2/reports/attachments/alerts/{id}/resources | Get alert attachment resources
[**get_alert_attachment_resource1**](ReportAttachmentsAlertsApi.md#get_alert_attachment_resource1) | **GET** /api/v1/reports/attachments/alerts/{id}/resources | Get alert attachment resources
[**get_alert_attachment_settings**](ReportAttachmentsAlertsApi.md#get_alert_attachment_settings) | **GET** /api/v2/reports/attachments/alerts/{id}/settings | Get attachment settings
[**get_alert_attachment_settings1**](ReportAttachmentsAlertsApi.md#get_alert_attachment_settings1) | **GET** /api/v1/reports/attachments/alerts/{id}/settings | Get attachment settings
[**get_alert_attachment_time_settings**](ReportAttachmentsAlertsApi.md#get_alert_attachment_time_settings) | **GET** /api/v2/reports/attachments/alerts/{id}/time | Get alert attachment time settings
[**get_alert_attachment_time_settings1**](ReportAttachmentsAlertsApi.md#get_alert_attachment_time_settings1) | **GET** /api/v1/reports/attachments/alerts/{id}/time | Get alert attachment time settings
[**get_alert_attachment_visualization_settings**](ReportAttachmentsAlertsApi.md#get_alert_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/alerts/{id}/visualizations | Get attachment visualization settings
[**get_alert_attachment_visualization_settings1**](ReportAttachmentsAlertsApi.md#get_alert_attachment_visualization_settings1) | **GET** /api/v1/reports/attachments/alerts/{id}/visualizations | Get attachment visualization settings
[**partially_update_alert_attachment_visualization_settings**](ReportAttachmentsAlertsApi.md#partially_update_alert_attachment_visualization_settings) | **PATCH** /api/v2/reports/attachments/alerts/{id}/visualizations | Partially update visualization settings
[**partially_update_alert_attachment_visualization_settings1**](ReportAttachmentsAlertsApi.md#partially_update_alert_attachment_visualization_settings1) | **PATCH** /api/v1/reports/attachments/alerts/{id}/visualizations | Partially update visualization settings
[**update_alert_attachment_aggregation**](ReportAttachmentsAlertsApi.md#update_alert_attachment_aggregation) | **PUT** /api/v2/reports/attachments/alerts/{id}/aggregation | Update attachment aggregation
[**update_alert_attachment_aggregation1**](ReportAttachmentsAlertsApi.md#update_alert_attachment_aggregation1) | **PUT** /api/v1/reports/attachments/alerts/{id}/aggregation | Update attachment aggregation
[**update_alert_attachment_filters**](ReportAttachmentsAlertsApi.md#update_alert_attachment_filters) | **PUT** /api/v2/reports/attachments/alerts/{id}/filters | Update filters
[**update_alert_attachment_filters1**](ReportAttachmentsAlertsApi.md#update_alert_attachment_filters1) | **PUT** /api/v1/reports/attachments/alerts/{id}/filters | Update filters
[**update_alert_attachment_resource**](ReportAttachmentsAlertsApi.md#update_alert_attachment_resource) | **PUT** /api/v2/reports/attachments/alerts/{id}/resources | Update alert attachment resource
[**update_alert_attachment_resource1**](ReportAttachmentsAlertsApi.md#update_alert_attachment_resource1) | **PUT** /api/v1/reports/attachments/alerts/{id}/resources | Update alert attachment resource
[**update_alert_attachment_settings**](ReportAttachmentsAlertsApi.md#update_alert_attachment_settings) | **PUT** /api/v2/reports/attachments/alerts/{id}/settings | Update attachment settings
[**update_alert_attachment_settings1**](ReportAttachmentsAlertsApi.md#update_alert_attachment_settings1) | **PUT** /api/v1/reports/attachments/alerts/{id}/settings | Update attachment settings
[**update_alert_attachment_time_settings**](ReportAttachmentsAlertsApi.md#update_alert_attachment_time_settings) | **PUT** /api/v2/reports/attachments/alerts/{id}/time | Update alert attachment time settings
[**update_alert_attachment_time_settings1**](ReportAttachmentsAlertsApi.md#update_alert_attachment_time_settings1) | **PUT** /api/v1/reports/attachments/alerts/{id}/time | Update alert attachment time settings
[**update_alert_attachment_visualization_settings**](ReportAttachmentsAlertsApi.md#update_alert_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/alerts/{id}/visualizations | Update visualization settings
[**update_alert_attachment_visualization_settings1**](ReportAttachmentsAlertsApi.md#update_alert_attachment_visualization_settings1) | **PUT** /api/v1/reports/attachments/alerts/{id}/visualizations | Update visualization settings

# **create_alert_attachment**
> AlertAttachmentDto create_alert_attachment(body, id)

Create alert report attachment

Creates a new alert report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentCreateDto() # AlertAttachmentCreateDto | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create alert report attachment
    api_response = api_instance.create_alert_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->create_alert_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentCreateDto**](AlertAttachmentCreateDto.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**AlertAttachmentDto**](AlertAttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert_attachment1**
> AlertAttachmentResponseDtoV1 create_alert_attachment1(body, id)

Create alert report attachment

Creates a new alert report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentRequestDtoV1() # AlertAttachmentRequestDtoV1 | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create alert report attachment
    api_response = api_instance.create_alert_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->create_alert_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentRequestDtoV1**](AlertAttachmentRequestDtoV1.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**AlertAttachmentResponseDtoV1**](AlertAttachmentResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment**
> AlertAttachmentDto get_alert_attachment(id)

Get alert attachment

Get an existing alert attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | Alert attachment id

try:
    # Get alert attachment
    api_response = api_instance.get_alert_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert attachment id | 

### Return type

[**AlertAttachmentDto**](AlertAttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_aggregation**
> AlertAttachmentAggregation get_alert_attachment_aggregation(id)

Get attachment aggregation

Get alert attachment aggregation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment aggregation
    api_response = api_instance.get_alert_attachment_aggregation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_aggregation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentAggregation**](AlertAttachmentAggregation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_aggregation1**
> AlertAttachmentAggregation get_alert_attachment_aggregation1(id)

Get attachment aggregation

Get alert attachment aggregation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment aggregation
    api_response = api_instance.get_alert_attachment_aggregation1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_aggregation1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentAggregation**](AlertAttachmentAggregation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_filter_schema**
> AlertAttachmentFiltersSchema get_alert_attachment_filter_schema()

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
api_instance = swagger_client.ReportAttachmentsAlertsApi()

try:
    # Gets the filters schema
    api_response = api_instance.get_alert_attachment_filter_schema()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_filter_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertAttachmentFiltersSchema**](AlertAttachmentFiltersSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_filter_schema1**
> AlertAttachmentFiltersSchema get_alert_attachment_filter_schema1()

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
api_instance = swagger_client.ReportAttachmentsAlertsApi()

try:
    # Gets the filters schema
    api_response = api_instance.get_alert_attachment_filter_schema1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_filter_schema1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertAttachmentFiltersSchema**](AlertAttachmentFiltersSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_filters**
> AttachmentFilters get_alert_attachment_filters(id)

Get filters

Gets the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get filters
    api_response = api_instance.get_alert_attachment_filters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_filters: %s\n" % e)
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

# **get_alert_attachment_filters1**
> AttachmentFilters get_alert_attachment_filters1(id)

Get filters

Gets the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get filters
    api_response = api_instance.get_alert_attachment_filters1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_filters1: %s\n" % e)
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

# **get_alert_attachment_resource**
> list[AlertAttachmentResource] get_alert_attachment_resource(id)

Get alert attachment resources

Get alert attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get alert attachment resources
    api_response = api_instance.get_alert_attachment_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**list[AlertAttachmentResource]**](AlertAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_resource1**
> AlertAttachmentResourceV1 get_alert_attachment_resource1(id)

Get alert attachment resources

Get alert attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get alert attachment resources
    api_response = api_instance.get_alert_attachment_resource1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_resource1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentResourceV1**](AlertAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_settings**
> AlertAttachmentSettings get_alert_attachment_settings(id)

Get attachment settings

Get alert attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_alert_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentSettings**](AlertAttachmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_settings1**
> AlertAttachmentSettingsV1 get_alert_attachment_settings1(id)

Get attachment settings

Get alert attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_alert_attachment_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentSettingsV1**](AlertAttachmentSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_time_settings**
> TimeSettings get_alert_attachment_time_settings(id)

Get alert attachment time settings

Get alert attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get alert attachment time settings
    api_response = api_instance.get_alert_attachment_time_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_time_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TimeSettings**](TimeSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_time_settings1**
> TimeSettingV1 get_alert_attachment_time_settings1(id)

Get alert attachment time settings

Get alert attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get alert attachment time settings
    api_response = api_instance.get_alert_attachment_time_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_time_settings1: %s\n" % e)
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

# **get_alert_attachment_visualization_settings**
> AlertAttachmentVisualization get_alert_attachment_visualization_settings(id)

Get attachment visualization settings

Get alert attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_alert_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentVisualization**](AlertAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_attachment_visualization_settings1**
> AlertAttachmentVisualizationV1 get_alert_attachment_visualization_settings1(id)

Get attachment visualization settings

Get alert attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_alert_attachment_visualization_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->get_alert_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentVisualizationV1**](AlertAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_alert_attachment_visualization_settings**
> AlertAttachmentVisualization partially_update_alert_attachment_visualization_settings(body, id)

Partially update visualization settings

Partial update alert attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentVisualization() # AlertAttachmentVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_alert_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->partially_update_alert_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentVisualization**](AlertAttachmentVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentVisualization**](AlertAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_alert_attachment_visualization_settings1**
> AlertAttachmentVisualizationV1 partially_update_alert_attachment_visualization_settings1(body, id)

Partially update visualization settings

Partial update alert attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentVisualizationV1() # AlertAttachmentVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_alert_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->partially_update_alert_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentVisualizationV1**](AlertAttachmentVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentVisualizationV1**](AlertAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_attachment_aggregation**
> AlertAttachmentAggregation update_alert_attachment_aggregation(body, id)

Update attachment aggregation

Update alert attachment aggregation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentAggregation() # AlertAttachmentAggregation | 
id = 789 # int | The id of the report attachment

try:
    # Update attachment aggregation
    api_response = api_instance.update_alert_attachment_aggregation(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_aggregation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentAggregation**](AlertAttachmentAggregation.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentAggregation**](AlertAttachmentAggregation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_attachment_aggregation1**
> AlertAttachmentAggregation update_alert_attachment_aggregation1(body, id)

Update attachment aggregation

Update alert attachment aggregation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentAggregation() # AlertAttachmentAggregation | 
id = 789 # int | The id of the report attachment

try:
    # Update attachment aggregation
    api_response = api_instance.update_alert_attachment_aggregation1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_aggregation1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentAggregation**](AlertAttachmentAggregation.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentAggregation**](AlertAttachmentAggregation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_attachment_filters**
> AttachmentFilters update_alert_attachment_filters(body, id)

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
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AttachmentFilters() # AttachmentFilters | 
id = 789 # int | The id of the report attachment

try:
    # Update filters
    api_response = api_instance.update_alert_attachment_filters(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_filters: %s\n" % e)
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

# **update_alert_attachment_filters1**
> AttachmentFilters update_alert_attachment_filters1(body, id)

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
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AttachmentFilters() # AttachmentFilters | 
id = 789 # int | The id of the report attachment

try:
    # Update filters
    api_response = api_instance.update_alert_attachment_filters1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_filters1: %s\n" % e)
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

# **update_alert_attachment_resource**
> list[AlertAttachmentResource] update_alert_attachment_resource(body, id)

Update alert attachment resource

Update alert attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = [swagger_client.AlertAttachmentResource()] # list[AlertAttachmentResource] | 
id = 789 # int | The id of the report attachment

try:
    # Update alert attachment resource
    api_response = api_instance.update_alert_attachment_resource(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AlertAttachmentResource]**](AlertAttachmentResource.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**list[AlertAttachmentResource]**](AlertAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_attachment_resource1**
> AlertAttachmentResourceV1 update_alert_attachment_resource1(body, id)

Update alert attachment resource

Update alert attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentResourceV1() # AlertAttachmentResourceV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update alert attachment resource
    api_response = api_instance.update_alert_attachment_resource1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_resource1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentResourceV1**](AlertAttachmentResourceV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentResourceV1**](AlertAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_attachment_settings**
> AlertAttachmentSettings update_alert_attachment_settings(body, id)

Update attachment settings

Update alert attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentSettings() # AlertAttachmentSettings | 
id = 789 # int | The id of the report attachment

try:
    # Update attachment settings
    api_response = api_instance.update_alert_attachment_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentSettings**](AlertAttachmentSettings.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentSettings**](AlertAttachmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_attachment_settings1**
> AlertAttachmentSettingsV1 update_alert_attachment_settings1(body, id)

Update attachment settings

Update alert attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentSettingsV1() # AlertAttachmentSettingsV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update attachment settings
    api_response = api_instance.update_alert_attachment_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentSettingsV1**](AlertAttachmentSettingsV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentSettingsV1**](AlertAttachmentSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_attachment_time_settings**
> TimeSettings update_alert_attachment_time_settings(body, id)

Update alert attachment time settings

Update alert attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.TimeSettings() # TimeSettings | 
id = 789 # int | The id of the report attachment

try:
    # Update alert attachment time settings
    api_response = api_instance.update_alert_attachment_time_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_time_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeSettings**](TimeSettings.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**TimeSettings**](TimeSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_attachment_time_settings1**
> TimeSettingV1 update_alert_attachment_time_settings1(body, id)

Update alert attachment time settings

Update alert attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.TimeSettingV1() # TimeSettingV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update alert attachment time settings
    api_response = api_instance.update_alert_attachment_time_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_time_settings1: %s\n" % e)
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

# **update_alert_attachment_visualization_settings**
> AlertAttachmentVisualization update_alert_attachment_visualization_settings(body, id)

Update visualization settings

Update alert attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentVisualization() # AlertAttachmentVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_alert_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentVisualization**](AlertAttachmentVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentVisualization**](AlertAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_attachment_visualization_settings1**
> AlertAttachmentVisualizationV1 update_alert_attachment_visualization_settings1(body, id)

Update visualization settings

Update alert attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsAlertsApi()
body = swagger_client.AlertAttachmentVisualizationV1() # AlertAttachmentVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_alert_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsAlertsApi->update_alert_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAttachmentVisualizationV1**](AlertAttachmentVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertAttachmentVisualizationV1**](AlertAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

