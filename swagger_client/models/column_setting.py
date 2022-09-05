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

class ColumnSetting(object):
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
        'include': 'list[str]',
        'exclude': 'list[str]'
    }

    attribute_map = {
        'include': 'include',
        'exclude': 'exclude'
    }

    def __init__(self, include=None, exclude=None):  # noqa: E501
        """ColumnSetting - a model defined in Swagger"""  # noqa: E501
        self._include = None
        self._exclude = None
        self.discriminator = None
        if include is not None:
            self.include = include
        if exclude is not None:
            self.exclude = exclude

    @property
    def include(self):
        """Gets the include of this ColumnSetting.  # noqa: E501


        :return: The include of this ColumnSetting.  # noqa: E501
        :rtype: list[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this ColumnSetting.


        :param include: The include of this ColumnSetting.  # noqa: E501
        :type: list[str]
        """

        self._include = include

    @property
    def exclude(self):
        """Gets the exclude of this ColumnSetting.  # noqa: E501


        :return: The exclude of this ColumnSetting.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this ColumnSetting.


        :param exclude: The exclude of this ColumnSetting.  # noqa: E501
        :type: list[str]
        """

        self._exclude = exclude

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
        if issubclass(ColumnSetting, dict):
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
        if not isinstance(other, ColumnSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other