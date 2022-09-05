# swagger_client.ReportAttachmentsMetadataApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata_attachment**](ReportAttachmentsMetadataApi.md#create_metadata_attachment) | **POST** /api/v2/reports/{id}/attachments/metadata | Create metadata attachment
[**create_metadata_attachment1**](ReportAttachmentsMetadataApi.md#create_metadata_attachment1) | **POST** /api/v1/reports/{id}/attachments/metadata | Create metadata attachment
[**get_metadata_attachment**](ReportAttachmentsMetadataApi.md#get_metadata_attachment) | **GET** /api/v2/reports/attachments/metadata/{id} | Get metadata attachment
[**get_metadata_attachment_resources**](ReportAttachmentsMetadataApi.md#get_metadata_attachment_resources) | **GET** /api/v2/reports/attachments/metadata/{id}/resources | Get resources
[**get_metadata_attachment_resources1**](ReportAttachmentsMetadataApi.md#get_metadata_attachment_resources1) | **GET** /api/v1/reports/attachments/metadata/{id}/resources | Get resources
[**get_metadata_attachment_visualization_settings**](ReportAttachmentsMetadataApi.md#get_metadata_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/metadata/{id}/visualizations | Get attachment visualization settings
[**get_metadata_attachment_visualization_settings1**](ReportAttachmentsMetadataApi.md#get_metadata_attachment_visualization_settings1) | **GET** /api/v1/reports/attachments/metadata/{id}/visualizations | Get attachment visualization settings
[**partially_update_metadata_attachment_visualization_settings**](ReportAttachmentsMetadataApi.md#partially_update_metadata_attachment_visualization_settings) | **PATCH** /api/v2/reports/attachments/metadata/{id}/visualizations | Partially update visualization settings
[**partially_update_metadata_attachment_visualization_settings1**](ReportAttachmentsMetadataApi.md#partially_update_metadata_attachment_visualization_settings1) | **PATCH** /api/v1/reports/attachments/metadata/{id}/visualizations | Partially update visualization settings
[**update_metadata_attachment_resources**](ReportAttachmentsMetadataApi.md#update_metadata_attachment_resources) | **PUT** /api/v2/reports/attachments/metadata/{id}/resources | Update resources
[**update_metadata_attachment_resources1**](ReportAttachmentsMetadataApi.md#update_metadata_attachment_resources1) | **PUT** /api/v1/reports/attachments/metadata/{id}/resources | Update resources
[**update_metadata_attachment_visualization_settings**](ReportAttachmentsMetadataApi.md#update_metadata_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/metadata/{id}/visualizations | Update visualization settings
[**update_metadata_attachment_visualization_settings1**](ReportAttachmentsMetadataApi.md#update_metadata_attachment_visualization_settings1) | **PUT** /api/v1/reports/attachments/metadata/{id}/visualizations | Update visualization settings

# **create_metadata_attachment**
> MetadataAttachmentResponseDto create_metadata_attachment(body, id)

Create metadata attachment

Create a new metadata attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
body = swagger_client.MetadataAttachmentRequestDto() # MetadataAttachmentRequestDto | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create metadata attachment
    api_response = api_instance.create_metadata_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->create_metadata_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataAttachmentRequestDto**](MetadataAttachmentRequestDto.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**MetadataAttachmentResponseDto**](MetadataAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metadata_attachment1**
> MetadataAttachmentResponseDtoV1 create_metadata_attachment1(body, id)

Create metadata attachment

Create a new metadata attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
body = swagger_client.MetadataAttachmentRequestDtoV1() # MetadataAttachmentRequestDtoV1 | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create metadata attachment
    api_response = api_instance.create_metadata_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->create_metadata_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataAttachmentRequestDtoV1**](MetadataAttachmentRequestDtoV1.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**MetadataAttachmentResponseDtoV1**](MetadataAttachmentResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_attachment**
> MetadataAttachmentResponseDto get_metadata_attachment(id)

Get metadata attachment

Get an existing metadata attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
id = 789 # int | Metadata attachment id

try:
    # Get metadata attachment
    api_response = api_instance.get_metadata_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->get_metadata_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Metadata attachment id | 

### Return type

[**MetadataAttachmentResponseDto**](MetadataAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_attachment_resources**
> MetadataAttachmentResource get_metadata_attachment_resources(id)

Get resources

Get Metadata resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_metadata_attachment_resources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->get_metadata_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentResource**](MetadataAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_attachment_resources1**
> MetadataAttachmentResourceV1 get_metadata_attachment_resources1(id)

Get resources

Get Metadata resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_metadata_attachment_resources1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->get_metadata_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentResourceV1**](MetadataAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_attachment_visualization_settings**
> MetadataAttachmentVisualization get_metadata_attachment_visualization_settings(id)

Get attachment visualization settings

Get metadata attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_metadata_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->get_metadata_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentVisualization**](MetadataAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_attachment_visualization_settings1**
> MetadataAttachmentVisualizationV1 get_metadata_attachment_visualization_settings1(id)

Get attachment visualization settings

Get metadata attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_metadata_attachment_visualization_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->get_metadata_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentVisualizationV1**](MetadataAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_metadata_attachment_visualization_settings**
> MetadataAttachmentVisualization partially_update_metadata_attachment_visualization_settings(body, id)

Partially update visualization settings

Partially update metadata visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
body = swagger_client.MetadataAttachmentVisualization() # MetadataAttachmentVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_metadata_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->partially_update_metadata_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataAttachmentVisualization**](MetadataAttachmentVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentVisualization**](MetadataAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_metadata_attachment_visualization_settings1**
> MetadataAttachmentVisualizationV1 partially_update_metadata_attachment_visualization_settings1(body, id)

Partially update visualization settings

Partially update metadata visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
body = swagger_client.MetadataAttachmentVisualizationV1() # MetadataAttachmentVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_metadata_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->partially_update_metadata_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataAttachmentVisualizationV1**](MetadataAttachmentVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentVisualizationV1**](MetadataAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_attachment_resources**
> MetadataAttachmentResource update_metadata_attachment_resources(body, id)

Update resources

Update Metadata resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
body = swagger_client.MetadataAttachmentResource() # MetadataAttachmentResource | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_metadata_attachment_resources(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->update_metadata_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataAttachmentResource**](MetadataAttachmentResource.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentResource**](MetadataAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_attachment_resources1**
> MetadataAttachmentResourceV1 update_metadata_attachment_resources1(body, id)

Update resources

Update Metadata resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
body = swagger_client.MetadataAttachmentResourceV1() # MetadataAttachmentResourceV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_metadata_attachment_resources1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->update_metadata_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataAttachmentResourceV1**](MetadataAttachmentResourceV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentResourceV1**](MetadataAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_attachment_visualization_settings**
> MetadataAttachmentVisualization update_metadata_attachment_visualization_settings(body, id)

Update visualization settings

Update Metadata visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
body = swagger_client.MetadataAttachmentVisualization() # MetadataAttachmentVisualization | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_metadata_attachment_visualization_settings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->update_metadata_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataAttachmentVisualization**](MetadataAttachmentVisualization.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentVisualization**](MetadataAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_attachment_visualization_settings1**
> MetadataAttachmentVisualizationV1 update_metadata_attachment_visualization_settings1(body, id)

Update visualization settings

Update Metadata visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsMetadataApi()
body = swagger_client.MetadataAttachmentVisualizationV1() # MetadataAttachmentVisualizationV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update visualization settings
    api_response = api_instance.update_metadata_attachment_visualization_settings1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsMetadataApi->update_metadata_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataAttachmentVisualizationV1**](MetadataAttachmentVisualizationV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**MetadataAttachmentVisualizationV1**](MetadataAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

