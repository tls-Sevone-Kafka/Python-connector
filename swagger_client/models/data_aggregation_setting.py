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

class DataAggregationSetting(object):
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
        'use_aggregation': 'bool',
        'aggregation_type': 'str',
        'aggregation_value': 'int',
        'aggregation_units': 'str'
    }

    attribute_map = {
        'use_aggregation': 'useAggregation',
        'aggregation_type': 'aggregationType',
        'aggregation_value': 'aggregationValue',
        'aggregation_units': 'aggregationUnits'
    }

    def __init__(self, use_aggregation=None, aggregation_type=None, aggregation_value=None, aggregation_units=None):  # noqa: E501
        """DataAggregationSetting - a model defined in Swagger"""  # noqa: E501
        self._use_aggregation = None
        self._aggregation_type = None
        self._aggregation_value = None
        self._aggregation_units = None
        self.discriminator = None
        if use_aggregation is not None:
            self.use_aggregation = use_aggregation
        if aggregation_type is not None:
            self.aggregation_type = aggregation_type
        if aggregation_value is not None:
            self.aggregation_value = aggregation_value
        if aggregation_units is not None:
            self.aggregation_units = aggregation_units

    @property
    def use_aggregation(self):
        """Gets the use_aggregation of this DataAggregationSetting.  # noqa: E501


        :return: The use_aggregation of this DataAggregationSetting.  # noqa: E501
        :rtype: bool
        """
        return self._use_aggregation

    @use_aggregation.setter
    def use_aggregation(self, use_aggregation):
        """Sets the use_aggregation of this DataAggregationSetting.


        :param use_aggregation: The use_aggregation of this DataAggregationSetting.  # noqa: E501
        :type: bool
        """

        self._use_aggregation = use_aggregation

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this DataAggregationSetting.  # noqa: E501


        :return: The aggregation_type of this DataAggregationSetting.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this DataAggregationSetting.


        :param aggregation_type: The aggregation_type of this DataAggregationSetting.  # noqa: E501
        :type: str
        """
        allowed_values = ["auto", "autoBar", "autoStacked", "autoStackedBar", "average", "minimum", "maximum", "total"]  # noqa: E501
        if aggregation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_type, allowed_values)
            )

        self._aggregation_type = aggregation_type

    @property
    def aggregation_value(self):
        """Gets the aggregation_value of this DataAggregationSetting.  # noqa: E501


        :return: The aggregation_value of this DataAggregationSetting.  # noqa: E501
        :rtype: int
        """
        return self._aggregation_value

    @aggregation_value.setter
    def aggregation_value(self, aggregation_value):
        """Sets the aggregation_value of this DataAggregationSetting.


        :param aggregation_value: The aggregation_value of this DataAggregationSetting.  # noqa: E501
        :type: int
        """

        self._aggregation_value = aggregation_value

    @property
    def aggregation_units(self):
        """Gets the aggregation_units of this DataAggregationSetting.  # noqa: E501


        :return: The aggregation_units of this DataAggregationSetting.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_units

    @aggregation_units.setter
    def aggregation_units(self, aggregation_units):
        """Sets the aggregation_units of this DataAggregationSetting.


        :param aggregation_units: The aggregation_units of this DataAggregationSetting.  # noqa: E501
        :type: str
        """
        allowed_values = ["second", "seconds", "minute", "minutes", "hour", "hours", "sixhour", "sixhours", "day", "days", "week", "weeks", "month", "months", "quarter", "quarters", "year", "years"]  # noqa: E501
        if aggregation_units not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_units` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_units, allowed_values)
            )

        self._aggregation_units = aggregation_units

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
        if issubclass(DataAggregationSetting, dict):
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
        if not isinstance(other, DataAggregationSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
