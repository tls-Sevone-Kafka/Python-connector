# swagger_client.PluginsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plugin_indicator_type**](PluginsApi.md#create_plugin_indicator_type) | **POST** /api/v2/plugins/indicatortypes | Creates a plugin indicator type
[**create_plugin_indicator_type1**](PluginsApi.md#create_plugin_indicator_type1) | **POST** /api/v1/plugins/indicatortypes | Creates a plugin indicator type
[**create_plugin_object_type**](PluginsApi.md#create_plugin_object_type) | **POST** /api/v2/plugins/objecttypes | Creates an plugin object type
[**create_plugin_object_type1**](PluginsApi.md#create_plugin_object_type1) | **POST** /api/v1/plugins/objecttypes | Creates an plugin object type
[**filter_plugin_indicator_types**](PluginsApi.md#filter_plugin_indicator_types) | **POST** /api/v2/plugins/indicatortypes/filter | Find plugin indicator types
[**filter_plugin_indicator_types1**](PluginsApi.md#filter_plugin_indicator_types1) | **POST** /api/v1/plugins/indicatortypes/filter | Find plugin indicator types
[**filter_plugin_object_types**](PluginsApi.md#filter_plugin_object_types) | **POST** /api/v2/plugins/objecttypes/filter | Find plugin object types
[**filter_plugin_object_types1**](PluginsApi.md#filter_plugin_object_types1) | **POST** /api/v1/plugins/objecttypes/filter | Find plugin object types
[**get_all_plugin_indicator_types**](PluginsApi.md#get_all_plugin_indicator_types) | **GET** /api/v2/plugins/indicatortypes | Get all plugin indicator types
[**get_all_plugin_indicator_types1**](PluginsApi.md#get_all_plugin_indicator_types1) | **GET** /api/v1/plugins/indicatortypes | Get all plugin indicator types
[**get_all_plugin_object_types**](PluginsApi.md#get_all_plugin_object_types) | **GET** /api/v2/plugins/objecttypes | Get all plugin object types
[**get_all_plugin_object_types1**](PluginsApi.md#get_all_plugin_object_types1) | **GET** /api/v1/plugins/objecttypes | Get all plugin object types
[**get_all_plugins**](PluginsApi.md#get_all_plugins) | **GET** /api/v2/plugins | Get all plugins
[**get_all_plugins1**](PluginsApi.md#get_all_plugins1) | **GET** /api/v1/plugins | Get all plugins
[**get_device_plugin_info_schema**](PluginsApi.md#get_device_plugin_info_schema) | **GET** /api/v2/plugins/device/schema | Get all device extended plugin info schema
[**get_device_plugin_info_schema1**](PluginsApi.md#get_device_plugin_info_schema1) | **GET** /api/v1/plugins/device/schema | Get all device extended plugin info schema
[**get_indicator_extended_info_schema**](PluginsApi.md#get_indicator_extended_info_schema) | **GET** /api/v2/plugins/indicator/schema/{pluginId} | Get indicator extended info schema by plugin Id
[**get_indicator_extended_info_schema1**](PluginsApi.md#get_indicator_extended_info_schema1) | **GET** /api/v1/plugins/indicator/schema/{pluginId} | Get indicator extended info schema by plugin Id
[**get_object_extended_info_schema**](PluginsApi.md#get_object_extended_info_schema) | **GET** /api/v2/plugins/object/schema/{pluginId} | Get object extended info schema by plugin Id
[**get_object_extended_info_schema1**](PluginsApi.md#get_object_extended_info_schema1) | **GET** /api/v1/plugins/object/schema/{pluginId} | Get object extended info schema by plugin Id
[**get_schema_for_all_plugin_indicator_types**](PluginsApi.md#get_schema_for_all_plugin_indicator_types) | **GET** /api/v2/plugins/indicatortypes/schema/{pluginId} | Get schema for plugin indicator type extended info
[**get_schema_for_all_plugin_indicator_types1**](PluginsApi.md#get_schema_for_all_plugin_indicator_types1) | **GET** /api/v1/plugins/indicatortypes/schema/{pluginId} | Get schema for plugin indicator type extended info
[**get_schema_for_all_plugin_object_types**](PluginsApi.md#get_schema_for_all_plugin_object_types) | **GET** /api/v2/plugins/objecttypes/schema/{pluginId} | Get schema for plugin object type extended info
[**get_schema_for_all_plugin_object_types1**](PluginsApi.md#get_schema_for_all_plugin_object_types1) | **GET** /api/v1/plugins/objecttypes/schema/{pluginId} | Get schema for plugin object type extended info
[**update_plugin_indicator_type**](PluginsApi.md#update_plugin_indicator_type) | **PUT** /api/v2/plugins/indicatortypes/{id} | Updates a plugin indicator type
[**update_plugin_indicator_type1**](PluginsApi.md#update_plugin_indicator_type1) | **PUT** /api/v1/plugins/indicatortypes/{id} | Updates a plugin indicator type
[**update_plugin_object_type**](PluginsApi.md#update_plugin_object_type) | **PUT** /api/v2/plugins/objecttypes/{id} | Updates an plugin object type
[**update_plugin_object_type1**](PluginsApi.md#update_plugin_object_type1) | **PUT** /api/v1/plugins/objecttypes/{id} | Updates an plugin object type

# **create_plugin_indicator_type**
> PluginIndicatorTypeDto create_plugin_indicator_type(body)

Creates a plugin indicator type

Endpoint for creating plugin indicator types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginIndicatorTypeRequestDto() # PluginIndicatorTypeRequestDto | 

try:
    # Creates a plugin indicator type
    api_response = api_instance.create_plugin_indicator_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->create_plugin_indicator_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginIndicatorTypeRequestDto**](PluginIndicatorTypeRequestDto.md)|  | 

### Return type

[**PluginIndicatorTypeDto**](PluginIndicatorTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plugin_indicator_type1**
> PluginIndicatorTypeDtoV1 create_plugin_indicator_type1(body)

Creates a plugin indicator type

Endpoint for creating plugin indicator types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginIndicatorTypeRequestDtoV1() # PluginIndicatorTypeRequestDtoV1 | 

try:
    # Creates a plugin indicator type
    api_response = api_instance.create_plugin_indicator_type1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->create_plugin_indicator_type1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginIndicatorTypeRequestDtoV1**](PluginIndicatorTypeRequestDtoV1.md)|  | 

### Return type

[**PluginIndicatorTypeDtoV1**](PluginIndicatorTypeDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plugin_object_type**
> PluginObjectTypeDto create_plugin_object_type(body)

Creates an plugin object type

Endpoint for creating plugin object types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginObjectTypeRequestDto() # PluginObjectTypeRequestDto | 

try:
    # Creates an plugin object type
    api_response = api_instance.create_plugin_object_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->create_plugin_object_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginObjectTypeRequestDto**](PluginObjectTypeRequestDto.md)|  | 

### Return type

[**PluginObjectTypeDto**](PluginObjectTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plugin_object_type1**
> PluginObjectTypeDtoV1 create_plugin_object_type1(body)

Creates an plugin object type

Endpoint for creating plugin object types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginObjectTypeRequestDtoV1() # PluginObjectTypeRequestDtoV1 | 

try:
    # Creates an plugin object type
    api_response = api_instance.create_plugin_object_type1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->create_plugin_object_type1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginObjectTypeRequestDtoV1**](PluginObjectTypeRequestDtoV1.md)|  | 

### Return type

[**PluginObjectTypeDtoV1**](PluginObjectTypeDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_plugin_indicator_types**
> PagerPluginIndicatorTypeDto filter_plugin_indicator_types(body, include_extended_info=include_extended_info)

Find plugin indicator types

Filter plugin indicator types that match the criteria with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.IndicatortypesFilterBody() # IndicatortypesFilterBody | 
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Find plugin indicator types
    api_response = api_instance.filter_plugin_indicator_types(body, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->filter_plugin_indicator_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndicatortypesFilterBody**](IndicatortypesFilterBody.md)|  | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerPluginIndicatorTypeDto**](PagerPluginIndicatorTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_plugin_indicator_types1**
> PagerPluginIndicatorTypeDtoV1 filter_plugin_indicator_types1(body, page=page, size=size, include_extended_info=include_extended_info)

Find plugin indicator types

Filter plugin indicator types that match the criteria with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginIndicatorTypeFilterDto() # PluginIndicatorTypeFilterDto | 
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Find plugin indicator types
    api_response = api_instance.filter_plugin_indicator_types1(body, page=page, size=size, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->filter_plugin_indicator_types1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginIndicatorTypeFilterDto**](PluginIndicatorTypeFilterDto.md)|  | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerPluginIndicatorTypeDtoV1**](PagerPluginIndicatorTypeDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_plugin_object_types**
> PagerPluginObjectTypeDto filter_plugin_object_types(body, include_extended_info=include_extended_info)

Find plugin object types

Filter plugin object types that match the criteria with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.ObjecttypesFilterBody() # ObjecttypesFilterBody | 
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Find plugin object types
    api_response = api_instance.filter_plugin_object_types(body, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->filter_plugin_object_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjecttypesFilterBody**](ObjecttypesFilterBody.md)|  | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerPluginObjectTypeDto**](PagerPluginObjectTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_plugin_object_types1**
> PagerPluginObjectTypeDtoV1 filter_plugin_object_types1(body, page=page, size=size, include_extended_info=include_extended_info)

Find plugin object types

Filter plugin object types that match the criteria with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginObjectTypeFilterDto() # PluginObjectTypeFilterDto | 
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Find plugin object types
    api_response = api_instance.filter_plugin_object_types1(body, page=page, size=size, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->filter_plugin_object_types1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginObjectTypeFilterDto**](PluginObjectTypeFilterDto.md)|  | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerPluginObjectTypeDtoV1**](PagerPluginObjectTypeDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plugin_indicator_types**
> PagerPluginIndicatorTypeDto get_all_plugin_indicator_types(options, include_extended_info=include_extended_info)

Get all plugin indicator types

Endpoint for retrieving all plugin indicator types with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get all plugin indicator types
    api_response = api_instance.get_all_plugin_indicator_types(options, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_all_plugin_indicator_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerPluginIndicatorTypeDto**](PagerPluginIndicatorTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plugin_indicator_types1**
> PagerPluginIndicatorTypeDtoV1 get_all_plugin_indicator_types1(page=page, size=size, include_extended_info=include_extended_info)

Get all plugin indicator types

Endpoint for retrieving all plugin indicator types with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get all plugin indicator types
    api_response = api_instance.get_all_plugin_indicator_types1(page=page, size=size, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_all_plugin_indicator_types1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerPluginIndicatorTypeDtoV1**](PagerPluginIndicatorTypeDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plugin_object_types**
> PagerPluginObjectTypeDto get_all_plugin_object_types(options, include_extended_info=include_extended_info)

Get all plugin object types

Endpoint for retrieving all plugin object types with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get all plugin object types
    api_response = api_instance.get_all_plugin_object_types(options, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_all_plugin_object_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerPluginObjectTypeDto**](PagerPluginObjectTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plugin_object_types1**
> PagerPluginObjectTypeDtoV1 get_all_plugin_object_types1(page=page, size=size, include_extended_info=include_extended_info)

Get all plugin object types

Endpoint for retrieving all plugin object types with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get all plugin object types
    api_response = api_instance.get_all_plugin_object_types1(page=page, size=size, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_all_plugin_object_types1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerPluginObjectTypeDtoV1**](PagerPluginObjectTypeDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plugins**
> PagerPluginDto get_all_plugins(plugin, options)

Get all plugins

Endpoint for retrieving all plugins with support for filters and pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
plugin = swagger_client.PluginFilterDto() # PluginFilterDto | 
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all plugins
    api_response = api_instance.get_all_plugins(plugin, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_all_plugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin** | [**PluginFilterDto**](.md)|  | 
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerPluginDto**](PagerPluginDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plugins1**
> PagerPluginDto get_all_plugins1(page=page, size=size)

Get all plugins

Endpoint for retrieving all plugins with support for filters and pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)

try:
    # Get all plugins
    api_response = api_instance.get_all_plugins1(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_all_plugins1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]

### Return type

[**PagerPluginDto**](PagerPluginDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_plugin_info_schema**
> dict(str, PluginInfo) get_device_plugin_info_schema()

Get all device extended plugin info schema

Endpoint for retrieving a template of plugin info for device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()

try:
    # Get all device extended plugin info schema
    api_response = api_instance.get_device_plugin_info_schema()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_device_plugin_info_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, PluginInfo)**](PluginInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_plugin_info_schema1**
> dict(str, PluginInfo) get_device_plugin_info_schema1()

Get all device extended plugin info schema

Endpoint for retrieving a template of plugin info for device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()

try:
    # Get all device extended plugin info schema
    api_response = api_instance.get_device_plugin_info_schema1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_device_plugin_info_schema1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, PluginInfo)**](PluginInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator_extended_info_schema**
> dict(str, str) get_indicator_extended_info_schema(plugin_id)

Get indicator extended info schema by plugin Id

Gets schema for Indicator extended info by provided plugin Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
plugin_id = 789 # int | The plugin id of the requested indicator extended info schema

try:
    # Get indicator extended info schema by plugin Id
    api_response = api_instance.get_indicator_extended_info_schema(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_indicator_extended_info_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **int**| The plugin id of the requested indicator extended info schema | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator_extended_info_schema1**
> dict(str, str) get_indicator_extended_info_schema1(plugin_id)

Get indicator extended info schema by plugin Id

Gets schema for Indicator extended info by provided plugin Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
plugin_id = 789 # int | The plugin id of the requested indicator extended info schema

try:
    # Get indicator extended info schema by plugin Id
    api_response = api_instance.get_indicator_extended_info_schema1(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_indicator_extended_info_schema1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **int**| The plugin id of the requested indicator extended info schema | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_extended_info_schema**
> dict(str, str) get_object_extended_info_schema(plugin_id)

Get object extended info schema by plugin Id

Gets schema for object extended info by provided plugin Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
plugin_id = 789 # int | The plugin id of the requested object extended info schema

try:
    # Get object extended info schema by plugin Id
    api_response = api_instance.get_object_extended_info_schema(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_object_extended_info_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **int**| The plugin id of the requested object extended info schema | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_extended_info_schema1**
> dict(str, str) get_object_extended_info_schema1(plugin_id)

Get object extended info schema by plugin Id

Gets schema for object extended info by provided plugin Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
plugin_id = 789 # int | The plugin id of the requested object extended info schema

try:
    # Get object extended info schema by plugin Id
    api_response = api_instance.get_object_extended_info_schema1(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_object_extended_info_schema1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **int**| The plugin id of the requested object extended info schema | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_for_all_plugin_indicator_types**
> dict(str, str) get_schema_for_all_plugin_indicator_types(plugin_id)

Get schema for plugin indicator type extended info

Endpoint for retrieving schema for plugin indicator types extended info by plugin id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
plugin_id = 789 # int | The plugin id of the requested plugin indicator type schema

try:
    # Get schema for plugin indicator type extended info
    api_response = api_instance.get_schema_for_all_plugin_indicator_types(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_schema_for_all_plugin_indicator_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **int**| The plugin id of the requested plugin indicator type schema | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_for_all_plugin_indicator_types1**
> dict(str, str) get_schema_for_all_plugin_indicator_types1(plugin_id)

Get schema for plugin indicator type extended info

Endpoint for retrieving schema for plugin indicator types extended info by plugin id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
plugin_id = 789 # int | The plugin id of the requested plugin indicator type schema

try:
    # Get schema for plugin indicator type extended info
    api_response = api_instance.get_schema_for_all_plugin_indicator_types1(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_schema_for_all_plugin_indicator_types1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **int**| The plugin id of the requested plugin indicator type schema | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_for_all_plugin_object_types**
> dict(str, str) get_schema_for_all_plugin_object_types(plugin_id)

Get schema for plugin object type extended info

Endpoint for retrieving schema for plugin object types extended info by plugin id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
plugin_id = 789 # int | The plugin id of the requested plugin object type schema

try:
    # Get schema for plugin object type extended info
    api_response = api_instance.get_schema_for_all_plugin_object_types(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_schema_for_all_plugin_object_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **int**| The plugin id of the requested plugin object type schema | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_for_all_plugin_object_types1**
> dict(str, str) get_schema_for_all_plugin_object_types1(plugin_id)

Get schema for plugin object type extended info

Endpoint for retrieving schema for plugin object types extended info by plugin id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
plugin_id = 789 # int | The plugin id of the requested plugin object type schema

try:
    # Get schema for plugin object type extended info
    api_response = api_instance.get_schema_for_all_plugin_object_types1(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->get_schema_for_all_plugin_object_types1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **int**| The plugin id of the requested plugin object type schema | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin_indicator_type**
> PluginIndicatorTypeDto update_plugin_indicator_type(body, id)

Updates a plugin indicator type

Endpoint for updating plugin indicator types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginIndicatorTypeRequestDto() # PluginIndicatorTypeRequestDto | 
id = 789 # int | The id of the indicator type to be updated

try:
    # Updates a plugin indicator type
    api_response = api_instance.update_plugin_indicator_type(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->update_plugin_indicator_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginIndicatorTypeRequestDto**](PluginIndicatorTypeRequestDto.md)|  | 
 **id** | **int**| The id of the indicator type to be updated | 

### Return type

[**PluginIndicatorTypeDto**](PluginIndicatorTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin_indicator_type1**
> PluginIndicatorTypeDtoV1 update_plugin_indicator_type1(body, id)

Updates a plugin indicator type

Endpoint for updating plugin indicator types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginIndicatorTypeRequestDtoV1() # PluginIndicatorTypeRequestDtoV1 | 
id = 789 # int | The id of the indicator type to be updated

try:
    # Updates a plugin indicator type
    api_response = api_instance.update_plugin_indicator_type1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->update_plugin_indicator_type1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginIndicatorTypeRequestDtoV1**](PluginIndicatorTypeRequestDtoV1.md)|  | 
 **id** | **int**| The id of the indicator type to be updated | 

### Return type

[**PluginIndicatorTypeDtoV1**](PluginIndicatorTypeDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin_object_type**
> PluginObjectTypeDto update_plugin_object_type(body, id)

Updates an plugin object type

Endpoint for updating plugin object types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginObjectTypeRequestDto() # PluginObjectTypeRequestDto | 
id = 789 # int | The id of the object type to be updated

try:
    # Updates an plugin object type
    api_response = api_instance.update_plugin_object_type(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->update_plugin_object_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginObjectTypeRequestDto**](PluginObjectTypeRequestDto.md)|  | 
 **id** | **int**| The id of the object type to be updated | 

### Return type

[**PluginObjectTypeDto**](PluginObjectTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin_object_type1**
> PluginObjectTypeDtoV1 update_plugin_object_type1(body, id)

Updates an plugin object type

Endpoint for updating plugin object types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsApi()
body = swagger_client.PluginObjectTypeRequestDtoV1() # PluginObjectTypeRequestDtoV1 | 
id = 789 # int | The id of the object type to be updated

try:
    # Updates an plugin object type
    api_response = api_instance.update_plugin_object_type1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsApi->update_plugin_object_type1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PluginObjectTypeRequestDtoV1**](PluginObjectTypeRequestDtoV1.md)|  | 
 **id** | **int**| The id of the object type to be updated | 

### Return type

[**PluginObjectTypeDtoV1**](PluginObjectTypeDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

