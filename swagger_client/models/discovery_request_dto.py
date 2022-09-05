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

class DiscoveryRequestDto(object):
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
        'queue': 'str',
        'allow_manual': 'bool',
        'allow_automatic': 'bool',
        'is_working': 'bool'
    }

    attribute_map = {
        'queue': 'queue',
        'allow_manual': 'allowManual',
        'allow_automatic': 'allowAutomatic',
        'is_working': 'isWorking'
    }

    def __init__(self, queue=None, allow_manual=None, allow_automatic=None, is_working=None):  # noqa: E501
        """DiscoveryRequestDto - a model defined in Swagger"""  # noqa: E501
        self._queue = None
        self._allow_manual = None
        self._allow_automatic = None
        self._is_working = None
        self.discriminator = None
        if queue is not None:
            self.queue = queue
        if allow_manual is not None:
            self.allow_manual = allow_manual
        if allow_automatic is not None:
            self.allow_automatic = allow_automatic
        if is_working is not None:
            self.is_working = is_working

    @property
    def queue(self):
        """Gets the queue of this DiscoveryRequestDto.  # noqa: E501


        :return: The queue of this DiscoveryRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this DiscoveryRequestDto.


        :param queue: The queue of this DiscoveryRequestDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["BLANK", "high", "low", "cancel"]  # noqa: E501
        if queue not in allowed_values:
            raise ValueError(
                "Invalid value for `queue` ({0}), must be one of {1}"  # noqa: E501
                .format(queue, allowed_values)
            )

        self._queue = queue

    @property
    def allow_manual(self):
        """Gets the allow_manual of this DiscoveryRequestDto.  # noqa: E501


        :return: The allow_manual of this DiscoveryRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._allow_manual

    @allow_manual.setter
    def allow_manual(self, allow_manual):
        """Sets the allow_manual of this DiscoveryRequestDto.


        :param allow_manual: The allow_manual of this DiscoveryRequestDto.  # noqa: E501
        :type: bool
        """

        self._allow_manual = allow_manual

    @property
    def allow_automatic(self):
        """Gets the allow_automatic of this DiscoveryRequestDto.  # noqa: E501


        :return: The allow_automatic of this DiscoveryRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._allow_automatic

    @allow_automatic.setter
    def allow_automatic(self, allow_automatic):
        """Sets the allow_automatic of this DiscoveryRequestDto.


        :param allow_automatic: The allow_automatic of this DiscoveryRequestDto.  # noqa: E501
        :type: bool
        """

        self._allow_automatic = allow_automatic

    @property
    def is_working(self):
        """Gets the is_working of this DiscoveryRequestDto.  # noqa: E501


        :return: The is_working of this DiscoveryRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_working

    @is_working.setter
    def is_working(self, is_working):
        """Sets the is_working of this DiscoveryRequestDto.


        :param is_working: The is_working of this DiscoveryRequestDto.  # noqa: E501
        :type: bool
        """

        self._is_working = is_working

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
        if issubclass(DiscoveryRequestDto, dict):
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
        if not isinstance(other, DiscoveryRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
