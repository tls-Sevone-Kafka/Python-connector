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

class FlowFalconSettingsV1(object):
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
        'flow_falcon_setting': 'FlowFalconSettingV1',
        'flow_falcon_resolution_settings': 'FlowFalconResolutionSetting',
        'flow_falcon_template_setting': 'FlowFalconTemplateSettingV1',
        'result_limit_setting': 'ResultLimitSettingV1',
        'source_fields': 'SourceFieldsSetting',
        'units_setting': 'UnitsSetting'
    }

    attribute_map = {
        'flow_falcon_setting': 'flowFalconSetting',
        'flow_falcon_resolution_settings': 'flowFalconResolutionSettings',
        'flow_falcon_template_setting': 'flowFalconTemplateSetting',
        'result_limit_setting': 'resultLimitSetting',
        'source_fields': 'sourceFields',
        'units_setting': 'unitsSetting'
    }

    def __init__(self, flow_falcon_setting=None, flow_falcon_resolution_settings=None, flow_falcon_template_setting=None, result_limit_setting=None, source_fields=None, units_setting=None):  # noqa: E501
        """FlowFalconSettingsV1 - a model defined in Swagger"""  # noqa: E501
        self._flow_falcon_setting = None
        self._flow_falcon_resolution_settings = None
        self._flow_falcon_template_setting = None
        self._result_limit_setting = None
        self._source_fields = None
        self._units_setting = None
        self.discriminator = None
        if flow_falcon_setting is not None:
            self.flow_falcon_setting = flow_falcon_setting
        if flow_falcon_resolution_settings is not None:
            self.flow_falcon_resolution_settings = flow_falcon_resolution_settings
        if flow_falcon_template_setting is not None:
            self.flow_falcon_template_setting = flow_falcon_template_setting
        if result_limit_setting is not None:
            self.result_limit_setting = result_limit_setting
        if source_fields is not None:
            self.source_fields = source_fields
        if units_setting is not None:
            self.units_setting = units_setting

    @property
    def flow_falcon_setting(self):
        """Gets the flow_falcon_setting of this FlowFalconSettingsV1.  # noqa: E501


        :return: The flow_falcon_setting of this FlowFalconSettingsV1.  # noqa: E501
        :rtype: FlowFalconSettingV1
        """
        return self._flow_falcon_setting

    @flow_falcon_setting.setter
    def flow_falcon_setting(self, flow_falcon_setting):
        """Sets the flow_falcon_setting of this FlowFalconSettingsV1.


        :param flow_falcon_setting: The flow_falcon_setting of this FlowFalconSettingsV1.  # noqa: E501
        :type: FlowFalconSettingV1
        """

        self._flow_falcon_setting = flow_falcon_setting

    @property
    def flow_falcon_resolution_settings(self):
        """Gets the flow_falcon_resolution_settings of this FlowFalconSettingsV1.  # noqa: E501


        :return: The flow_falcon_resolution_settings of this FlowFalconSettingsV1.  # noqa: E501
        :rtype: FlowFalconResolutionSetting
        """
        return self._flow_falcon_resolution_settings

    @flow_falcon_resolution_settings.setter
    def flow_falcon_resolution_settings(self, flow_falcon_resolution_settings):
        """Sets the flow_falcon_resolution_settings of this FlowFalconSettingsV1.


        :param flow_falcon_resolution_settings: The flow_falcon_resolution_settings of this FlowFalconSettingsV1.  # noqa: E501
        :type: FlowFalconResolutionSetting
        """

        self._flow_falcon_resolution_settings = flow_falcon_resolution_settings

    @property
    def flow_falcon_template_setting(self):
        """Gets the flow_falcon_template_setting of this FlowFalconSettingsV1.  # noqa: E501


        :return: The flow_falcon_template_setting of this FlowFalconSettingsV1.  # noqa: E501
        :rtype: FlowFalconTemplateSettingV1
        """
        return self._flow_falcon_template_setting

    @flow_falcon_template_setting.setter
    def flow_falcon_template_setting(self, flow_falcon_template_setting):
        """Sets the flow_falcon_template_setting of this FlowFalconSettingsV1.


        :param flow_falcon_template_setting: The flow_falcon_template_setting of this FlowFalconSettingsV1.  # noqa: E501
        :type: FlowFalconTemplateSettingV1
        """

        self._flow_falcon_template_setting = flow_falcon_template_setting

    @property
    def result_limit_setting(self):
        """Gets the result_limit_setting of this FlowFalconSettingsV1.  # noqa: E501


        :return: The result_limit_setting of this FlowFalconSettingsV1.  # noqa: E501
        :rtype: ResultLimitSettingV1
        """
        return self._result_limit_setting

    @result_limit_setting.setter
    def result_limit_setting(self, result_limit_setting):
        """Sets the result_limit_setting of this FlowFalconSettingsV1.


        :param result_limit_setting: The result_limit_setting of this FlowFalconSettingsV1.  # noqa: E501
        :type: ResultLimitSettingV1
        """

        self._result_limit_setting = result_limit_setting

    @property
    def source_fields(self):
        """Gets the source_fields of this FlowFalconSettingsV1.  # noqa: E501


        :return: The source_fields of this FlowFalconSettingsV1.  # noqa: E501
        :rtype: SourceFieldsSetting
        """
        return self._source_fields

    @source_fields.setter
    def source_fields(self, source_fields):
        """Sets the source_fields of this FlowFalconSettingsV1.


        :param source_fields: The source_fields of this FlowFalconSettingsV1.  # noqa: E501
        :type: SourceFieldsSetting
        """

        self._source_fields = source_fields

    @property
    def units_setting(self):
        """Gets the units_setting of this FlowFalconSettingsV1.  # noqa: E501


        :return: The units_setting of this FlowFalconSettingsV1.  # noqa: E501
        :rtype: UnitsSetting
        """
        return self._units_setting

    @units_setting.setter
    def units_setting(self, units_setting):
        """Sets the units_setting of this FlowFalconSettingsV1.


        :param units_setting: The units_setting of this FlowFalconSettingsV1.  # noqa: E501
        :type: UnitsSetting
        """

        self._units_setting = units_setting

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
        if issubclass(FlowFalconSettingsV1, dict):
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
        if not isinstance(other, FlowFalconSettingsV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
