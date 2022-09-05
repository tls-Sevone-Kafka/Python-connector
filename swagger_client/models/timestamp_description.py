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

class TimestampDescription(object):
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
        'timestamp': 'int',
        'indicators': 'list[IndicatorDescription]'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'indicators': 'indicators'
    }

    def __init__(self, timestamp=None, indicators=None):  # noqa: E501
        """TimestampDescription - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._indicators = None
        self.discriminator = None
        if timestamp is not None:
            self.timestamp = timestamp
        if indicators is not None:
            self.indicators = indicators

    @property
    def timestamp(self):
        """Gets the timestamp of this TimestampDescription.  # noqa: E501


        :return: The timestamp of this TimestampDescription.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TimestampDescription.


        :param timestamp: The timestamp of this TimestampDescription.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def indicators(self):
        """Gets the indicators of this TimestampDescription.  # noqa: E501


        :return: The indicators of this TimestampDescription.  # noqa: E501
        :rtype: list[IndicatorDescription]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this TimestampDescription.


        :param indicators: The indicators of this TimestampDescription.  # noqa: E501
        :type: list[IndicatorDescription]
        """

        self._indicators = indicators

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
        if issubclass(TimestampDescription, dict):
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
        if not isinstance(other, TimestampDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other