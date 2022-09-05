# swagger_client.UsersApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_specific_user_roles**](UsersApi.md#add_specific_user_roles) | **PATCH** /api/v2/users/{id}/roles | Add roles to user
[**change_password**](UsersApi.md#change_password) | **PUT** /api/v2/users/mypreferences/password | Change user password
[**create_user**](UsersApi.md#create_user) | **POST** /api/v2/users | Create user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /api/v2/users/{id} | Delete user
[**filter_users**](UsersApi.md#filter_users) | **POST** /api/v2/users/filter | Filter users
[**force_password_change**](UsersApi.md#force_password_change) | **POST** /api/v2/users/force-password-change | Force password change
[**get_all_users**](UsersApi.md#get_all_users) | **GET** /api/v2/users | Get all users
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /api/v1/users/mypreferences | Get user
[**get_current_user1**](UsersApi.md#get_current_user1) | **GET** /api/v2/users/mypreferences | Get user
[**get_specific_user_roles**](UsersApi.md#get_specific_user_roles) | **GET** /api/v2/users/{id}/roles | Get all roles for a specific user
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /api/v2/users/{id} | Get one user
[**get_user_roles**](UsersApi.md#get_user_roles) | **GET** /api/v2/users/myroles | Get user roles
[**partially_update_user**](UsersApi.md#partially_update_user) | **PATCH** /api/v2/users/{id} | Update user
[**remove_specific_user_roles**](UsersApi.md#remove_specific_user_roles) | **DELETE** /api/v2/users/{id}/roles | Remove roles for user
[**update_user_preferences**](UsersApi.md#update_user_preferences) | **PATCH** /api/v2/users/mypreferences | Update user preferences

# **add_specific_user_roles**
> str add_specific_user_roles(body, id)

Add roles to user

Adds roles to a specific user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = [56] # list[int] | 
id = 789 # int | userId

try:
    # Add roles to user
    api_response = api_instance.add_specific_user_roles(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->add_specific_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | 
 **id** | **int**| userId | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> str change_password(body)

Change user password

Change password for the logged user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.PasswordDto() # PasswordDto | 

try:
    # Change user password
    api_response = api_instance.change_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordDto**](PasswordDto.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserDto create_user(body)

Create user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UserDto() # UserDto | 

try:
    # Create user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDto**](UserDto.md)|  | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> str delete_user(id)

Delete user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 789 # int | 

try:
    # Delete user
    api_response = api_instance.delete_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_users**
> PagerUserDto filter_users(body)

Filter users

The method will return all users that match the filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UsersFilterBody() # UsersFilterBody | 

try:
    # Filter users
    api_response = api_instance.filter_users(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->filter_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersFilterBody**](UsersFilterBody.md)|  | 

### Return type

[**PagerUserDto**](PagerUserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_password_change**
> str force_password_change(body)

Force password change

This method changes a password for a user with force password change set.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.ForcePasswordChangeDto() # ForcePasswordChangeDto | 

try:
    # Force password change
    api_response = api_instance.force_password_change(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->force_password_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForcePasswordChangeDto**](ForcePasswordChangeDto.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> PagerUserDto get_all_users(options)

Get all users

The method will return all visible users for the logged user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all users
    api_response = api_instance.get_all_users(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerUserDto**](PagerUserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> UserDto get_current_user()

Get user

Get user and user preferences

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Get user
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user1**
> UserDto get_current_user1()

Get user

Get user and user preferences

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Get user
    api_response = api_instance.get_current_user1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_current_user1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_user_roles**
> list[UserRoleDto] get_specific_user_roles(id)

Get all roles for a specific user

Get all roles for a specific user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 789 # int | userId

try:
    # Get all roles for a specific user
    api_response = api_instance.get_specific_user_roles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_specific_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| userId | 

### Return type

[**list[UserRoleDto]**](UserRoleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserDto get_user_by_id(id)

Get one user

Get a single user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 789 # int | 

try:
    # Get one user
    api_response = api_instance.get_user_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> list[UserRoleDto] get_user_roles()

Get user roles

Get user and user roles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Get user roles
    api_response = api_instance.get_user_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserRoleDto]**](UserRoleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_user**
> UserDto partially_update_user(body, id)

Update user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UserDto() # UserDto | 
id = 789 # int | 

try:
    # Update user
    api_response = api_instance.partially_update_user(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->partially_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDto**](UserDto.md)|  | 
 **id** | **int**|  | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_specific_user_roles**
> str remove_specific_user_roles(body, id)

Remove roles for user

Removes roles from a specific user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = [56] # list[int] | 
id = 789 # int | userId

try:
    # Remove roles for user
    api_response = api_instance.remove_specific_user_roles(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->remove_specific_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | 
 **id** | **int**| userId | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_preferences**
> UserPreferencesDto update_user_preferences(body)

Update user preferences

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UserPreferencesDto() # UserPreferencesDto | 

try:
    # Update user preferences
    api_response = api_instance.update_user_preferences(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserPreferencesDto**](UserPreferencesDto.md)|  | 

### Return type

[**UserPreferencesDto**](UserPreferencesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

