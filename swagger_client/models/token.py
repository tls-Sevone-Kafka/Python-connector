# coding: utf-8

"""
    SevOne API Documentation

    Supported endpoints by the new RESTful API  # noqa: E501

    OpenAPI spec version: 2.1.42, Hash: 719f8be
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Token(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'int',
        'token': 'str',
        'expiration_date': 'int',
        'created_date': 'int',
        'number_of_api_calls': 'int',
        'php_session_id': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'token': 'token',
        'expiration_date': 'expirationDate',
        'created_date': 'createdDate',
        'number_of_api_calls': 'numberOfApiCalls',
        'php_session_id': 'phpSessionId'
    }

    def __init__(self, user_id=None, token=None, expiration_date=None, created_date=None, number_of_api_calls=None, php_session_id=None):  # noqa: E501
        """Token - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._token = None
        self._expiration_date = None
        self._created_date = None
        self._number_of_api_calls = None
        self._php_session_id = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if token is not None:
            self.token = token
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if created_date is not None:
            self.created_date = created_date
        if number_of_api_calls is not None:
            self.number_of_api_calls = number_of_api_calls
        if php_session_id is not None:
            self.php_session_id = php_session_id

    @property
    def user_id(self):
        """Gets the user_id of this Token.  # noqa: E501


        :return: The user_id of this Token.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Token.


        :param user_id: The user_id of this Token.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def token(self):
        """Gets the token of this Token.  # noqa: E501


        :return: The token of this Token.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Token.


        :param token: The token of this Token.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def expiration_date(self):
        """Gets the expiration_date of this Token.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The expiration_date of this Token.  # noqa: E501
        :rtype: int
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this Token.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param expiration_date: The expiration_date of this Token.  # noqa: E501
        :type: int
        """

        self._expiration_date = expiration_date

    @property
    def created_date(self):
        """Gets the created_date of this Token.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The created_date of this Token.  # noqa: E501
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Token.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param created_date: The created_date of this Token.  # noqa: E501
        :type: int
        """

        self._created_date = created_date

    @property
    def number_of_api_calls(self):
        """Gets the number_of_api_calls of this Token.  # noqa: E501


        :return: The number_of_api_calls of this Token.  # noqa: E501
        :rtype: int
        """
        return self._number_of_api_calls

    @number_of_api_calls.setter
    def number_of_api_calls(self, number_of_api_calls):
        """Sets the number_of_api_calls of this Token.


        :param number_of_api_calls: The number_of_api_calls of this Token.  # noqa: E501
        :type: int
        """

        self._number_of_api_calls = number_of_api_calls

    @property
    def php_session_id(self):
        """Gets the php_session_id of this Token.  # noqa: E501


        :return: The php_session_id of this Token.  # noqa: E501
        :rtype: str
        """
        return self._php_session_id

    @php_session_id.setter
    def php_session_id(self, php_session_id):
        """Sets the php_session_id of this Token.


        :param php_session_id: The php_session_id of this Token.  # noqa: E501
        :type: str
        """

        self._php_session_id = php_session_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Token, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Token):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
