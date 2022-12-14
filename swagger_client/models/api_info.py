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

class ApiInfo(object):
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
        'commit_id_abbrev': 'str',
        'commit_time': 'str',
        'build_time': 'str',
        'build_version': 'str'
    }

    attribute_map = {
        'commit_id_abbrev': 'commitIdAbbrev',
        'commit_time': 'commitTime',
        'build_time': 'buildTime',
        'build_version': 'buildVersion'
    }

    def __init__(self, commit_id_abbrev=None, commit_time=None, build_time=None, build_version=None):  # noqa: E501
        """ApiInfo - a model defined in Swagger"""  # noqa: E501
        self._commit_id_abbrev = None
        self._commit_time = None
        self._build_time = None
        self._build_version = None
        self.discriminator = None
        if commit_id_abbrev is not None:
            self.commit_id_abbrev = commit_id_abbrev
        if commit_time is not None:
            self.commit_time = commit_time
        if build_time is not None:
            self.build_time = build_time
        if build_version is not None:
            self.build_version = build_version

    @property
    def commit_id_abbrev(self):
        """Gets the commit_id_abbrev of this ApiInfo.  # noqa: E501


        :return: The commit_id_abbrev of this ApiInfo.  # noqa: E501
        :rtype: str
        """
        return self._commit_id_abbrev

    @commit_id_abbrev.setter
    def commit_id_abbrev(self, commit_id_abbrev):
        """Sets the commit_id_abbrev of this ApiInfo.


        :param commit_id_abbrev: The commit_id_abbrev of this ApiInfo.  # noqa: E501
        :type: str
        """

        self._commit_id_abbrev = commit_id_abbrev

    @property
    def commit_time(self):
        """Gets the commit_time of this ApiInfo.  # noqa: E501


        :return: The commit_time of this ApiInfo.  # noqa: E501
        :rtype: str
        """
        return self._commit_time

    @commit_time.setter
    def commit_time(self, commit_time):
        """Sets the commit_time of this ApiInfo.


        :param commit_time: The commit_time of this ApiInfo.  # noqa: E501
        :type: str
        """

        self._commit_time = commit_time

    @property
    def build_time(self):
        """Gets the build_time of this ApiInfo.  # noqa: E501


        :return: The build_time of this ApiInfo.  # noqa: E501
        :rtype: str
        """
        return self._build_time

    @build_time.setter
    def build_time(self, build_time):
        """Sets the build_time of this ApiInfo.


        :param build_time: The build_time of this ApiInfo.  # noqa: E501
        :type: str
        """

        self._build_time = build_time

    @property
    def build_version(self):
        """Gets the build_version of this ApiInfo.  # noqa: E501


        :return: The build_version of this ApiInfo.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this ApiInfo.


        :param build_version: The build_version of this ApiInfo.  # noqa: E501
        :type: str
        """

        self._build_version = build_version

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
        if issubclass(ApiInfo, dict):
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
        if not isinstance(other, ApiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
