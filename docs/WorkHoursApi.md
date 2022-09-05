# swagger_client.WorkHoursApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_work_hours**](WorkHoursApi.md#create_work_hours) | **POST** /api/v2/workhours | Create WorkHours
[**delete_work_hours_group_by_id**](WorkHoursApi.md#delete_work_hours_group_by_id) | **DELETE** /api/v2/workhours/{id} | Delete WorkHour group
[**get_work_hours**](WorkHoursApi.md#get_work_hours) | **GET** /api/v2/workhours | Get all WorkHours
[**get_work_hours_by_group**](WorkHoursApi.md#get_work_hours_by_group) | **GET** /api/v2/workhours/{id} | Get WorkHour by group
[**update_work_hours_by_group_id**](WorkHoursApi.md#update_work_hours_by_group_id) | **PUT** /api/v2/workhours/{id} | Update WorkHours

# **create_work_hours**
> WorkHoursGroupDto create_work_hours(body)

Create WorkHours

Creates a new WorkHours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkHoursApi()
body = swagger_client.WorkHoursGroupDto() # WorkHoursGroupDto | 

try:
    # Create WorkHours
    api_response = api_instance.create_work_hours(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkHoursApi->create_work_hours: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkHoursGroupDto**](WorkHoursGroupDto.md)|  | 

### Return type

[**WorkHoursGroupDto**](WorkHoursGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_hours_group_by_id**
> str delete_work_hours_group_by_id(id)

Delete WorkHour group

Deletes an existing WorkHour group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkHoursApi()
id = 789 # int | The id of the WorkHour group to be deleted

try:
    # Delete WorkHour group
    api_response = api_instance.delete_work_hours_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkHoursApi->delete_work_hours_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the WorkHour group to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_hours**
> PagerWorkHoursGroupDto get_work_hours(options, name=name)

Get all WorkHours

Endpoint for retrieving all WorkHours that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkHoursApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
name = 'name_example' # str | Filter by WorkHours group name (optional)

try:
    # Get all WorkHours
    api_response = api_instance.get_work_hours(options, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkHoursApi->get_work_hours: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **name** | **str**| Filter by WorkHours group name | [optional] 

### Return type

[**PagerWorkHoursGroupDto**](PagerWorkHoursGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_hours_by_group**
> WorkHoursGroupDto get_work_hours_by_group(id)

Get WorkHour by group

Endpoint for retrieving WorkHours info by group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkHoursApi()
id = 789 # int | WorkHour group Id

try:
    # Get WorkHour by group
    api_response = api_instance.get_work_hours_by_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkHoursApi->get_work_hours_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| WorkHour group Id | 

### Return type

[**WorkHoursGroupDto**](WorkHoursGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work_hours_by_group_id**
> WorkHoursGroupDto update_work_hours_by_group_id(body, id)

Update WorkHours

Updates an existing WorkHours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkHoursApi()
body = swagger_client.WorkHoursGroupDto() # WorkHoursGroupDto | 
id = 789 # int | The id of the WorkHours to be updated

try:
    # Update WorkHours
    api_response = api_instance.update_work_hours_by_group_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkHoursApi->update_work_hours_by_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkHoursGroupDto**](WorkHoursGroupDto.md)|  | 
 **id** | **int**| The id of the WorkHours to be updated | 

### Return type

[**WorkHoursGroupDto**](WorkHoursGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

