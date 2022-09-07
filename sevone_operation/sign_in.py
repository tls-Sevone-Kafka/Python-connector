from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

class SignIn(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def request(self):
        # create an instance of the API class
        api_instance = swagger_client.AuthenticationApi()
        body = swagger_client.UserRequestDto(name=self.name, password=self.password) # UserRequestDto | 
        nms_login = False # bool |  (optional) (default to false)

        try:
            # Sign in user
            api_response = api_instance.sign_in(body, nms_login=nms_login)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticationApi->sign_in: %s\n" % e)
        return api_response