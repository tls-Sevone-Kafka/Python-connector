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

class NetFlowViewFilterDto(object):
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
        'ids': 'list[int]',
        'search_text': 'str',
        'name': 'str',
        'category': 'str',
        'is_aggregated': 'bool',
        'is_enabled': 'bool',
        'last_update': 'int'
    }

    attribute_map = {
        'ids': 'ids',
        'search_text': 'searchText',
        'name': 'name',
        'category': 'category',
        'is_aggregated': 'isAggregated',
        'is_enabled': 'isEnabled',
        'last_update': 'lastUpdate'
    }

    def __init__(self, ids=None, search_text=None, name=None, category=None, is_aggregated=None, is_enabled=None, last_update=None):  # noqa: E501
        """NetFlowViewFilterDto - a model defined in Swagger"""  # noqa: E501
        self._ids = None
        self._search_text = None
        self._name = None
        self._category = None
        self._is_aggregated = None
        self._is_enabled = None
        self._last_update = None
        self.discriminator = None
        if ids is not None:
            self.ids = ids
        if search_text is not None:
            self.search_text = search_text
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if is_aggregated is not None:
            self.is_aggregated = is_aggregated
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if last_update is not None:
            self.last_update = last_update

    @property
    def ids(self):
        """Gets the ids of this NetFlowViewFilterDto.  # noqa: E501


        :return: The ids of this NetFlowViewFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this NetFlowViewFilterDto.


        :param ids: The ids of this NetFlowViewFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def search_text(self):
        """Gets the search_text of this NetFlowViewFilterDto.  # noqa: E501


        :return: The search_text of this NetFlowViewFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this NetFlowViewFilterDto.


        :param search_text: The search_text of this NetFlowViewFilterDto.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def name(self):
        """Gets the name of this NetFlowViewFilterDto.  # noqa: E501


        :return: The name of this NetFlowViewFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetFlowViewFilterDto.


        :param name: The name of this NetFlowViewFilterDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category(self):
        """Gets the category of this NetFlowViewFilterDto.  # noqa: E501


        :return: The category of this NetFlowViewFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this NetFlowViewFilterDto.


        :param category: The category of this NetFlowViewFilterDto.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def is_aggregated(self):
        """Gets the is_aggregated of this NetFlowViewFilterDto.  # noqa: E501


        :return: The is_aggregated of this NetFlowViewFilterDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_aggregated

    @is_aggregated.setter
    def is_aggregated(self, is_aggregated):
        """Sets the is_aggregated of this NetFlowViewFilterDto.


        :param is_aggregated: The is_aggregated of this NetFlowViewFilterDto.  # noqa: E501
        :type: bool
        """

        self._is_aggregated = is_aggregated

    @property
    def is_enabled(self):
        """Gets the is_enabled of this NetFlowViewFilterDto.  # noqa: E501


        :return: The is_enabled of this NetFlowViewFilterDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this NetFlowViewFilterDto.


        :param is_enabled: The is_enabled of this NetFlowViewFilterDto.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def last_update(self):
        """Gets the last_update of this NetFlowViewFilterDto.  # noqa: E501


        :return: The last_update of this NetFlowViewFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this NetFlowViewFilterDto.


        :param last_update: The last_update of this NetFlowViewFilterDto.  # noqa: E501
        :type: int
        """

        self._last_update = last_update

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
        if issubclass(NetFlowViewFilterDto, dict):
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
        if not isinstance(other, NetFlowViewFilterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
