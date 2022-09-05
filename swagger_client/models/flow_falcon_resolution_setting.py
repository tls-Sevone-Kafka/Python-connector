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

class FlowFalconResolutionSetting(object):
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
        'show_as': 'str',
        'show_dns': 'str',
        'show_dscp': 'str',
        'show_port': 'str',
        'show_protocol': 'str'
    }

    attribute_map = {
        'show_as': 'showAs',
        'show_dns': 'showDns',
        'show_dscp': 'showDscp',
        'show_port': 'showPort',
        'show_protocol': 'showProtocol'
    }

    def __init__(self, show_as=None, show_dns=None, show_dscp=None, show_port=None, show_protocol=None):  # noqa: E501
        """FlowFalconResolutionSetting - a model defined in Swagger"""  # noqa: E501
        self._show_as = None
        self._show_dns = None
        self._show_dscp = None
        self._show_port = None
        self._show_protocol = None
        self.discriminator = None
        if show_as is not None:
            self.show_as = show_as
        if show_dns is not None:
            self.show_dns = show_dns
        if show_dscp is not None:
            self.show_dscp = show_dscp
        if show_port is not None:
            self.show_port = show_port
        if show_protocol is not None:
            self.show_protocol = show_protocol

    @property
    def show_as(self):
        """Gets the show_as of this FlowFalconResolutionSetting.  # noqa: E501


        :return: The show_as of this FlowFalconResolutionSetting.  # noqa: E501
        :rtype: str
        """
        return self._show_as

    @show_as.setter
    def show_as(self, show_as):
        """Sets the show_as of this FlowFalconResolutionSetting.


        :param show_as: The show_as of this FlowFalconResolutionSetting.  # noqa: E501
        :type: str
        """

        self._show_as = show_as

    @property
    def show_dns(self):
        """Gets the show_dns of this FlowFalconResolutionSetting.  # noqa: E501


        :return: The show_dns of this FlowFalconResolutionSetting.  # noqa: E501
        :rtype: str
        """
        return self._show_dns

    @show_dns.setter
    def show_dns(self, show_dns):
        """Sets the show_dns of this FlowFalconResolutionSetting.


        :param show_dns: The show_dns of this FlowFalconResolutionSetting.  # noqa: E501
        :type: str
        """

        self._show_dns = show_dns

    @property
    def show_dscp(self):
        """Gets the show_dscp of this FlowFalconResolutionSetting.  # noqa: E501


        :return: The show_dscp of this FlowFalconResolutionSetting.  # noqa: E501
        :rtype: str
        """
        return self._show_dscp

    @show_dscp.setter
    def show_dscp(self, show_dscp):
        """Sets the show_dscp of this FlowFalconResolutionSetting.


        :param show_dscp: The show_dscp of this FlowFalconResolutionSetting.  # noqa: E501
        :type: str
        """

        self._show_dscp = show_dscp

    @property
    def show_port(self):
        """Gets the show_port of this FlowFalconResolutionSetting.  # noqa: E501


        :return: The show_port of this FlowFalconResolutionSetting.  # noqa: E501
        :rtype: str
        """
        return self._show_port

    @show_port.setter
    def show_port(self, show_port):
        """Sets the show_port of this FlowFalconResolutionSetting.


        :param show_port: The show_port of this FlowFalconResolutionSetting.  # noqa: E501
        :type: str
        """

        self._show_port = show_port

    @property
    def show_protocol(self):
        """Gets the show_protocol of this FlowFalconResolutionSetting.  # noqa: E501


        :return: The show_protocol of this FlowFalconResolutionSetting.  # noqa: E501
        :rtype: str
        """
        return self._show_protocol

    @show_protocol.setter
    def show_protocol(self, show_protocol):
        """Sets the show_protocol of this FlowFalconResolutionSetting.


        :param show_protocol: The show_protocol of this FlowFalconResolutionSetting.  # noqa: E501
        :type: str
        """

        self._show_protocol = show_protocol

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
        if issubclass(FlowFalconResolutionSetting, dict):
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
        if not isinstance(other, FlowFalconResolutionSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
