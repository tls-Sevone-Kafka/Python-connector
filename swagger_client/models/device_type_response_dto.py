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

class DeviceTypeResponseDto(object):
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
        'device_type': 'DeviceTypeDto',
        'object_types': 'list[ObjectTypeDto]',
        'devices': 'list[DeviceDto]'
    }

    attribute_map = {
        'device_type': 'deviceType',
        'object_types': 'objectTypes',
        'devices': 'devices'
    }

    def __init__(self, device_type=None, object_types=None, devices=None):  # noqa: E501
        """DeviceTypeResponseDto - a model defined in Swagger"""  # noqa: E501
        self._device_type = None
        self._object_types = None
        self._devices = None
        self.discriminator = None
        if device_type is not None:
            self.device_type = device_type
        if object_types is not None:
            self.object_types = object_types
        if devices is not None:
            self.devices = devices

    @property
    def device_type(self):
        """Gets the device_type of this DeviceTypeResponseDto.  # noqa: E501


        :return: The device_type of this DeviceTypeResponseDto.  # noqa: E501
        :rtype: DeviceTypeDto
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this DeviceTypeResponseDto.


        :param device_type: The device_type of this DeviceTypeResponseDto.  # noqa: E501
        :type: DeviceTypeDto
        """

        self._device_type = device_type

    @property
    def object_types(self):
        """Gets the object_types of this DeviceTypeResponseDto.  # noqa: E501


        :return: The object_types of this DeviceTypeResponseDto.  # noqa: E501
        :rtype: list[ObjectTypeDto]
        """
        return self._object_types

    @object_types.setter
    def object_types(self, object_types):
        """Sets the object_types of this DeviceTypeResponseDto.


        :param object_types: The object_types of this DeviceTypeResponseDto.  # noqa: E501
        :type: list[ObjectTypeDto]
        """

        self._object_types = object_types

    @property
    def devices(self):
        """Gets the devices of this DeviceTypeResponseDto.  # noqa: E501


        :return: The devices of this DeviceTypeResponseDto.  # noqa: E501
        :rtype: list[DeviceDto]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this DeviceTypeResponseDto.


        :param devices: The devices of this DeviceTypeResponseDto.  # noqa: E501
        :type: list[DeviceDto]
        """

        self._devices = devices

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
        if issubclass(DeviceTypeResponseDto, dict):
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
        if not isinstance(other, DeviceTypeResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
