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

class AlertAttachmentDto(object):
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
        'aggregation': 'str',
        'resources': 'list[AlertAttachmentResource]',
        'time': 'TimeSettings',
        'settings': 'AlertAttachmentSettings',
        'visualization': 'AlertAttachmentVisualization',
        'filters': 'AttachmentFilters'
    }

    attribute_map = {
        'name': 'name',
        'aggregation': 'aggregation',
        'resources': 'resources',
        'time': 'time',
        'settings': 'settings',
        'visualization': 'visualization',
        'filters': 'filters'
    }

    def __init__(self, name=None, aggregation=None, resources=None, time=None, settings=None, visualization=None, filters=None):  # noqa: E501
        """AlertAttachmentDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._aggregation = None
        self._resources = None
        self._time = None
        self._settings = None
        self._visualization = None
        self._filters = None
        self.discriminator = None
        self.name = name
        if aggregation is not None:
            self.aggregation = aggregation
        if resources is not None:
            self.resources = resources
        if time is not None:
            self.time = time
        if settings is not None:
            self.settings = settings
        if visualization is not None:
            self.visualization = visualization
        if filters is not None:
            self.filters = filters

    @property
    def name(self):
        """Gets the name of this AlertAttachmentDto.  # noqa: E501


        :return: The name of this AlertAttachmentDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertAttachmentDto.


        :param name: The name of this AlertAttachmentDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def aggregation(self):
        """Gets the aggregation of this AlertAttachmentDto.  # noqa: E501


        :return: The aggregation of this AlertAttachmentDto.  # noqa: E501
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this AlertAttachmentDto.


        :param aggregation: The aggregation of this AlertAttachmentDto.  # noqa: E501
        :type: str
        """

        self._aggregation = aggregation

    @property
    def resources(self):
        """Gets the resources of this AlertAttachmentDto.  # noqa: E501


        :return: The resources of this AlertAttachmentDto.  # noqa: E501
        :rtype: list[AlertAttachmentResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this AlertAttachmentDto.


        :param resources: The resources of this AlertAttachmentDto.  # noqa: E501
        :type: list[AlertAttachmentResource]
        """

        self._resources = resources

    @property
    def time(self):
        """Gets the time of this AlertAttachmentDto.  # noqa: E501


        :return: The time of this AlertAttachmentDto.  # noqa: E501
        :rtype: TimeSettings
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this AlertAttachmentDto.


        :param time: The time of this AlertAttachmentDto.  # noqa: E501
        :type: TimeSettings
        """

        self._time = time

    @property
    def settings(self):
        """Gets the settings of this AlertAttachmentDto.  # noqa: E501


        :return: The settings of this AlertAttachmentDto.  # noqa: E501
        :rtype: AlertAttachmentSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this AlertAttachmentDto.


        :param settings: The settings of this AlertAttachmentDto.  # noqa: E501
        :type: AlertAttachmentSettings
        """

        self._settings = settings

    @property
    def visualization(self):
        """Gets the visualization of this AlertAttachmentDto.  # noqa: E501


        :return: The visualization of this AlertAttachmentDto.  # noqa: E501
        :rtype: AlertAttachmentVisualization
        """
        return self._visualization

    @visualization.setter
    def visualization(self, visualization):
        """Sets the visualization of this AlertAttachmentDto.


        :param visualization: The visualization of this AlertAttachmentDto.  # noqa: E501
        :type: AlertAttachmentVisualization
        """

        self._visualization = visualization

    @property
    def filters(self):
        """Gets the filters of this AlertAttachmentDto.  # noqa: E501


        :return: The filters of this AlertAttachmentDto.  # noqa: E501
        :rtype: AttachmentFilters
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this AlertAttachmentDto.


        :param filters: The filters of this AlertAttachmentDto.  # noqa: E501
        :type: AttachmentFilters
        """

        self._filters = filters

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
        if issubclass(AlertAttachmentDto, dict):
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
        if not isinstance(other, AlertAttachmentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
