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

class FlowInterfaceDto(object):
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
        'netflow_device_id': 'int',
        'interface_id': 'int',
        'direction': 'int'
    }

    attribute_map = {
        'netflow_device_id': 'netflowDeviceId',
        'interface_id': 'interfaceId',
        'direction': 'direction'
    }

    def __init__(self, netflow_device_id=None, interface_id=None, direction=None):  # noqa: E501
        """FlowInterfaceDto - a model defined in Swagger"""  # noqa: E501
        self._netflow_device_id = None
        self._interface_id = None
        self._direction = None
        self.discriminator = None
        if netflow_device_id is not None:
            self.netflow_device_id = netflow_device_id
        if interface_id is not None:
            self.interface_id = interface_id
        if direction is not None:
            self.direction = direction

    @property
    def netflow_device_id(self):
        """Gets the netflow_device_id of this FlowInterfaceDto.  # noqa: E501


        :return: The netflow_device_id of this FlowInterfaceDto.  # noqa: E501
        :rtype: int
        """
        return self._netflow_device_id

    @netflow_device_id.setter
    def netflow_device_id(self, netflow_device_id):
        """Sets the netflow_device_id of this FlowInterfaceDto.


        :param netflow_device_id: The netflow_device_id of this FlowInterfaceDto.  # noqa: E501
        :type: int
        """

        self._netflow_device_id = netflow_device_id

    @property
    def interface_id(self):
        """Gets the interface_id of this FlowInterfaceDto.  # noqa: E501


        :return: The interface_id of this FlowInterfaceDto.  # noqa: E501
        :rtype: int
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """Sets the interface_id of this FlowInterfaceDto.


        :param interface_id: The interface_id of this FlowInterfaceDto.  # noqa: E501
        :type: int
        """

        self._interface_id = interface_id

    @property
    def direction(self):
        """Gets the direction of this FlowInterfaceDto.  # noqa: E501


        :return: The direction of this FlowInterfaceDto.  # noqa: E501
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this FlowInterfaceDto.


        :param direction: The direction of this FlowInterfaceDto.  # noqa: E501
        :type: int
        """

        self._direction = direction

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
        if issubclass(FlowInterfaceDto, dict):
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
        if not isinstance(other, FlowInterfaceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
