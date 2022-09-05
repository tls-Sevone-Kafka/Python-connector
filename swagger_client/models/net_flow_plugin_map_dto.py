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

class NetFlowPluginMapDto(object):
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
        'id': 'int',
        'netflow_device_id': 'int',
        'device_id': 'int',
        'automatic': 'bool',
        'allow': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'netflow_device_id': 'netflowDeviceId',
        'device_id': 'deviceId',
        'automatic': 'automatic',
        'allow': 'allow'
    }

    def __init__(self, id=None, netflow_device_id=None, device_id=None, automatic=None, allow=None):  # noqa: E501
        """NetFlowPluginMapDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._netflow_device_id = None
        self._device_id = None
        self._automatic = None
        self._allow = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.netflow_device_id = netflow_device_id
        self.device_id = device_id
        if automatic is not None:
            self.automatic = automatic
        if allow is not None:
            self.allow = allow

    @property
    def id(self):
        """Gets the id of this NetFlowPluginMapDto.  # noqa: E501


        :return: The id of this NetFlowPluginMapDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetFlowPluginMapDto.


        :param id: The id of this NetFlowPluginMapDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def netflow_device_id(self):
        """Gets the netflow_device_id of this NetFlowPluginMapDto.  # noqa: E501


        :return: The netflow_device_id of this NetFlowPluginMapDto.  # noqa: E501
        :rtype: int
        """
        return self._netflow_device_id

    @netflow_device_id.setter
    def netflow_device_id(self, netflow_device_id):
        """Sets the netflow_device_id of this NetFlowPluginMapDto.


        :param netflow_device_id: The netflow_device_id of this NetFlowPluginMapDto.  # noqa: E501
        :type: int
        """
        if netflow_device_id is None:
            raise ValueError("Invalid value for `netflow_device_id`, must not be `None`")  # noqa: E501

        self._netflow_device_id = netflow_device_id

    @property
    def device_id(self):
        """Gets the device_id of this NetFlowPluginMapDto.  # noqa: E501


        :return: The device_id of this NetFlowPluginMapDto.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this NetFlowPluginMapDto.


        :param device_id: The device_id of this NetFlowPluginMapDto.  # noqa: E501
        :type: int
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def automatic(self):
        """Gets the automatic of this NetFlowPluginMapDto.  # noqa: E501


        :return: The automatic of this NetFlowPluginMapDto.  # noqa: E501
        :rtype: bool
        """
        return self._automatic

    @automatic.setter
    def automatic(self, automatic):
        """Sets the automatic of this NetFlowPluginMapDto.


        :param automatic: The automatic of this NetFlowPluginMapDto.  # noqa: E501
        :type: bool
        """

        self._automatic = automatic

    @property
    def allow(self):
        """Gets the allow of this NetFlowPluginMapDto.  # noqa: E501


        :return: The allow of this NetFlowPluginMapDto.  # noqa: E501
        :rtype: bool
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """Sets the allow of this NetFlowPluginMapDto.


        :param allow: The allow of this NetFlowPluginMapDto.  # noqa: E501
        :type: bool
        """

        self._allow = allow

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
        if issubclass(NetFlowPluginMapDto, dict):
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
        if not isinstance(other, NetFlowPluginMapDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
