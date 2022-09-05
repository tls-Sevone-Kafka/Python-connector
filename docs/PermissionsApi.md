# swagger_client.PermissionsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_permissions**](PermissionsApi.md#get_access_permissions) | **GET** /api/v2/permissions/{roleId}/access | Get access permissions
[**get_page_permissions**](PermissionsApi.md#get_page_permissions) | **GET** /api/v2/permissions/{roleId}/page | Get page permissions
[**get_role_permissions**](PermissionsApi.md#get_role_permissions) | **PUT** /api/v2/permissions/{roleId}/role/{targetRoleId} | Update userrole permissions
[**get_role_permissions1**](PermissionsApi.md#get_role_permissions1) | **GET** /api/v2/permissions/{roleId}/role | Get userrole permissions
[**get_role_permissions2**](PermissionsApi.md#get_role_permissions2) | **GET** /api/v2/permissions/{roleId}/role/{targetRoleId} | Get userrole permissions
[**update_access_permissions**](PermissionsApi.md#update_access_permissions) | **PUT** /api/v2/permissions/{roleId}/access | Update access permissions
[**update_device_group_permissions**](PermissionsApi.md#update_device_group_permissions) | **PATCH** /api/v2/permissions/{roleId}/devicegroup/{id} | Update deviceGroup permissions
[**update_device_group_permissions1**](PermissionsApi.md#update_device_group_permissions1) | **GET** /api/v2/permissions/{roleId}/devicegroup | Get deviceGroup permissions
[**update_device_group_permissions2**](PermissionsApi.md#update_device_group_permissions2) | **GET** /api/v2/permissions/{roleId}/devicegroup/{id} | Get deviceGroup permissions
[**update_page_permissions**](PermissionsApi.md#update_page_permissions) | **PUT** /api/v2/permissions/{roleId}/page | Update page permissions

# **get_access_permissions**
> list[str] get_access_permissions(role_id)

Get access permissions

Get role's access permissions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
role_id = 789 # int | RoleId

try:
    # Get access permissions
    api_response = api_instance.get_access_permissions(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_access_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| RoleId | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_permissions**
> list[str] get_page_permissions(role_id)

Get page permissions

Get role's page permissions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
role_id = 789 # int | RoleId

try:
    # Get page permissions
    api_response = api_instance.get_page_permissions(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_page_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| RoleId | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_permissions**
> RolePermissionDto get_role_permissions(body, role_id, target_role_id)

Update userrole permissions

Update role's permissions to view/edit other roles and users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
body = swagger_client.RolePermissionDto() # RolePermissionDto | 
role_id = 789 # int | RoleId
target_role_id = 789 # int | TargetRoleId

try:
    # Update userrole permissions
    api_response = api_instance.get_role_permissions(body, role_id, target_role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_role_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RolePermissionDto**](RolePermissionDto.md)|  | 
 **role_id** | **int**| RoleId | 
 **target_role_id** | **int**| TargetRoleId | 

### Return type

[**RolePermissionDto**](RolePermissionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_permissions1**
> PagerRolePermissionDto get_role_permissions1(role_id, options)

Get userrole permissions

Get role's permissions to view/edit other roles and users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
role_id = 789 # int | RoleId
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get userrole permissions
    api_response = api_instance.get_role_permissions1(role_id, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_role_permissions1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| RoleId | 
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerRolePermissionDto**](PagerRolePermissionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_permissions2**
> RolePermissionDto get_role_permissions2(role_id, target_role_id)

Get userrole permissions

Get role's permissions to view/edit other roles and users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
role_id = 789 # int | RoleId
target_role_id = 789 # int | TargetRoleId

try:
    # Get userrole permissions
    api_response = api_instance.get_role_permissions2(role_id, target_role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_role_permissions2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| RoleId | 
 **target_role_id** | **int**| TargetRoleId | 

### Return type

[**RolePermissionDto**](RolePermissionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_permissions**
> list[str] update_access_permissions(body, role_id)

Update access permissions

Update role's access permissions, the method will replace all existing access permissions with one passed in the body of the request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
body = ['body_example'] # list[str] | 
role_id = 789 # int | RoleId

try:
    # Update access permissions
    api_response = api_instance.update_access_permissions(body, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->update_access_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **role_id** | **int**| RoleId | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_permissions**
> DeviceGroupPermissionDto update_device_group_permissions(body, role_id, id)

Update deviceGroup permissions

Update role's device and deviceGroup permissions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
body = swagger_client.DeviceGroupPermissionDto() # DeviceGroupPermissionDto | 
role_id = 789 # int | RoleId
id = 789 # int | DeviceGroupId

try:
    # Update deviceGroup permissions
    api_response = api_instance.update_device_group_permissions(body, role_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->update_device_group_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroupPermissionDto**](DeviceGroupPermissionDto.md)|  | 
 **role_id** | **int**| RoleId | 
 **id** | **int**| DeviceGroupId | 

### Return type

[**DeviceGroupPermissionDto**](DeviceGroupPermissionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_permissions1**
> PagerDeviceGroupPermissionDto update_device_group_permissions1(role_id, options)

Get deviceGroup permissions

Get role's device and deviceGroup permissions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
role_id = 789 # int | RoleId
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get deviceGroup permissions
    api_response = api_instance.update_device_group_permissions1(role_id, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->update_device_group_permissions1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| RoleId | 
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerDeviceGroupPermissionDto**](PagerDeviceGroupPermissionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_permissions2**
> DeviceGroupPermissionDto update_device_group_permissions2(role_id, id)

Get deviceGroup permissions

Get role's device and deviceGroup permissions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
role_id = 789 # int | RoleId
id = 789 # int | DeviceGroupId

try:
    # Get deviceGroup permissions
    api_response = api_instance.update_device_group_permissions2(role_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->update_device_group_permissions2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **int**| RoleId | 
 **id** | **int**| DeviceGroupId | 

### Return type

[**DeviceGroupPermissionDto**](DeviceGroupPermissionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_page_permissions**
> list[str] update_page_permissions(body, role_id)

Update page permissions

Update role's access permissions, the method will replace all existing page permissions with ones passed in the body of the request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
body = ['body_example'] # list[str] | 
role_id = 789 # int | RoleId

try:
    # Update page permissions
    api_response = api_instance.update_page_permissions(body, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->update_page_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **role_id** | **int**| RoleId | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

