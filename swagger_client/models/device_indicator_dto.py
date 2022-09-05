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

class DeviceIndicatorDto(object):
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
        'device_id': 'int',
        'object_id': 'int',
        'indicator_id': 'int'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'object_id': 'objectId',
        'indicator_id': 'indicatorId'
    }

    def __init__(self, device_id=None, object_id=None, indicator_id=None):  # noqa: E501
        """DeviceIndicatorDto - a model defined in Swagger"""  # noqa: E501
        self._device_id = None
        self._object_id = None
        self._indicator_id = None
        self.discriminator = None
        if device_id is not None:
            self.device_id = device_id
        if object_id is not None:
            self.object_id = object_id
        if indicator_id is not None:
            self.indicator_id = indicator_id

    @property
    def device_id(self):
        """Gets the device_id of this DeviceIndicatorDto.  # noqa: E501


        :return: The device_id of this DeviceIndicatorDto.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceIndicatorDto.


        :param device_id: The device_id of this DeviceIndicatorDto.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def object_id(self):
        """Gets the object_id of this DeviceIndicatorDto.  # noqa: E501


        :return: The object_id of this DeviceIndicatorDto.  # noqa: E501
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this DeviceIndicatorDto.


        :param object_id: The object_id of this DeviceIndicatorDto.  # noqa: E501
        :type: int
        """

        self._object_id = object_id

    @property
    def indicator_id(self):
        """Gets the indicator_id of this DeviceIndicatorDto.  # noqa: E501


        :return: The indicator_id of this DeviceIndicatorDto.  # noqa: E501
        :rtype: int
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this DeviceIndicatorDto.


        :param indicator_id: The indicator_id of this DeviceIndicatorDto.  # noqa: E501
        :type: int
        """

        self._indicator_id = indicator_id

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
        if issubclass(DeviceIndicatorDto, dict):
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
        if not isinstance(other, DeviceIndicatorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other