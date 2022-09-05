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

class AttributeFilterDto(object):
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
        'ids': 'list[int]',
        'namespace_ids': 'list[int]',
        'name': 'str',
        'type': 'list[str]',
        'entity_type': 'str',
        'singleton': 'bool',
        'validation_expression': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'namespace_ids': 'namespaceIds',
        'name': 'name',
        'type': 'type',
        'entity_type': 'entityType',
        'singleton': 'singleton',
        'validation_expression': 'validationExpression'
    }

    def __init__(self, ids=None, namespace_ids=None, name=None, type=None, entity_type=None, singleton=None, validation_expression=None):  # noqa: E501
        """AttributeFilterDto - a model defined in Swagger"""  # noqa: E501
        self._ids = None
        self._namespace_ids = None
        self._name = None
        self._type = None
        self._entity_type = None
        self._singleton = None
        self._validation_expression = None
        self.discriminator = None
        if ids is not None:
            self.ids = ids
        if namespace_ids is not None:
            self.namespace_ids = namespace_ids
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if entity_type is not None:
            self.entity_type = entity_type
        if singleton is not None:
            self.singleton = singleton
        if validation_expression is not None:
            self.validation_expression = validation_expression

    @property
    def ids(self):
        """Gets the ids of this AttributeFilterDto.  # noqa: E501


        :return: The ids of this AttributeFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this AttributeFilterDto.


        :param ids: The ids of this AttributeFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def namespace_ids(self):
        """Gets the namespace_ids of this AttributeFilterDto.  # noqa: E501


        :return: The namespace_ids of this AttributeFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._namespace_ids

    @namespace_ids.setter
    def namespace_ids(self, namespace_ids):
        """Sets the namespace_ids of this AttributeFilterDto.


        :param namespace_ids: The namespace_ids of this AttributeFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._namespace_ids = namespace_ids

    @property
    def name(self):
        """Gets the name of this AttributeFilterDto.  # noqa: E501


        :return: The name of this AttributeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttributeFilterDto.


        :param name: The name of this AttributeFilterDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this AttributeFilterDto.  # noqa: E501

        Type can be `integer`, `string`, `ip`, `mac`, `dateTime`, `regex`, `url`, `latLong`, `acceptedValues`  # noqa: E501

        :return: The type of this AttributeFilterDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AttributeFilterDto.

        Type can be `integer`, `string`, `ip`, `mac`, `dateTime`, `regex`, `url`, `latLong`, `acceptedValues`  # noqa: E501

        :param type: The type of this AttributeFilterDto.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["integer", "ip", "mac", "url", "dateTime", "regex", "latLong", "string", "acceptedValues"]  # noqa: E501
        if not set(type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._type = type

    @property
    def entity_type(self):
        """Gets the entity_type of this AttributeFilterDto.  # noqa: E501


        :return: The entity_type of this AttributeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this AttributeFilterDto.


        :param entity_type: The entity_type of this AttributeFilterDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["device", "object", "devicegroup", "objectgroup", "objecttype", "indicatortype"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def singleton(self):
        """Gets the singleton of this AttributeFilterDto.  # noqa: E501


        :return: The singleton of this AttributeFilterDto.  # noqa: E501
        :rtype: bool
        """
        return self._singleton

    @singleton.setter
    def singleton(self, singleton):
        """Sets the singleton of this AttributeFilterDto.


        :param singleton: The singleton of this AttributeFilterDto.  # noqa: E501
        :type: bool
        """

        self._singleton = singleton

    @property
    def validation_expression(self):
        """Gets the validation_expression of this AttributeFilterDto.  # noqa: E501


        :return: The validation_expression of this AttributeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._validation_expression

    @validation_expression.setter
    def validation_expression(self, validation_expression):
        """Sets the validation_expression of this AttributeFilterDto.


        :param validation_expression: The validation_expression of this AttributeFilterDto.  # noqa: E501
        :type: str
        """

        self._validation_expression = validation_expression

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
        if issubclass(AttributeFilterDto, dict):
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
        if not isinstance(other, AttributeFilterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
