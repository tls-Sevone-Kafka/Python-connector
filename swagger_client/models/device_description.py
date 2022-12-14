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

class DeviceDescription(object):
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
        'type': 'str',
        'old_ts': 'int',
        'new_ts': 'int',
        'ip': 'str',
        'automatic_creation': 'bool',
        'objects': 'list[ObjectDescription]',
        'distribution_on_all_peers': 'bool',
        'distribution_peer_list': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'old_ts': 'oldTs',
        'new_ts': 'newTs',
        'ip': 'ip',
        'automatic_creation': 'automaticCreation',
        'objects': 'objects',
        'distribution_on_all_peers': 'distributionOnAllPeers',
        'distribution_peer_list': 'distributionPeerList'
    }

    def __init__(self, name='The name of the device', type='The device type for this device', old_ts=None, new_ts=None, ip='The ip address of the device', automatic_creation=False, objects=None, distribution_on_all_peers=False, distribution_peer_list=None):  # noqa: E501
        """DeviceDescription - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._old_ts = None
        self._new_ts = None
        self._ip = None
        self._automatic_creation = None
        self._objects = None
        self._distribution_on_all_peers = None
        self._distribution_peer_list = None
        self.discriminator = None
        self.name = name
        self.type = type
        self.old_ts = old_ts
        self.new_ts = new_ts
        if ip is not None:
            self.ip = ip
        if automatic_creation is not None:
            self.automatic_creation = automatic_creation
        if objects is not None:
            self.objects = objects
        if distribution_on_all_peers is not None:
            self.distribution_on_all_peers = distribution_on_all_peers
        if distribution_peer_list is not None:
            self.distribution_peer_list = distribution_peer_list

    @property
    def name(self):
        """Gets the name of this DeviceDescription.  # noqa: E501


        :return: The name of this DeviceDescription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceDescription.


        :param name: The name of this DeviceDescription.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this DeviceDescription.  # noqa: E501


        :return: The type of this DeviceDescription.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceDescription.


        :param type: The type of this DeviceDescription.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def old_ts(self):
        """Gets the old_ts of this DeviceDescription.  # noqa: E501


        :return: The old_ts of this DeviceDescription.  # noqa: E501
        :rtype: int
        """
        return self._old_ts

    @old_ts.setter
    def old_ts(self, old_ts):
        """Sets the old_ts of this DeviceDescription.


        :param old_ts: The old_ts of this DeviceDescription.  # noqa: E501
        :type: int
        """
        if old_ts is None:
            raise ValueError("Invalid value for `old_ts`, must not be `None`")  # noqa: E501

        self._old_ts = old_ts

    @property
    def new_ts(self):
        """Gets the new_ts of this DeviceDescription.  # noqa: E501


        :return: The new_ts of this DeviceDescription.  # noqa: E501
        :rtype: int
        """
        return self._new_ts

    @new_ts.setter
    def new_ts(self, new_ts):
        """Sets the new_ts of this DeviceDescription.


        :param new_ts: The new_ts of this DeviceDescription.  # noqa: E501
        :type: int
        """
        if new_ts is None:
            raise ValueError("Invalid value for `new_ts`, must not be `None`")  # noqa: E501

        self._new_ts = new_ts

    @property
    def ip(self):
        """Gets the ip of this DeviceDescription.  # noqa: E501


        :return: The ip of this DeviceDescription.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this DeviceDescription.


        :param ip: The ip of this DeviceDescription.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def automatic_creation(self):
        """Gets the automatic_creation of this DeviceDescription.  # noqa: E501


        :return: The automatic_creation of this DeviceDescription.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_creation

    @automatic_creation.setter
    def automatic_creation(self, automatic_creation):
        """Sets the automatic_creation of this DeviceDescription.


        :param automatic_creation: The automatic_creation of this DeviceDescription.  # noqa: E501
        :type: bool
        """

        self._automatic_creation = automatic_creation

    @property
    def objects(self):
        """Gets the objects of this DeviceDescription.  # noqa: E501


        :return: The objects of this DeviceDescription.  # noqa: E501
        :rtype: list[ObjectDescription]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this DeviceDescription.


        :param objects: The objects of this DeviceDescription.  # noqa: E501
        :type: list[ObjectDescription]
        """

        self._objects = objects

    @property
    def distribution_on_all_peers(self):
        """Gets the distribution_on_all_peers of this DeviceDescription.  # noqa: E501


        :return: The distribution_on_all_peers of this DeviceDescription.  # noqa: E501
        :rtype: bool
        """
        return self._distribution_on_all_peers

    @distribution_on_all_peers.setter
    def distribution_on_all_peers(self, distribution_on_all_peers):
        """Sets the distribution_on_all_peers of this DeviceDescription.


        :param distribution_on_all_peers: The distribution_on_all_peers of this DeviceDescription.  # noqa: E501
        :type: bool
        """

        self._distribution_on_all_peers = distribution_on_all_peers

    @property
    def distribution_peer_list(self):
        """Gets the distribution_peer_list of this DeviceDescription.  # noqa: E501


        :return: The distribution_peer_list of this DeviceDescription.  # noqa: E501
        :rtype: list[int]
        """
        return self._distribution_peer_list

    @distribution_peer_list.setter
    def distribution_peer_list(self, distribution_peer_list):
        """Sets the distribution_peer_list of this DeviceDescription.


        :param distribution_peer_list: The distribution_peer_list of this DeviceDescription.  # noqa: E501
        :type: list[int]
        """

        self._distribution_peer_list = distribution_peer_list

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
        if issubclass(DeviceDescription, dict):
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
        if not isinstance(other, DeviceDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
