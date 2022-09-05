# swagger_client.StatusMapImagesApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_map_image_by_id**](StatusMapImagesApi.md#get_map_image_by_id) | **GET** /api/v1/mapimages/{id} | Get map image
[**get_map_image_by_id1**](StatusMapImagesApi.md#get_map_image_by_id1) | **GET** /api/v2/mapimages/{id} | Get map image
[**get_map_images**](StatusMapImagesApi.md#get_map_images) | **GET** /api/v1/mapimages | Get all map images
[**get_map_images1**](StatusMapImagesApi.md#get_map_images1) | **GET** /api/v2/mapimages | Get all map images

# **get_map_image_by_id**
> get_map_image_by_id(id)

Get map image

Endpoint for retrieving the map image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapImagesApi()
id = 789 # int | The id of the image to be retrieved

try:
    # Get map image
    api_instance.get_map_image_by_id(id)
except ApiException as e:
    print("Exception when calling StatusMapImagesApi->get_map_image_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the image to be retrieved | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_image_by_id1**
> get_map_image_by_id1(id)

Get map image

Endpoint for retrieving the map image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapImagesApi()
id = 789 # int | The id of the image to be retrieved

try:
    # Get map image
    api_instance.get_map_image_by_id1(id)
except ApiException as e:
    print("Exception when calling StatusMapImagesApi->get_map_image_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the image to be retrieved | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_images**
> PagerMapImageDto get_map_images(options)

Get all map images

Endpoint for retrieving all map images that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapImagesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all map images
    api_response = api_instance.get_map_images(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapImagesApi->get_map_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerMapImageDto**](PagerMapImageDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_images1**
> PagerMapImageDto get_map_images1(options)

Get all map images

Endpoint for retrieving all map images that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusMapImagesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all map images
    api_response = api_instance.get_map_images1(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusMapImagesApi->get_map_images1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerMapImageDto**](PagerMapImageDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

