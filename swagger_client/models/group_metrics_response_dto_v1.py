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

class GroupMetricsResponseDtoV1(object):
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
        'name': 'str',
        'resource': 'GroupMetricsResourceV1',
        'time_settings': 'TimeSettingV1',
        'settings': 'GroupMetricsSettingsDtoV1',
        'visualization': 'GroupMetricsVisualizationV1'
    }

    attribute_map = {
        'name': 'name',
        'resource': 'resource',
        'time_settings': 'timeSettings',
        'settings': 'settings',
        'visualization': 'visualization'
    }

    def __init__(self, name=None, resource=None, time_settings=None, settings=None, visualization=None):  # noqa: E501
        """GroupMetricsResponseDtoV1 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._resource = None
        self._time_settings = None
        self._settings = None
        self._visualization = None
        self.discriminator = None
        self.name = name
        if resource is not None:
            self.resource = resource
        if time_settings is not None:
            self.time_settings = time_settings
        if settings is not None:
            self.settings = settings
        if visualization is not None:
            self.visualization = visualization

    @property
    def name(self):
        """Gets the name of this GroupMetricsResponseDtoV1.  # noqa: E501


        :return: The name of this GroupMetricsResponseDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupMetricsResponseDtoV1.


        :param name: The name of this GroupMetricsResponseDtoV1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resource(self):
        """Gets the resource of this GroupMetricsResponseDtoV1.  # noqa: E501


        :return: The resource of this GroupMetricsResponseDtoV1.  # noqa: E501
        :rtype: GroupMetricsResourceV1
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this GroupMetricsResponseDtoV1.


        :param resource: The resource of this GroupMetricsResponseDtoV1.  # noqa: E501
        :type: GroupMetricsResourceV1
        """

        self._resource = resource

    @property
    def time_settings(self):
        """Gets the time_settings of this GroupMetricsResponseDtoV1.  # noqa: E501


        :return: The time_settings of this GroupMetricsResponseDtoV1.  # noqa: E501
        :rtype: TimeSettingV1
        """
        return self._time_settings

    @time_settings.setter
    def time_settings(self, time_settings):
        """Sets the time_settings of this GroupMetricsResponseDtoV1.


        :param time_settings: The time_settings of this GroupMetricsResponseDtoV1.  # noqa: E501
        :type: TimeSettingV1
        """

        self._time_settings = time_settings

    @property
    def settings(self):
        """Gets the settings of this GroupMetricsResponseDtoV1.  # noqa: E501


        :return: The settings of this GroupMetricsResponseDtoV1.  # noqa: E501
        :rtype: GroupMetricsSettingsDtoV1
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this GroupMetricsResponseDtoV1.


        :param settings: The settings of this GroupMetricsResponseDtoV1.  # noqa: E501
        :type: GroupMetricsSettingsDtoV1
        """

        self._settings = settings

    @property
    def visualization(self):
        """Gets the visualization of this GroupMetricsResponseDtoV1.  # noqa: E501


        :return: The visualization of this GroupMetricsResponseDtoV1.  # noqa: E501
        :rtype: GroupMetricsVisualizationV1
        """
        return self._visualization

    @visualization.setter
    def visualization(self, visualization):
        """Sets the visualization of this GroupMetricsResponseDtoV1.


        :param visualization: The visualization of this GroupMetricsResponseDtoV1.  # noqa: E501
        :type: GroupMetricsVisualizationV1
        """

        self._visualization = visualization

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
        if issubclass(GroupMetricsResponseDtoV1, dict):
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
        if not isinstance(other, GroupMetricsResponseDtoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
