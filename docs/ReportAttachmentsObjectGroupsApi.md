# swagger_client.ReportAttachmentsObjectGroupsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_group_attachment**](ReportAttachmentsObjectGroupsApi.md#create_object_group_attachment) | **POST** /api/v2/reports/{id}/attachments/object-groups | Create object group attachment
[**create_object_group_attachment1**](ReportAttachmentsObjectGroupsApi.md#create_object_group_attachment1) | **POST** /api/v1/reports/{id}/attachments/object-groups | Create object group attachment
[**get_object_group_attachment**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment) | **GET** /api/v2/reports/attachments/object-groups/{id} | Get object group attachment
[**get_object_group_attachment_resources**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment_resources) | **GET** /api/v2/reports/attachments/object-groups/{id}/resources | Get resources
[**get_object_group_attachment_resources1**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment_resources1) | **GET** /api/v1/reports/attachments/object-groups/{id}/resources | Get resources
[**get_object_group_attachment_visualization_settings**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/object-groups/{id}/visualizations | Get attachment visualization settings
[**get_object_group_attachment_visualization_settings1**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment_visualization_settings1) | **GET** /api/v1/reports/attachments/object-groups/{id}/visualizations | Get attachment visualization settings
[**partially_update_object_group_attachment_visualization_settings**](ReportAttachmentsObjectGroupsApi.md#partially_update_object_group_attachment_visualization_settings) | **PATCH** /api/v2/reports/attachments/object-groups/{id}/visualizations | Partially update visualization settings
[**partially_update_object_group_attachment_visualization_settings1**](ReportAttachmentsObjectGroupsApi.md#partially_update_object_group_attachment_visualization_settings1) | **PATCH** /api/v1/reports/attachments/object-groups/{id}/visualizations | Partially update visualization settings
[**update_object_group_attachment_resources**](ReportAttachmentsObjectGroupsApi.md#update_object_group_attachment_resources) | **PUT** /api/v2/reports/attachments/object-groups/{id}/resources | Update resources
[**update_object_group_attachment_resources1**](ReportAttachmentsObjectGroupsApi.md#update_object_group_attachment_resources1) | **PUT** /api/v1/reports/attachments/object-groups/{id}/resources | Update resources
[**update_object_group_attachment_visualization_settings**](ReportAttachmentsObjectGroupsApi.md#update_object_group_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/object-groups/{id}/visualizations | Update visualization settings
[**update_object_group_attachment_visualization_settings1**](ReportAttachmentsObjectGroupsApi.md#update_object_group_attachment_visualization_settings1) | **PUT** /api/v1/reports/attachments/object-groups/{id}/visualizations | Update visualization settings

# **create_object_group_attachment**
> ObjectGroupAttachmentResponseDto create_object_group_attachment(body, id)

Create object group attachment

Create a new object group attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
body = swagger_client.ObjectGroupAttachmentRequestDto() # ObjectGroupAttachmentRequestDto | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create object group attachment
    api_response = api_instance.create_object_group_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->create_object_group_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectGroupAttachmentRequestDto**](ObjectGroupAttachmentRequestDto.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**ObjectGroupAttachmentResponseDto**](ObjectGroupAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_group_attachment1**
> ObjectGroupAttachmentResponseDtoV1 create_object_group_attachment1(body, id)

Create object group attachment

Create a new object group attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
body = swagger_client.ObjectGroupAttachmentRequestDtoV1() # ObjectGroupAttachmentRequestDtoV1 | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create object group attachment
    api_response = api_instance.create_object_group_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->create_object_group_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectGroupAttachmentRequestDtoV1**](ObjectGroupAttachmentRequestDtoV1.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**ObjectGroupAttachmentResponseDtoV1**](ObjectGroupAttachmentResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment**
> ObjectGroupAttachmentResponseDto get_object_group_attachment(id)

Get object group attachment

Get an existing object group attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | Object group attachment id

try:
    # Get object group attachment
    api_response = api_instance.get_object_group_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Object group attachment id | 

### Return type

[**ObjectGroupAttachmentResponseDto**](ObjectGroupAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment_resources**
> ObjectGroupAttachmentResource get_object_group_attachment_resources(id)

Get resources

Get object group resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_object_group_attachment_resources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentResource**](ObjectGroupAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment_resources1**
> ObjectGroupAttachmentResourceV1 get_object_group_attachment_resources1(id)

Get resources

Get object group resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_object_group_attachment_resources1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentResourceV1**](ObjectGroupAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment_visualization_settings**
> ObjectGroupAttachmentVisualization get_object_group_attachment_visualization_settings(id)

Get attachment visualization settings

Get object group attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_object_group_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment_visualization_settings1**
> ObjectGroupAttachmentVisualizationV1 get_object_group_attachment_visualization_settings1(id)

Get attachment visualization settings

Get object group attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_object_group_attachment_visualization_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_group_attachment_visualization_settings**
> ObjectGroupAttachmentVisualization partially_update_object_group_attachment_visualization_settings(body, id)

Partially update visualization settings

Partially update object group visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
body = swagger_client.ObjectGroupAttachmentVisualization() # ObjectGroupAttachmentVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_object_group_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->partially_update_object_group_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_group_attachment_visualization_settings1**
> ObjectGroupAttachmentVisualizationV1 partially_update_object_group_attachment_visualization_settings1(body, id)

Partially update visualization settings

Partially update object group visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
body = swagger_client.ObjectGroupAttachmentVisualizationV1() # ObjectGroupAttachmentVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_object_group_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->partially_update_object_group_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_attachment_resources**
> ObjectGroupAttachmentResource update_object_group_attachment_resources(body, id)

Update resources

Update object group resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
body = swagger_client.ObjectGroupAttachmentResource() # ObjectGroupAttachmentResource | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_object_group_attachment_resources(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->update_object_group_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectGroupAttachmentResource**](ObjectGroupAttachmentResource.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentResource**](ObjectGroupAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_attachment_resources1**
> ObjectGroupAttachmentResourceV1 update_object_group_attachment_resources1(body, id)

Update resources

Update object group resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
body = swagger_client.ObjectGroupAttachmentResourceV1() # ObjectGroupAttachmentResourceV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_object_group_attachment_resources1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->update_object_group_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectGroupAttachmentResourceV1**](ObjectGroupAttachmentResourceV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentResourceV1**](ObjectGroupAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_attachment_visualization_settings**
> ObjectGroupAttachmentVisualization update_object_group_attachment_visualization_settings(body, id)

Update visualization settings

Update object group visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
body = swagger_client.ObjectGroupAttachmentVisualization() # ObjectGroupAttachmentVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_object_group_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->update_object_group_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_attachment_visualization_settings1**
> ObjectGroupAttachmentVisualizationV1 update_object_group_attachment_visualization_settings1(body, id)

Update visualization settings

Update object group visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
body = swagger_client.ObjectGroupAttachmentVisualizationV1() # ObjectGroupAttachmentVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_object_group_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->update_object_group_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

