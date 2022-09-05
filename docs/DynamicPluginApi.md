# swagger_client.DynamicPluginApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_dynamic_plugin**](DynamicPluginApi.md#register_dynamic_plugin) | **POST** /api/v1/pluginmanager/{id}/plugin/register | Register plugin in dynamic plugin manager
[**register_dynamic_plugin1**](DynamicPluginApi.md#register_dynamic_plugin1) | **POST** /api/v2/pluginmanager/{id}/plugin/register | Register plugin in dynamic plugin manager
[**register_dynamic_plugin_manager**](DynamicPluginApi.md#register_dynamic_plugin_manager) | **POST** /api/v2/pluginmanager/register | Register dynamic plugin manager
[**register_dynamic_plugin_manager1**](DynamicPluginApi.md#register_dynamic_plugin_manager1) | **POST** /api/v1/pluginmanager/register | Register dynamic plugin manager

# **register_dynamic_plugin**
> DynamicPluginResponseDto register_dynamic_plugin(body, id)

Register plugin in dynamic plugin manager

Register plugin in dynamic plugin manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamicPluginApi()
body = swagger_client.DynamicPluginRequestDto() # DynamicPluginRequestDto | 
id = 789 # int | The id of the pluginmanager

try:
    # Register plugin in dynamic plugin manager
    api_response = api_instance.register_dynamic_plugin(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicPluginApi->register_dynamic_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicPluginRequestDto**](DynamicPluginRequestDto.md)|  | 
 **id** | **int**| The id of the pluginmanager | 

### Return type

[**DynamicPluginResponseDto**](DynamicPluginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_dynamic_plugin1**
> DynamicPluginResponseDto register_dynamic_plugin1(body, id)

Register plugin in dynamic plugin manager

Register plugin in dynamic plugin manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamicPluginApi()
body = swagger_client.DynamicPluginRequestDto() # DynamicPluginRequestDto | 
id = 789 # int | The id of the pluginmanager

try:
    # Register plugin in dynamic plugin manager
    api_response = api_instance.register_dynamic_plugin1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicPluginApi->register_dynamic_plugin1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicPluginRequestDto**](DynamicPluginRequestDto.md)|  | 
 **id** | **int**| The id of the pluginmanager | 

### Return type

[**DynamicPluginResponseDto**](DynamicPluginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_dynamic_plugin_manager**
> DynamicPluginManagerResponseDto register_dynamic_plugin_manager(body)

Register dynamic plugin manager

Registers new dynamic plugin manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamicPluginApi()
body = swagger_client.DynamicPluginManagerRequestDto() # DynamicPluginManagerRequestDto | 

try:
    # Register dynamic plugin manager
    api_response = api_instance.register_dynamic_plugin_manager(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicPluginApi->register_dynamic_plugin_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicPluginManagerRequestDto**](DynamicPluginManagerRequestDto.md)|  | 

### Return type

[**DynamicPluginManagerResponseDto**](DynamicPluginManagerResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_dynamic_plugin_manager1**
> DynamicPluginManagerResponseDto register_dynamic_plugin_manager1(body)

Register dynamic plugin manager

Registers new dynamic plugin manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamicPluginApi()
body = swagger_client.DynamicPluginManagerRequestDto() # DynamicPluginManagerRequestDto | 

try:
    # Register dynamic plugin manager
    api_response = api_instance.register_dynamic_plugin_manager1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicPluginApi->register_dynamic_plugin_manager1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicPluginManagerRequestDto**](DynamicPluginManagerRequestDto.md)|  | 

### Return type

[**DynamicPluginManagerResponseDto**](DynamicPluginManagerResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

