# swagger_client.ReportAttachmentsObjectsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_attachment**](ReportAttachmentsObjectsApi.md#create_object_attachment) | **POST** /api/v2/reports/{id}/attachments/objects | Create objects attachment
[**create_object_attachment1**](ReportAttachmentsObjectsApi.md#create_object_attachment1) | **POST** /api/v1/reports/{id}/attachments/objects | Create objects attachment
[**get_object_attachment**](ReportAttachmentsObjectsApi.md#get_object_attachment) | **GET** /api/v2/reports/attachments/objects/{id} | Get object attachment
[**get_object_attachment_resources**](ReportAttachmentsObjectsApi.md#get_object_attachment_resources) | **GET** /api/v2/reports/attachments/objects/{id}/resources | Get resources
[**get_object_attachment_resources1**](ReportAttachmentsObjectsApi.md#get_object_attachment_resources1) | **GET** /api/v1/reports/attachments/objects/{id}/resources | Get resources
[**get_object_attachment_settings**](ReportAttachmentsObjectsApi.md#get_object_attachment_settings) | **GET** /api/v2/reports/attachments/objects/{id}/settings | Get attachment settings
[**get_object_attachment_settings1**](ReportAttachmentsObjectsApi.md#get_object_attachment_settings1) | **GET** /api/v1/reports/attachments/objects/{id}/settings | Get attachment settings
[**get_object_attachment_visualization_settings**](ReportAttachmentsObjectsApi.md#get_object_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/objects/{id}/visualizations | Get attachment visualization settings
[**get_object_attachment_visualization_settings1**](ReportAttachmentsObjectsApi.md#get_object_attachment_visualization_settings1) | **GET** /api/v1/reports/attachments/objects/{id}/visualizations | Get attachment visualization settings
[**partially_update_object_attachment_visualization_settings**](ReportAttachmentsObjectsApi.md#partially_update_object_attachment_visualization_settings) | **PATCH** /api/v2/reports/attachments/objects/{id}/visualizations | Partially update visualization settings
[**partially_update_object_attachment_visualization_settings1**](ReportAttachmentsObjectsApi.md#partially_update_object_attachment_visualization_settings1) | **PATCH** /api/v1/reports/attachments/objects/{id}/visualizations | Partially update visualization settings
[**update_object_attachment_resources**](ReportAttachmentsObjectsApi.md#update_object_attachment_resources) | **PUT** /api/v2/reports/attachments/objects/{id}/resources | Update resources
[**update_object_attachment_resources1**](ReportAttachmentsObjectsApi.md#update_object_attachment_resources1) | **PUT** /api/v1/reports/attachments/objects/{id}/resources | Update resources
[**update_object_attachment_settings**](ReportAttachmentsObjectsApi.md#update_object_attachment_settings) | **PUT** /api/v2/reports/attachments/objects/{id}/settings | Update attachment settings
[**update_object_attachment_settings1**](ReportAttachmentsObjectsApi.md#update_object_attachment_settings1) | **PUT** /api/v1/reports/attachments/objects/{id}/settings | Update attachment settings
[**update_object_attachment_visualization_settings**](ReportAttachmentsObjectsApi.md#update_object_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/objects/{id}/visualizations | Update visualization settings
[**update_object_attachment_visualization_settings1**](ReportAttachmentsObjectsApi.md#update_object_attachment_visualization_settings1) | **PUT** /api/v1/reports/attachments/objects/{id}/visualizations | Update visualization settings

# **create_object_attachment**
> ObjectAttachmentResponseDto create_object_attachment(body, id)

Create objects attachment

Create a new objects attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentRequestDto() # ObjectAttachmentRequestDto | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create objects attachment
    api_response = api_instance.create_object_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->create_object_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentRequestDto**](ObjectAttachmentRequestDto.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**ObjectAttachmentResponseDto**](ObjectAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_attachment1**
> ObjectAttachmentResponseDtoV1 create_object_attachment1(body, id)

Create objects attachment

Create a new objects attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentRequestDtoV1() # ObjectAttachmentRequestDtoV1 | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create objects attachment
    api_response = api_instance.create_object_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->create_object_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentRequestDtoV1**](ObjectAttachmentRequestDtoV1.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**ObjectAttachmentResponseDtoV1**](ObjectAttachmentResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_attachment**
> ObjectAttachmentResponseDto get_object_attachment(id)

Get object attachment

Get an existing object attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
id = 789 # int | Object attachment id

try:
    # Get object attachment
    api_response = api_instance.get_object_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->get_object_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Object attachment id | 

### Return type

[**ObjectAttachmentResponseDto**](ObjectAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_attachment_resources**
> ObjectAttachmentResource get_object_attachment_resources(id)

Get resources

Get Objects resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_object_attachment_resources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->get_object_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentResource**](ObjectAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_attachment_resources1**
> ObjectAttachmentResource get_object_attachment_resources1(id)

Get resources

Get Objects resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_object_attachment_resources1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->get_object_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentResource**](ObjectAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_attachment_settings**
> ObjectAttachmentSettings get_object_attachment_settings(id)

Get attachment settings

Get Objects attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_object_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->get_object_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentSettings**](ObjectAttachmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_attachment_settings1**
> ObjectAttachmentSettingsV1 get_object_attachment_settings1(id)

Get attachment settings

Get Objects attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_object_attachment_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->get_object_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentSettingsV1**](ObjectAttachmentSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_attachment_visualization_settings**
> ObjectAttachmentVisualization get_object_attachment_visualization_settings(id)

Get attachment visualization settings

Get objects attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_object_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->get_object_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentVisualization**](ObjectAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_attachment_visualization_settings1**
> ObjectAttachmentVisualizationV1 get_object_attachment_visualization_settings1(id)

Get attachment visualization settings

Get objects attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_object_attachment_visualization_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->get_object_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentVisualizationV1**](ObjectAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_attachment_visualization_settings**
> ObjectAttachmentVisualization partially_update_object_attachment_visualization_settings(body, id)

Partially update visualization settings

Partially update objects visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentVisualization() # ObjectAttachmentVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_object_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->partially_update_object_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentVisualization**](ObjectAttachmentVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentVisualization**](ObjectAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_attachment_visualization_settings1**
> ObjectAttachmentVisualizationV1 partially_update_object_attachment_visualization_settings1(body, id)

Partially update visualization settings

Partially update objects visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentVisualizationV1() # ObjectAttachmentVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_object_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->partially_update_object_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentVisualizationV1**](ObjectAttachmentVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentVisualizationV1**](ObjectAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_attachment_resources**
> ObjectAttachmentResource update_object_attachment_resources(body, id)

Update resources

Update Objects resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentResource() # ObjectAttachmentResource | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_object_attachment_resources(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->update_object_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentResource**](ObjectAttachmentResource.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentResource**](ObjectAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_attachment_resources1**
> ObjectAttachmentResource update_object_attachment_resources1(body, id)

Update resources

Update Objects resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentResource() # ObjectAttachmentResource | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_object_attachment_resources1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->update_object_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentResource**](ObjectAttachmentResource.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentResource**](ObjectAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_attachment_settings**
> ObjectAttachmentSettings update_object_attachment_settings(body, id)

Update attachment settings

Update Object attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentSettings() # ObjectAttachmentSettings | 
id = 789 # int | The id of the report attachment

try:
    # Update attachment settings
    api_response = api_instance.update_object_attachment_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->update_object_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentSettings**](ObjectAttachmentSettings.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentSettings**](ObjectAttachmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_attachment_settings1**
> ObjectAttachmentSettingsV1 update_object_attachment_settings1(body, id)

Update attachment settings

Update Object attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentSettingsV1() # ObjectAttachmentSettingsV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update attachment settings
    api_response = api_instance.update_object_attachment_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->update_object_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentSettingsV1**](ObjectAttachmentSettingsV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentSettingsV1**](ObjectAttachmentSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_attachment_visualization_settings**
> ObjectAttachmentVisualization update_object_attachment_visualization_settings(body, id)

Update visualization settings

Update Objects visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentVisualization() # ObjectAttachmentVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_object_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->update_object_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentVisualization**](ObjectAttachmentVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentVisualization**](ObjectAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_attachment_visualization_settings1**
> ObjectAttachmentVisualizationV1 update_object_attachment_visualization_settings1(body, id)

Update visualization settings

Update Objects visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectsApi()
body = swagger_client.ObjectAttachmentVisualizationV1() # ObjectAttachmentVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_object_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectsApi->update_object_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectAttachmentVisualizationV1**](ObjectAttachmentVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectAttachmentVisualizationV1**](ObjectAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

