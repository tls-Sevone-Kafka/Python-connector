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

class PluginObjectTypeRequestDto(object):
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
        'name': 'str',
        'parent_object_type_id': 'int',
        'is_enabled': 'bool',
        'extended_info': 'dict(str, str)'
    }

    attribute_map = {
        'plugin_id': 'pluginId',
        'name': 'name',
        'parent_object_type_id': 'parentObjectTypeId',
        'is_enabled': 'isEnabled',
        'extended_info': 'extendedInfo'
    }

    def __init__(self, plugin_id=None, name=None, parent_object_type_id=None, is_enabled=None, extended_info=None):  # noqa: E501
        """PluginObjectTypeRequestDto - a model defined in Swagger"""  # noqa: E501
        self._plugin_id = None
        self._name = None
        self._parent_object_type_id = None
        self._is_enabled = None
        self._extended_info = None
        self.discriminator = None
        self.plugin_id = plugin_id
        self.name = name
        self.parent_object_type_id = parent_object_type_id
        self.is_enabled = is_enabled
        if extended_info is not None:
            self.extended_info = extended_info

    @property
    def plugin_id(self):
        """Gets the plugin_id of this PluginObjectTypeRequestDto.  # noqa: E501


        :return: The plugin_id of this PluginObjectTypeRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this PluginObjectTypeRequestDto.


        :param plugin_id: The plugin_id of this PluginObjectTypeRequestDto.  # noqa: E501
        :type: int
        """
        if plugin_id is None:
            raise ValueError("Invalid value for `plugin_id`, must not be `None`")  # noqa: E501

        self._plugin_id = plugin_id

    @property
    def name(self):
        """Gets the name of this PluginObjectTypeRequestDto.  # noqa: E501


        :return: The name of this PluginObjectTypeRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PluginObjectTypeRequestDto.


        :param name: The name of this PluginObjectTypeRequestDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parent_object_type_id(self):
        """Gets the parent_object_type_id of this PluginObjectTypeRequestDto.  # noqa: E501


        :return: The parent_object_type_id of this PluginObjectTypeRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._parent_object_type_id

    @parent_object_type_id.setter
    def parent_object_type_id(self, parent_object_type_id):
        """Sets the parent_object_type_id of this PluginObjectTypeRequestDto.


        :param parent_object_type_id: The parent_object_type_id of this PluginObjectTypeRequestDto.  # noqa: E501
        :type: int
        """
        if parent_object_type_id is None:
            raise ValueError("Invalid value for `parent_object_type_id`, must not be `None`")  # noqa: E501

        self._parent_object_type_id = parent_object_type_id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this PluginObjectTypeRequestDto.  # noqa: E501


        :return: The is_enabled of this PluginObjectTypeRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this PluginObjectTypeRequestDto.


        :param is_enabled: The is_enabled of this PluginObjectTypeRequestDto.  # noqa: E501
        :type: bool
        """
        if is_enabled is None:
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    @property
    def extended_info(self):
        """Gets the extended_info of this PluginObjectTypeRequestDto.  # noqa: E501


        :return: The extended_info of this PluginObjectTypeRequestDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extended_info

    @extended_info.setter
    def extended_info(self, extended_info):
        """Sets the extended_info of this PluginObjectTypeRequestDto.


        :param extended_info: The extended_info of this PluginObjectTypeRequestDto.  # noqa: E501
        :type: dict(str, str)
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
        if issubclass(PluginObjectTypeRequestDto, dict):
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
        if not isinstance(other, PluginObjectTypeRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
