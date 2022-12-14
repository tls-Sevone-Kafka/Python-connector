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

class FlowFalconReportResponseDto(object):
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
        'key_headers': 'list[FieldDescription]',
        'value_headers': 'list[FieldDescription]',
        'nodes': 'list[ResultNode]',
        'other_traffic': 'ResultNode',
        'total_traffic': 'ResultNode',
        'no_template_match': 'bool',
        'maximum_sample_rate': 'int'
    }

    attribute_map = {
        'key_headers': 'keyHeaders',
        'value_headers': 'valueHeaders',
        'nodes': 'nodes',
        'other_traffic': 'otherTraffic',
        'total_traffic': 'totalTraffic',
        'no_template_match': 'noTemplateMatch',
        'maximum_sample_rate': 'maximumSampleRate'
    }

    def __init__(self, key_headers=None, value_headers=None, nodes=None, other_traffic=None, total_traffic=None, no_template_match=None, maximum_sample_rate=None):  # noqa: E501
        """FlowFalconReportResponseDto - a model defined in Swagger"""  # noqa: E501
        self._key_headers = None
        self._value_headers = None
        self._nodes = None
        self._other_traffic = None
        self._total_traffic = None
        self._no_template_match = None
        self._maximum_sample_rate = None
        self.discriminator = None
        if key_headers is not None:
            self.key_headers = key_headers
        if value_headers is not None:
            self.value_headers = value_headers
        if nodes is not None:
            self.nodes = nodes
        if other_traffic is not None:
            self.other_traffic = other_traffic
        if total_traffic is not None:
            self.total_traffic = total_traffic
        if no_template_match is not None:
            self.no_template_match = no_template_match
        if maximum_sample_rate is not None:
            self.maximum_sample_rate = maximum_sample_rate

    @property
    def key_headers(self):
        """Gets the key_headers of this FlowFalconReportResponseDto.  # noqa: E501


        :return: The key_headers of this FlowFalconReportResponseDto.  # noqa: E501
        :rtype: list[FieldDescription]
        """
        return self._key_headers

    @key_headers.setter
    def key_headers(self, key_headers):
        """Sets the key_headers of this FlowFalconReportResponseDto.


        :param key_headers: The key_headers of this FlowFalconReportResponseDto.  # noqa: E501
        :type: list[FieldDescription]
        """

        self._key_headers = key_headers

    @property
    def value_headers(self):
        """Gets the value_headers of this FlowFalconReportResponseDto.  # noqa: E501


        :return: The value_headers of this FlowFalconReportResponseDto.  # noqa: E501
        :rtype: list[FieldDescription]
        """
        return self._value_headers

    @value_headers.setter
    def value_headers(self, value_headers):
        """Sets the value_headers of this FlowFalconReportResponseDto.


        :param value_headers: The value_headers of this FlowFalconReportResponseDto.  # noqa: E501
        :type: list[FieldDescription]
        """

        self._value_headers = value_headers

    @property
    def nodes(self):
        """Gets the nodes of this FlowFalconReportResponseDto.  # noqa: E501


        :return: The nodes of this FlowFalconReportResponseDto.  # noqa: E501
        :rtype: list[ResultNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this FlowFalconReportResponseDto.


        :param nodes: The nodes of this FlowFalconReportResponseDto.  # noqa: E501
        :type: list[ResultNode]
        """

        self._nodes = nodes

    @property
    def other_traffic(self):
        """Gets the other_traffic of this FlowFalconReportResponseDto.  # noqa: E501


        :return: The other_traffic of this FlowFalconReportResponseDto.  # noqa: E501
        :rtype: ResultNode
        """
        return self._other_traffic

    @other_traffic.setter
    def other_traffic(self, other_traffic):
        """Sets the other_traffic of this FlowFalconReportResponseDto.


        :param other_traffic: The other_traffic of this FlowFalconReportResponseDto.  # noqa: E501
        :type: ResultNode
        """

        self._other_traffic = other_traffic

    @property
    def total_traffic(self):
        """Gets the total_traffic of this FlowFalconReportResponseDto.  # noqa: E501


        :return: The total_traffic of this FlowFalconReportResponseDto.  # noqa: E501
        :rtype: ResultNode
        """
        return self._total_traffic

    @total_traffic.setter
    def total_traffic(self, total_traffic):
        """Sets the total_traffic of this FlowFalconReportResponseDto.


        :param total_traffic: The total_traffic of this FlowFalconReportResponseDto.  # noqa: E501
        :type: ResultNode
        """

        self._total_traffic = total_traffic

    @property
    def no_template_match(self):
        """Gets the no_template_match of this FlowFalconReportResponseDto.  # noqa: E501


        :return: The no_template_match of this FlowFalconReportResponseDto.  # noqa: E501
        :rtype: bool
        """
        return self._no_template_match

    @no_template_match.setter
    def no_template_match(self, no_template_match):
        """Sets the no_template_match of this FlowFalconReportResponseDto.


        :param no_template_match: The no_template_match of this FlowFalconReportResponseDto.  # noqa: E501
        :type: bool
        """

        self._no_template_match = no_template_match

    @property
    def maximum_sample_rate(self):
        """Gets the maximum_sample_rate of this FlowFalconReportResponseDto.  # noqa: E501


        :return: The maximum_sample_rate of this FlowFalconReportResponseDto.  # noqa: E501
        :rtype: int
        """
        return self._maximum_sample_rate

    @maximum_sample_rate.setter
    def maximum_sample_rate(self, maximum_sample_rate):
        """Sets the maximum_sample_rate of this FlowFalconReportResponseDto.


        :param maximum_sample_rate: The maximum_sample_rate of this FlowFalconReportResponseDto.  # noqa: E501
        :type: int
        """

        self._maximum_sample_rate = maximum_sample_rate

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
        if issubclass(FlowFalconReportResponseDto, dict):
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
        if not isinstance(other, FlowFalconReportResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
