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

class DeviceGroupRuleDto(object):
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
        'group_id': 'int',
        'name_expression': 'str',
        'description_expression': 'str',
        'mgt_ip_expression': 'str',
        'sys_name_expression': 'str',
        'sys_descr_expression': 'str',
        'sys_location_expression': 'str',
        'sys_object_id_expression': 'str',
        'sys_contact_expression': 'str',
        'walk_check_oid': 'str',
        'namespace_id': 'int',
        'attribute_id': 'int',
        'metadata_value_expression': 'str'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'name_expression': 'nameExpression',
        'description_expression': 'descriptionExpression',
        'mgt_ip_expression': 'mgtIpExpression',
        'sys_name_expression': 'sysNameExpression',
        'sys_descr_expression': 'sysDescrExpression',
        'sys_location_expression': 'sysLocationExpression',
        'sys_object_id_expression': 'sysObjectIdExpression',
        'sys_contact_expression': 'sysContactExpression',
        'walk_check_oid': 'walkCheckOid',
        'namespace_id': 'namespaceId',
        'attribute_id': 'attributeId',
        'metadata_value_expression': 'metadataValueExpression'
    }

    def __init__(self, id=None, group_id=None, name_expression=None, description_expression=None, mgt_ip_expression=None, sys_name_expression=None, sys_descr_expression=None, sys_location_expression=None, sys_object_id_expression=None, sys_contact_expression=None, walk_check_oid=None, namespace_id=None, attribute_id=None, metadata_value_expression=None):  # noqa: E501
        """DeviceGroupRuleDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._group_id = None
        self._name_expression = None
        self._description_expression = None
        self._mgt_ip_expression = None
        self._sys_name_expression = None
        self._sys_descr_expression = None
        self._sys_location_expression = None
        self._sys_object_id_expression = None
        self._sys_contact_expression = None
        self._walk_check_oid = None
        self._namespace_id = None
        self._attribute_id = None
        self._metadata_value_expression = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.group_id = group_id
        if name_expression is not None:
            self.name_expression = name_expression
        if description_expression is not None:
            self.description_expression = description_expression
        if mgt_ip_expression is not None:
            self.mgt_ip_expression = mgt_ip_expression
        if sys_name_expression is not None:
            self.sys_name_expression = sys_name_expression
        if sys_descr_expression is not None:
            self.sys_descr_expression = sys_descr_expression
        if sys_location_expression is not None:
            self.sys_location_expression = sys_location_expression
        if sys_object_id_expression is not None:
            self.sys_object_id_expression = sys_object_id_expression
        if sys_contact_expression is not None:
            self.sys_contact_expression = sys_contact_expression
        if walk_check_oid is not None:
            self.walk_check_oid = walk_check_oid
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if attribute_id is not None:
            self.attribute_id = attribute_id
        if metadata_value_expression is not None:
            self.metadata_value_expression = metadata_value_expression

    @property
    def id(self):
        """Gets the id of this DeviceGroupRuleDto.  # noqa: E501


        :return: The id of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceGroupRuleDto.


        :param id: The id of this DeviceGroupRuleDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this DeviceGroupRuleDto.  # noqa: E501


        :return: The group_id of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DeviceGroupRuleDto.


        :param group_id: The group_id of this DeviceGroupRuleDto.  # noqa: E501
        :type: int
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def name_expression(self):
        """Gets the name_expression of this DeviceGroupRuleDto.  # noqa: E501


        :return: The name_expression of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._name_expression

    @name_expression.setter
    def name_expression(self, name_expression):
        """Sets the name_expression of this DeviceGroupRuleDto.


        :param name_expression: The name_expression of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._name_expression = name_expression

    @property
    def description_expression(self):
        """Gets the description_expression of this DeviceGroupRuleDto.  # noqa: E501


        :return: The description_expression of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._description_expression

    @description_expression.setter
    def description_expression(self, description_expression):
        """Sets the description_expression of this DeviceGroupRuleDto.


        :param description_expression: The description_expression of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._description_expression = description_expression

    @property
    def mgt_ip_expression(self):
        """Gets the mgt_ip_expression of this DeviceGroupRuleDto.  # noqa: E501


        :return: The mgt_ip_expression of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._mgt_ip_expression

    @mgt_ip_expression.setter
    def mgt_ip_expression(self, mgt_ip_expression):
        """Sets the mgt_ip_expression of this DeviceGroupRuleDto.


        :param mgt_ip_expression: The mgt_ip_expression of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._mgt_ip_expression = mgt_ip_expression

    @property
    def sys_name_expression(self):
        """Gets the sys_name_expression of this DeviceGroupRuleDto.  # noqa: E501


        :return: The sys_name_expression of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._sys_name_expression

    @sys_name_expression.setter
    def sys_name_expression(self, sys_name_expression):
        """Sets the sys_name_expression of this DeviceGroupRuleDto.


        :param sys_name_expression: The sys_name_expression of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._sys_name_expression = sys_name_expression

    @property
    def sys_descr_expression(self):
        """Gets the sys_descr_expression of this DeviceGroupRuleDto.  # noqa: E501


        :return: The sys_descr_expression of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._sys_descr_expression

    @sys_descr_expression.setter
    def sys_descr_expression(self, sys_descr_expression):
        """Sets the sys_descr_expression of this DeviceGroupRuleDto.


        :param sys_descr_expression: The sys_descr_expression of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._sys_descr_expression = sys_descr_expression

    @property
    def sys_location_expression(self):
        """Gets the sys_location_expression of this DeviceGroupRuleDto.  # noqa: E501


        :return: The sys_location_expression of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._sys_location_expression

    @sys_location_expression.setter
    def sys_location_expression(self, sys_location_expression):
        """Sets the sys_location_expression of this DeviceGroupRuleDto.


        :param sys_location_expression: The sys_location_expression of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._sys_location_expression = sys_location_expression

    @property
    def sys_object_id_expression(self):
        """Gets the sys_object_id_expression of this DeviceGroupRuleDto.  # noqa: E501


        :return: The sys_object_id_expression of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._sys_object_id_expression

    @sys_object_id_expression.setter
    def sys_object_id_expression(self, sys_object_id_expression):
        """Sets the sys_object_id_expression of this DeviceGroupRuleDto.


        :param sys_object_id_expression: The sys_object_id_expression of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._sys_object_id_expression = sys_object_id_expression

    @property
    def sys_contact_expression(self):
        """Gets the sys_contact_expression of this DeviceGroupRuleDto.  # noqa: E501


        :return: The sys_contact_expression of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._sys_contact_expression

    @sys_contact_expression.setter
    def sys_contact_expression(self, sys_contact_expression):
        """Sets the sys_contact_expression of this DeviceGroupRuleDto.


        :param sys_contact_expression: The sys_contact_expression of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._sys_contact_expression = sys_contact_expression

    @property
    def walk_check_oid(self):
        """Gets the walk_check_oid of this DeviceGroupRuleDto.  # noqa: E501


        :return: The walk_check_oid of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._walk_check_oid

    @walk_check_oid.setter
    def walk_check_oid(self, walk_check_oid):
        """Sets the walk_check_oid of this DeviceGroupRuleDto.


        :param walk_check_oid: The walk_check_oid of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._walk_check_oid = walk_check_oid

    @property
    def namespace_id(self):
        """Gets the namespace_id of this DeviceGroupRuleDto.  # noqa: E501


        :return: The namespace_id of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        """Sets the namespace_id of this DeviceGroupRuleDto.


        :param namespace_id: The namespace_id of this DeviceGroupRuleDto.  # noqa: E501
        :type: int
        """

        self._namespace_id = namespace_id

    @property
    def attribute_id(self):
        """Gets the attribute_id of this DeviceGroupRuleDto.  # noqa: E501


        :return: The attribute_id of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this DeviceGroupRuleDto.


        :param attribute_id: The attribute_id of this DeviceGroupRuleDto.  # noqa: E501
        :type: int
        """

        self._attribute_id = attribute_id

    @property
    def metadata_value_expression(self):
        """Gets the metadata_value_expression of this DeviceGroupRuleDto.  # noqa: E501


        :return: The metadata_value_expression of this DeviceGroupRuleDto.  # noqa: E501
        :rtype: str
        """
        return self._metadata_value_expression

    @metadata_value_expression.setter
    def metadata_value_expression(self, metadata_value_expression):
        """Sets the metadata_value_expression of this DeviceGroupRuleDto.


        :param metadata_value_expression: The metadata_value_expression of this DeviceGroupRuleDto.  # noqa: E501
        :type: str
        """

        self._metadata_value_expression = metadata_value_expression

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
        if issubclass(DeviceGroupRuleDto, dict):
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
        if not isinstance(other, DeviceGroupRuleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other