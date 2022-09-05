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

class PeerDto(object):
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
        'server_id': 'int',
        'name': 'str',
        'ip': 'str',
        'primary_ip': 'str',
        'secondary_ip': 'str',
        'active_appliance': 'str',
        'disabled': 'bool',
        'virtual_ip': 'str',
        'master': 'bool',
        'capacity': 'int',
        'interface_limit': 'int',
        'flow_limit': 'int',
        'netflow_interface_count': 'int',
        'server_load': 'int',
        'flow_load': 'int',
        'model': 'str',
        'total_load': 'int',
        'total_capacity': 'float',
        'netflow_device_count': 'int',
        'flows_per_second': 'int',
        'processed_flows_per_second': 'int',
        'dropped_flows_per_second': 'int',
        'group_poller_device_count': 'int',
        'group_poller_object_count': 'int',
        'self_mon_device_count': 'int',
        'self_mon_object_count': 'int'
    }

    attribute_map = {
        'server_id': 'serverId',
        'name': 'name',
        'ip': 'ip',
        'primary_ip': 'primaryIp',
        'secondary_ip': 'secondaryIp',
        'active_appliance': 'activeAppliance',
        'disabled': 'disabled',
        'virtual_ip': 'virtualIp',
        'master': 'master',
        'capacity': 'capacity',
        'interface_limit': 'interfaceLimit',
        'flow_limit': 'flowLimit',
        'netflow_interface_count': 'netflowInterfaceCount',
        'server_load': 'serverLoad',
        'flow_load': 'flowLoad',
        'model': 'model',
        'total_load': 'totalLoad',
        'total_capacity': 'totalCapacity',
        'netflow_device_count': 'netflowDeviceCount',
        'flows_per_second': 'flowsPerSecond',
        'processed_flows_per_second': 'processedFlowsPerSecond',
        'dropped_flows_per_second': 'droppedFlowsPerSecond',
        'group_poller_device_count': 'groupPollerDeviceCount',
        'group_poller_object_count': 'groupPollerObjectCount',
        'self_mon_device_count': 'selfMonDeviceCount',
        'self_mon_object_count': 'selfMonObjectCount'
    }

    def __init__(self, server_id=None, name=None, ip=None, primary_ip=None, secondary_ip=None, active_appliance=None, disabled=None, virtual_ip=None, master=None, capacity=None, interface_limit=None, flow_limit=None, netflow_interface_count=None, server_load=None, flow_load=None, model=None, total_load=None, total_capacity=None, netflow_device_count=None, flows_per_second=None, processed_flows_per_second=None, dropped_flows_per_second=None, group_poller_device_count=None, group_poller_object_count=None, self_mon_device_count=None, self_mon_object_count=None):  # noqa: E501
        """PeerDto - a model defined in Swagger"""  # noqa: E501
        self._server_id = None
        self._name = None
        self._ip = None
        self._primary_ip = None
        self._secondary_ip = None
        self._active_appliance = None
        self._disabled = None
        self._virtual_ip = None
        self._master = None
        self._capacity = None
        self._interface_limit = None
        self._flow_limit = None
        self._netflow_interface_count = None
        self._server_load = None
        self._flow_load = None
        self._model = None
        self._total_load = None
        self._total_capacity = None
        self._netflow_device_count = None
        self._flows_per_second = None
        self._processed_flows_per_second = None
        self._dropped_flows_per_second = None
        self._group_poller_device_count = None
        self._group_poller_object_count = None
        self._self_mon_device_count = None
        self._self_mon_object_count = None
        self.discriminator = None
        if server_id is not None:
            self.server_id = server_id
        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip
        if primary_ip is not None:
            self.primary_ip = primary_ip
        if secondary_ip is not None:
            self.secondary_ip = secondary_ip
        if active_appliance is not None:
            self.active_appliance = active_appliance
        if disabled is not None:
            self.disabled = disabled
        if virtual_ip is not None:
            self.virtual_ip = virtual_ip
        if master is not None:
            self.master = master
        if capacity is not None:
            self.capacity = capacity
        if interface_limit is not None:
            self.interface_limit = interface_limit
        if flow_limit is not None:
            self.flow_limit = flow_limit
        if netflow_interface_count is not None:
            self.netflow_interface_count = netflow_interface_count
        if server_load is not None:
            self.server_load = server_load
        if flow_load is not None:
            self.flow_load = flow_load
        if model is not None:
            self.model = model
        if total_load is not None:
            self.total_load = total_load
        if total_capacity is not None:
            self.total_capacity = total_capacity
        if netflow_device_count is not None:
            self.netflow_device_count = netflow_device_count
        if flows_per_second is not None:
            self.flows_per_second = flows_per_second
        if processed_flows_per_second is not None:
            self.processed_flows_per_second = processed_flows_per_second
        if dropped_flows_per_second is not None:
            self.dropped_flows_per_second = dropped_flows_per_second
        if group_poller_device_count is not None:
            self.group_poller_device_count = group_poller_device_count
        if group_poller_object_count is not None:
            self.group_poller_object_count = group_poller_object_count
        if self_mon_device_count is not None:
            self.self_mon_device_count = self_mon_device_count
        if self_mon_object_count is not None:
            self.self_mon_object_count = self_mon_object_count

    @property
    def server_id(self):
        """Gets the server_id of this PeerDto.  # noqa: E501


        :return: The server_id of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this PeerDto.


        :param server_id: The server_id of this PeerDto.  # noqa: E501
        :type: int
        """

        self._server_id = server_id

    @property
    def name(self):
        """Gets the name of this PeerDto.  # noqa: E501


        :return: The name of this PeerDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PeerDto.


        :param name: The name of this PeerDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ip(self):
        """Gets the ip of this PeerDto.  # noqa: E501


        :return: The ip of this PeerDto.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this PeerDto.


        :param ip: The ip of this PeerDto.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def primary_ip(self):
        """Gets the primary_ip of this PeerDto.  # noqa: E501


        :return: The primary_ip of this PeerDto.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """Sets the primary_ip of this PeerDto.


        :param primary_ip: The primary_ip of this PeerDto.  # noqa: E501
        :type: str
        """

        self._primary_ip = primary_ip

    @property
    def secondary_ip(self):
        """Gets the secondary_ip of this PeerDto.  # noqa: E501


        :return: The secondary_ip of this PeerDto.  # noqa: E501
        :rtype: str
        """
        return self._secondary_ip

    @secondary_ip.setter
    def secondary_ip(self, secondary_ip):
        """Sets the secondary_ip of this PeerDto.


        :param secondary_ip: The secondary_ip of this PeerDto.  # noqa: E501
        :type: str
        """

        self._secondary_ip = secondary_ip

    @property
    def active_appliance(self):
        """Gets the active_appliance of this PeerDto.  # noqa: E501


        :return: The active_appliance of this PeerDto.  # noqa: E501
        :rtype: str
        """
        return self._active_appliance

    @active_appliance.setter
    def active_appliance(self, active_appliance):
        """Sets the active_appliance of this PeerDto.


        :param active_appliance: The active_appliance of this PeerDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["PRIMARY", "SECONDARY"]  # noqa: E501
        if active_appliance not in allowed_values:
            raise ValueError(
                "Invalid value for `active_appliance` ({0}), must be one of {1}"  # noqa: E501
                .format(active_appliance, allowed_values)
            )

        self._active_appliance = active_appliance

    @property
    def disabled(self):
        """Gets the disabled of this PeerDto.  # noqa: E501


        :return: The disabled of this PeerDto.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this PeerDto.


        :param disabled: The disabled of this PeerDto.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def virtual_ip(self):
        """Gets the virtual_ip of this PeerDto.  # noqa: E501


        :return: The virtual_ip of this PeerDto.  # noqa: E501
        :rtype: str
        """
        return self._virtual_ip

    @virtual_ip.setter
    def virtual_ip(self, virtual_ip):
        """Sets the virtual_ip of this PeerDto.


        :param virtual_ip: The virtual_ip of this PeerDto.  # noqa: E501
        :type: str
        """

        self._virtual_ip = virtual_ip

    @property
    def master(self):
        """Gets the master of this PeerDto.  # noqa: E501


        :return: The master of this PeerDto.  # noqa: E501
        :rtype: bool
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this PeerDto.


        :param master: The master of this PeerDto.  # noqa: E501
        :type: bool
        """

        self._master = master

    @property
    def capacity(self):
        """Gets the capacity of this PeerDto.  # noqa: E501


        :return: The capacity of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this PeerDto.


        :param capacity: The capacity of this PeerDto.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def interface_limit(self):
        """Gets the interface_limit of this PeerDto.  # noqa: E501


        :return: The interface_limit of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._interface_limit

    @interface_limit.setter
    def interface_limit(self, interface_limit):
        """Sets the interface_limit of this PeerDto.


        :param interface_limit: The interface_limit of this PeerDto.  # noqa: E501
        :type: int
        """

        self._interface_limit = interface_limit

    @property
    def flow_limit(self):
        """Gets the flow_limit of this PeerDto.  # noqa: E501


        :return: The flow_limit of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._flow_limit

    @flow_limit.setter
    def flow_limit(self, flow_limit):
        """Sets the flow_limit of this PeerDto.


        :param flow_limit: The flow_limit of this PeerDto.  # noqa: E501
        :type: int
        """

        self._flow_limit = flow_limit

    @property
    def netflow_interface_count(self):
        """Gets the netflow_interface_count of this PeerDto.  # noqa: E501


        :return: The netflow_interface_count of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._netflow_interface_count

    @netflow_interface_count.setter
    def netflow_interface_count(self, netflow_interface_count):
        """Sets the netflow_interface_count of this PeerDto.


        :param netflow_interface_count: The netflow_interface_count of this PeerDto.  # noqa: E501
        :type: int
        """

        self._netflow_interface_count = netflow_interface_count

    @property
    def server_load(self):
        """Gets the server_load of this PeerDto.  # noqa: E501


        :return: The server_load of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._server_load

    @server_load.setter
    def server_load(self, server_load):
        """Sets the server_load of this PeerDto.


        :param server_load: The server_load of this PeerDto.  # noqa: E501
        :type: int
        """

        self._server_load = server_load

    @property
    def flow_load(self):
        """Gets the flow_load of this PeerDto.  # noqa: E501


        :return: The flow_load of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._flow_load

    @flow_load.setter
    def flow_load(self, flow_load):
        """Sets the flow_load of this PeerDto.


        :param flow_load: The flow_load of this PeerDto.  # noqa: E501
        :type: int
        """

        self._flow_load = flow_load

    @property
    def model(self):
        """Gets the model of this PeerDto.  # noqa: E501


        :return: The model of this PeerDto.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PeerDto.


        :param model: The model of this PeerDto.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def total_load(self):
        """Gets the total_load of this PeerDto.  # noqa: E501


        :return: The total_load of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._total_load

    @total_load.setter
    def total_load(self, total_load):
        """Sets the total_load of this PeerDto.


        :param total_load: The total_load of this PeerDto.  # noqa: E501
        :type: int
        """

        self._total_load = total_load

    @property
    def total_capacity(self):
        """Gets the total_capacity of this PeerDto.  # noqa: E501


        :return: The total_capacity of this PeerDto.  # noqa: E501
        :rtype: float
        """
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, total_capacity):
        """Sets the total_capacity of this PeerDto.


        :param total_capacity: The total_capacity of this PeerDto.  # noqa: E501
        :type: float
        """

        self._total_capacity = total_capacity

    @property
    def netflow_device_count(self):
        """Gets the netflow_device_count of this PeerDto.  # noqa: E501


        :return: The netflow_device_count of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._netflow_device_count

    @netflow_device_count.setter
    def netflow_device_count(self, netflow_device_count):
        """Sets the netflow_device_count of this PeerDto.


        :param netflow_device_count: The netflow_device_count of this PeerDto.  # noqa: E501
        :type: int
        """

        self._netflow_device_count = netflow_device_count

    @property
    def flows_per_second(self):
        """Gets the flows_per_second of this PeerDto.  # noqa: E501


        :return: The flows_per_second of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._flows_per_second

    @flows_per_second.setter
    def flows_per_second(self, flows_per_second):
        """Sets the flows_per_second of this PeerDto.


        :param flows_per_second: The flows_per_second of this PeerDto.  # noqa: E501
        :type: int
        """

        self._flows_per_second = flows_per_second

    @property
    def processed_flows_per_second(self):
        """Gets the processed_flows_per_second of this PeerDto.  # noqa: E501


        :return: The processed_flows_per_second of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._processed_flows_per_second

    @processed_flows_per_second.setter
    def processed_flows_per_second(self, processed_flows_per_second):
        """Sets the processed_flows_per_second of this PeerDto.


        :param processed_flows_per_second: The processed_flows_per_second of this PeerDto.  # noqa: E501
        :type: int
        """

        self._processed_flows_per_second = processed_flows_per_second

    @property
    def dropped_flows_per_second(self):
        """Gets the dropped_flows_per_second of this PeerDto.  # noqa: E501


        :return: The dropped_flows_per_second of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._dropped_flows_per_second

    @dropped_flows_per_second.setter
    def dropped_flows_per_second(self, dropped_flows_per_second):
        """Sets the dropped_flows_per_second of this PeerDto.


        :param dropped_flows_per_second: The dropped_flows_per_second of this PeerDto.  # noqa: E501
        :type: int
        """

        self._dropped_flows_per_second = dropped_flows_per_second

    @property
    def group_poller_device_count(self):
        """Gets the group_poller_device_count of this PeerDto.  # noqa: E501


        :return: The group_poller_device_count of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._group_poller_device_count

    @group_poller_device_count.setter
    def group_poller_device_count(self, group_poller_device_count):
        """Sets the group_poller_device_count of this PeerDto.


        :param group_poller_device_count: The group_poller_device_count of this PeerDto.  # noqa: E501
        :type: int
        """

        self._group_poller_device_count = group_poller_device_count

    @property
    def group_poller_object_count(self):
        """Gets the group_poller_object_count of this PeerDto.  # noqa: E501


        :return: The group_poller_object_count of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._group_poller_object_count

    @group_poller_object_count.setter
    def group_poller_object_count(self, group_poller_object_count):
        """Sets the group_poller_object_count of this PeerDto.


        :param group_poller_object_count: The group_poller_object_count of this PeerDto.  # noqa: E501
        :type: int
        """

        self._group_poller_object_count = group_poller_object_count

    @property
    def self_mon_device_count(self):
        """Gets the self_mon_device_count of this PeerDto.  # noqa: E501


        :return: The self_mon_device_count of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._self_mon_device_count

    @self_mon_device_count.setter
    def self_mon_device_count(self, self_mon_device_count):
        """Sets the self_mon_device_count of this PeerDto.


        :param self_mon_device_count: The self_mon_device_count of this PeerDto.  # noqa: E501
        :type: int
        """

        self._self_mon_device_count = self_mon_device_count

    @property
    def self_mon_object_count(self):
        """Gets the self_mon_object_count of this PeerDto.  # noqa: E501


        :return: The self_mon_object_count of this PeerDto.  # noqa: E501
        :rtype: int
        """
        return self._self_mon_object_count

    @self_mon_object_count.setter
    def self_mon_object_count(self, self_mon_object_count):
        """Sets the self_mon_object_count of this PeerDto.


        :param self_mon_object_count: The self_mon_object_count of this PeerDto.  # noqa: E501
        :type: int
        """

        self._self_mon_object_count = self_mon_object_count

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
        if issubclass(PeerDto, dict):
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
        if not isinstance(other, PeerDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
