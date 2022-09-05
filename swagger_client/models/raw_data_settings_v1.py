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

class RawDataSettingsV1(object):
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
        'data_aggregation_setting': 'DataAggregationSetting',
        'raw_data_setting': 'RawDataSettingV1',
        'units_setting': 'UnitsSetting',
        'work_hours_setting': 'WorkHoursSetting'
    }

    attribute_map = {
        'data_aggregation_setting': 'dataAggregationSetting',
        'raw_data_setting': 'rawDataSetting',
        'units_setting': 'unitsSetting',
        'work_hours_setting': 'workHoursSetting'
    }

    def __init__(self, data_aggregation_setting=None, raw_data_setting=None, units_setting=None, work_hours_setting=None):  # noqa: E501
        """RawDataSettingsV1 - a model defined in Swagger"""  # noqa: E501
        self._data_aggregation_setting = None
        self._raw_data_setting = None
        self._units_setting = None
        self._work_hours_setting = None
        self.discriminator = None
        if data_aggregation_setting is not None:
            self.data_aggregation_setting = data_aggregation_setting
        if raw_data_setting is not None:
            self.raw_data_setting = raw_data_setting
        if units_setting is not None:
            self.units_setting = units_setting
        if work_hours_setting is not None:
            self.work_hours_setting = work_hours_setting

    @property
    def data_aggregation_setting(self):
        """Gets the data_aggregation_setting of this RawDataSettingsV1.  # noqa: E501


        :return: The data_aggregation_setting of this RawDataSettingsV1.  # noqa: E501
        :rtype: DataAggregationSetting
        """
        return self._data_aggregation_setting

    @data_aggregation_setting.setter
    def data_aggregation_setting(self, data_aggregation_setting):
        """Sets the data_aggregation_setting of this RawDataSettingsV1.


        :param data_aggregation_setting: The data_aggregation_setting of this RawDataSettingsV1.  # noqa: E501
        :type: DataAggregationSetting
        """

        self._data_aggregation_setting = data_aggregation_setting

    @property
    def raw_data_setting(self):
        """Gets the raw_data_setting of this RawDataSettingsV1.  # noqa: E501


        :return: The raw_data_setting of this RawDataSettingsV1.  # noqa: E501
        :rtype: RawDataSettingV1
        """
        return self._raw_data_setting

    @raw_data_setting.setter
    def raw_data_setting(self, raw_data_setting):
        """Sets the raw_data_setting of this RawDataSettingsV1.


        :param raw_data_setting: The raw_data_setting of this RawDataSettingsV1.  # noqa: E501
        :type: RawDataSettingV1
        """

        self._raw_data_setting = raw_data_setting

    @property
    def units_setting(self):
        """Gets the units_setting of this RawDataSettingsV1.  # noqa: E501


        :return: The units_setting of this RawDataSettingsV1.  # noqa: E501
        :rtype: UnitsSetting
        """
        return self._units_setting

    @units_setting.setter
    def units_setting(self, units_setting):
        """Sets the units_setting of this RawDataSettingsV1.


        :param units_setting: The units_setting of this RawDataSettingsV1.  # noqa: E501
        :type: UnitsSetting
        """

        self._units_setting = units_setting

    @property
    def work_hours_setting(self):
        """Gets the work_hours_setting of this RawDataSettingsV1.  # noqa: E501


        :return: The work_hours_setting of this RawDataSettingsV1.  # noqa: E501
        :rtype: WorkHoursSetting
        """
        return self._work_hours_setting

    @work_hours_setting.setter
    def work_hours_setting(self, work_hours_setting):
        """Sets the work_hours_setting of this RawDataSettingsV1.


        :param work_hours_setting: The work_hours_setting of this RawDataSettingsV1.  # noqa: E501
        :type: WorkHoursSetting
        """

        self._work_hours_setting = work_hours_setting

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
        if issubclass(RawDataSettingsV1, dict):
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
        if not isinstance(other, RawDataSettingsV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other