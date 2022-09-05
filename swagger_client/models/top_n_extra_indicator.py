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

class TopNExtraIndicator(object):
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
        'indicator_id': 'int',
        'indicator_type_id': 'int',
        'indicator_type_name': 'str',
        'indicator_type_description': 'str',
        'indicator_alias': 'str',
        'unit': 'str',
        'is_child_indicator_type': 'bool',
        'data': 'list[TopNDataDto]'
    }

    attribute_map = {
        'indicator_id': 'indicatorId',
        'indicator_type_id': 'indicatorTypeId',
        'indicator_type_name': 'indicatorTypeName',
        'indicator_type_description': 'indicatorTypeDescription',
        'indicator_alias': 'indicatorAlias',
        'unit': 'unit',
        'is_child_indicator_type': 'isChildIndicatorType',
        'data': 'data'
    }

    def __init__(self, indicator_id=None, indicator_type_id=None, indicator_type_name=None, indicator_type_description=None, indicator_alias=None, unit=None, is_child_indicator_type=None, data=None):  # noqa: E501
        """TopNExtraIndicator - a model defined in Swagger"""  # noqa: E501
        self._indicator_id = None
        self._indicator_type_id = None
        self._indicator_type_name = None
        self._indicator_type_description = None
        self._indicator_alias = None
        self._unit = None
        self._is_child_indicator_type = None
        self._data = None
        self.discriminator = None
        self.indicator_id = indicator_id
        self.indicator_type_id = indicator_type_id
        self.indicator_type_name = indicator_type_name
        self.indicator_type_description = indicator_type_description
        self.indicator_alias = indicator_alias
        self.unit = unit
        self.is_child_indicator_type = is_child_indicator_type
        self.data = data

    @property
    def indicator_id(self):
        """Gets the indicator_id of this TopNExtraIndicator.  # noqa: E501


        :return: The indicator_id of this TopNExtraIndicator.  # noqa: E501
        :rtype: int
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this TopNExtraIndicator.


        :param indicator_id: The indicator_id of this TopNExtraIndicator.  # noqa: E501
        :type: int
        """
        if indicator_id is None:
            raise ValueError("Invalid value for `indicator_id`, must not be `None`")  # noqa: E501

        self._indicator_id = indicator_id

    @property
    def indicator_type_id(self):
        """Gets the indicator_type_id of this TopNExtraIndicator.  # noqa: E501


        :return: The indicator_type_id of this TopNExtraIndicator.  # noqa: E501
        :rtype: int
        """
        return self._indicator_type_id

    @indicator_type_id.setter
    def indicator_type_id(self, indicator_type_id):
        """Sets the indicator_type_id of this TopNExtraIndicator.


        :param indicator_type_id: The indicator_type_id of this TopNExtraIndicator.  # noqa: E501
        :type: int
        """
        if indicator_type_id is None:
            raise ValueError("Invalid value for `indicator_type_id`, must not be `None`")  # noqa: E501

        self._indicator_type_id = indicator_type_id

    @property
    def indicator_type_name(self):
        """Gets the indicator_type_name of this TopNExtraIndicator.  # noqa: E501


        :return: The indicator_type_name of this TopNExtraIndicator.  # noqa: E501
        :rtype: str
        """
        return self._indicator_type_name

    @indicator_type_name.setter
    def indicator_type_name(self, indicator_type_name):
        """Sets the indicator_type_name of this TopNExtraIndicator.


        :param indicator_type_name: The indicator_type_name of this TopNExtraIndicator.  # noqa: E501
        :type: str
        """
        if indicator_type_name is None:
            raise ValueError("Invalid value for `indicator_type_name`, must not be `None`")  # noqa: E501

        self._indicator_type_name = indicator_type_name

    @property
    def indicator_type_description(self):
        """Gets the indicator_type_description of this TopNExtraIndicator.  # noqa: E501


        :return: The indicator_type_description of this TopNExtraIndicator.  # noqa: E501
        :rtype: str
        """
        return self._indicator_type_description

    @indicator_type_description.setter
    def indicator_type_description(self, indicator_type_description):
        """Sets the indicator_type_description of this TopNExtraIndicator.


        :param indicator_type_description: The indicator_type_description of this TopNExtraIndicator.  # noqa: E501
        :type: str
        """
        if indicator_type_description is None:
            raise ValueError("Invalid value for `indicator_type_description`, must not be `None`")  # noqa: E501

        self._indicator_type_description = indicator_type_description

    @property
    def indicator_alias(self):
        """Gets the indicator_alias of this TopNExtraIndicator.  # noqa: E501


        :return: The indicator_alias of this TopNExtraIndicator.  # noqa: E501
        :rtype: str
        """
        return self._indicator_alias

    @indicator_alias.setter
    def indicator_alias(self, indicator_alias):
        """Sets the indicator_alias of this TopNExtraIndicator.


        :param indicator_alias: The indicator_alias of this TopNExtraIndicator.  # noqa: E501
        :type: str
        """
        if indicator_alias is None:
            raise ValueError("Invalid value for `indicator_alias`, must not be `None`")  # noqa: E501

        self._indicator_alias = indicator_alias

    @property
    def unit(self):
        """Gets the unit of this TopNExtraIndicator.  # noqa: E501


        :return: The unit of this TopNExtraIndicator.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TopNExtraIndicator.


        :param unit: The unit of this TopNExtraIndicator.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def is_child_indicator_type(self):
        """Gets the is_child_indicator_type of this TopNExtraIndicator.  # noqa: E501


        :return: The is_child_indicator_type of this TopNExtraIndicator.  # noqa: E501
        :rtype: bool
        """
        return self._is_child_indicator_type

    @is_child_indicator_type.setter
    def is_child_indicator_type(self, is_child_indicator_type):
        """Sets the is_child_indicator_type of this TopNExtraIndicator.


        :param is_child_indicator_type: The is_child_indicator_type of this TopNExtraIndicator.  # noqa: E501
        :type: bool
        """
        if is_child_indicator_type is None:
            raise ValueError("Invalid value for `is_child_indicator_type`, must not be `None`")  # noqa: E501

        self._is_child_indicator_type = is_child_indicator_type

    @property
    def data(self):
        """Gets the data of this TopNExtraIndicator.  # noqa: E501


        :return: The data of this TopNExtraIndicator.  # noqa: E501
        :rtype: list[TopNDataDto]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TopNExtraIndicator.


        :param data: The data of this TopNExtraIndicator.  # noqa: E501
        :type: list[TopNDataDto]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(TopNExtraIndicator, dict):
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
        if not isinstance(other, TopNExtraIndicator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
