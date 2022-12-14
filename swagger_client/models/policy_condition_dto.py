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

class PolicyConditionDto(object):
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
        'policy_id': 'int',
        'indicator_type_id': 'int',
        'type': 'int',
        'is_trigger': 'bool',
        'value': 'float',
        'unit': 'str',
        'comparison': 'int',
        'aggregation': 'int',
        'duration': 'int',
        'message': 'str',
        'sigma_direction': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policy_id': 'policyId',
        'indicator_type_id': 'indicatorTypeId',
        'type': 'type',
        'is_trigger': 'isTrigger',
        'value': 'value',
        'unit': 'unit',
        'comparison': 'comparison',
        'aggregation': 'aggregation',
        'duration': 'duration',
        'message': 'message',
        'sigma_direction': 'sigmaDirection'
    }

    def __init__(self, id=None, policy_id=None, indicator_type_id=None, type=None, is_trigger=None, value=None, unit=None, comparison=None, aggregation=None, duration=None, message=None, sigma_direction=None):  # noqa: E501
        """PolicyConditionDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._policy_id = None
        self._indicator_type_id = None
        self._type = None
        self._is_trigger = None
        self._value = None
        self._unit = None
        self._comparison = None
        self._aggregation = None
        self._duration = None
        self._message = None
        self._sigma_direction = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if policy_id is not None:
            self.policy_id = policy_id
        if indicator_type_id is not None:
            self.indicator_type_id = indicator_type_id
        if type is not None:
            self.type = type
        if is_trigger is not None:
            self.is_trigger = is_trigger
        if value is not None:
            self.value = value
        if unit is not None:
            self.unit = unit
        if comparison is not None:
            self.comparison = comparison
        if aggregation is not None:
            self.aggregation = aggregation
        if duration is not None:
            self.duration = duration
        if message is not None:
            self.message = message
        if sigma_direction is not None:
            self.sigma_direction = sigma_direction

    @property
    def id(self):
        """Gets the id of this PolicyConditionDto.  # noqa: E501

        For POST /policies, id is compulsory in triggerConditions and clearConditions.  # noqa: E501

        :return: The id of this PolicyConditionDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyConditionDto.

        For POST /policies, id is compulsory in triggerConditions and clearConditions.  # noqa: E501

        :param id: The id of this PolicyConditionDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def policy_id(self):
        """Gets the policy_id of this PolicyConditionDto.  # noqa: E501


        :return: The policy_id of this PolicyConditionDto.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this PolicyConditionDto.


        :param policy_id: The policy_id of this PolicyConditionDto.  # noqa: E501
        :type: int
        """

        self._policy_id = policy_id

    @property
    def indicator_type_id(self):
        """Gets the indicator_type_id of this PolicyConditionDto.  # noqa: E501


        :return: The indicator_type_id of this PolicyConditionDto.  # noqa: E501
        :rtype: int
        """
        return self._indicator_type_id

    @indicator_type_id.setter
    def indicator_type_id(self, indicator_type_id):
        """Sets the indicator_type_id of this PolicyConditionDto.


        :param indicator_type_id: The indicator_type_id of this PolicyConditionDto.  # noqa: E501
        :type: int
        """

        self._indicator_type_id = indicator_type_id

    @property
    def type(self):
        """Gets the type of this PolicyConditionDto.  # noqa: E501


        :return: The type of this PolicyConditionDto.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyConditionDto.


        :param type: The type of this PolicyConditionDto.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def is_trigger(self):
        """Gets the is_trigger of this PolicyConditionDto.  # noqa: E501

        isTrigger is READ-ONLY in all endpoints except POST /policies/{policyId}/conditions  # noqa: E501

        :return: The is_trigger of this PolicyConditionDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_trigger

    @is_trigger.setter
    def is_trigger(self, is_trigger):
        """Sets the is_trigger of this PolicyConditionDto.

        isTrigger is READ-ONLY in all endpoints except POST /policies/{policyId}/conditions  # noqa: E501

        :param is_trigger: The is_trigger of this PolicyConditionDto.  # noqa: E501
        :type: bool
        """

        self._is_trigger = is_trigger

    @property
    def value(self):
        """Gets the value of this PolicyConditionDto.  # noqa: E501


        :return: The value of this PolicyConditionDto.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PolicyConditionDto.


        :param value: The value of this PolicyConditionDto.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this PolicyConditionDto.  # noqa: E501


        :return: The unit of this PolicyConditionDto.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this PolicyConditionDto.


        :param unit: The unit of this PolicyConditionDto.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def comparison(self):
        """Gets the comparison of this PolicyConditionDto.  # noqa: E501


        :return: The comparison of this PolicyConditionDto.  # noqa: E501
        :rtype: int
        """
        return self._comparison

    @comparison.setter
    def comparison(self, comparison):
        """Sets the comparison of this PolicyConditionDto.


        :param comparison: The comparison of this PolicyConditionDto.  # noqa: E501
        :type: int
        """

        self._comparison = comparison

    @property
    def aggregation(self):
        """Gets the aggregation of this PolicyConditionDto.  # noqa: E501


        :return: The aggregation of this PolicyConditionDto.  # noqa: E501
        :rtype: int
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this PolicyConditionDto.


        :param aggregation: The aggregation of this PolicyConditionDto.  # noqa: E501
        :type: int
        """

        self._aggregation = aggregation

    @property
    def duration(self):
        """Gets the duration of this PolicyConditionDto.  # noqa: E501


        :return: The duration of this PolicyConditionDto.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this PolicyConditionDto.


        :param duration: The duration of this PolicyConditionDto.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def message(self):
        """Gets the message of this PolicyConditionDto.  # noqa: E501


        :return: The message of this PolicyConditionDto.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PolicyConditionDto.


        :param message: The message of this PolicyConditionDto.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def sigma_direction(self):
        """Gets the sigma_direction of this PolicyConditionDto.  # noqa: E501


        :return: The sigma_direction of this PolicyConditionDto.  # noqa: E501
        :rtype: int
        """
        return self._sigma_direction

    @sigma_direction.setter
    def sigma_direction(self, sigma_direction):
        """Sets the sigma_direction of this PolicyConditionDto.


        :param sigma_direction: The sigma_direction of this PolicyConditionDto.  # noqa: E501
        :type: int
        """

        self._sigma_direction = sigma_direction

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
        if issubclass(PolicyConditionDto, dict):
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
        if not isinstance(other, PolicyConditionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
