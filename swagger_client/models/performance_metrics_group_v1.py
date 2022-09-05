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

class PerformanceMetricsGroupV1(object):
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
        'id': 'int',
        'indicator_types': 'PerformanceMetricsIndicatorTypesV1'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'indicator_types': 'indicatorTypes'
    }

    def __init__(self, type=None, id=None, indicator_types=None):  # noqa: E501
        """PerformanceMetricsGroupV1 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._indicator_types = None
        self.discriminator = None
        self.type = type
        self.id = id
        self.indicator_types = indicator_types

    @property
    def type(self):
        """Gets the type of this PerformanceMetricsGroupV1.  # noqa: E501


        :return: The type of this PerformanceMetricsGroupV1.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PerformanceMetricsGroupV1.


        :param type: The type of this PerformanceMetricsGroupV1.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["DeviceGroup", "ObjectGroup"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """Gets the id of this PerformanceMetricsGroupV1.  # noqa: E501


        :return: The id of this PerformanceMetricsGroupV1.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PerformanceMetricsGroupV1.


        :param id: The id of this PerformanceMetricsGroupV1.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def indicator_types(self):
        """Gets the indicator_types of this PerformanceMetricsGroupV1.  # noqa: E501


        :return: The indicator_types of this PerformanceMetricsGroupV1.  # noqa: E501
        :rtype: PerformanceMetricsIndicatorTypesV1
        """
        return self._indicator_types

    @indicator_types.setter
    def indicator_types(self, indicator_types):
        """Sets the indicator_types of this PerformanceMetricsGroupV1.


        :param indicator_types: The indicator_types of this PerformanceMetricsGroupV1.  # noqa: E501
        :type: PerformanceMetricsIndicatorTypesV1
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
        if issubclass(PerformanceMetricsGroupV1, dict):
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
        if not isinstance(other, PerformanceMetricsGroupV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
