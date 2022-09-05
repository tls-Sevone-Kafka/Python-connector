#!/usr/bin/env python3

from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


configuration = swagger_client.Configuration()

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.UserRequestDto() # UserRequestDto | 
nms_login = False # bool |  (optional) (default to false)

try:
    # Sign in user
    api_response = api_instance.sign_in(body, nms_login=nms_login)
    pprint(api_response)
    # print(type(api_response))
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_in: %s\n" % e)



# # create an instance of the API class
# api_instance = swagger_client.DevicesApi()
# options = swagger_client.PageAndSortOptions() # PageAndSortOptions | 

# try:
#     # Get all devices
#     api_response = api_instance.get_devices(options)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling DevicesApi->get_devices: %s\n" % e)