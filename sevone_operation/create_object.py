from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

class CreateObject(object):
    def __init__(self,token,device_id,object_name,poll_frequency,description,plugin_id,plugin_object_type_id):
        self.token = token #String
        self.object_name = object_name #String
        self.poll_frequency = poll_frequency #Int
        self.description = description #String
        self.plugin_id = plugin_id #Int
        self.plugin_object_type_id = plugin_object_type_id #Int
        self.device_id = device_id #Int

    def request(self):

        api_client = swagger_client.ApiClient(None, header_name='X-AUTH-TOKEN', header_value=self.token)

        # create an instance of the API class
        api_instance = swagger_client.ObjectsApi(api_client=api_client)
        body = swagger_client.DeviceObjectRequestDto(name=self.object_name,poll_frequency=self.poll_frequency,description=self.description,plugin_id=self.plugin_id,plugin_object_type_id=self.plugin_object_type_id) # DeviceObjectRequestDto |
        device_id = self.device_id # int | The id of the device

        try:
            # Create object
            api_response = api_instance.create_object(body, device_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ObjectsApi->create_object: %s\n" % e)

