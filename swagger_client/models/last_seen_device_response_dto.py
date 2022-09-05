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

class LastSeenDeviceResponseDto(object):
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
        'name': 'str',
        'objects': 'list[LastSeenObjectResponseDto]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'objects': 'objects'
    }

    def __init__(self, id=None, name=None, objects=None):  # noqa: E501
        """LastSeenDeviceResponseDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._objects = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if objects is not None:
            self.objects = objects

    @property
    def id(self):
        """Gets the id of this LastSeenDeviceResponseDto.  # noqa: E501


        :return: The id of this LastSeenDeviceResponseDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LastSeenDeviceResponseDto.


        :param id: The id of this LastSeenDeviceResponseDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LastSeenDeviceResponseDto.  # noqa: E501


        :return: The name of this LastSeenDeviceResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LastSeenDeviceResponseDto.


        :param name: The name of this LastSeenDeviceResponseDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def objects(self):
        """Gets the objects of this LastSeenDeviceResponseDto.  # noqa: E501


        :return: The objects of this LastSeenDeviceResponseDto.  # noqa: E501
        :rtype: list[LastSeenObjectResponseDto]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this LastSeenDeviceResponseDto.


        :param objects: The objects of this LastSeenDeviceResponseDto.  # noqa: E501
        :type: list[LastSeenObjectResponseDto]
        """

        self._objects = objects

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
        if issubclass(LastSeenDeviceResponseDto, dict):
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
        if not isinstance(other, LastSeenDeviceResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other