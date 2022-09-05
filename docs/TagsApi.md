# swagger_client.TagsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tags**](TagsApi.md#get_tags) | **GET** /api/v2/tags | Get all Tags
[**get_tags1**](TagsApi.md#get_tags1) | **GET** /api/v2/tags/{name}/indicatortypes | Get Indicator Types Based On Tag Name 

# **get_tags**
> PagerTagsDto get_tags(options, name=name)

Get all Tags

Endpoint for retrieving all Tags that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
name = 'name_example' # str | Name of the tag (optional)

try:
    # Get all Tags
    api_response = api_instance.get_tags(options, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **name** | **str**| Name of the tag | [optional] 

### Return type

[**PagerTagsDto**](PagerTagsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags1**
> PagerTagIndicatorTypesDto get_tags1(name, page=page, size=size)

Get Indicator Types Based On Tag Name 

Endpoint for retrieving all Indicator Types Based On Tag Name that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
name = 'name_example' # str | Name of the tag
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20 (optional) (default to 20)

try:
    # Get Indicator Types Based On Tag Name 
    api_response = api_instance.get_tags1(name, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tags1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the tag | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20 | [optional] [default to 20]

### Return type

[**PagerTagIndicatorTypesDto**](PagerTagIndicatorTypesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

