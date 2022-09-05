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

class IndicatorTypeRequestDtoV1(object):
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
        'plugin_id': 'int',
        'plugin_object_type_id': 'int',
        'description': 'str',
        'format': 'str',
        'allow_maximum_value': 'bool',
        'data_units': 'str',
        'display_units': 'str',
        'synthetic_expression': 'str',
        'synthetic_maximum_expression': 'str',
        'is_enabled': 'bool',
        'is_default': 'bool',
        'extended_info': 'dict(str, dict(str, str))'
    }

    attribute_map = {
        'name': 'name',
        'plugin_id': 'pluginId',
        'plugin_object_type_id': 'pluginObjectTypeId',
        'description': 'description',
        'format': 'format',
        'allow_maximum_value': 'allowMaximumValue',
        'data_units': 'dataUnits',
        'display_units': 'displayUnits',
        'synthetic_expression': 'syntheticExpression',
        'synthetic_maximum_expression': 'syntheticMaximumExpression',
        'is_enabled': 'isEnabled',
        'is_default': 'isDefault',
        'extended_info': 'extendedInfo'
    }

    def __init__(self, name=None, plugin_id=None, plugin_object_type_id=None, description=None, format=None, allow_maximum_value=None, data_units=None, display_units=None, synthetic_expression=None, synthetic_maximum_expression=None, is_enabled=None, is_default=None, extended_info=None):  # noqa: E501
        """IndicatorTypeRequestDtoV1 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._plugin_id = None
        self._plugin_object_type_id = None
        self._description = None
        self._format = None
        self._allow_maximum_value = None
        self._data_units = None
        self._display_units = None
        self._synthetic_expression = None
        self._synthetic_maximum_expression = None
        self._is_enabled = None
        self._is_default = None
        self._extended_info = None
        self.discriminator = None
        self.name = name
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if plugin_object_type_id is not None:
            self.plugin_object_type_id = plugin_object_type_id
        self.description = description
        self.format = format
        self.allow_maximum_value = allow_maximum_value
        if data_units is not None:
            self.data_units = data_units
        if display_units is not None:
            self.display_units = display_units
        if synthetic_expression is not None:
            self.synthetic_expression = synthetic_expression
        if synthetic_maximum_expression is not None:
            self.synthetic_maximum_expression = synthetic_maximum_expression
        self.is_enabled = is_enabled
        self.is_default = is_default
        if extended_info is not None:
            self.extended_info = extended_info

    @property
    def name(self):
        """Gets the name of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The name of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IndicatorTypeRequestDtoV1.


        :param name: The name of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def plugin_id(self):
        """Gets the plugin_id of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The plugin_id of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: int
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this IndicatorTypeRequestDtoV1.


        :param plugin_id: The plugin_id of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: int
        """

        self._plugin_id = plugin_id

    @property
    def plugin_object_type_id(self):
        """Gets the plugin_object_type_id of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The plugin_object_type_id of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: int
        """
        return self._plugin_object_type_id

    @plugin_object_type_id.setter
    def plugin_object_type_id(self, plugin_object_type_id):
        """Sets the plugin_object_type_id of this IndicatorTypeRequestDtoV1.


        :param plugin_object_type_id: The plugin_object_type_id of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: int
        """

        self._plugin_object_type_id = plugin_object_type_id

    @property
    def description(self):
        """Gets the description of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The description of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IndicatorTypeRequestDtoV1.


        :param description: The description of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def format(self):
        """Gets the format of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The format of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this IndicatorTypeRequestDtoV1.


        :param format: The format of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        allowed_values = ["GAUGE", "COUNTER32", "COUNTER64"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def allow_maximum_value(self):
        """Gets the allow_maximum_value of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The allow_maximum_value of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: bool
        """
        return self._allow_maximum_value

    @allow_maximum_value.setter
    def allow_maximum_value(self, allow_maximum_value):
        """Sets the allow_maximum_value of this IndicatorTypeRequestDtoV1.


        :param allow_maximum_value: The allow_maximum_value of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: bool
        """
        if allow_maximum_value is None:
            raise ValueError("Invalid value for `allow_maximum_value`, must not be `None`")  # noqa: E501

        self._allow_maximum_value = allow_maximum_value

    @property
    def data_units(self):
        """Gets the data_units of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The data_units of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._data_units

    @data_units.setter
    def data_units(self, data_units):
        """Sets the data_units of this IndicatorTypeRequestDtoV1.


        :param data_units: The data_units of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: str
        """

        self._data_units = data_units

    @property
    def display_units(self):
        """Gets the display_units of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The display_units of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._display_units

    @display_units.setter
    def display_units(self, display_units):
        """Sets the display_units of this IndicatorTypeRequestDtoV1.


        :param display_units: The display_units of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: str
        """

        self._display_units = display_units

    @property
    def synthetic_expression(self):
        """Gets the synthetic_expression of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The synthetic_expression of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._synthetic_expression

    @synthetic_expression.setter
    def synthetic_expression(self, synthetic_expression):
        """Sets the synthetic_expression of this IndicatorTypeRequestDtoV1.


        :param synthetic_expression: The synthetic_expression of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: str
        """

        self._synthetic_expression = synthetic_expression

    @property
    def synthetic_maximum_expression(self):
        """Gets the synthetic_maximum_expression of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The synthetic_maximum_expression of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._synthetic_maximum_expression

    @synthetic_maximum_expression.setter
    def synthetic_maximum_expression(self, synthetic_maximum_expression):
        """Sets the synthetic_maximum_expression of this IndicatorTypeRequestDtoV1.


        :param synthetic_maximum_expression: The synthetic_maximum_expression of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: str
        """

        self._synthetic_maximum_expression = synthetic_maximum_expression

    @property
    def is_enabled(self):
        """Gets the is_enabled of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The is_enabled of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this IndicatorTypeRequestDtoV1.


        :param is_enabled: The is_enabled of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: bool
        """
        if is_enabled is None:
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    @property
    def is_default(self):
        """Gets the is_default of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The is_default of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this IndicatorTypeRequestDtoV1.


        :param is_default: The is_default of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: bool
        """
        if is_default is None:
            raise ValueError("Invalid value for `is_default`, must not be `None`")  # noqa: E501

        self._is_default = is_default

    @property
    def extended_info(self):
        """Gets the extended_info of this IndicatorTypeRequestDtoV1.  # noqa: E501


        :return: The extended_info of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._extended_info

    @extended_info.setter
    def extended_info(self, extended_info):
        """Sets the extended_info of this IndicatorTypeRequestDtoV1.


        :param extended_info: The extended_info of this IndicatorTypeRequestDtoV1.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._extended_info = extended_info

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
        if issubclass(IndicatorTypeRequestDtoV1, dict):
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
        if not isinstance(other, IndicatorTypeRequestDtoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other