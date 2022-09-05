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

class ObjectGroupAttachmentRequestDtoV1(object):
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
        'resource': 'ObjectGroupAttachmentResourceV1'
    }

    attribute_map = {
        'name': 'name',
        'resource': 'resource'
    }

    def __init__(self, name=None, resource=None):  # noqa: E501
        """ObjectGroupAttachmentRequestDtoV1 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._resource = None
        self.discriminator = None
        self.name = name
        self.resource = resource

    @property
    def name(self):
        """Gets the name of this ObjectGroupAttachmentRequestDtoV1.  # noqa: E501


        :return: The name of this ObjectGroupAttachmentRequestDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectGroupAttachmentRequestDtoV1.


        :param name: The name of this ObjectGroupAttachmentRequestDtoV1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resource(self):
        """Gets the resource of this ObjectGroupAttachmentRequestDtoV1.  # noqa: E501


        :return: The resource of this ObjectGroupAttachmentRequestDtoV1.  # noqa: E501
        :rtype: ObjectGroupAttachmentResourceV1
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ObjectGroupAttachmentRequestDtoV1.


        :param resource: The resource of this ObjectGroupAttachmentRequestDtoV1.  # noqa: E501
        :type: ObjectGroupAttachmentResourceV1
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

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
        if issubclass(ObjectGroupAttachmentRequestDtoV1, dict):
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
        if not isinstance(other, ObjectGroupAttachmentRequestDtoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
