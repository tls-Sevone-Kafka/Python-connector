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

class MailActionDto(object):
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
        'role_ids': 'list[int]',
        'mails': 'list[str]',
        'user_ids': 'list[int]',
        'repeated_period': 'int',
        'repeated': 'bool'
    }

    attribute_map = {
        'role_ids': 'roleIds',
        'mails': 'mails',
        'user_ids': 'userIds',
        'repeated_period': 'repeatedPeriod',
        'repeated': 'repeated'
    }

    def __init__(self, role_ids=None, mails=None, user_ids=None, repeated_period=None, repeated=None):  # noqa: E501
        """MailActionDto - a model defined in Swagger"""  # noqa: E501
        self._role_ids = None
        self._mails = None
        self._user_ids = None
        self._repeated_period = None
        self._repeated = None
        self.discriminator = None
        if role_ids is not None:
            self.role_ids = role_ids
        if mails is not None:
            self.mails = mails
        if user_ids is not None:
            self.user_ids = user_ids
        if repeated_period is not None:
            self.repeated_period = repeated_period
        if repeated is not None:
            self.repeated = repeated

    @property
    def role_ids(self):
        """Gets the role_ids of this MailActionDto.  # noqa: E501


        :return: The role_ids of this MailActionDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this MailActionDto.


        :param role_ids: The role_ids of this MailActionDto.  # noqa: E501
        :type: list[int]
        """

        self._role_ids = role_ids

    @property
    def mails(self):
        """Gets the mails of this MailActionDto.  # noqa: E501


        :return: The mails of this MailActionDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._mails

    @mails.setter
    def mails(self, mails):
        """Sets the mails of this MailActionDto.


        :param mails: The mails of this MailActionDto.  # noqa: E501
        :type: list[str]
        """

        self._mails = mails

    @property
    def user_ids(self):
        """Gets the user_ids of this MailActionDto.  # noqa: E501


        :return: The user_ids of this MailActionDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this MailActionDto.


        :param user_ids: The user_ids of this MailActionDto.  # noqa: E501
        :type: list[int]
        """

        self._user_ids = user_ids

    @property
    def repeated_period(self):
        """Gets the repeated_period of this MailActionDto.  # noqa: E501


        :return: The repeated_period of this MailActionDto.  # noqa: E501
        :rtype: int
        """
        return self._repeated_period

    @repeated_period.setter
    def repeated_period(self, repeated_period):
        """Sets the repeated_period of this MailActionDto.


        :param repeated_period: The repeated_period of this MailActionDto.  # noqa: E501
        :type: int
        """

        self._repeated_period = repeated_period

    @property
    def repeated(self):
        """Gets the repeated of this MailActionDto.  # noqa: E501


        :return: The repeated of this MailActionDto.  # noqa: E501
        :rtype: bool
        """
        return self._repeated

    @repeated.setter
    def repeated(self, repeated):
        """Sets the repeated of this MailActionDto.


        :param repeated: The repeated of this MailActionDto.  # noqa: E501
        :type: bool
        """

        self._repeated = repeated

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
        if issubclass(MailActionDto, dict):
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
        if not isinstance(other, MailActionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
