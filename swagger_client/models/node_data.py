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

class NodeData(object):
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
        'group_id': 'int',
        'device_data': 'DeviceDto',
        'pos_x': 'float',
        'pos_y': 'float'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'group_id': 'groupId',
        'device_data': 'deviceData',
        'pos_x': 'posX',
        'pos_y': 'posY'
    }

    def __init__(self, device_id=None, group_id=None, device_data=None, pos_x=None, pos_y=None):  # noqa: E501
        """NodeData - a model defined in Swagger"""  # noqa: E501
        self._device_id = None
        self._group_id = None
        self._device_data = None
        self._pos_x = None
        self._pos_y = None
        self.discriminator = None
        if device_id is not None:
            self.device_id = device_id
        if group_id is not None:
            self.group_id = group_id
        if device_data is not None:
            self.device_data = device_data
        if pos_x is not None:
            self.pos_x = pos_x
        if pos_y is not None:
            self.pos_y = pos_y

    @property
    def device_id(self):
        """Gets the device_id of this NodeData.  # noqa: E501


        :return: The device_id of this NodeData.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this NodeData.


        :param device_id: The device_id of this NodeData.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def group_id(self):
        """Gets the group_id of this NodeData.  # noqa: E501


        :return: The group_id of this NodeData.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this NodeData.


        :param group_id: The group_id of this NodeData.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def device_data(self):
        """Gets the device_data of this NodeData.  # noqa: E501


        :return: The device_data of this NodeData.  # noqa: E501
        :rtype: DeviceDto
        """
        return self._device_data

    @device_data.setter
    def device_data(self, device_data):
        """Sets the device_data of this NodeData.


        :param device_data: The device_data of this NodeData.  # noqa: E501
        :type: DeviceDto
        """

        self._device_data = device_data

    @property
    def pos_x(self):
        """Gets the pos_x of this NodeData.  # noqa: E501


        :return: The pos_x of this NodeData.  # noqa: E501
        :rtype: float
        """
        return self._pos_x

    @pos_x.setter
    def pos_x(self, pos_x):
        """Sets the pos_x of this NodeData.


        :param pos_x: The pos_x of this NodeData.  # noqa: E501
        :type: float
        """

        self._pos_x = pos_x

    @property
    def pos_y(self):
        """Gets the pos_y of this NodeData.  # noqa: E501


        :return: The pos_y of this NodeData.  # noqa: E501
        :rtype: float
        """
        return self._pos_y

    @pos_y.setter
    def pos_y(self, pos_y):
        """Sets the pos_y of this NodeData.


        :param pos_y: The pos_y of this NodeData.  # noqa: E501
        :type: float
        """

        self._pos_y = pos_y

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
        if issubclass(NodeData, dict):
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
        if not isinstance(other, NodeData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other