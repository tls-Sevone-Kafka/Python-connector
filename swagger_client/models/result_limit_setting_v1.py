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

class ResultLimitSettingV1(object):
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
        'result_limit': 'int'
    }

    attribute_map = {
        'result_limit': 'resultLimit'
    }

    def __init__(self, result_limit=None):  # noqa: E501
        """ResultLimitSettingV1 - a model defined in Swagger"""  # noqa: E501
        self._result_limit = None
        self.discriminator = None
        if result_limit is not None:
            self.result_limit = result_limit

    @property
    def result_limit(self):
        """Gets the result_limit of this ResultLimitSettingV1.  # noqa: E501


        :return: The result_limit of this ResultLimitSettingV1.  # noqa: E501
        :rtype: int
        """
        return self._result_limit

    @result_limit.setter
    def result_limit(self, result_limit):
        """Sets the result_limit of this ResultLimitSettingV1.


        :param result_limit: The result_limit of this ResultLimitSettingV1.  # noqa: E501
        :type: int
        """

        self._result_limit = result_limit

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
        if issubclass(ResultLimitSettingV1, dict):
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
        if not isinstance(other, ResultLimitSettingV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
