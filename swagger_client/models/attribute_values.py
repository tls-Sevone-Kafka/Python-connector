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

class AttributeValues(object):
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
        'attribute_type': 'str',
        'attribute_id': 'int',
        'values': 'list[dict(str, object)]'
    }

    attribute_map = {
        'attribute_type': 'attributeType',
        'attribute_id': 'attributeId',
        'values': 'values'
    }

    def __init__(self, attribute_type=None, attribute_id=None, values=None):  # noqa: E501
        """AttributeValues - a model defined in Swagger"""  # noqa: E501
        self._attribute_type = None
        self._attribute_id = None
        self._values = None
        self.discriminator = None
        if attribute_type is not None:
            self.attribute_type = attribute_type
        if attribute_id is not None:
            self.attribute_id = attribute_id
        if values is not None:
            self.values = values

    @property
    def attribute_type(self):
        """Gets the attribute_type of this AttributeValues.  # noqa: E501


        :return: The attribute_type of this AttributeValues.  # noqa: E501
        :rtype: str
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this AttributeValues.


        :param attribute_type: The attribute_type of this AttributeValues.  # noqa: E501
        :type: str
        """
        allowed_values = ["integer", "ip", "mac", "url", "dateTime", "regex", "latLong", "string", "acceptedValues"]  # noqa: E501
        if attribute_type not in allowed_values:
            raise ValueError(
                "Invalid value for `attribute_type` ({0}), must be one of {1}"  # noqa: E501
                .format(attribute_type, allowed_values)
            )

        self._attribute_type = attribute_type

    @property
    def attribute_id(self):
        """Gets the attribute_id of this AttributeValues.  # noqa: E501


        :return: The attribute_id of this AttributeValues.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this AttributeValues.


        :param attribute_id: The attribute_id of this AttributeValues.  # noqa: E501
        :type: int
        """

        self._attribute_id = attribute_id

    @property
    def values(self):
        """Gets the values of this AttributeValues.  # noqa: E501

        The string key can be `value`, `url`, `label`, `latitude`, `longitude`, `id`  # noqa: E501

        :return: The values of this AttributeValues.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AttributeValues.

        The string key can be `value`, `url`, `label`, `latitude`, `longitude`, `id`  # noqa: E501

        :param values: The values of this AttributeValues.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._values = values

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
        if issubclass(AttributeValues, dict):
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
        if not isinstance(other, AttributeValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
