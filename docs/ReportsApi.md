# swagger_client.ReportsApi

All URIs are relative to *http://watto-nms.coc-ibm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportsApi.md#create_report) | **POST** /api/v2/reports | Create report
[**create_report1**](ReportsApi.md#create_report1) | **POST** /api/v1/reports | Create report
[**create_report_folder**](ReportsApi.md#create_report_folder) | **POST** /api/v2/reports/folders | Create report folder
[**create_report_folder1**](ReportsApi.md#create_report_folder1) | **POST** /api/v1/reports/folders | Create report folder
[**delete_report_by_id**](ReportsApi.md#delete_report_by_id) | **DELETE** /api/v2/reports/{id} | Delete report
[**delete_report_by_id1**](ReportsApi.md#delete_report_by_id1) | **DELETE** /api/v1/reports/{id} | Delete report
[**delete_report_folder_by_id**](ReportsApi.md#delete_report_folder_by_id) | **DELETE** /api/v2/reports/folders/{id} | Delete report folder
[**delete_report_folder_by_id1**](ReportsApi.md#delete_report_folder_by_id1) | **DELETE** /api/v1/reports/folders/{id} | Delete report folder
[**get_all_report_folders**](ReportsApi.md#get_all_report_folders) | **GET** /api/v2/reports/folders | Get all report folders
[**get_all_report_folders1**](ReportsApi.md#get_all_report_folders1) | **GET** /api/v1/reports/folders | Get all report folders
[**get_all_reports**](ReportsApi.md#get_all_reports) | **GET** /api/v2/reports | Get all reports
[**get_all_reports1**](ReportsApi.md#get_all_reports1) | **GET** /api/v1/reports | Get all reports
[**get_report**](ReportsApi.md#get_report) | **GET** /api/v2/reports/{id} | Get report
[**get_report1**](ReportsApi.md#get_report1) | **GET** /api/v1/reports/{id} | Get report
[**update_report_by_id**](ReportsApi.md#update_report_by_id) | **PUT** /api/v2/reports/{id} | Update report
[**update_report_by_id1**](ReportsApi.md#update_report_by_id1) | **PUT** /api/v1/reports/{id} | Update report
[**update_report_folder_by_id**](ReportsApi.md#update_report_folder_by_id) | **PUT** /api/v2/reports/folders/{id} | Update report folder
[**update_report_folder_by_id1**](ReportsApi.md#update_report_folder_by_id1) | **PUT** /api/v1/reports/folders/{id} | Update report folder

# **create_report**
> ReportDto create_report(body)

Create report

Creates a new report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.ReportRequestDto() # ReportRequestDto | 

try:
    # Create report
    api_response = api_instance.create_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportRequestDto**](ReportRequestDto.md)|  | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_report1**
> ReportDto create_report1(body)

Create report

Creates a new report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.ReportRequestDto() # ReportRequestDto | 

try:
    # Create report
    api_response = api_instance.create_report1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->create_report1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportRequestDto**](ReportRequestDto.md)|  | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_report_folder**
> ReportFolderDto create_report_folder(body)

Create report folder

Creates a new report folder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.ReportFolderDto() # ReportFolderDto | 

try:
    # Create report folder
    api_response = api_instance.create_report_folder(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->create_report_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportFolderDto**](ReportFolderDto.md)|  | 

### Return type

[**ReportFolderDto**](ReportFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_report_folder1**
> ReportFolderDto create_report_folder1(body)

Create report folder

Creates a new report folder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.ReportFolderDto() # ReportFolderDto | 

try:
    # Create report folder
    api_response = api_instance.create_report_folder1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->create_report_folder1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportFolderDto**](ReportFolderDto.md)|  | 

### Return type

[**ReportFolderDto**](ReportFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_by_id**
> str delete_report_by_id(id)

Delete report

Deletes an existing report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | The id of the report to be deleted

try:
    # Delete report
    api_response = api_instance.delete_report_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_by_id1**
> str delete_report_by_id1(id)

Delete report

Deletes an existing report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | The id of the report to be deleted

try:
    # Delete report
    api_response = api_instance.delete_report_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_report_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_folder_by_id**
> str delete_report_folder_by_id(id)

Delete report folder

Deletes an existing report folder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | The id of the report folder to be deleted

try:
    # Delete report folder
    api_response = api_instance.delete_report_folder_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_report_folder_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report folder to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_folder_by_id1**
> str delete_report_folder_by_id1(id)

Delete report folder

Deletes an existing report folder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | The id of the report folder to be deleted

try:
    # Delete report folder
    api_response = api_instance.delete_report_folder_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_report_folder_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report folder to be deleted | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_report_folders**
> PagerReportFolderDto get_all_report_folders(options)

Get all report folders

Endpoint for retrieving all report folders that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

try:
    # Get all report folders
    api_response = api_instance.get_all_report_folders(options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_all_report_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 

### Return type

[**PagerReportFolderDto**](PagerReportFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_report_folders1**
> PagerReportFolderDto get_all_report_folders1(page=page, size=size)

Get all report folders

Endpoint for retrieving all report folders that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)

try:
    # Get all report folders
    api_response = api_instance.get_all_report_folders1(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_all_report_folders1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]

### Return type

[**PagerReportFolderDto**](PagerReportFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_reports**
> PagerReportDto get_all_reports(options, user_id=user_id, name=name)

Get all reports

Endpoint for retrieving all reports that supports pagination.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 
user_id = 789 # int | Filter by owner id (optional)
name = 'name_example' # str | Filter by report name (optional)

try:
    # Get all reports
    api_response = api_instance.get_all_reports(options, user_id=user_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_all_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**PageAndSortOptions**](.md)|  | 
 **user_id** | **int**| Filter by owner id | [optional] 
 **name** | **str**| Filter by report name | [optional] 

### Return type

[**PagerReportDto**](PagerReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_reports1**
> PagerReportDto get_all_reports1(page=page, size=size, user_id=user_id, name=name)

Get all reports

Endpoint for retrieving all reports that supports pagination.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
user_id = 789 # int | Filter by owner id (optional)
name = 'name_example' # str | Filter by report name (optional)

try:
    # Get all reports
    api_response = api_instance.get_all_reports1(page=page, size=size, user_id=user_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_all_reports1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **user_id** | **int**| Filter by owner id | [optional] 
 **name** | **str**| Filter by report name | [optional] 

### Return type

[**PagerReportDto**](PagerReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> ReportDto get_report(id)

Get report

Endpoint for retrieving all report info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | Report Id

try:
    # Get report
    api_response = api_instance.get_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Report Id | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report1**
> ReportDto get_report1(id)

Get report

Endpoint for retrieving all report info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | Report Id

try:
    # Get report
    api_response = api_instance.get_report1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_report1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Report Id | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_by_id**
> ReportDto update_report_by_id(body, id)

Update report

Updates an existing report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.ReportRequestDto() # ReportRequestDto | 
id = 789 # int | The id of the report to be updated

try:
    # Update report
    api_response = api_instance.update_report_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportRequestDto**](ReportRequestDto.md)|  | 
 **id** | **int**| The id of the report to be updated | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_by_id1**
> ReportDto update_report_by_id1(body, id)

Update report

Updates an existing report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.ReportRequestDto() # ReportRequestDto | 
id = 789 # int | The id of the report to be updated

try:
    # Update report
    api_response = api_instance.update_report_by_id1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportRequestDto**](ReportRequestDto.md)|  | 
 **id** | **int**| The id of the report to be updated | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_folder_by_id**
> ReportFolderDto update_report_folder_by_id(body, id)

Update report folder

Updates an existing report folder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.ReportFolderDto() # ReportFolderDto | 
id = 789 # int | The id of the report folder to be updated

try:
    # Update report folder
    api_response = api_instance.update_report_folder_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report_folder_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportFolderDto**](ReportFolderDto.md)|  | 
 **id** | **int**| The id of the report folder to be updated | 

### Return type

[**ReportFolderDto**](ReportFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_folder_by_id1**
> ReportFolderDto update_report_folder_by_id1(body, id)

Update report folder

Updates an existing report folder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.ReportFolderDto() # ReportFolderDto | 
id = 789 # int | The id of the report folder to be updated

try:
    # Update report folder
    api_response = api_instance.update_report_folder_by_id1(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report_folder_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportFolderDto**](ReportFolderDto.md)|  | 
 **id** | **int**| The id of the report folder to be updated | 

### Return type

[**ReportFolderDto**](ReportFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

