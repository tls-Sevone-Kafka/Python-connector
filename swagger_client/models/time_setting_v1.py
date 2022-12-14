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

class TimeSettingV1(object):
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
        'ranges': 'TimeRangeV1',
        'timezone': 'str'
    }

    attribute_map = {
        'ranges': 'ranges',
        'timezone': 'timezone'
    }

    def __init__(self, ranges=None, timezone=None):  # noqa: E501
        """TimeSettingV1 - a model defined in Swagger"""  # noqa: E501
        self._ranges = None
        self._timezone = None
        self.discriminator = None
        self.ranges = ranges
        self.timezone = timezone

    @property
    def ranges(self):
        """Gets the ranges of this TimeSettingV1.  # noqa: E501


        :return: The ranges of this TimeSettingV1.  # noqa: E501
        :rtype: TimeRangeV1
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """Sets the ranges of this TimeSettingV1.


        :param ranges: The ranges of this TimeSettingV1.  # noqa: E501
        :type: TimeRangeV1
        """
        if ranges is None:
            raise ValueError("Invalid value for `ranges`, must not be `None`")  # noqa: E501

        self._ranges = ranges

    @property
    def timezone(self):
        """Gets the timezone of this TimeSettingV1.  # noqa: E501


        :return: The timezone of this TimeSettingV1.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this TimeSettingV1.


        :param timezone: The timezone of this TimeSettingV1.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

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
        if issubclass(TimeSettingV1, dict):
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
        if not isinstance(other, TimeSettingV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
