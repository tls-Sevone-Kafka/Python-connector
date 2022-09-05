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

class DeviceBulkUpdateRequestDto(object):
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
        'alternate_name': 'str',
        'description': 'str',
        'ip_address': 'str',
        'poll_frequency': 'int',
        'allow_delete': 'bool',
        'timezone': 'str',
        'workhours_group_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'alternate_name': 'alternateName',
        'description': 'description',
        'ip_address': 'ipAddress',
        'poll_frequency': 'pollFrequency',
        'allow_delete': 'allowDelete',
        'timezone': 'timezone',
        'workhours_group_id': 'workhoursGroupId'
    }

    def __init__(self, id=None, name=None, alternate_name=None, description=None, ip_address=None, poll_frequency=None, allow_delete=None, timezone=None, workhours_group_id=None):  # noqa: E501
        """DeviceBulkUpdateRequestDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._alternate_name = None
        self._description = None
        self._ip_address = None
        self._poll_frequency = None
        self._allow_delete = None
        self._timezone = None
        self._workhours_group_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if alternate_name is not None:
            self.alternate_name = alternate_name
        if description is not None:
            self.description = description
        if ip_address is not None:
            self.ip_address = ip_address
        if poll_frequency is not None:
            self.poll_frequency = poll_frequency
        if allow_delete is not None:
            self.allow_delete = allow_delete
        if timezone is not None:
            self.timezone = timezone
        if workhours_group_id is not None:
            self.workhours_group_id = workhours_group_id

    @property
    def id(self):
        """Gets the id of this DeviceBulkUpdateRequestDto.  # noqa: E501


        :return: The id of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceBulkUpdateRequestDto.


        :param id: The id of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeviceBulkUpdateRequestDto.  # noqa: E501


        :return: The name of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceBulkUpdateRequestDto.


        :param name: The name of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def alternate_name(self):
        """Gets the alternate_name of this DeviceBulkUpdateRequestDto.  # noqa: E501


        :return: The alternate_name of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._alternate_name

    @alternate_name.setter
    def alternate_name(self, alternate_name):
        """Sets the alternate_name of this DeviceBulkUpdateRequestDto.


        :param alternate_name: The alternate_name of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :type: str
        """

        self._alternate_name = alternate_name

    @property
    def description(self):
        """Gets the description of this DeviceBulkUpdateRequestDto.  # noqa: E501


        :return: The description of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceBulkUpdateRequestDto.


        :param description: The description of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip_address(self):
        """Gets the ip_address of this DeviceBulkUpdateRequestDto.  # noqa: E501


        :return: The ip_address of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DeviceBulkUpdateRequestDto.


        :param ip_address: The ip_address of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def poll_frequency(self):
        """Gets the poll_frequency of this DeviceBulkUpdateRequestDto.  # noqa: E501


        :return: The poll_frequency of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._poll_frequency

    @poll_frequency.setter
    def poll_frequency(self, poll_frequency):
        """Sets the poll_frequency of this DeviceBulkUpdateRequestDto.


        :param poll_frequency: The poll_frequency of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :type: int
        """

        self._poll_frequency = poll_frequency

    @property
    def allow_delete(self):
        """Gets the allow_delete of this DeviceBulkUpdateRequestDto.  # noqa: E501


        :return: The allow_delete of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._allow_delete

    @allow_delete.setter
    def allow_delete(self, allow_delete):
        """Sets the allow_delete of this DeviceBulkUpdateRequestDto.


        :param allow_delete: The allow_delete of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :type: bool
        """

        self._allow_delete = allow_delete

    @property
    def timezone(self):
        """Gets the timezone of this DeviceBulkUpdateRequestDto.  # noqa: E501


        :return: The timezone of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this DeviceBulkUpdateRequestDto.


        :param timezone: The timezone of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def workhours_group_id(self):
        """Gets the workhours_group_id of this DeviceBulkUpdateRequestDto.  # noqa: E501


        :return: The workhours_group_id of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._workhours_group_id

    @workhours_group_id.setter
    def workhours_group_id(self, workhours_group_id):
        """Sets the workhours_group_id of this DeviceBulkUpdateRequestDto.


        :param workhours_group_id: The workhours_group_id of this DeviceBulkUpdateRequestDto.  # noqa: E501
        :type: int
        """

        self._workhours_group_id = workhours_group_id

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
        if issubclass(DeviceBulkUpdateRequestDto, dict):
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
        if not isinstance(other, DeviceBulkUpdateRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
