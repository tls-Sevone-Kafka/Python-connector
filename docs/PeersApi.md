# swagger_client.PeersApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_incorporate_mode**](PeersApi.md#edit_incorporate_mode) | **PATCH** /api/v2/peers/incorporateMode | Edit peer status
[**edit_incorporate_mode1**](PeersApi.md#edit_incorporate_mode1) | **PATCH** /api/v1/peers/incorporateMode | Edit peer status
[**get_cluster_settings**](PeersApi.md#get_cluster_settings) | **GET** /api/v2/peers/clusterSettings | Get cluster settings
[**get_cluster_settings1**](PeersApi.md#get_cluster_settings1) | **GET** /api/v1/peers/clusterSettings | Get cluster settings
[**get_current_peer**](PeersApi.md#get_current_peer) | **GET** /api/v2/peers/current | Current peer
[**get_current_peer1**](PeersApi.md#get_current_peer1) | **GET** /api/v1/peers/current | Current peer
[**get_incorporate_mode**](PeersApi.md#get_incorporate_mode) | **GET** /api/v2/peers/incorporateMode | Get peer status
[**get_incorporate_mode1**](PeersApi.md#get_incorporate_mode1) | **GET** /api/v1/peers/incorporateMode | Get peer status
[**get_peer**](PeersApi.md#get_peer) | **GET** /api/v2/peers/{id} | Get peer
[**get_peer1**](PeersApi.md#get_peer1) | **GET** /api/v1/peers/{id} | Get peer
[**get_peers**](PeersApi.md#get_peers) | **GET** /api/v1/peers | Get peers
[**get_peers1**](PeersApi.md#get_peers1) | **GET** /api/v2/peers | Get peers
[**get_settings**](PeersApi.md#get_settings) | **GET** /api/v1/peers/{id}/settings | Get settings
[**get_settings1**](PeersApi.md#get_settings1) | **GET** /api/v2/peers/{id}/settings | Get settings

# **edit_incorporate_mode**
> IncorporateResponse edit_incorporate_mode(body)

Edit peer status

Edit current peer status - activate or deactivate incorporate mode

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
body = swagger_client.PeerStatus() # PeerStatus | 

try:
    # Edit peer status
    api_response = api_instance.edit_incorporate_mode(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->edit_incorporate_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PeerStatus**](PeerStatus.md)|  | 

### Return type

[**IncorporateResponse**](IncorporateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_incorporate_mode1**
> IncorporateResponse edit_incorporate_mode1(body)

Edit peer status

Edit current peer status - activate or deactivate incorporate mode

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
body = swagger_client.PeerStatus() # PeerStatus | 

try:
    # Edit peer status
    api_response = api_instance.edit_incorporate_mode1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->edit_incorporate_mode1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PeerStatus**](PeerStatus.md)|  | 

### Return type

[**IncorporateResponse**](IncorporateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_settings**
> dict(str, object) get_cluster_settings(filter=filter)

Get cluster settings

Get cluster settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
filter = 'filter_example' # str | Filter to retrieve only subset of cluster settings (optional)

try:
    # Get cluster settings
    api_response = api_instance.get_cluster_settings(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_cluster_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to retrieve only subset of cluster settings | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_settings1**
> dict(str, object) get_cluster_settings1(filter=filter)

Get cluster settings

Get cluster settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
filter = 'filter_example' # str | Filter to retrieve only subset of cluster settings (optional)

try:
    # Get cluster settings
    api_response = api_instance.get_cluster_settings1(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_cluster_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to retrieve only subset of cluster settings | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_peer**
> PeerDto get_current_peer()

Current peer

Gets current peer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()

try:
    # Current peer
    api_response = api_instance.get_current_peer()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_current_peer: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PeerDto**](PeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_peer1**
> PeerDto get_current_peer1()

Current peer

Gets current peer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()

try:
    # Current peer
    api_response = api_instance.get_current_peer1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_current_peer1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PeerDto**](PeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incorporate_mode**
> IncorporateResponse get_incorporate_mode()

Get peer status

Gets incorporate mode status for current peer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()

try:
    # Get peer status
    api_response = api_instance.get_incorporate_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_incorporate_mode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IncorporateResponse**](IncorporateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incorporate_mode1**
> IncorporateResponse get_incorporate_mode1()

Get peer status

Gets incorporate mode status for current peer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()

try:
    # Get peer status
    api_response = api_instance.get_incorporate_mode1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_incorporate_mode1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IncorporateResponse**](IncorporateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer**
> PeerDto get_peer(id)

Get peer

Gets peer by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
id = 789 # int | The id of the peer

try:
    # Get peer
    api_response = api_instance.get_peer(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the peer | 

### Return type

[**PeerDto**](PeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer1**
> PeerDto get_peer1(id)

Get peer

Gets peer by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
id = 789 # int | The id of the peer

try:
    # Get peer
    api_response = api_instance.get_peer1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_peer1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the peer | 

### Return type

[**PeerDto**](PeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peers**
> PagerPeerDto get_peers(options)

Get peers

Gets all peers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get peers
    api_response = api_instance.get_peers(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerPeerDto**](PagerPeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peers1**
> PagerPeerDto get_peers1(options)

Get peers

Gets all peers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get peers
    api_response = api_instance.get_peers1(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_peers1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerPeerDto**](PagerPeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> dict(str, object) get_settings(id, filter=filter)

Get settings

Get settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
id = 789 # int | The id of the peer
filter = 'filter_example' # str | Filter to retrieve only subset of settings (optional)

try:
    # Get settings
    api_response = api_instance.get_settings(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the peer | 
 **filter** | **str**| Filter to retrieve only subset of settings | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings1**
> dict(str, object) get_settings1(id, filter=filter)

Get settings

Get settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
id = 789 # int | The id of the peer
filter = 'filter_example' # str | Filter to retrieve only subset of settings (optional)

try:
    # Get settings
    api_response = api_instance.get_settings1(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the peer | 
 **filter** | **str**| Filter to retrieve only subset of settings | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

