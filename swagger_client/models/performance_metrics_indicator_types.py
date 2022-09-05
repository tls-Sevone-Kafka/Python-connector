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

class PerformanceMetricsIndicatorTypes(object):
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
        'plugin_id': 'int',
        'object_type_id': 'int',
        'ids': 'list[int]'
    }

    attribute_map = {
        'plugin_id': 'pluginId',
        'object_type_id': 'objectTypeId',
        'ids': 'ids'
    }

    def __init__(self, plugin_id=None, object_type_id=None, ids=None):  # noqa: E501
        """PerformanceMetricsIndicatorTypes - a model defined in Swagger"""  # noqa: E501
        self._plugin_id = None
        self._object_type_id = None
        self._ids = None
        self.discriminator = None
        self.plugin_id = plugin_id
        self.object_type_id = object_type_id
        self.ids = ids

    @property
    def plugin_id(self):
        """Gets the plugin_id of this PerformanceMetricsIndicatorTypes.  # noqa: E501


        :return: The plugin_id of this PerformanceMetricsIndicatorTypes.  # noqa: E501
        :rtype: int
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this PerformanceMetricsIndicatorTypes.


        :param plugin_id: The plugin_id of this PerformanceMetricsIndicatorTypes.  # noqa: E501
        :type: int
        """
        if plugin_id is None:
            raise ValueError("Invalid value for `plugin_id`, must not be `None`")  # noqa: E501

        self._plugin_id = plugin_id

    @property
    def object_type_id(self):
        """Gets the object_type_id of this PerformanceMetricsIndicatorTypes.  # noqa: E501


        :return: The object_type_id of this PerformanceMetricsIndicatorTypes.  # noqa: E501
        :rtype: int
        """
        return self._object_type_id

    @object_type_id.setter
    def object_type_id(self, object_type_id):
        """Sets the object_type_id of this PerformanceMetricsIndicatorTypes.


        :param object_type_id: The object_type_id of this PerformanceMetricsIndicatorTypes.  # noqa: E501
        :type: int
        """
        if object_type_id is None:
            raise ValueError("Invalid value for `object_type_id`, must not be `None`")  # noqa: E501

        self._object_type_id = object_type_id

    @property
    def ids(self):
        """Gets the ids of this PerformanceMetricsIndicatorTypes.  # noqa: E501


        :return: The ids of this PerformanceMetricsIndicatorTypes.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this PerformanceMetricsIndicatorTypes.


        :param ids: The ids of this PerformanceMetricsIndicatorTypes.  # noqa: E501
        :type: list[int]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")  # noqa: E501

        self._ids = ids

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
        if issubclass(PerformanceMetricsIndicatorTypes, dict):
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
        if not isinstance(other, PerformanceMetricsIndicatorTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other