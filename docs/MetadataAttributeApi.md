# swagger_client.MetadataAttributeApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attribute**](MetadataAttributeApi.md#create_attribute) | **POST** /api/v2/metadata/attribute | Create Metadata Attribute
[**delete_attribute_by_id**](MetadataAttributeApi.md#delete_attribute_by_id) | **DELETE** /api/v2/metadata/attribute/{id} | Delete Metadata Attribute
[**filter_attributes**](MetadataAttributeApi.md#filter_attributes) | **POST** /api/v2/metadata/attribute/filter | Filter Metadata Attributes
[**get_attribute**](MetadataAttributeApi.md#get_attribute) | **GET** /api/v2/metadata/attribute/{id} | Get Metadata Attribute
[**get_attributes**](MetadataAttributeApi.md#get_attributes) | **GET** /api/v2/metadata/attribute | Get all Metadata Attributes
[**update_attribute_by_id**](MetadataAttributeApi.md#update_attribute_by_id) | **PUT** /api/v2/metadata/attribute/{id} | Update Metadata Attribute

# **create_attribute**
> AttributeDto create_attribute(body)

Create Metadata Attribute

Creates a new Metadata Attribute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
body = swagger_client.AttributeDto() # AttributeDto | 

try:
    # Create Metadata Attribute
    api_response = api_instance.create_attribute(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeDto**](AttributeDto.md)|  | 

### Return type

[**AttributeDto**](AttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute_by_id**
> str delete_attribute_by_id(id)

Delete Metadata Attribute

Deletes an existing Metadata Attribute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
id = 789 # int | The id of the deleteAttributeById to be deleted

try:
    # Delete Metadata Attribute
    api_response = api_instance.delete_attribute_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->delete_attribute_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the deleteAttributeById to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_attributes**
> PagerAttributeDto filter_attributes(body)

Filter Metadata Attributes

Endpoint for retrieving metadata attributes that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
body = swagger_client.AttributeFilterBody() # AttributeFilterBody | 

try:
    # Filter Metadata Attributes
    api_response = api_instance.filter_attributes(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->filter_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeFilterBody**](AttributeFilterBody.md)|  | 

### Return type

[**PagerAttributeDto**](PagerAttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute**
> AttributeDto get_attribute(id)

Get Metadata Attribute

Endpoint for retrieving Metadata Attribute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
id = 789 # int | Attribute Id

try:
    # Get Metadata Attribute
    api_response = api_instance.get_attribute(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->get_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Attribute Id | 

### Return type

[**AttributeDto**](AttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> PagerAttributeDto get_attributes(options)

Get all Metadata Attributes

Endpoint for retrieving all metadata attributes that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all Metadata Attributes
    api_response = api_instance.get_attributes(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerAttributeDto**](PagerAttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_by_id**
> AttributeDto update_attribute_by_id(body, id)

Update Metadata Attribute

Updates an existing Metadata Attribute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
body = swagger_client.AttributeDto() # AttributeDto | 
id = 789 # int | The id of the Attribute to be updated

try:
    # Update Metadata Attribute
    api_response = api_instance.update_attribute_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->update_attribute_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeDto**](AttributeDto.md)|  | 
 **id** | **int**| The id of the Attribute to be updated | 

### Return type

[**AttributeDto**](AttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

