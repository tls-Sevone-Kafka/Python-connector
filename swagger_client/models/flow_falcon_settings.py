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

class FlowFalconSettings(object):
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
        'flow_falcon': 'FlowFalconSetting',
        'flow_falcon_resolution': 'FlowFalconResolutionSetting',
        'flow_falcon_template': 'FlowFalconTemplateSetting',
        'result_limit': 'ResultLimitSetting',
        'source_fields': 'SourceFieldsSetting',
        'units': 'UnitsSetting'
    }

    attribute_map = {
        'flow_falcon': 'flowFalcon',
        'flow_falcon_resolution': 'flowFalconResolution',
        'flow_falcon_template': 'flowFalconTemplate',
        'result_limit': 'resultLimit',
        'source_fields': 'sourceFields',
        'units': 'units'
    }

    def __init__(self, flow_falcon=None, flow_falcon_resolution=None, flow_falcon_template=None, result_limit=None, source_fields=None, units=None):  # noqa: E501
        """FlowFalconSettings - a model defined in Swagger"""  # noqa: E501
        self._flow_falcon = None
        self._flow_falcon_resolution = None
        self._flow_falcon_template = None
        self._result_limit = None
        self._source_fields = None
        self._units = None
        self.discriminator = None
        self.flow_falcon = flow_falcon
        self.flow_falcon_resolution = flow_falcon_resolution
        self.flow_falcon_template = flow_falcon_template
        if result_limit is not None:
            self.result_limit = result_limit
        if source_fields is not None:
            self.source_fields = source_fields
        if units is not None:
            self.units = units

    @property
    def flow_falcon(self):
        """Gets the flow_falcon of this FlowFalconSettings.  # noqa: E501


        :return: The flow_falcon of this FlowFalconSettings.  # noqa: E501
        :rtype: FlowFalconSetting
        """
        return self._flow_falcon

    @flow_falcon.setter
    def flow_falcon(self, flow_falcon):
        """Sets the flow_falcon of this FlowFalconSettings.


        :param flow_falcon: The flow_falcon of this FlowFalconSettings.  # noqa: E501
        :type: FlowFalconSetting
        """
        if flow_falcon is None:
            raise ValueError("Invalid value for `flow_falcon`, must not be `None`")  # noqa: E501

        self._flow_falcon = flow_falcon

    @property
    def flow_falcon_resolution(self):
        """Gets the flow_falcon_resolution of this FlowFalconSettings.  # noqa: E501


        :return: The flow_falcon_resolution of this FlowFalconSettings.  # noqa: E501
        :rtype: FlowFalconResolutionSetting
        """
        return self._flow_falcon_resolution

    @flow_falcon_resolution.setter
    def flow_falcon_resolution(self, flow_falcon_resolution):
        """Sets the flow_falcon_resolution of this FlowFalconSettings.


        :param flow_falcon_resolution: The flow_falcon_resolution of this FlowFalconSettings.  # noqa: E501
        :type: FlowFalconResolutionSetting
        """
        if flow_falcon_resolution is None:
            raise ValueError("Invalid value for `flow_falcon_resolution`, must not be `None`")  # noqa: E501

        self._flow_falcon_resolution = flow_falcon_resolution

    @property
    def flow_falcon_template(self):
        """Gets the flow_falcon_template of this FlowFalconSettings.  # noqa: E501


        :return: The flow_falcon_template of this FlowFalconSettings.  # noqa: E501
        :rtype: FlowFalconTemplateSetting
        """
        return self._flow_falcon_template

    @flow_falcon_template.setter
    def flow_falcon_template(self, flow_falcon_template):
        """Sets the flow_falcon_template of this FlowFalconSettings.


        :param flow_falcon_template: The flow_falcon_template of this FlowFalconSettings.  # noqa: E501
        :type: FlowFalconTemplateSetting
        """
        if flow_falcon_template is None:
            raise ValueError("Invalid value for `flow_falcon_template`, must not be `None`")  # noqa: E501

        self._flow_falcon_template = flow_falcon_template

    @property
    def result_limit(self):
        """Gets the result_limit of this FlowFalconSettings.  # noqa: E501


        :return: The result_limit of this FlowFalconSettings.  # noqa: E501
        :rtype: ResultLimitSetting
        """
        return self._result_limit

    @result_limit.setter
    def result_limit(self, result_limit):
        """Sets the result_limit of this FlowFalconSettings.


        :param result_limit: The result_limit of this FlowFalconSettings.  # noqa: E501
        :type: ResultLimitSetting
        """

        self._result_limit = result_limit

    @property
    def source_fields(self):
        """Gets the source_fields of this FlowFalconSettings.  # noqa: E501


        :return: The source_fields of this FlowFalconSettings.  # noqa: E501
        :rtype: SourceFieldsSetting
        """
        return self._source_fields

    @source_fields.setter
    def source_fields(self, source_fields):
        """Sets the source_fields of this FlowFalconSettings.


        :param source_fields: The source_fields of this FlowFalconSettings.  # noqa: E501
        :type: SourceFieldsSetting
        """

        self._source_fields = source_fields

    @property
    def units(self):
        """Gets the units of this FlowFalconSettings.  # noqa: E501


        :return: The units of this FlowFalconSettings.  # noqa: E501
        :rtype: UnitsSetting
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this FlowFalconSettings.


        :param units: The units of this FlowFalconSettings.  # noqa: E501
        :type: UnitsSetting
        """

        self._units = units

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
        if issubclass(FlowFalconSettings, dict):
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
        if not isinstance(other, FlowFalconSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
