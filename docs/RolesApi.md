# swagger_client.RolesApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /api/v2/roles | Create Role
[**delete_role_by_id**](RolesApi.md#delete_role_by_id) | **DELETE** /api/v2/roles/{id} | Delete role
[**filter_roles**](RolesApi.md#filter_roles) | **POST** /api/v2/roles/filter | Filter roles
[**get_all_roles**](RolesApi.md#get_all_roles) | **GET** /api/v2/roles | Get roles
[**get_role**](RolesApi.md#get_role) | **GET** /api/v2/roles/{id} | Get Role
[**patch_role**](RolesApi.md#patch_role) | **PATCH** /api/v2/roles/{id} | Update role

# **create_role**
> UserRoleDto create_role(body)

Create Role

Create a role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
body = swagger_client.UserRoleDto() # UserRoleDto | 

try:
    # Create Role
    api_response = api_instance.create_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRoleDto**](UserRoleDto.md)|  | 

### Return type

[**UserRoleDto**](UserRoleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_by_id**
> str delete_role_by_id(id)

Delete role

Deletes an existing role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
id = 789 # int | The id of the role to be deleted

try:
    # Delete role
    api_response = api_instance.delete_role_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->delete_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the role to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_roles**
> PagerUserRoleDto filter_roles(body)

Filter roles

Endpoint for filtering all roles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
body = swagger_client.RolesFilterBody() # RolesFilterBody | 

try:
    # Filter roles
    api_response = api_instance.filter_roles(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->filter_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolesFilterBody**](RolesFilterBody.md)|  | 

### Return type

[**PagerUserRoleDto**](PagerUserRoleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> PagerUserRoleDto get_all_roles(options)

Get roles

Get all roles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get roles
    api_response = api_instance.get_all_roles(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_all_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerUserRoleDto**](PagerUserRoleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> UserRoleDto get_role(id)

Get Role

Endpoint for retrieving role info by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
id = 789 # int | Role Id

try:
    # Get Role
    api_response = api_instance.get_role(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Role Id | 

### Return type

[**UserRoleDto**](UserRoleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_role**
> UserRoleDto patch_role(body, id)

Update role

Updates an existing role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
body = swagger_client.Role() # Role | 
id = 789 # int | The id of the role to update

try:
    # Update role
    api_response = api_instance.patch_role(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->patch_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Role**](Role.md)|  | 
 **id** | **int**| The id of the role to update | 

### Return type

[**UserRoleDto**](UserRoleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

