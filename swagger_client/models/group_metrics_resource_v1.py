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

class GroupMetricsResourceV1(object):
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
        'type': 'str',
        'ids': 'list[int]',
        'indicator_types': 'list[GroupMetricsIndicatorTypesV1]'
    }

    attribute_map = {
        'type': 'type',
        'ids': 'ids',
        'indicator_types': 'indicatorTypes'
    }

    def __init__(self, type=None, ids=None, indicator_types=None):  # noqa: E501
        """GroupMetricsResourceV1 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._ids = None
        self._indicator_types = None
        self.discriminator = None
        self.type = type
        self.ids = ids
        self.indicator_types = indicator_types

    @property
    def type(self):
        """Gets the type of this GroupMetricsResourceV1.  # noqa: E501


        :return: The type of this GroupMetricsResourceV1.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupMetricsResourceV1.


        :param type: The type of this GroupMetricsResourceV1.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["DeviceGroup", "DeviceGroupChildren", "ObjectGroup"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def ids(self):
        """Gets the ids of this GroupMetricsResourceV1.  # noqa: E501


        :return: The ids of this GroupMetricsResourceV1.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this GroupMetricsResourceV1.


        :param ids: The ids of this GroupMetricsResourceV1.  # noqa: E501
        :type: list[int]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")  # noqa: E501

        self._ids = ids

    @property
    def indicator_types(self):
        """Gets the indicator_types of this GroupMetricsResourceV1.  # noqa: E501


        :return: The indicator_types of this GroupMetricsResourceV1.  # noqa: E501
        :rtype: list[GroupMetricsIndicatorTypesV1]
        """
        return self._indicator_types

    @indicator_types.setter
    def indicator_types(self, indicator_types):
        """Sets the indicator_types of this GroupMetricsResourceV1.


        :param indicator_types: The indicator_types of this GroupMetricsResourceV1.  # noqa: E501
        :type: list[GroupMetricsIndicatorTypesV1]
        """
        if indicator_types is None:
            raise ValueError("Invalid value for `indicator_types`, must not be `None`")  # noqa: E501

        self._indicator_types = indicator_types

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
        if issubclass(GroupMetricsResourceV1, dict):
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
        if not isinstance(other, GroupMetricsResourceV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
