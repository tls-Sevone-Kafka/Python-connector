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

class DeviceTypeFilterDto(object):
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
        'name': 'str',
        'device_id': 'int',
        'ids': 'list[int]',
        'parent_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'device_id': 'deviceId',
        'ids': 'ids',
        'parent_ids': 'parentIds'
    }

    def __init__(self, name=None, device_id=None, ids=None, parent_ids=None):  # noqa: E501
        """DeviceTypeFilterDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._device_id = None
        self._ids = None
        self._parent_ids = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if device_id is not None:
            self.device_id = device_id
        if ids is not None:
            self.ids = ids
        if parent_ids is not None:
            self.parent_ids = parent_ids

    @property
    def name(self):
        """Gets the name of this DeviceTypeFilterDto.  # noqa: E501


        :return: The name of this DeviceTypeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceTypeFilterDto.


        :param name: The name of this DeviceTypeFilterDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def device_id(self):
        """Gets the device_id of this DeviceTypeFilterDto.  # noqa: E501


        :return: The device_id of this DeviceTypeFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceTypeFilterDto.


        :param device_id: The device_id of this DeviceTypeFilterDto.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def ids(self):
        """Gets the ids of this DeviceTypeFilterDto.  # noqa: E501


        :return: The ids of this DeviceTypeFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this DeviceTypeFilterDto.


        :param ids: The ids of this DeviceTypeFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def parent_ids(self):
        """Gets the parent_ids of this DeviceTypeFilterDto.  # noqa: E501


        :return: The parent_ids of this DeviceTypeFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._parent_ids

    @parent_ids.setter
    def parent_ids(self, parent_ids):
        """Sets the parent_ids of this DeviceTypeFilterDto.


        :param parent_ids: The parent_ids of this DeviceTypeFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._parent_ids = parent_ids

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
        if issubclass(DeviceTypeFilterDto, dict):
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
        if not isinstance(other, DeviceTypeFilterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other