# swagger_client.ReportAttachmentsStatusMapApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_status_map_attachment**](ReportAttachmentsStatusMapApi.md#create_status_map_attachment) | **POST** /api/v2/reports/{id}/attachments/statusmap | Create statusmap attachment
[**create_status_map_attachment1**](ReportAttachmentsStatusMapApi.md#create_status_map_attachment1) | **POST** /api/v1/reports/{id}/attachments/statusmap | Create statusmap attachment
[**get_status_attachment**](ReportAttachmentsStatusMapApi.md#get_status_attachment) | **GET** /api/v2/reports/attachments/statusmap/{id} | Get status map attachment
[**get_status_map_attachment_resources**](ReportAttachmentsStatusMapApi.md#get_status_map_attachment_resources) | **GET** /api/v2/reports/attachments/statusmap/{id}/resources | Get resources
[**get_status_map_attachment_resources1**](ReportAttachmentsStatusMapApi.md#get_status_map_attachment_resources1) | **GET** /api/v1/reports/attachments/statusmap/{id}/resources | Get resources
[**update_status_map_attachment_resources**](ReportAttachmentsStatusMapApi.md#update_status_map_attachment_resources) | **PUT** /api/v2/reports/attachments/statusmap/{id}/resources | Update resources
[**update_status_map_attachment_resources1**](ReportAttachmentsStatusMapApi.md#update_status_map_attachment_resources1) | **PUT** /api/v1/reports/attachments/statusmap/{id}/resources | Update resources

# **create_status_map_attachment**
> StatusMapAttachmentResponseDto create_status_map_attachment(body, id)

Create statusmap attachment

Create a new statusmap attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsStatusMapApi()
body = swagger_client.StatusMapAttachmentRequestDto() # StatusMapAttachmentRequestDto | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create statusmap attachment
    api_response = api_instance.create_status_map_attachment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsStatusMapApi->create_status_map_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapAttachmentRequestDto**](StatusMapAttachmentRequestDto.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**StatusMapAttachmentResponseDto**](StatusMapAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_status_map_attachment1**
> StatusMapAttachmentResponseDtoV1 create_status_map_attachment1(body, id)

Create statusmap attachment

Create a new statusmap attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsStatusMapApi()
body = swagger_client.StatusMapAttachmentRequestDtoV1() # StatusMapAttachmentRequestDtoV1 | 
id = 789 # int | The id of the report where the report attachment will be created

try:
    # Create statusmap attachment
    api_response = api_instance.create_status_map_attachment1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsStatusMapApi->create_status_map_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapAttachmentRequestDtoV1**](StatusMapAttachmentRequestDtoV1.md)|  | 
 **id** | **int**| The id of the report where the report attachment will be created | 

### Return type

[**StatusMapAttachmentResponseDtoV1**](StatusMapAttachmentResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_attachment**
> StatusMapAttachmentResponseDto get_status_attachment(id)

Get status map attachment

Get an existing status map attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsStatusMapApi()
id = 789 # int | StatusMap attachment id

try:
    # Get status map attachment
    api_response = api_instance.get_status_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsStatusMapApi->get_status_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| StatusMap attachment id | 

### Return type

[**StatusMapAttachmentResponseDto**](StatusMapAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_map_attachment_resources**
> StatusMapAttachmentResource get_status_map_attachment_resources(id)

Get resources

Get statusmap resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsStatusMapApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_status_map_attachment_resources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsStatusMapApi->get_status_map_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**StatusMapAttachmentResource**](StatusMapAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_map_attachment_resources1**
> StatusMapAttachmentResourceV1 get_status_map_attachment_resources1(id)

Get resources

Get statusmap resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsStatusMapApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_status_map_attachment_resources1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsStatusMapApi->get_status_map_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**StatusMapAttachmentResourceV1**](StatusMapAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status_map_attachment_resources**
> StatusMapAttachmentResource update_status_map_attachment_resources(body, id)

Update resources

Update statusmap resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsStatusMapApi()
body = swagger_client.StatusMapAttachmentResource() # StatusMapAttachmentResource | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_status_map_attachment_resources(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsStatusMapApi->update_status_map_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapAttachmentResource**](StatusMapAttachmentResource.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**StatusMapAttachmentResource**](StatusMapAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status_map_attachment_resources1**
> StatusMapAttachmentResourceV1 update_status_map_attachment_resources1(body, id)

Update resources

Update statusmap resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsStatusMapApi()
body = swagger_client.StatusMapAttachmentResourceV1() # StatusMapAttachmentResourceV1 | 
id = 789 # int | The id of the report attachment

try:
    # Update resources
    api_response = api_instance.update_status_map_attachment_resources1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsStatusMapApi->update_status_map_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusMapAttachmentResourceV1**](StatusMapAttachmentResourceV1.md)|  | 
 **id** | **int**| The id of the report attachment | 

### Return type

[**StatusMapAttachmentResourceV1**](StatusMapAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

