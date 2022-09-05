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

class ThresholdAbsoluteTimeDto(object):
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
        'threshold_id': 'int',
        'device_id': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'on_off': 'bool',
        'time_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'threshold_id': 'thresholdId',
        'device_id': 'deviceId',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'on_off': 'onOff',
        'time_zone': 'timeZone'
    }

    def __init__(self, id=None, threshold_id=None, device_id=None, start_time=None, end_time=None, on_off=None, time_zone=None):  # noqa: E501
        """ThresholdAbsoluteTimeDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._threshold_id = None
        self._device_id = None
        self._start_time = None
        self._end_time = None
        self._on_off = None
        self._time_zone = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if threshold_id is not None:
            self.threshold_id = threshold_id
        if device_id is not None:
            self.device_id = device_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if on_off is not None:
            self.on_off = on_off
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def id(self):
        """Gets the id of this ThresholdAbsoluteTimeDto.  # noqa: E501


        :return: The id of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThresholdAbsoluteTimeDto.


        :param id: The id of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def threshold_id(self):
        """Gets the threshold_id of this ThresholdAbsoluteTimeDto.  # noqa: E501


        :return: The threshold_id of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :rtype: int
        """
        return self._threshold_id

    @threshold_id.setter
    def threshold_id(self, threshold_id):
        """Sets the threshold_id of this ThresholdAbsoluteTimeDto.


        :param threshold_id: The threshold_id of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :type: int
        """

        self._threshold_id = threshold_id

    @property
    def device_id(self):
        """Gets the device_id of this ThresholdAbsoluteTimeDto.  # noqa: E501


        :return: The device_id of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ThresholdAbsoluteTimeDto.


        :param device_id: The device_id of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def start_time(self):
        """Gets the start_time of this ThresholdAbsoluteTimeDto.  # noqa: E501


        :return: The start_time of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ThresholdAbsoluteTimeDto.


        :param start_time: The start_time of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ThresholdAbsoluteTimeDto.  # noqa: E501


        :return: The end_time of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ThresholdAbsoluteTimeDto.


        :param end_time: The end_time of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def on_off(self):
        """Gets the on_off of this ThresholdAbsoluteTimeDto.  # noqa: E501


        :return: The on_off of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :rtype: bool
        """
        return self._on_off

    @on_off.setter
    def on_off(self, on_off):
        """Sets the on_off of this ThresholdAbsoluteTimeDto.


        :param on_off: The on_off of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :type: bool
        """

        self._on_off = on_off

    @property
    def time_zone(self):
        """Gets the time_zone of this ThresholdAbsoluteTimeDto.  # noqa: E501


        :return: The time_zone of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ThresholdAbsoluteTimeDto.


        :param time_zone: The time_zone of this ThresholdAbsoluteTimeDto.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

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
        if issubclass(ThresholdAbsoluteTimeDto, dict):
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
        if not isinstance(other, ThresholdAbsoluteTimeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
