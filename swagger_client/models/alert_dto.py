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

class AlertDto(object):
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
        'threshold_name': 'str',
        'policy_name': 'str',
        'object_name': 'str',
        'indicator_name': 'str',
        'id': 'int',
        'severity': 'int',
        'origin': 'str',
        'device_id': 'int',
        'plugin_name': 'str',
        'object_id': 'int',
        'poll_id': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'clear_time': 'int',
        'message': 'str',
        'number': 'int',
        'ignore_until': 'int',
        'ignore_uid': 'int',
        'ignore_comment': 'str',
        'threshold_id': 'int',
        'alert_flow_falcon': 'AlertFlowFalconDto',
        'closed': 'int',
        'closed_key': 'int',
        'indicator_id': 'int',
        'assigned_to': 'int',
        'comments': 'str',
        'clear_message': 'str',
        'acknowledged_by': 'str',
        'last_processed': 'int',
        'is_maintenance_alert': 'bool'
    }

    attribute_map = {
        'threshold_name': 'thresholdName',
        'policy_name': 'policyName',
        'object_name': 'objectName',
        'indicator_name': 'indicatorName',
        'id': 'id',
        'severity': 'severity',
        'origin': 'origin',
        'device_id': 'deviceId',
        'plugin_name': 'pluginName',
        'object_id': 'objectId',
        'poll_id': 'pollId',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'clear_time': 'clearTime',
        'message': 'message',
        'number': 'number',
        'ignore_until': 'ignoreUntil',
        'ignore_uid': 'ignoreUid',
        'ignore_comment': 'ignoreComment',
        'threshold_id': 'thresholdId',
        'alert_flow_falcon': 'alertFlowFalcon',
        'closed': 'closed',
        'closed_key': 'closedKey',
        'indicator_id': 'indicatorId',
        'assigned_to': 'assignedTo',
        'comments': 'comments',
        'clear_message': 'clearMessage',
        'acknowledged_by': 'acknowledgedBy',
        'last_processed': 'lastProcessed',
        'is_maintenance_alert': 'isMaintenanceAlert'
    }

    def __init__(self, threshold_name=None, policy_name=None, object_name=None, indicator_name=None, id=None, severity=None, origin=None, device_id=None, plugin_name=None, object_id=None, poll_id=None, start_time=None, end_time=None, clear_time=None, message=None, number=None, ignore_until=None, ignore_uid=None, ignore_comment=None, threshold_id=None, alert_flow_falcon=None, closed=None, closed_key=None, indicator_id=None, assigned_to=None, comments=None, clear_message=None, acknowledged_by=None, last_processed=None, is_maintenance_alert=None):  # noqa: E501
        """AlertDto - a model defined in Swagger"""  # noqa: E501
        self._threshold_name = None
        self._policy_name = None
        self._object_name = None
        self._indicator_name = None
        self._id = None
        self._severity = None
        self._origin = None
        self._device_id = None
        self._plugin_name = None
        self._object_id = None
        self._poll_id = None
        self._start_time = None
        self._end_time = None
        self._clear_time = None
        self._message = None
        self._number = None
        self._ignore_until = None
        self._ignore_uid = None
        self._ignore_comment = None
        self._threshold_id = None
        self._alert_flow_falcon = None
        self._closed = None
        self._closed_key = None
        self._indicator_id = None
        self._assigned_to = None
        self._comments = None
        self._clear_message = None
        self._acknowledged_by = None
        self._last_processed = None
        self._is_maintenance_alert = None
        self.discriminator = None
        if threshold_name is not None:
            self.threshold_name = threshold_name
        if policy_name is not None:
            self.policy_name = policy_name
        if object_name is not None:
            self.object_name = object_name
        if indicator_name is not None:
            self.indicator_name = indicator_name
        if id is not None:
            self.id = id
        if severity is not None:
            self.severity = severity
        self.origin = origin
        if device_id is not None:
            self.device_id = device_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if object_id is not None:
            self.object_id = object_id
        if poll_id is not None:
            self.poll_id = poll_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if clear_time is not None:
            self.clear_time = clear_time
        if message is not None:
            self.message = message
        if number is not None:
            self.number = number
        if ignore_until is not None:
            self.ignore_until = ignore_until
        if ignore_uid is not None:
            self.ignore_uid = ignore_uid
        if ignore_comment is not None:
            self.ignore_comment = ignore_comment
        if threshold_id is not None:
            self.threshold_id = threshold_id
        if alert_flow_falcon is not None:
            self.alert_flow_falcon = alert_flow_falcon
        if closed is not None:
            self.closed = closed
        if closed_key is not None:
            self.closed_key = closed_key
        if indicator_id is not None:
            self.indicator_id = indicator_id
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if comments is not None:
            self.comments = comments
        if clear_message is not None:
            self.clear_message = clear_message
        if acknowledged_by is not None:
            self.acknowledged_by = acknowledged_by
        if last_processed is not None:
            self.last_processed = last_processed
        if is_maintenance_alert is not None:
            self.is_maintenance_alert = is_maintenance_alert

    @property
    def threshold_name(self):
        """Gets the threshold_name of this AlertDto.  # noqa: E501


        :return: The threshold_name of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._threshold_name

    @threshold_name.setter
    def threshold_name(self, threshold_name):
        """Sets the threshold_name of this AlertDto.


        :param threshold_name: The threshold_name of this AlertDto.  # noqa: E501
        :type: str
        """

        self._threshold_name = threshold_name

    @property
    def policy_name(self):
        """Gets the policy_name of this AlertDto.  # noqa: E501


        :return: The policy_name of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this AlertDto.


        :param policy_name: The policy_name of this AlertDto.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def object_name(self):
        """Gets the object_name of this AlertDto.  # noqa: E501


        :return: The object_name of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this AlertDto.


        :param object_name: The object_name of this AlertDto.  # noqa: E501
        :type: str
        """

        self._object_name = object_name

    @property
    def indicator_name(self):
        """Gets the indicator_name of this AlertDto.  # noqa: E501


        :return: The indicator_name of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._indicator_name

    @indicator_name.setter
    def indicator_name(self, indicator_name):
        """Sets the indicator_name of this AlertDto.


        :param indicator_name: The indicator_name of this AlertDto.  # noqa: E501
        :type: str
        """

        self._indicator_name = indicator_name

    @property
    def id(self):
        """Gets the id of this AlertDto.  # noqa: E501


        :return: The id of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertDto.


        :param id: The id of this AlertDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def severity(self):
        """Gets the severity of this AlertDto.  # noqa: E501


        :return: The severity of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this AlertDto.


        :param severity: The severity of this AlertDto.  # noqa: E501
        :type: int
        """

        self._severity = severity

    @property
    def origin(self):
        """Gets the origin of this AlertDto.  # noqa: E501


        :return: The origin of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this AlertDto.


        :param origin: The origin of this AlertDto.  # noqa: E501
        :type: str
        """
        if origin is None:
            raise ValueError("Invalid value for `origin`, must not be `None`")  # noqa: E501
        allowed_values = ["system", "trap", "flow"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"  # noqa: E501
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def device_id(self):
        """Gets the device_id of this AlertDto.  # noqa: E501


        :return: The device_id of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this AlertDto.


        :param device_id: The device_id of this AlertDto.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def plugin_name(self):
        """Gets the plugin_name of this AlertDto.  # noqa: E501


        :return: The plugin_name of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this AlertDto.


        :param plugin_name: The plugin_name of this AlertDto.  # noqa: E501
        :type: str
        """

        self._plugin_name = plugin_name

    @property
    def object_id(self):
        """Gets the object_id of this AlertDto.  # noqa: E501


        :return: The object_id of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this AlertDto.


        :param object_id: The object_id of this AlertDto.  # noqa: E501
        :type: int
        """

        self._object_id = object_id

    @property
    def poll_id(self):
        """Gets the poll_id of this AlertDto.  # noqa: E501


        :return: The poll_id of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._poll_id

    @poll_id.setter
    def poll_id(self, poll_id):
        """Sets the poll_id of this AlertDto.


        :param poll_id: The poll_id of this AlertDto.  # noqa: E501
        :type: int
        """

        self._poll_id = poll_id

    @property
    def start_time(self):
        """Gets the start_time of this AlertDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The start_time of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AlertDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param start_time: The start_time of this AlertDto.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this AlertDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The end_time of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AlertDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param end_time: The end_time of this AlertDto.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def clear_time(self):
        """Gets the clear_time of this AlertDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The clear_time of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._clear_time

    @clear_time.setter
    def clear_time(self, clear_time):
        """Sets the clear_time of this AlertDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param clear_time: The clear_time of this AlertDto.  # noqa: E501
        :type: int
        """

        self._clear_time = clear_time

    @property
    def message(self):
        """Gets the message of this AlertDto.  # noqa: E501


        :return: The message of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AlertDto.


        :param message: The message of this AlertDto.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def number(self):
        """Gets the number of this AlertDto.  # noqa: E501


        :return: The number of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this AlertDto.


        :param number: The number of this AlertDto.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def ignore_until(self):
        """Gets the ignore_until of this AlertDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The ignore_until of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._ignore_until

    @ignore_until.setter
    def ignore_until(self, ignore_until):
        """Sets the ignore_until of this AlertDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param ignore_until: The ignore_until of this AlertDto.  # noqa: E501
        :type: int
        """

        self._ignore_until = ignore_until

    @property
    def ignore_uid(self):
        """Gets the ignore_uid of this AlertDto.  # noqa: E501


        :return: The ignore_uid of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._ignore_uid

    @ignore_uid.setter
    def ignore_uid(self, ignore_uid):
        """Sets the ignore_uid of this AlertDto.


        :param ignore_uid: The ignore_uid of this AlertDto.  # noqa: E501
        :type: int
        """

        self._ignore_uid = ignore_uid

    @property
    def ignore_comment(self):
        """Gets the ignore_comment of this AlertDto.  # noqa: E501


        :return: The ignore_comment of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._ignore_comment

    @ignore_comment.setter
    def ignore_comment(self, ignore_comment):
        """Sets the ignore_comment of this AlertDto.


        :param ignore_comment: The ignore_comment of this AlertDto.  # noqa: E501
        :type: str
        """

        self._ignore_comment = ignore_comment

    @property
    def threshold_id(self):
        """Gets the threshold_id of this AlertDto.  # noqa: E501


        :return: The threshold_id of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._threshold_id

    @threshold_id.setter
    def threshold_id(self, threshold_id):
        """Sets the threshold_id of this AlertDto.


        :param threshold_id: The threshold_id of this AlertDto.  # noqa: E501
        :type: int
        """

        self._threshold_id = threshold_id

    @property
    def alert_flow_falcon(self):
        """Gets the alert_flow_falcon of this AlertDto.  # noqa: E501


        :return: The alert_flow_falcon of this AlertDto.  # noqa: E501
        :rtype: AlertFlowFalconDto
        """
        return self._alert_flow_falcon

    @alert_flow_falcon.setter
    def alert_flow_falcon(self, alert_flow_falcon):
        """Sets the alert_flow_falcon of this AlertDto.


        :param alert_flow_falcon: The alert_flow_falcon of this AlertDto.  # noqa: E501
        :type: AlertFlowFalconDto
        """

        self._alert_flow_falcon = alert_flow_falcon

    @property
    def closed(self):
        """Gets the closed of this AlertDto.  # noqa: E501


        :return: The closed of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this AlertDto.


        :param closed: The closed of this AlertDto.  # noqa: E501
        :type: int
        """

        self._closed = closed

    @property
    def closed_key(self):
        """Gets the closed_key of this AlertDto.  # noqa: E501


        :return: The closed_key of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._closed_key

    @closed_key.setter
    def closed_key(self, closed_key):
        """Sets the closed_key of this AlertDto.


        :param closed_key: The closed_key of this AlertDto.  # noqa: E501
        :type: int
        """

        self._closed_key = closed_key

    @property
    def indicator_id(self):
        """Gets the indicator_id of this AlertDto.  # noqa: E501


        :return: The indicator_id of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this AlertDto.


        :param indicator_id: The indicator_id of this AlertDto.  # noqa: E501
        :type: int
        """

        self._indicator_id = indicator_id

    @property
    def assigned_to(self):
        """Gets the assigned_to of this AlertDto.  # noqa: E501


        :return: The assigned_to of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this AlertDto.


        :param assigned_to: The assigned_to of this AlertDto.  # noqa: E501
        :type: int
        """

        self._assigned_to = assigned_to

    @property
    def comments(self):
        """Gets the comments of this AlertDto.  # noqa: E501


        :return: The comments of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this AlertDto.


        :param comments: The comments of this AlertDto.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def clear_message(self):
        """Gets the clear_message of this AlertDto.  # noqa: E501


        :return: The clear_message of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._clear_message

    @clear_message.setter
    def clear_message(self, clear_message):
        """Sets the clear_message of this AlertDto.


        :param clear_message: The clear_message of this AlertDto.  # noqa: E501
        :type: str
        """

        self._clear_message = clear_message

    @property
    def acknowledged_by(self):
        """Gets the acknowledged_by of this AlertDto.  # noqa: E501


        :return: The acknowledged_by of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._acknowledged_by

    @acknowledged_by.setter
    def acknowledged_by(self, acknowledged_by):
        """Sets the acknowledged_by of this AlertDto.


        :param acknowledged_by: The acknowledged_by of this AlertDto.  # noqa: E501
        :type: str
        """

        self._acknowledged_by = acknowledged_by

    @property
    def last_processed(self):
        """Gets the last_processed of this AlertDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The last_processed of this AlertDto.  # noqa: E501
        :rtype: int
        """
        return self._last_processed

    @last_processed.setter
    def last_processed(self, last_processed):
        """Sets the last_processed of this AlertDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param last_processed: The last_processed of this AlertDto.  # noqa: E501
        :type: int
        """

        self._last_processed = last_processed

    @property
    def is_maintenance_alert(self):
        """Gets the is_maintenance_alert of this AlertDto.  # noqa: E501


        :return: The is_maintenance_alert of this AlertDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_maintenance_alert

    @is_maintenance_alert.setter
    def is_maintenance_alert(self, is_maintenance_alert):
        """Sets the is_maintenance_alert of this AlertDto.


        :param is_maintenance_alert: The is_maintenance_alert of this AlertDto.  # noqa: E501
        :type: bool
        """

        self._is_maintenance_alert = is_maintenance_alert

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
        if issubclass(AlertDto, dict):
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
        if not isinstance(other, AlertDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
