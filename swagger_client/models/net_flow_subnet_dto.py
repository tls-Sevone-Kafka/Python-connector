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

class NetFlowSubnetDto(object):
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
        'id': 'int',
        'name': 'str',
        'ip': 'str',
        'prefix': 'int',
        'segment_id': 'int',
        'segment_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ip': 'ip',
        'prefix': 'prefix',
        'segment_id': 'segmentId',
        'segment_name': 'segmentName'
    }

    def __init__(self, id=None, name=None, ip=None, prefix=None, segment_id=None, segment_name=None):  # noqa: E501
        """NetFlowSubnetDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._ip = None
        self._prefix = None
        self._segment_id = None
        self._segment_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip
        if prefix is not None:
            self.prefix = prefix
        if segment_id is not None:
            self.segment_id = segment_id
        if segment_name is not None:
            self.segment_name = segment_name

    @property
    def id(self):
        """Gets the id of this NetFlowSubnetDto.  # noqa: E501


        :return: The id of this NetFlowSubnetDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetFlowSubnetDto.


        :param id: The id of this NetFlowSubnetDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NetFlowSubnetDto.  # noqa: E501


        :return: The name of this NetFlowSubnetDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetFlowSubnetDto.


        :param name: The name of this NetFlowSubnetDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ip(self):
        """Gets the ip of this NetFlowSubnetDto.  # noqa: E501


        :return: The ip of this NetFlowSubnetDto.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this NetFlowSubnetDto.


        :param ip: The ip of this NetFlowSubnetDto.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def prefix(self):
        """Gets the prefix of this NetFlowSubnetDto.  # noqa: E501


        :return: The prefix of this NetFlowSubnetDto.  # noqa: E501
        :rtype: int
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this NetFlowSubnetDto.


        :param prefix: The prefix of this NetFlowSubnetDto.  # noqa: E501
        :type: int
        """

        self._prefix = prefix

    @property
    def segment_id(self):
        """Gets the segment_id of this NetFlowSubnetDto.  # noqa: E501


        :return: The segment_id of this NetFlowSubnetDto.  # noqa: E501
        :rtype: int
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this NetFlowSubnetDto.


        :param segment_id: The segment_id of this NetFlowSubnetDto.  # noqa: E501
        :type: int
        """

        self._segment_id = segment_id

    @property
    def segment_name(self):
        """Gets the segment_name of this NetFlowSubnetDto.  # noqa: E501


        :return: The segment_name of this NetFlowSubnetDto.  # noqa: E501
        :rtype: str
        """
        return self._segment_name

    @segment_name.setter
    def segment_name(self, segment_name):
        """Sets the segment_name of this NetFlowSubnetDto.


        :param segment_name: The segment_name of this NetFlowSubnetDto.  # noqa: E501
        :type: str
        """

        self._segment_name = segment_name

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
        if issubclass(NetFlowSubnetDto, dict):
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
        if not isinstance(other, NetFlowSubnetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
