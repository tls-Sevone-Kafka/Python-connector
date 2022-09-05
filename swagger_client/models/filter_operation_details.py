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

class FilterOperationDetails(object):
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
        'arity': 'int'
    }

    attribute_map = {
        'name': 'name',
        'arity': 'arity'
    }

    def __init__(self, name=None, arity=None):  # noqa: E501
        """FilterOperationDetails - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._arity = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if arity is not None:
            self.arity = arity

    @property
    def name(self):
        """Gets the name of this FilterOperationDetails.  # noqa: E501


        :return: The name of this FilterOperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilterOperationDetails.


        :param name: The name of this FilterOperationDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def arity(self):
        """Gets the arity of this FilterOperationDetails.  # noqa: E501


        :return: The arity of this FilterOperationDetails.  # noqa: E501
        :rtype: int
        """
        return self._arity

    @arity.setter
    def arity(self, arity):
        """Sets the arity of this FilterOperationDetails.


        :param arity: The arity of this FilterOperationDetails.  # noqa: E501
        :type: int
        """

        self._arity = arity

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
        if issubclass(FilterOperationDetails, dict):
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
        if not isinstance(other, FilterOperationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
