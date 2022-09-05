# swagger_client.TopNViewsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_top_n_view**](TopNViewsApi.md#create_top_n_view) | **POST** /api/v2/topnviews | Create TopNView
[**delete_top_n_view_by_id**](TopNViewsApi.md#delete_top_n_view_by_id) | **DELETE** /api/v2/topnviews/{id} | Delete TopNVIew
[**get_top_n_view**](TopNViewsApi.md#get_top_n_view) | **GET** /api/v2/topnviews/{id} | Get TopNView
[**get_top_n_views**](TopNViewsApi.md#get_top_n_views) | **GET** /api/v2/topnviews | Get all TopNViews
[**update_top_n_view_by_id**](TopNViewsApi.md#update_top_n_view_by_id) | **PUT** /api/v2/topnviews/{id} | Update TopNView

# **create_top_n_view**
> TopNViewDto create_top_n_view(body)

Create TopNView

Creates a new TopNView

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
body = swagger_client.TopNViewDto() # TopNViewDto | 

try:
    # Create TopNView
    api_response = api_instance.create_top_n_view(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->create_top_n_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TopNViewDto**](TopNViewDto.md)|  | 

### Return type

[**TopNViewDto**](TopNViewDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_top_n_view_by_id**
> str delete_top_n_view_by_id(id)

Delete TopNVIew

Deletes an existing TopNView

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
id = 789 # int | The id of the TopNView to be deleted

try:
    # Delete TopNVIew
    api_response = api_instance.delete_top_n_view_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->delete_top_n_view_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the TopNView to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_view**
> TopNViewDto get_top_n_view(id)

Get TopNView

Endpoint for retrieving TopNView info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
id = 789 # int | TopNView Id

try:
    # Get TopNView
    api_response = api_instance.get_top_n_view(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->get_top_n_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TopNView Id | 

### Return type

[**TopNViewDto**](TopNViewDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_views**
> PagerTopNViewDto get_top_n_views(options, name=name)

Get all TopNViews

Endpoint for retrieving all views that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
name = 'name_example' # str | Filter by TopNView name (optional)

try:
    # Get all TopNViews
    api_response = api_instance.get_top_n_views(options, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->get_top_n_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **name** | **str**| Filter by TopNView name | [optional] 

### Return type

[**PagerTopNViewDto**](PagerTopNViewDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_view_by_id**
> TopNViewDto update_top_n_view_by_id(body, id)

Update TopNView

Updates an existing TopNVIew

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
body = swagger_client.TopNViewDto() # TopNViewDto | 
id = 789 # int | The id of the TopNView to be updated

try:
    # Update TopNView
    api_response = api_instance.update_top_n_view_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->update_top_n_view_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TopNViewDto**](TopNViewDto.md)|  | 
 **id** | **int**| The id of the TopNView to be updated | 

### Return type

[**TopNViewDto**](TopNViewDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

