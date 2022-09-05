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

class NodeDto(object):
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
        'type': 'str',
        'data': 'list[InternalObjectDto]',
        'x': 'float',
        'y': 'float',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'data': 'data',
        'x': 'x',
        'y': 'y',
        'id': 'id'
    }

    def __init__(self, name=None, type=None, data=None, x=None, y=None, id=None):  # noqa: E501
        """NodeDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._data = None
        self._x = None
        self._y = None
        self._id = None
        self.discriminator = None
        self.name = name
        self.type = type
        self.data = data
        self.x = x
        self.y = y
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this NodeDto.  # noqa: E501


        :return: The name of this NodeDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeDto.


        :param name: The name of this NodeDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this NodeDto.  # noqa: E501


        :return: The type of this NodeDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeDto.


        :param type: The type of this NodeDto.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Device", "DeviceGroup", "Object", "ObjectGroup", "StatusMap"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def data(self):
        """Gets the data of this NodeDto.  # noqa: E501


        :return: The data of this NodeDto.  # noqa: E501
        :rtype: list[InternalObjectDto]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this NodeDto.


        :param data: The data of this NodeDto.  # noqa: E501
        :type: list[InternalObjectDto]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def x(self):
        """Gets the x of this NodeDto.  # noqa: E501


        :return: The x of this NodeDto.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this NodeDto.


        :param x: The x of this NodeDto.  # noqa: E501
        :type: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this NodeDto.  # noqa: E501


        :return: The y of this NodeDto.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this NodeDto.


        :param y: The y of this NodeDto.  # noqa: E501
        :type: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def id(self):
        """Gets the id of this NodeDto.  # noqa: E501


        :return: The id of this NodeDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeDto.


        :param id: The id of this NodeDto.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(NodeDto, dict):
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
        if not isinstance(other, NodeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other