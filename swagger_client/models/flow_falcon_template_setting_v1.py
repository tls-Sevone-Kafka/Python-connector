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

class FlowFalconTemplateSettingV1(object):
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
        'is_aggregated': 'bool',
        'template_id': 'int',
        'metric_id': 'int'
    }

    attribute_map = {
        'is_aggregated': 'isAggregated',
        'template_id': 'templateId',
        'metric_id': 'metricId'
    }

    def __init__(self, is_aggregated=None, template_id=None, metric_id=None):  # noqa: E501
        """FlowFalconTemplateSettingV1 - a model defined in Swagger"""  # noqa: E501
        self._is_aggregated = None
        self._template_id = None
        self._metric_id = None
        self.discriminator = None
        if is_aggregated is not None:
            self.is_aggregated = is_aggregated
        if template_id is not None:
            self.template_id = template_id
        if metric_id is not None:
            self.metric_id = metric_id

    @property
    def is_aggregated(self):
        """Gets the is_aggregated of this FlowFalconTemplateSettingV1.  # noqa: E501


        :return: The is_aggregated of this FlowFalconTemplateSettingV1.  # noqa: E501
        :rtype: bool
        """
        return self._is_aggregated

    @is_aggregated.setter
    def is_aggregated(self, is_aggregated):
        """Sets the is_aggregated of this FlowFalconTemplateSettingV1.


        :param is_aggregated: The is_aggregated of this FlowFalconTemplateSettingV1.  # noqa: E501
        :type: bool
        """

        self._is_aggregated = is_aggregated

    @property
    def template_id(self):
        """Gets the template_id of this FlowFalconTemplateSettingV1.  # noqa: E501


        :return: The template_id of this FlowFalconTemplateSettingV1.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this FlowFalconTemplateSettingV1.


        :param template_id: The template_id of this FlowFalconTemplateSettingV1.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def metric_id(self):
        """Gets the metric_id of this FlowFalconTemplateSettingV1.  # noqa: E501


        :return: The metric_id of this FlowFalconTemplateSettingV1.  # noqa: E501
        :rtype: int
        """
        return self._metric_id

    @metric_id.setter
    def metric_id(self, metric_id):
        """Sets the metric_id of this FlowFalconTemplateSettingV1.


        :param metric_id: The metric_id of this FlowFalconTemplateSettingV1.  # noqa: E501
        :type: int
        """

        self._metric_id = metric_id

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
        if issubclass(FlowFalconTemplateSettingV1, dict):
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
        if not isinstance(other, FlowFalconTemplateSettingV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
