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

class ObjectsFilterBody(object):
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
        'object_filter': 'ObjectFilterNoMetadata',
        'options': 'PageAndSortOptionsNoMetadata'
    }

    attribute_map = {
        'object_filter': 'objectFilter',
        'options': 'options'
    }

    def __init__(self, object_filter=None, options=None):  # noqa: E501
        """ObjectsFilterBody - a model defined in Swagger"""  # noqa: E501
        self._object_filter = None
        self._options = None
        self.discriminator = None
        if object_filter is not None:
            self.object_filter = object_filter
        if options is not None:
            self.options = options

    @property
    def object_filter(self):
        """Gets the object_filter of this ObjectsFilterBody.  # noqa: E501


        :return: The object_filter of this ObjectsFilterBody.  # noqa: E501
        :rtype: ObjectFilterNoMetadata
        """
        return self._object_filter

    @object_filter.setter
    def object_filter(self, object_filter):
        """Sets the object_filter of this ObjectsFilterBody.


        :param object_filter: The object_filter of this ObjectsFilterBody.  # noqa: E501
        :type: ObjectFilterNoMetadata
        """

        self._object_filter = object_filter

    @property
    def options(self):
        """Gets the options of this ObjectsFilterBody.  # noqa: E501


        :return: The options of this ObjectsFilterBody.  # noqa: E501
        :rtype: PageAndSortOptionsNoMetadata
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ObjectsFilterBody.


        :param options: The options of this ObjectsFilterBody.  # noqa: E501
        :type: PageAndSortOptionsNoMetadata
        """

        self._options = options

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
        if issubclass(ObjectsFilterBody, dict):
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
        if not isinstance(other, ObjectsFilterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
