# swagger_client.MetadataNamespaceApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespace**](MetadataNamespaceApi.md#create_namespace) | **POST** /api/v2/metadata/namespace | Create Metadata Namespace
[**delete_namespace_by_id**](MetadataNamespaceApi.md#delete_namespace_by_id) | **DELETE** /api/v2/metadata/namespace/{id} | Delete Metadata Namespace
[**get_namespace**](MetadataNamespaceApi.md#get_namespace) | **GET** /api/v2/metadata/namespace/{id} | Get Metadata Namespace
[**get_namespaces**](MetadataNamespaceApi.md#get_namespaces) | **GET** /api/v2/metadata/namespace | Get all Metadata Namespaces
[**update_namespace_by_id**](MetadataNamespaceApi.md#update_namespace_by_id) | **PUT** /api/v2/metadata/namespace/{id} | Update Metadata Namespace

# **create_namespace**
> NamespaceDto create_namespace(body)

Create Metadata Namespace

Creates a new Metadata Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
body = swagger_client.NamespaceDto() # NamespaceDto | 

try:
    # Create Metadata Namespace
    api_response = api_instance.create_namespace(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->create_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamespaceDto**](NamespaceDto.md)|  | 

### Return type

[**NamespaceDto**](NamespaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespace_by_id**
> str delete_namespace_by_id(id)

Delete Metadata Namespace

Deletes an existing Metadata Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
id = 789 # int | The id of the Namespace to be deleted

try:
    # Delete Metadata Namespace
    api_response = api_instance.delete_namespace_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->delete_namespace_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the Namespace to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespace**
> NamespaceDto get_namespace(id)

Get Metadata Namespace

Endpoint for retrieving Metadata Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
id = 789 # int | Namespace Id

try:
    # Get Metadata Namespace
    api_response = api_instance.get_namespace(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->get_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Namespace Id | 

### Return type

[**NamespaceDto**](NamespaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaces**
> PagerNamespaceDto get_namespaces(options, name=name)

Get all Metadata Namespaces

Endpoint for retrieving all metadata namespaces that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
name = 'name_example' # str | Filter by Namespace name (optional)

try:
    # Get all Metadata Namespaces
    api_response = api_instance.get_namespaces(options, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->get_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **name** | **str**| Filter by Namespace name | [optional] 

### Return type

[**PagerNamespaceDto**](PagerNamespaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_namespace_by_id**
> NamespaceDto update_namespace_by_id(body, id)

Update Metadata Namespace

Updates an existing Metadata Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
body = swagger_client.NamespaceDto() # NamespaceDto | 
id = 789 # int | The id of the Namespace to be updated

try:
    # Update Metadata Namespace
    api_response = api_instance.update_namespace_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->update_namespace_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamespaceDto**](NamespaceDto.md)|  | 
 **id** | **int**| The id of the Namespace to be updated | 

### Return type

[**NamespaceDto**](NamespaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

