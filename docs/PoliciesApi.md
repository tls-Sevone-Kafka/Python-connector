# swagger_client.PoliciesApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](PoliciesApi.md#create_policy) | **POST** /api/v1/policies/folders | Create new policy folder
[**create_policy1**](PoliciesApi.md#create_policy1) | **POST** /api/v2/policies/folders | Create new policy folder
[**create_policy2**](PoliciesApi.md#create_policy2) | **POST** /api/v1/policies | Create new policy
[**create_policy3**](PoliciesApi.md#create_policy3) | **POST** /api/v2/policies | Create new policy
[**create_policy_condition**](PoliciesApi.md#create_policy_condition) | **POST** /api/v2/policies/{policyId}/conditions | Create new policy condition
[**create_policy_condition1**](PoliciesApi.md#create_policy_condition1) | **POST** /api/v1/policies/{policyId}/conditions | Create new policy condition
[**delete_policy_action_by_id**](PoliciesApi.md#delete_policy_action_by_id) | **DELETE** /api/v1/policies/{policyId}/actions | Delete policy action
[**delete_policy_action_by_id1**](PoliciesApi.md#delete_policy_action_by_id1) | **DELETE** /api/v2/policies/{policyId}/actions | Delete policy action
[**delete_policy_by_id**](PoliciesApi.md#delete_policy_by_id) | **DELETE** /api/v1/policies/{id} | Delete policy
[**delete_policy_by_id1**](PoliciesApi.md#delete_policy_by_id1) | **DELETE** /api/v2/policies/{id} | Delete policy
[**delete_policy_condition_by_id**](PoliciesApi.md#delete_policy_condition_by_id) | **DELETE** /api/v2/policies/{policyId}/conditions/{conditionId} | Delete policy condition
[**delete_policy_condition_by_id1**](PoliciesApi.md#delete_policy_condition_by_id1) | **DELETE** /api/v1/policies/{policyId}/conditions/{conditionId} | Delete policy condition
[**delete_policy_folder_by_id**](PoliciesApi.md#delete_policy_folder_by_id) | **DELETE** /api/v1/policies/folders/{id} | Delete policy folder
[**delete_policy_folder_by_id1**](PoliciesApi.md#delete_policy_folder_by_id1) | **DELETE** /api/v2/policies/folders/{id} | Delete policy folder
[**filter_policies**](PoliciesApi.md#filter_policies) | **POST** /api/v1/policies/filter | Filter policies
[**filter_policies1**](PoliciesApi.md#filter_policies1) | **POST** /api/v2/policies/filter | Filter policies
[**find_all**](PoliciesApi.md#find_all) | **GET** /api/v2/policies/{policyId}/conditions | Get all policy conditions
[**find_all1**](PoliciesApi.md#find_all1) | **GET** /api/v1/policies/{policyId}/conditions | Get all policy conditions
[**get_actions**](PoliciesApi.md#get_actions) | **GET** /api/v1/policies/{policyId}/actions | Get all policy actions
[**get_actions1**](PoliciesApi.md#get_actions1) | **GET** /api/v2/policies/{policyId}/actions | Get all policy actions
[**get_policies**](PoliciesApi.md#get_policies) | **GET** /api/v1/policies | Get all policies
[**get_policies1**](PoliciesApi.md#get_policies1) | **GET** /api/v2/policies | Get all policies
[**get_policy**](PoliciesApi.md#get_policy) | **GET** /api/v1/policies/{id} | Get policy by Id
[**get_policy1**](PoliciesApi.md#get_policy1) | **GET** /api/v2/policies/{id} | Get policy by Id
[**get_policy_condition_by_id**](PoliciesApi.md#get_policy_condition_by_id) | **GET** /api/v2/policies/{policyId}/conditions/{conditionId} | Get policy condition by policyId and conditionId
[**get_policy_condition_by_id1**](PoliciesApi.md#get_policy_condition_by_id1) | **GET** /api/v1/policies/{policyId}/conditions/{conditionId} | Get policy condition by policyId and conditionId
[**get_policy_folders**](PoliciesApi.md#get_policy_folders) | **GET** /api/v1/policies/folders | Get all policy Folders
[**get_policy_folders1**](PoliciesApi.md#get_policy_folders1) | **GET** /api/v2/policies/folders | Get all policy Folders
[**update_policy**](PoliciesApi.md#update_policy) | **PUT** /api/v1/policies/{id} | Update policy
[**update_policy1**](PoliciesApi.md#update_policy1) | **PUT** /api/v2/policies/{id} | Update policy
[**update_policy_action**](PoliciesApi.md#update_policy_action) | **PUT** /api/v1/policies/{policyId}/actions | Update policy action
[**update_policy_action1**](PoliciesApi.md#update_policy_action1) | **PUT** /api/v2/policies/{policyId}/actions | Update policy action
[**update_policy_condition**](PoliciesApi.md#update_policy_condition) | **PUT** /api/v2/policies/{policyId}/conditions/{conditionId} | Update policy condition
[**update_policy_condition1**](PoliciesApi.md#update_policy_condition1) | **PUT** /api/v1/policies/{policyId}/conditions/{conditionId} | Update policy condition
[**update_policy_folder**](PoliciesApi.md#update_policy_folder) | **PUT** /api/v1/policies/folders/{id} | Update policy folder
[**update_policy_folder1**](PoliciesApi.md#update_policy_folder1) | **PUT** /api/v2/policies/folders/{id} | Update policy folder

# **create_policy**
> PolicyFolderDto create_policy(body)

Create new policy folder

Create new policy folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyFolderCreateDto() # PolicyFolderCreateDto | 

try:
    # Create new policy folder
    api_response = api_instance.create_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyFolderCreateDto**](PolicyFolderCreateDto.md)|  | 

### Return type

[**PolicyFolderDto**](PolicyFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy1**
> PolicyFolderDto create_policy1(body)

Create new policy folder

Create new policy folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyFolderCreateDto() # PolicyFolderCreateDto | 

try:
    # Create new policy folder
    api_response = api_instance.create_policy1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->create_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyFolderCreateDto**](PolicyFolderCreateDto.md)|  | 

### Return type

[**PolicyFolderDto**](PolicyFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy2**
> PolicyDto create_policy2(body)

Create new policy

Create new policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyDto() # PolicyDto | 

try:
    # Create new policy
    api_response = api_instance.create_policy2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->create_policy2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyDto**](PolicyDto.md)|  | 

### Return type

[**PolicyDto**](PolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy3**
> PolicyDto create_policy3(body)

Create new policy

Create new policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyDto() # PolicyDto | 

try:
    # Create new policy
    api_response = api_instance.create_policy3(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->create_policy3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyDto**](PolicyDto.md)|  | 

### Return type

[**PolicyDto**](PolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_condition**
> PolicyConditionDto create_policy_condition(body, policy_id)

Create new policy condition

Create new policy condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyConditionDto() # PolicyConditionDto | 
policy_id = 789 # int | The id of the policy which condition needs to be updated

try:
    # Create new policy condition
    api_response = api_instance.create_policy_condition(body, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->create_policy_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyConditionDto**](PolicyConditionDto.md)|  | 
 **policy_id** | **int**| The id of the policy which condition needs to be updated | 

### Return type

[**PolicyConditionDto**](PolicyConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_condition1**
> PolicyConditionDto create_policy_condition1(body, policy_id)

Create new policy condition

Create new policy condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyConditionDto() # PolicyConditionDto | 
policy_id = 789 # int | The id of the policy which condition needs to be updated

try:
    # Create new policy condition
    api_response = api_instance.create_policy_condition1(body, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->create_policy_condition1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyConditionDto**](PolicyConditionDto.md)|  | 
 **policy_id** | **int**| The id of the policy which condition needs to be updated | 

### Return type

[**PolicyConditionDto**](PolicyConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_action_by_id**
> str delete_policy_action_by_id(policy_id)

Delete policy action

Deletes an existing policy action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
policy_id = 789 # int | The id of the policy which action will be deleted

try:
    # Delete policy action
    api_response = api_instance.delete_policy_action_by_id(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy_action_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The id of the policy which action will be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_action_by_id1**
> str delete_policy_action_by_id1(policy_id)

Delete policy action

Deletes an existing policy action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
policy_id = 789 # int | The id of the policy which action will be deleted

try:
    # Delete policy action
    api_response = api_instance.delete_policy_action_by_id1(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy_action_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The id of the policy which action will be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_by_id**
> str delete_policy_by_id(id)

Delete policy

Deletes an existing policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 789 # int | The id of the policy to be deleted

try:
    # Delete policy
    api_response = api_instance.delete_policy_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the policy to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_by_id1**
> str delete_policy_by_id1(id)

Delete policy

Deletes an existing policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 789 # int | The id of the policy to be deleted

try:
    # Delete policy
    api_response = api_instance.delete_policy_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the policy to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_condition_by_id**
> str delete_policy_condition_by_id(policy_id, condition_id)

Delete policy condition

Deletes an existing policy condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
policy_id = 789 # int | The id of the policy which condition will be deleted
condition_id = 789 # int | The id of the policy condition to delete

try:
    # Delete policy condition
    api_response = api_instance.delete_policy_condition_by_id(policy_id, condition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy_condition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The id of the policy which condition will be deleted | 
 **condition_id** | **int**| The id of the policy condition to delete | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_condition_by_id1**
> str delete_policy_condition_by_id1(policy_id, condition_id)

Delete policy condition

Deletes an existing policy condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
policy_id = 789 # int | The id of the policy which condition will be deleted
condition_id = 789 # int | The id of the policy condition to delete

try:
    # Delete policy condition
    api_response = api_instance.delete_policy_condition_by_id1(policy_id, condition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy_condition_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The id of the policy which condition will be deleted | 
 **condition_id** | **int**| The id of the policy condition to delete | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_folder_by_id**
> str delete_policy_folder_by_id(id)

Delete policy folder

Deletes an existing policy folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 789 # int | The id of the policy folder to be deleted

try:
    # Delete policy folder
    api_response = api_instance.delete_policy_folder_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy_folder_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the policy folder to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_folder_by_id1**
> str delete_policy_folder_by_id1(id)

Delete policy folder

Deletes an existing policy folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 789 # int | The id of the policy folder to be deleted

try:
    # Delete policy folder
    api_response = api_instance.delete_policy_folder_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete_policy_folder_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the policy folder to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_policies**
> PagerPolicyDto filter_policies(body)

Filter policies

Endpoint for filtering all policies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PoliciesFilterBody() # PoliciesFilterBody | 

try:
    # Filter policies
    api_response = api_instance.filter_policies(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->filter_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoliciesFilterBody**](PoliciesFilterBody.md)|  | 

### Return type

[**PagerPolicyDto**](PagerPolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_policies1**
> PagerPolicyDto filter_policies1(body)

Filter policies

Endpoint for filtering all policies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PoliciesFilterBody1() # PoliciesFilterBody1 | 

try:
    # Filter policies
    api_response = api_instance.filter_policies1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->filter_policies1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoliciesFilterBody1**](PoliciesFilterBody1.md)|  | 

### Return type

[**PagerPolicyDto**](PagerPolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all**
> PagerPolicyConditionDto find_all(options, policy_id)

Get all policy conditions

Endpoint for retrieving all policy conditions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
policy_id = 789 # int | The id of the policy which conditions you need to select

try:
    # Get all policy conditions
    api_response = api_instance.find_all(options, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **policy_id** | **int**| The id of the policy which conditions you need to select | 

### Return type

[**PagerPolicyConditionDto**](PagerPolicyConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all1**
> PagerPolicyConditionDto find_all1(options, policy_id)

Get all policy conditions

Endpoint for retrieving all policy conditions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
policy_id = 789 # int | The id of the policy which conditions you need to select

try:
    # Get all policy conditions
    api_response = api_instance.find_all1(options, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->find_all1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **policy_id** | **int**| The id of the policy which conditions you need to select | 

### Return type

[**PagerPolicyConditionDto**](PagerPolicyConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions**
> PolicyActionDto get_actions(policy_id)

Get all policy actions

Endpoint for retrieving all policy actions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
policy_id = 789 # int | The id of the policy which actions you need to select

try:
    # Get all policy actions
    api_response = api_instance.get_actions(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The id of the policy which actions you need to select | 

### Return type

[**PolicyActionDto**](PolicyActionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions1**
> PolicyActionDto get_actions1(policy_id)

Get all policy actions

Endpoint for retrieving all policy actions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
policy_id = 789 # int | The id of the policy which actions you need to select

try:
    # Get all policy actions
    api_response = api_instance.get_actions1(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_actions1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The id of the policy which actions you need to select | 

### Return type

[**PolicyActionDto**](PolicyActionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> PagerPolicyDto get_policies(options, type=type)

Get all policies

Endpoint for retrieving all policies that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
type = 'type_example' # str | Policy type filter. If not set, both other and flow policies are returned (optional)

try:
    # Get all policies
    api_response = api_instance.get_policies(options, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **type** | **str**| Policy type filter. If not set, both other and flow policies are returned | [optional] 

### Return type

[**PagerPolicyDto**](PagerPolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies1**
> PagerPolicyDto get_policies1(options, type=type)

Get all policies

Endpoint for retrieving all policies that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
type = 'type_example' # str | Policy type filter. If not set, both other and flow policies are returned (optional)

try:
    # Get all policies
    api_response = api_instance.get_policies1(options, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policies1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **type** | **str**| Policy type filter. If not set, both other and flow policies are returned | [optional] 

### Return type

[**PagerPolicyDto**](PagerPolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> PolicyDto get_policy(id)

Get policy by Id

Gets policy information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 789 # int | The id of the requested policy

try:
    # Get policy by Id
    api_response = api_instance.get_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested policy | 

### Return type

[**PolicyDto**](PolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy1**
> PolicyDto get_policy1(id)

Get policy by Id

Gets policy information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
id = 789 # int | The id of the requested policy

try:
    # Get policy by Id
    api_response = api_instance.get_policy1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested policy | 

### Return type

[**PolicyDto**](PolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_condition_by_id**
> PolicyConditionDto get_policy_condition_by_id(policy_id, condition_id)

Get policy condition by policyId and conditionId

Gets policy condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
policy_id = 789 # int | The id of the policy which conditions you need to select
condition_id = 789 # int | The id of the requested policy condition

try:
    # Get policy condition by policyId and conditionId
    api_response = api_instance.get_policy_condition_by_id(policy_id, condition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy_condition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The id of the policy which conditions you need to select | 
 **condition_id** | **int**| The id of the requested policy condition | 

### Return type

[**PolicyConditionDto**](PolicyConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_condition_by_id1**
> PolicyConditionDto get_policy_condition_by_id1(policy_id, condition_id)

Get policy condition by policyId and conditionId

Gets policy condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
policy_id = 789 # int | The id of the policy which conditions you need to select
condition_id = 789 # int | The id of the requested policy condition

try:
    # Get policy condition by policyId and conditionId
    api_response = api_instance.get_policy_condition_by_id1(policy_id, condition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy_condition_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The id of the policy which conditions you need to select | 
 **condition_id** | **int**| The id of the requested policy condition | 

### Return type

[**PolicyConditionDto**](PolicyConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_folders**
> PagerPolicyFolderDto get_policy_folders(options)

Get all policy Folders

Endpoint for retrieving all policy Folders that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all policy Folders
    api_response = api_instance.get_policy_folders(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerPolicyFolderDto**](PagerPolicyFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_folders1**
> PagerPolicyFolderDto get_policy_folders1(options)

Get all policy Folders

Endpoint for retrieving all policy Folders that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all policy Folders
    api_response = api_instance.get_policy_folders1(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policy_folders1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerPolicyFolderDto**](PagerPolicyFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> PolicyDto update_policy(body, id)

Update policy

Update the existing policy. If folder is not editable (i.e. Selfmon Alerts), all fields except userEnabled will be ignored as user can only enable or disable policies. User needs to provide folderId and userEnabled fields in this case.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyDto() # PolicyDto | 
id = 789 # int | The id of the policy to be updated

try:
    # Update policy
    api_response = api_instance.update_policy(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyDto**](PolicyDto.md)|  | 
 **id** | **int**| The id of the policy to be updated | 

### Return type

[**PolicyDto**](PolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy1**
> PolicyDto update_policy1(body, id)

Update policy

Update the existing policy. If folder is not editable (i.e. Selfmon Alerts), all fields except userEnabled will be ignored as user can only enable or disable policies. User needs to provide folderId and userEnabled fields in this case.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyDto() # PolicyDto | 
id = 789 # int | The id of the policy to be updated

try:
    # Update policy
    api_response = api_instance.update_policy1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyDto**](PolicyDto.md)|  | 
 **id** | **int**| The id of the policy to be updated | 

### Return type

[**PolicyDto**](PolicyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_action**
> PolicyActionDto update_policy_action(body, policy_id)

Update policy action

Update the existing policy action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyActionDto() # PolicyActionDto | 
policy_id = 789 # int | The id of the policy which action needs to be updated

try:
    # Update policy action
    api_response = api_instance.update_policy_action(body, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyActionDto**](PolicyActionDto.md)|  | 
 **policy_id** | **int**| The id of the policy which action needs to be updated | 

### Return type

[**PolicyActionDto**](PolicyActionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_action1**
> PolicyActionDto update_policy_action1(body, policy_id)

Update policy action

Update the existing policy action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyActionDto() # PolicyActionDto | 
policy_id = 789 # int | The id of the policy which action needs to be updated

try:
    # Update policy action
    api_response = api_instance.update_policy_action1(body, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy_action1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyActionDto**](PolicyActionDto.md)|  | 
 **policy_id** | **int**| The id of the policy which action needs to be updated | 

### Return type

[**PolicyActionDto**](PolicyActionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_condition**
> PolicyConditionDto update_policy_condition(body, policy_id, condition_id)

Update policy condition

Update the existing policy condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyConditionDto() # PolicyConditionDto | 
policy_id = 789 # int | The id of the policy which condition needs to be updated
condition_id = 789 # int | The id of the requested policy condition

try:
    # Update policy condition
    api_response = api_instance.update_policy_condition(body, policy_id, condition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyConditionDto**](PolicyConditionDto.md)|  | 
 **policy_id** | **int**| The id of the policy which condition needs to be updated | 
 **condition_id** | **int**| The id of the requested policy condition | 

### Return type

[**PolicyConditionDto**](PolicyConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_condition1**
> PolicyConditionDto update_policy_condition1(body, policy_id, condition_id)

Update policy condition

Update the existing policy condition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyConditionDto() # PolicyConditionDto | 
policy_id = 789 # int | The id of the policy which condition needs to be updated
condition_id = 789 # int | The id of the requested policy condition

try:
    # Update policy condition
    api_response = api_instance.update_policy_condition1(body, policy_id, condition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy_condition1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyConditionDto**](PolicyConditionDto.md)|  | 
 **policy_id** | **int**| The id of the policy which condition needs to be updated | 
 **condition_id** | **int**| The id of the requested policy condition | 

### Return type

[**PolicyConditionDto**](PolicyConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_folder**
> PolicyFolderDto update_policy_folder(body, id)

Update policy folder

Update the existing policy folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyFolderUpdateDto() # PolicyFolderUpdateDto | 
id = 789 # int | The id of the policy to be updated

try:
    # Update policy folder
    api_response = api_instance.update_policy_folder(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyFolderUpdateDto**](PolicyFolderUpdateDto.md)|  | 
 **id** | **int**| The id of the policy to be updated | 

### Return type

[**PolicyFolderDto**](PolicyFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_folder1**
> PolicyFolderDto update_policy_folder1(body, id)

Update policy folder

Update the existing policy folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()
body = swagger_client.PolicyFolderUpdateDto() # PolicyFolderUpdateDto | 
id = 789 # int | The id of the policy to be updated

try:
    # Update policy folder
    api_response = api_instance.update_policy_folder1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update_policy_folder1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyFolderUpdateDto**](PolicyFolderUpdateDto.md)|  | 
 **id** | **int**| The id of the policy to be updated | 

### Return type

[**PolicyFolderDto**](PolicyFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

