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

class AlertFlowFalconDto(object):
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
        'alert_id': 'int',
        'netflow_device_id': 'int',
        'interface_id': 'int',
        'direction_id': 'int',
        'filter_id': 'int',
        'view_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'alert_id': 'alertId',
        'netflow_device_id': 'netflowDeviceId',
        'interface_id': 'interfaceId',
        'direction_id': 'directionId',
        'filter_id': 'filterId',
        'view_id': 'viewId'
    }

    def __init__(self, id=None, alert_id=None, netflow_device_id=None, interface_id=None, direction_id=None, filter_id=None, view_id=None):  # noqa: E501
        """AlertFlowFalconDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._alert_id = None
        self._netflow_device_id = None
        self._interface_id = None
        self._direction_id = None
        self._filter_id = None
        self._view_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if alert_id is not None:
            self.alert_id = alert_id
        if netflow_device_id is not None:
            self.netflow_device_id = netflow_device_id
        if interface_id is not None:
            self.interface_id = interface_id
        if direction_id is not None:
            self.direction_id = direction_id
        if filter_id is not None:
            self.filter_id = filter_id
        if view_id is not None:
            self.view_id = view_id

    @property
    def id(self):
        """Gets the id of this AlertFlowFalconDto.  # noqa: E501


        :return: The id of this AlertFlowFalconDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertFlowFalconDto.


        :param id: The id of this AlertFlowFalconDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def alert_id(self):
        """Gets the alert_id of this AlertFlowFalconDto.  # noqa: E501


        :return: The alert_id of this AlertFlowFalconDto.  # noqa: E501
        :rtype: int
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this AlertFlowFalconDto.


        :param alert_id: The alert_id of this AlertFlowFalconDto.  # noqa: E501
        :type: int
        """

        self._alert_id = alert_id

    @property
    def netflow_device_id(self):
        """Gets the netflow_device_id of this AlertFlowFalconDto.  # noqa: E501


        :return: The netflow_device_id of this AlertFlowFalconDto.  # noqa: E501
        :rtype: int
        """
        return self._netflow_device_id

    @netflow_device_id.setter
    def netflow_device_id(self, netflow_device_id):
        """Sets the netflow_device_id of this AlertFlowFalconDto.


        :param netflow_device_id: The netflow_device_id of this AlertFlowFalconDto.  # noqa: E501
        :type: int
        """

        self._netflow_device_id = netflow_device_id

    @property
    def interface_id(self):
        """Gets the interface_id of this AlertFlowFalconDto.  # noqa: E501


        :return: The interface_id of this AlertFlowFalconDto.  # noqa: E501
        :rtype: int
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """Sets the interface_id of this AlertFlowFalconDto.


        :param interface_id: The interface_id of this AlertFlowFalconDto.  # noqa: E501
        :type: int
        """

        self._interface_id = interface_id

    @property
    def direction_id(self):
        """Gets the direction_id of this AlertFlowFalconDto.  # noqa: E501


        :return: The direction_id of this AlertFlowFalconDto.  # noqa: E501
        :rtype: int
        """
        return self._direction_id

    @direction_id.setter
    def direction_id(self, direction_id):
        """Sets the direction_id of this AlertFlowFalconDto.


        :param direction_id: The direction_id of this AlertFlowFalconDto.  # noqa: E501
        :type: int
        """

        self._direction_id = direction_id

    @property
    def filter_id(self):
        """Gets the filter_id of this AlertFlowFalconDto.  # noqa: E501


        :return: The filter_id of this AlertFlowFalconDto.  # noqa: E501
        :rtype: int
        """
        return self._filter_id

    @filter_id.setter
    def filter_id(self, filter_id):
        """Sets the filter_id of this AlertFlowFalconDto.


        :param filter_id: The filter_id of this AlertFlowFalconDto.  # noqa: E501
        :type: int
        """

        self._filter_id = filter_id

    @property
    def view_id(self):
        """Gets the view_id of this AlertFlowFalconDto.  # noqa: E501


        :return: The view_id of this AlertFlowFalconDto.  # noqa: E501
        :rtype: int
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """Sets the view_id of this AlertFlowFalconDto.


        :param view_id: The view_id of this AlertFlowFalconDto.  # noqa: E501
        :type: int
        """

        self._view_id = view_id

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
        if issubclass(AlertFlowFalconDto, dict):
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
        if not isinstance(other, AlertFlowFalconDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
