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

class FlowFalconAttachmentFiltersSchema(object):
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
        'operations': 'dict(str, FilterOperationDetails)',
        'filters': 'dict(str, FilterSchemaDetails)',
        'default_operations': 'int'
    }

    attribute_map = {
        'operations': 'operations',
        'filters': 'filters',
        'default_operations': 'defaultOperations'
    }

    def __init__(self, operations=None, filters=None, default_operations=None):  # noqa: E501
        """FlowFalconAttachmentFiltersSchema - a model defined in Swagger"""  # noqa: E501
        self._operations = None
        self._filters = None
        self._default_operations = None
        self.discriminator = None
        if operations is not None:
            self.operations = operations
        if filters is not None:
            self.filters = filters
        if default_operations is not None:
            self.default_operations = default_operations

    @property
    def operations(self):
        """Gets the operations of this FlowFalconAttachmentFiltersSchema.  # noqa: E501


        :return: The operations of this FlowFalconAttachmentFiltersSchema.  # noqa: E501
        :rtype: dict(str, FilterOperationDetails)
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this FlowFalconAttachmentFiltersSchema.


        :param operations: The operations of this FlowFalconAttachmentFiltersSchema.  # noqa: E501
        :type: dict(str, FilterOperationDetails)
        """

        self._operations = operations

    @property
    def filters(self):
        """Gets the filters of this FlowFalconAttachmentFiltersSchema.  # noqa: E501


        :return: The filters of this FlowFalconAttachmentFiltersSchema.  # noqa: E501
        :rtype: dict(str, FilterSchemaDetails)
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this FlowFalconAttachmentFiltersSchema.


        :param filters: The filters of this FlowFalconAttachmentFiltersSchema.  # noqa: E501
        :type: dict(str, FilterSchemaDetails)
        """

        self._filters = filters

    @property
    def default_operations(self):
        """Gets the default_operations of this FlowFalconAttachmentFiltersSchema.  # noqa: E501


        :return: The default_operations of this FlowFalconAttachmentFiltersSchema.  # noqa: E501
        :rtype: int
        """
        return self._default_operations

    @default_operations.setter
    def default_operations(self, default_operations):
        """Sets the default_operations of this FlowFalconAttachmentFiltersSchema.


        :param default_operations: The default_operations of this FlowFalconAttachmentFiltersSchema.  # noqa: E501
        :type: int
        """

        self._default_operations = default_operations

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
        if issubclass(FlowFalconAttachmentFiltersSchema, dict):
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
        if not isinstance(other, FlowFalconAttachmentFiltersSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
