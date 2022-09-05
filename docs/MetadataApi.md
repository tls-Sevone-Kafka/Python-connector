# swagger_client.MetadataApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_metadata**](MetadataApi.md#bulk_update_metadata) | **PATCH** /api/v2/metadata/bulkUpdate | bulk update Metadata Attributes
[**bulk_update_metadata1**](MetadataApi.md#bulk_update_metadata1) | **PATCH** /api/v2/bulkUpdateMetadata | bulk update Metadata Attributes
[**get_metadata_value**](MetadataApi.md#get_metadata_value) | **GET** /api/v2/{entityType}/{entityId}/metadata | Get Metadata values
[**get_object_metadata_value**](MetadataApi.md#get_object_metadata_value) | **GET** /api/v2/devices/{deviceId}/objects/{objectId}/metadata | Get Object Metadata value
[**partial_update_metadata**](MetadataApi.md#partial_update_metadata) | **PATCH** /api/v2/{entityType}/{entityId}/metadata | Partially update Metadata Attributes
[**partial_update_metadata1**](MetadataApi.md#partial_update_metadata1) | **PATCH** /api/v2/devices/{deviceId}/objects/{objectId}/metadata | Partially update Metadata Attributes
[**update_metadata**](MetadataApi.md#update_metadata) | **PUT** /api/v2/{entityType}/{entityId}/metadata | Update Metadata Attributes
[**update_metadata1**](MetadataApi.md#update_metadata1) | **PUT** /api/v2/devices/{deviceId}/objects/{objectId}/metadata | Update Metadata Attributes
[**update_metadata_by_attribute**](MetadataApi.md#update_metadata_by_attribute) | **PUT** /api/v2/{entityType}/{entityId}/metadata/{attributeKey} | Update Metadata Attributes
[**update_metadata_by_attribute1**](MetadataApi.md#update_metadata_by_attribute1) | **PUT** /api/v2/devices/{deviceId}/objects/{objectId}/metadata/{attributeKey} | Update Metadata Attributes

# **bulk_update_metadata**
> dict(str, list[BulkUpdateMetadataDto]) bulk_update_metadata(body)

bulk update Metadata Attributes

This endpoint will bulk update the provided metadata values for objects.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = NULL # dict(str, list[BulkUpdateMetadataDto]) | 

try:
    # bulk update Metadata Attributes
    api_response = api_instance.bulk_update_metadata(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->bulk_update_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, list[BulkUpdateMetadataDto])**](dict.md)|  | 

### Return type

**dict(str, list[BulkUpdateMetadataDto])**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_metadata1**
> dict(str, dict(str, dict(str, AttributeValues))) bulk_update_metadata1(body)

bulk update Metadata Attributes

NOTE: This endpoint is deprecated. Please use /api/v2/metadata/bulkUpdate.    This endpoint will bulk update the provided metadata values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = NULL # dict(str, dict(str, dict(str, AttributeValues))) | 

try:
    # bulk update Metadata Attributes
    api_response = api_instance.bulk_update_metadata1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->bulk_update_metadata1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, dict(str, dict(str, AttributeValues)))**](dict.md)|  | 

### Return type

**dict(str, dict(str, dict(str, AttributeValues)))**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_value**
> dict(str, AttributeValues) get_metadata_value(entity_type, entity_id)

Get Metadata values

This endpoint will get metadata value for entity type (device/object group/device group/object type/indicator type) and entity id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
entity_type = 'entity_type_example' # str | Entity Type
entity_id = 789 # int | Entity Id

try:
    # Get Metadata values
    api_response = api_instance.get_metadata_value(entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Entity Type | 
 **entity_id** | **int**| Entity Id | 

### Return type

[**dict(str, AttributeValues)**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_metadata_value**
> dict(str, AttributeValues) get_object_metadata_value(device_id, object_id)

Get Object Metadata value

This endpoint will get metadata value for entity type (object) and entity id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
device_id = 789 # int | Device Id
object_id = 789 # int | Object Id

try:
    # Get Object Metadata value
    api_response = api_instance.get_object_metadata_value(device_id, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_object_metadata_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Device Id | 
 **object_id** | **int**| Object Id | 

### Return type

[**dict(str, AttributeValues)**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_metadata**
> dict(str, AttributeValues) partial_update_metadata(body, entity_type, entity_id)

Partially update Metadata Attributes

This endpoint will update the provided metadata values for this entity type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = NULL # dict(str, AttributeValues) | 
entity_type = 'entity_type_example' # str | Entity Type
entity_id = 789 # int | Entity Id

try:
    # Partially update Metadata Attributes
    api_response = api_instance.partial_update_metadata(body, entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->partial_update_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AttributeValues)**](dict.md)|  | 
 **entity_type** | **str**| Entity Type | 
 **entity_id** | **int**| Entity Id | 

### Return type

[**dict(str, AttributeValues)**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_metadata1**
> dict(str, AttributeValues) partial_update_metadata1(body, device_id, object_id)

Partially update Metadata Attributes

This endpoint will update the provided metadata values for this object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = NULL # dict(str, AttributeValues) | 
device_id = 789 # int | Device Id
object_id = 789 # int | Object Id

try:
    # Partially update Metadata Attributes
    api_response = api_instance.partial_update_metadata1(body, device_id, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->partial_update_metadata1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AttributeValues)**](dict.md)|  | 
 **device_id** | **int**| Device Id | 
 **object_id** | **int**| Object Id | 

### Return type

[**dict(str, AttributeValues)**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata**
> dict(str, AttributeValues) update_metadata(body, entity_type, entity_id)

Update Metadata Attributes

This endpoint will delete all metadata values for this entity type and will create the values provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = NULL # dict(str, AttributeValues) | 
entity_type = 'entity_type_example' # str | Entity Type
entity_id = 789 # int | Entity Id

try:
    # Update Metadata Attributes
    api_response = api_instance.update_metadata(body, entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AttributeValues)**](dict.md)|  | 
 **entity_type** | **str**| Entity Type | 
 **entity_id** | **int**| Entity Id | 

### Return type

[**dict(str, AttributeValues)**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata1**
> dict(str, AttributeValues) update_metadata1(body, device_id, object_id)

Update Metadata Attributes

This endpoint will delete all metadata values for this object and will create the values provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = NULL # dict(str, AttributeValues) | 
device_id = 789 # int | Device Id
object_id = 789 # int | Object Id

try:
    # Update Metadata Attributes
    api_response = api_instance.update_metadata1(body, device_id, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AttributeValues)**](dict.md)|  | 
 **device_id** | **int**| Device Id | 
 **object_id** | **int**| Object Id | 

### Return type

[**dict(str, AttributeValues)**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_by_attribute**
> dict(str, AttributeValues) update_metadata_by_attribute(body, entity_type, entity_id, attribute_key)

Update Metadata Attributes

This endpoint will delete all metadata values for this entity type and attribute and will create the values provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = swagger_client.AttributeValues() # AttributeValues | 
entity_type = 'entity_type_example' # str | Entity Type
entity_id = 789 # int | Entity Id
attribute_key = 'attribute_key_example' # str | AttributeKey

try:
    # Update Metadata Attributes
    api_response = api_instance.update_metadata_by_attribute(body, entity_type, entity_id, attribute_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata_by_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeValues**](AttributeValues.md)|  | 
 **entity_type** | **str**| Entity Type | 
 **entity_id** | **int**| Entity Id | 
 **attribute_key** | **str**| AttributeKey | 

### Return type

[**dict(str, AttributeValues)**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_by_attribute1**
> dict(str, AttributeValues) update_metadata_by_attribute1(body, device_id, object_id, attribute_key)

Update Metadata Attributes

This endpoint will delete all metadata values for this object and attribute and will create the values provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = swagger_client.AttributeValues() # AttributeValues | 
device_id = 789 # int | Device Id
object_id = 789 # int | Object Id
attribute_key = 'attribute_key_example' # str | AttributeKey

try:
    # Update Metadata Attributes
    api_response = api_instance.update_metadata_by_attribute1(body, device_id, object_id, attribute_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata_by_attribute1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeValues**](AttributeValues.md)|  | 
 **device_id** | **int**| Device Id | 
 **object_id** | **int**| Object Id | 
 **attribute_key** | **str**| AttributeKey | 

### Return type

[**dict(str, AttributeValues)**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

