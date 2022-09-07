#!/usr/bin/env python3

from __future__ import print_function
from email import header
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import json

configuration = swagger_client.Configuration()
# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.UserRequestDto() # UserRequestDto | 
nms_login = False # bool |  (optional) (default to false)

try:
    # Sign in user
    api_response = api_instance.sign_in(body, nms_login=nms_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_in: %s\n" % e)



api_client = swagger_client.ApiClient(None, header_name='X-AUTH-TOKEN', header_value=api_response.token)




# # create an instance of the API class
# api_instance = swagger_client.DevicesApi(api_client=api_client)
# options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

# try:
#     # Get all devices
#     api_response = api_instance.get_devices(options)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling DevicesApi->get_devices: %s\n" % e)


# # create an instance of the API class
# api_instance = swagger_client.DevicesApi()
# body = swagger_client.CreateDeviceRequestDto(name='new-device') # CreateDeviceRequestDto | 

# try:
#     # Create device
#     api_response = api_instance.create_device(body)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling DevicesApi->create_device: %s\n" % e)



# # create an instance of the API class
# api_instance = swagger_client.ObjectsApi(api_client=api_client)
# body = swagger_client.DeviceObjectRequestDto(name="new-object",poll_frequency=1,description="test",plugin_id=17,plugin_object_type_id=10) # DeviceObjectRequestDto | 
# device_id = 5 # int | The id of the device

# try:
#     # Create object
#     api_response = api_instance.create_object(body, device_id)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling ObjectsApi->create_object: %s\n" % e)



# # create an instance of the API class
# api_instance = swagger_client.ObjectsApi(api_client=api_client)
# device_id = 4 # int | The id of the device
# options = swagger_client.PageAndSortOptionsIncludeMetadata() # PageAndSortOptionsIncludeMetadata | 
# include_indicators = False # bool | Determines whether to include indicators (optional) (default to false)
# include_indicator_metadata = False # bool | Determines whether to include indicator metadata (optional) (default to false)
# include_extended_info = True # bool | Determines whether to include extendedInfo or not (optional) (default to true)

# try:
#     # Get all objects for a device
#     api_response = api_instance.get_objects(device_id, options, include_indicators=include_indicators, include_indicator_metadata=include_indicator_metadata, include_extended_info=include_extended_info)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling ObjectsApi->get_objects: %s\n" % e)




# # create an instance of the API class
# api_instance = swagger_client.IndicatorsApi(api_client=api_client)
# body = [swagger_client.ObjectDataDto(device_id=4, object_id=11, timestamp=1662603187000)] # list[ObjectDataDto] | 

# try:
#     # Create device indicator data
#     api_response = api_instance.create_device_indicator_data(body)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling IndicatorsApi->create_device_indicator_data: %s\n" % e)




for id in range(47,52):
    # create an instance of the API class
    api_instance = swagger_client.DevicesApi(api_client=api_client)
    # id = 35 # int | The id of the device to be deleted
    force_delete = True # bool | Determines whether to force delete device or not (put device in deletion queue).  If `days_to_delay` in cluster setting is set to 0, device will be deleted immediately in the next discovery. (optional) (default to false)

    try:
        # Delete devic
        api_response = api_instance.delete_device_by_id(id, force_delete=force_delete)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->delete_device_by_id: %s\n" % e)