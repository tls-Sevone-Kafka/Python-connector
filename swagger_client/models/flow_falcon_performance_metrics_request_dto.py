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

class FlowFalconPerformanceMetricsRequestDto(object):
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
        'resource': 'FlowFalconResource',
        'start_time': 'int',
        'end_time': 'int',
        'flow_falcon': 'FlowFalconSetting',
        'template': 'FlowFalconTemplateSetting',
        'key_fields': 'list[int]',
        'filters': 'list[FlowFalconFilter]',
        'data_columns': 'FlowFalconColumnsSetting',
        'units': 'UnitsSetting',
        'key_lines': 'list[list[str]]'
    }

    attribute_map = {
        'resource': 'resource',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'flow_falcon': 'flowFalcon',
        'template': 'template',
        'key_fields': 'keyFields',
        'filters': 'filters',
        'data_columns': 'dataColumns',
        'units': 'units',
        'key_lines': 'keyLines'
    }

    def __init__(self, resource=None, start_time=None, end_time=None, flow_falcon=None, template=None, key_fields=None, filters=None, data_columns=None, units=None, key_lines=None):  # noqa: E501
        """FlowFalconPerformanceMetricsRequestDto - a model defined in Swagger"""  # noqa: E501
        self._resource = None
        self._start_time = None
        self._end_time = None
        self._flow_falcon = None
        self._template = None
        self._key_fields = None
        self._filters = None
        self._data_columns = None
        self._units = None
        self._key_lines = None
        self.discriminator = None
        if resource is not None:
            self.resource = resource
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if flow_falcon is not None:
            self.flow_falcon = flow_falcon
        if template is not None:
            self.template = template
        if key_fields is not None:
            self.key_fields = key_fields
        if filters is not None:
            self.filters = filters
        if data_columns is not None:
            self.data_columns = data_columns
        if units is not None:
            self.units = units
        if key_lines is not None:
            self.key_lines = key_lines

    @property
    def resource(self):
        """Gets the resource of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The resource of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: FlowFalconResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this FlowFalconPerformanceMetricsRequestDto.


        :param resource: The resource of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: FlowFalconResource
        """

        self._resource = resource

    @property
    def start_time(self):
        """Gets the start_time of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The start_time of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this FlowFalconPerformanceMetricsRequestDto.


        :param start_time: The start_time of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The end_time of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this FlowFalconPerformanceMetricsRequestDto.


        :param end_time: The end_time of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def flow_falcon(self):
        """Gets the flow_falcon of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The flow_falcon of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: FlowFalconSetting
        """
        return self._flow_falcon

    @flow_falcon.setter
    def flow_falcon(self, flow_falcon):
        """Sets the flow_falcon of this FlowFalconPerformanceMetricsRequestDto.


        :param flow_falcon: The flow_falcon of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: FlowFalconSetting
        """

        self._flow_falcon = flow_falcon

    @property
    def template(self):
        """Gets the template of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The template of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: FlowFalconTemplateSetting
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this FlowFalconPerformanceMetricsRequestDto.


        :param template: The template of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: FlowFalconTemplateSetting
        """

        self._template = template

    @property
    def key_fields(self):
        """Gets the key_fields of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The key_fields of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._key_fields

    @key_fields.setter
    def key_fields(self, key_fields):
        """Sets the key_fields of this FlowFalconPerformanceMetricsRequestDto.


        :param key_fields: The key_fields of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: list[int]
        """

        self._key_fields = key_fields

    @property
    def filters(self):
        """Gets the filters of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The filters of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: list[FlowFalconFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this FlowFalconPerformanceMetricsRequestDto.


        :param filters: The filters of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: list[FlowFalconFilter]
        """

        self._filters = filters

    @property
    def data_columns(self):
        """Gets the data_columns of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The data_columns of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: FlowFalconColumnsSetting
        """
        return self._data_columns

    @data_columns.setter
    def data_columns(self, data_columns):
        """Sets the data_columns of this FlowFalconPerformanceMetricsRequestDto.


        :param data_columns: The data_columns of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: FlowFalconColumnsSetting
        """

        self._data_columns = data_columns

    @property
    def units(self):
        """Gets the units of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The units of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: UnitsSetting
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this FlowFalconPerformanceMetricsRequestDto.


        :param units: The units of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: UnitsSetting
        """

        self._units = units

    @property
    def key_lines(self):
        """Gets the key_lines of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501


        :return: The key_lines of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._key_lines

    @key_lines.setter
    def key_lines(self, key_lines):
        """Sets the key_lines of this FlowFalconPerformanceMetricsRequestDto.


        :param key_lines: The key_lines of this FlowFalconPerformanceMetricsRequestDto.  # noqa: E501
        :type: list[list[str]]
        """

        self._key_lines = key_lines

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
        if issubclass(FlowFalconPerformanceMetricsRequestDto, dict):
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
        if not isinstance(other, FlowFalconPerformanceMetricsRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
