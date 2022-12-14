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

class PerformanceMetricsDataDto(object):
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
        'device_id': 'int',
        'device_name': 'str',
        'plugin_id': 'int',
        'plugin_name': 'str',
        'object_id': 'int',
        'object_name': 'str',
        'object_description': 'str',
        'indicator_id': 'int',
        'indicator_name': 'str',
        'indicator_type_id': 'int',
        'indicator_type_description': 'str',
        'frequency': 'float',
        'indicator_data': 'ReportDataDto',
        'baseline_data': 'ReportDataDto',
        'time_over_time_data': 'ReportDataDto',
        'sigma_data': 'ReportDataDto'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'device_name': 'deviceName',
        'plugin_id': 'pluginId',
        'plugin_name': 'pluginName',
        'object_id': 'objectId',
        'object_name': 'objectName',
        'object_description': 'objectDescription',
        'indicator_id': 'indicatorId',
        'indicator_name': 'indicatorName',
        'indicator_type_id': 'indicatorTypeId',
        'indicator_type_description': 'indicatorTypeDescription',
        'frequency': 'frequency',
        'indicator_data': 'indicatorData',
        'baseline_data': 'baselineData',
        'time_over_time_data': 'timeOverTimeData',
        'sigma_data': 'sigmaData'
    }

    def __init__(self, device_id=None, device_name=None, plugin_id=None, plugin_name=None, object_id=None, object_name=None, object_description=None, indicator_id=None, indicator_name=None, indicator_type_id=None, indicator_type_description=None, frequency=None, indicator_data=None, baseline_data=None, time_over_time_data=None, sigma_data=None):  # noqa: E501
        """PerformanceMetricsDataDto - a model defined in Swagger"""  # noqa: E501
        self._device_id = None
        self._device_name = None
        self._plugin_id = None
        self._plugin_name = None
        self._object_id = None
        self._object_name = None
        self._object_description = None
        self._indicator_id = None
        self._indicator_name = None
        self._indicator_type_id = None
        self._indicator_type_description = None
        self._frequency = None
        self._indicator_data = None
        self._baseline_data = None
        self._time_over_time_data = None
        self._sigma_data = None
        self.discriminator = None
        if device_id is not None:
            self.device_id = device_id
        if device_name is not None:
            self.device_name = device_name
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if object_id is not None:
            self.object_id = object_id
        if object_name is not None:
            self.object_name = object_name
        if object_description is not None:
            self.object_description = object_description
        if indicator_id is not None:
            self.indicator_id = indicator_id
        if indicator_name is not None:
            self.indicator_name = indicator_name
        if indicator_type_id is not None:
            self.indicator_type_id = indicator_type_id
        if indicator_type_description is not None:
            self.indicator_type_description = indicator_type_description
        if frequency is not None:
            self.frequency = frequency
        if indicator_data is not None:
            self.indicator_data = indicator_data
        if baseline_data is not None:
            self.baseline_data = baseline_data
        if time_over_time_data is not None:
            self.time_over_time_data = time_over_time_data
        if sigma_data is not None:
            self.sigma_data = sigma_data

    @property
    def device_id(self):
        """Gets the device_id of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The device_id of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this PerformanceMetricsDataDto.


        :param device_id: The device_id of this PerformanceMetricsDataDto.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def device_name(self):
        """Gets the device_name of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The device_name of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this PerformanceMetricsDataDto.


        :param device_name: The device_name of this PerformanceMetricsDataDto.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def plugin_id(self):
        """Gets the plugin_id of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The plugin_id of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: int
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this PerformanceMetricsDataDto.


        :param plugin_id: The plugin_id of this PerformanceMetricsDataDto.  # noqa: E501
        :type: int
        """

        self._plugin_id = plugin_id

    @property
    def plugin_name(self):
        """Gets the plugin_name of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The plugin_name of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this PerformanceMetricsDataDto.


        :param plugin_name: The plugin_name of this PerformanceMetricsDataDto.  # noqa: E501
        :type: str
        """

        self._plugin_name = plugin_name

    @property
    def object_id(self):
        """Gets the object_id of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The object_id of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this PerformanceMetricsDataDto.


        :param object_id: The object_id of this PerformanceMetricsDataDto.  # noqa: E501
        :type: int
        """

        self._object_id = object_id

    @property
    def object_name(self):
        """Gets the object_name of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The object_name of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this PerformanceMetricsDataDto.


        :param object_name: The object_name of this PerformanceMetricsDataDto.  # noqa: E501
        :type: str
        """

        self._object_name = object_name

    @property
    def object_description(self):
        """Gets the object_description of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The object_description of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: str
        """
        return self._object_description

    @object_description.setter
    def object_description(self, object_description):
        """Sets the object_description of this PerformanceMetricsDataDto.


        :param object_description: The object_description of this PerformanceMetricsDataDto.  # noqa: E501
        :type: str
        """

        self._object_description = object_description

    @property
    def indicator_id(self):
        """Gets the indicator_id of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The indicator_id of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: int
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this PerformanceMetricsDataDto.


        :param indicator_id: The indicator_id of this PerformanceMetricsDataDto.  # noqa: E501
        :type: int
        """

        self._indicator_id = indicator_id

    @property
    def indicator_name(self):
        """Gets the indicator_name of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The indicator_name of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: str
        """
        return self._indicator_name

    @indicator_name.setter
    def indicator_name(self, indicator_name):
        """Sets the indicator_name of this PerformanceMetricsDataDto.


        :param indicator_name: The indicator_name of this PerformanceMetricsDataDto.  # noqa: E501
        :type: str
        """

        self._indicator_name = indicator_name

    @property
    def indicator_type_id(self):
        """Gets the indicator_type_id of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The indicator_type_id of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: int
        """
        return self._indicator_type_id

    @indicator_type_id.setter
    def indicator_type_id(self, indicator_type_id):
        """Sets the indicator_type_id of this PerformanceMetricsDataDto.


        :param indicator_type_id: The indicator_type_id of this PerformanceMetricsDataDto.  # noqa: E501
        :type: int
        """

        self._indicator_type_id = indicator_type_id

    @property
    def indicator_type_description(self):
        """Gets the indicator_type_description of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The indicator_type_description of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: str
        """
        return self._indicator_type_description

    @indicator_type_description.setter
    def indicator_type_description(self, indicator_type_description):
        """Sets the indicator_type_description of this PerformanceMetricsDataDto.


        :param indicator_type_description: The indicator_type_description of this PerformanceMetricsDataDto.  # noqa: E501
        :type: str
        """

        self._indicator_type_description = indicator_type_description

    @property
    def frequency(self):
        """Gets the frequency of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The frequency of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: float
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this PerformanceMetricsDataDto.


        :param frequency: The frequency of this PerformanceMetricsDataDto.  # noqa: E501
        :type: float
        """

        self._frequency = frequency

    @property
    def indicator_data(self):
        """Gets the indicator_data of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The indicator_data of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: ReportDataDto
        """
        return self._indicator_data

    @indicator_data.setter
    def indicator_data(self, indicator_data):
        """Sets the indicator_data of this PerformanceMetricsDataDto.


        :param indicator_data: The indicator_data of this PerformanceMetricsDataDto.  # noqa: E501
        :type: ReportDataDto
        """

        self._indicator_data = indicator_data

    @property
    def baseline_data(self):
        """Gets the baseline_data of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The baseline_data of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: ReportDataDto
        """
        return self._baseline_data

    @baseline_data.setter
    def baseline_data(self, baseline_data):
        """Sets the baseline_data of this PerformanceMetricsDataDto.


        :param baseline_data: The baseline_data of this PerformanceMetricsDataDto.  # noqa: E501
        :type: ReportDataDto
        """

        self._baseline_data = baseline_data

    @property
    def time_over_time_data(self):
        """Gets the time_over_time_data of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The time_over_time_data of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: ReportDataDto
        """
        return self._time_over_time_data

    @time_over_time_data.setter
    def time_over_time_data(self, time_over_time_data):
        """Sets the time_over_time_data of this PerformanceMetricsDataDto.


        :param time_over_time_data: The time_over_time_data of this PerformanceMetricsDataDto.  # noqa: E501
        :type: ReportDataDto
        """

        self._time_over_time_data = time_over_time_data

    @property
    def sigma_data(self):
        """Gets the sigma_data of this PerformanceMetricsDataDto.  # noqa: E501


        :return: The sigma_data of this PerformanceMetricsDataDto.  # noqa: E501
        :rtype: ReportDataDto
        """
        return self._sigma_data

    @sigma_data.setter
    def sigma_data(self, sigma_data):
        """Sets the sigma_data of this PerformanceMetricsDataDto.


        :param sigma_data: The sigma_data of this PerformanceMetricsDataDto.  # noqa: E501
        :type: ReportDataDto
        """

        self._sigma_data = sigma_data

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
        if issubclass(PerformanceMetricsDataDto, dict):
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
        if not isinstance(other, PerformanceMetricsDataDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
