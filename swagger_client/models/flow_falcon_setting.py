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

class FlowFalconSetting(object):
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
        'granularity': 'int',
        'graph_other': 'bool',
        'is_rate': 'bool',
        'is_total': 'bool',
        'split': 'int',
        'subnet_category_id': 'int',
        'can_zoom_in_cb': 'str'
    }

    attribute_map = {
        'granularity': 'granularity',
        'graph_other': 'graphOther',
        'is_rate': 'isRate',
        'is_total': 'isTotal',
        'split': 'split',
        'subnet_category_id': 'subnetCategoryId',
        'can_zoom_in_cb': 'canZoomInCb'
    }

    def __init__(self, granularity=None, graph_other=None, is_rate=None, is_total=None, split=None, subnet_category_id=None, can_zoom_in_cb=None):  # noqa: E501
        """FlowFalconSetting - a model defined in Swagger"""  # noqa: E501
        self._granularity = None
        self._graph_other = None
        self._is_rate = None
        self._is_total = None
        self._split = None
        self._subnet_category_id = None
        self._can_zoom_in_cb = None
        self.discriminator = None
        if granularity is not None:
            self.granularity = granularity
        if graph_other is not None:
            self.graph_other = graph_other
        if is_rate is not None:
            self.is_rate = is_rate
        if is_total is not None:
            self.is_total = is_total
        if split is not None:
            self.split = split
        if subnet_category_id is not None:
            self.subnet_category_id = subnet_category_id
        if can_zoom_in_cb is not None:
            self.can_zoom_in_cb = can_zoom_in_cb

    @property
    def granularity(self):
        """Gets the granularity of this FlowFalconSetting.  # noqa: E501


        :return: The granularity of this FlowFalconSetting.  # noqa: E501
        :rtype: int
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this FlowFalconSetting.


        :param granularity: The granularity of this FlowFalconSetting.  # noqa: E501
        :type: int
        """

        self._granularity = granularity

    @property
    def graph_other(self):
        """Gets the graph_other of this FlowFalconSetting.  # noqa: E501


        :return: The graph_other of this FlowFalconSetting.  # noqa: E501
        :rtype: bool
        """
        return self._graph_other

    @graph_other.setter
    def graph_other(self, graph_other):
        """Sets the graph_other of this FlowFalconSetting.


        :param graph_other: The graph_other of this FlowFalconSetting.  # noqa: E501
        :type: bool
        """

        self._graph_other = graph_other

    @property
    def is_rate(self):
        """Gets the is_rate of this FlowFalconSetting.  # noqa: E501


        :return: The is_rate of this FlowFalconSetting.  # noqa: E501
        :rtype: bool
        """
        return self._is_rate

    @is_rate.setter
    def is_rate(self, is_rate):
        """Sets the is_rate of this FlowFalconSetting.


        :param is_rate: The is_rate of this FlowFalconSetting.  # noqa: E501
        :type: bool
        """

        self._is_rate = is_rate

    @property
    def is_total(self):
        """Gets the is_total of this FlowFalconSetting.  # noqa: E501


        :return: The is_total of this FlowFalconSetting.  # noqa: E501
        :rtype: bool
        """
        return self._is_total

    @is_total.setter
    def is_total(self, is_total):
        """Sets the is_total of this FlowFalconSetting.


        :param is_total: The is_total of this FlowFalconSetting.  # noqa: E501
        :type: bool
        """

        self._is_total = is_total

    @property
    def split(self):
        """Gets the split of this FlowFalconSetting.  # noqa: E501


        :return: The split of this FlowFalconSetting.  # noqa: E501
        :rtype: int
        """
        return self._split

    @split.setter
    def split(self, split):
        """Sets the split of this FlowFalconSetting.


        :param split: The split of this FlowFalconSetting.  # noqa: E501
        :type: int
        """

        self._split = split

    @property
    def subnet_category_id(self):
        """Gets the subnet_category_id of this FlowFalconSetting.  # noqa: E501


        :return: The subnet_category_id of this FlowFalconSetting.  # noqa: E501
        :rtype: int
        """
        return self._subnet_category_id

    @subnet_category_id.setter
    def subnet_category_id(self, subnet_category_id):
        """Sets the subnet_category_id of this FlowFalconSetting.


        :param subnet_category_id: The subnet_category_id of this FlowFalconSetting.  # noqa: E501
        :type: int
        """

        self._subnet_category_id = subnet_category_id

    @property
    def can_zoom_in_cb(self):
        """Gets the can_zoom_in_cb of this FlowFalconSetting.  # noqa: E501


        :return: The can_zoom_in_cb of this FlowFalconSetting.  # noqa: E501
        :rtype: str
        """
        return self._can_zoom_in_cb

    @can_zoom_in_cb.setter
    def can_zoom_in_cb(self, can_zoom_in_cb):
        """Sets the can_zoom_in_cb of this FlowFalconSetting.


        :param can_zoom_in_cb: The can_zoom_in_cb of this FlowFalconSetting.  # noqa: E501
        :type: str
        """

        self._can_zoom_in_cb = can_zoom_in_cb

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
        if issubclass(FlowFalconSetting, dict):
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
        if not isinstance(other, FlowFalconSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
