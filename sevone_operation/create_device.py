from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

class CreateDevice(object):
    def __init__(self,device_name,token):
        self.token = token
        self.device_name = device_name

    def request(self):

        api_client = swagger_client.ApiClient(None, header_name='X-AUTH-TOKEN', header_value=self.token)

        # create an instance of the API class
        api_instance = swagger_client.DevicesApi(api_client=api_client)
        body = swagger_client.CreateDeviceRequestDto(name=self.device_name) # CreateDeviceRequestDto | 

        try:
            # Create device
            api_response = api_instance.create_device(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling DevicesApi->create_device: %s\n" % e)
