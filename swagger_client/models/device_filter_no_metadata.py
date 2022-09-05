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

class DeviceFilterNoMetadata(object):
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
        'ids': 'list[int]',
        'name': 'str',
        'names': 'list[str]',
        'alternate_name': 'str',
        'description': 'str',
        'ip_address': 'str',
        'ip_addresses': 'list[str]',
        'peer_ids': 'list[int]',
        'timezone': 'str',
        'workhours_group_id': 'int',
        'snmp_version': 'int',
        'poll_frequency': 'int',
        'disable_polling': 'bool',
        'disable_concurrent_polling': 'bool',
        'disable_thresholding': 'bool',
        'in_device_group_ids': 'list[int]',
        'not_in_device_group_ids': 'list[int]',
        'plugin_manager_id': 'int',
        'allow_delete': 'bool',
        'num_elements': 'int',
        'is_queued_for_deletion': 'bool',
        'metadata': 'dict(str, str)',
        'plugins': 'list[PluginFilterDtoNoMetadata]',
        'new': 'bool',
        'deleted': 'bool'
    }

    attribute_map = {
        'ids': 'ids',
        'name': 'name',
        'names': 'names',
        'alternate_name': 'alternateName',
        'description': 'description',
        'ip_address': 'ipAddress',
        'ip_addresses': 'ipAddresses',
        'peer_ids': 'peerIds',
        'timezone': 'timezone',
        'workhours_group_id': 'workhoursGroupId',
        'snmp_version': 'snmpVersion',
        'poll_frequency': 'pollFrequency',
        'disable_polling': 'disablePolling',
        'disable_concurrent_polling': 'disableConcurrentPolling',
        'disable_thresholding': 'disableThresholding',
        'in_device_group_ids': 'inDeviceGroupIds',
        'not_in_device_group_ids': 'notInDeviceGroupIds',
        'plugin_manager_id': 'pluginManagerId',
        'allow_delete': 'allowDelete',
        'num_elements': 'numElements',
        'is_queued_for_deletion': 'isQueuedForDeletion',
        'metadata': 'metadata',
        'plugins': 'plugins',
        'new': 'new',
        'deleted': 'deleted'
    }

    def __init__(self, ids=None, name=None, names=None, alternate_name=None, description=None, ip_address=None, ip_addresses=None, peer_ids=None, timezone=None, workhours_group_id=None, snmp_version=None, poll_frequency=None, disable_polling=None, disable_concurrent_polling=None, disable_thresholding=None, in_device_group_ids=None, not_in_device_group_ids=None, plugin_manager_id=None, allow_delete=None, num_elements=None, is_queued_for_deletion=None, metadata=None, plugins=None, new=None, deleted=None):  # noqa: E501
        """DeviceFilterNoMetadata - a model defined in Swagger"""  # noqa: E501
        self._ids = None
        self._name = None
        self._names = None
        self._alternate_name = None
        self._description = None
        self._ip_address = None
        self._ip_addresses = None
        self._peer_ids = None
        self._timezone = None
        self._workhours_group_id = None
        self._snmp_version = None
        self._poll_frequency = None
        self._disable_polling = None
        self._disable_concurrent_polling = None
        self._disable_thresholding = None
        self._in_device_group_ids = None
        self._not_in_device_group_ids = None
        self._plugin_manager_id = None
        self._allow_delete = None
        self._num_elements = None
        self._is_queued_for_deletion = None
        self._metadata = None
        self._plugins = None
        self._new = None
        self._deleted = None
        self.discriminator = None
        if ids is not None:
            self.ids = ids
        if name is not None:
            self.name = name
        if names is not None:
            self.names = names
        if alternate_name is not None:
            self.alternate_name = alternate_name
        if description is not None:
            self.description = description
        if ip_address is not None:
            self.ip_address = ip_address
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if peer_ids is not None:
            self.peer_ids = peer_ids
        if timezone is not None:
            self.timezone = timezone
        if workhours_group_id is not None:
            self.workhours_group_id = workhours_group_id
        if snmp_version is not None:
            self.snmp_version = snmp_version
        if poll_frequency is not None:
            self.poll_frequency = poll_frequency
        if disable_polling is not None:
            self.disable_polling = disable_polling
        if disable_concurrent_polling is not None:
            self.disable_concurrent_polling = disable_concurrent_polling
        if disable_thresholding is not None:
            self.disable_thresholding = disable_thresholding
        if in_device_group_ids is not None:
            self.in_device_group_ids = in_device_group_ids
        if not_in_device_group_ids is not None:
            self.not_in_device_group_ids = not_in_device_group_ids
        if plugin_manager_id is not None:
            self.plugin_manager_id = plugin_manager_id
        if allow_delete is not None:
            self.allow_delete = allow_delete
        if num_elements is not None:
            self.num_elements = num_elements
        if is_queued_for_deletion is not None:
            self.is_queued_for_deletion = is_queued_for_deletion
        if metadata is not None:
            self.metadata = metadata
        if plugins is not None:
            self.plugins = plugins
        if new is not None:
            self.new = new
        if deleted is not None:
            self.deleted = deleted

    @property
    def ids(self):
        """Gets the ids of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The ids of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this DeviceFilterNoMetadata.


        :param ids: The ids of this DeviceFilterNoMetadata.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def name(self):
        """Gets the name of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The name of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceFilterNoMetadata.


        :param name: The name of this DeviceFilterNoMetadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def names(self):
        """Gets the names of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The names of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this DeviceFilterNoMetadata.


        :param names: The names of this DeviceFilterNoMetadata.  # noqa: E501
        :type: list[str]
        """

        self._names = names

    @property
    def alternate_name(self):
        """Gets the alternate_name of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The alternate_name of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: str
        """
        return self._alternate_name

    @alternate_name.setter
    def alternate_name(self, alternate_name):
        """Sets the alternate_name of this DeviceFilterNoMetadata.


        :param alternate_name: The alternate_name of this DeviceFilterNoMetadata.  # noqa: E501
        :type: str
        """

        self._alternate_name = alternate_name

    @property
    def description(self):
        """Gets the description of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The description of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceFilterNoMetadata.


        :param description: The description of this DeviceFilterNoMetadata.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip_address(self):
        """Gets the ip_address of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The ip_address of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DeviceFilterNoMetadata.


        :param ip_address: The ip_address of this DeviceFilterNoMetadata.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The ip_addresses of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this DeviceFilterNoMetadata.


        :param ip_addresses: The ip_addresses of this DeviceFilterNoMetadata.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def peer_ids(self):
        """Gets the peer_ids of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The peer_ids of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: list[int]
        """
        return self._peer_ids

    @peer_ids.setter
    def peer_ids(self, peer_ids):
        """Sets the peer_ids of this DeviceFilterNoMetadata.


        :param peer_ids: The peer_ids of this DeviceFilterNoMetadata.  # noqa: E501
        :type: list[int]
        """

        self._peer_ids = peer_ids

    @property
    def timezone(self):
        """Gets the timezone of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The timezone of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this DeviceFilterNoMetadata.


        :param timezone: The timezone of this DeviceFilterNoMetadata.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def workhours_group_id(self):
        """Gets the workhours_group_id of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The workhours_group_id of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: int
        """
        return self._workhours_group_id

    @workhours_group_id.setter
    def workhours_group_id(self, workhours_group_id):
        """Sets the workhours_group_id of this DeviceFilterNoMetadata.


        :param workhours_group_id: The workhours_group_id of this DeviceFilterNoMetadata.  # noqa: E501
        :type: int
        """

        self._workhours_group_id = workhours_group_id

    @property
    def snmp_version(self):
        """Gets the snmp_version of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The snmp_version of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: int
        """
        return self._snmp_version

    @snmp_version.setter
    def snmp_version(self, snmp_version):
        """Sets the snmp_version of this DeviceFilterNoMetadata.


        :param snmp_version: The snmp_version of this DeviceFilterNoMetadata.  # noqa: E501
        :type: int
        """

        self._snmp_version = snmp_version

    @property
    def poll_frequency(self):
        """Gets the poll_frequency of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The poll_frequency of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: int
        """
        return self._poll_frequency

    @poll_frequency.setter
    def poll_frequency(self, poll_frequency):
        """Sets the poll_frequency of this DeviceFilterNoMetadata.


        :param poll_frequency: The poll_frequency of this DeviceFilterNoMetadata.  # noqa: E501
        :type: int
        """

        self._poll_frequency = poll_frequency

    @property
    def disable_polling(self):
        """Gets the disable_polling of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The disable_polling of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._disable_polling

    @disable_polling.setter
    def disable_polling(self, disable_polling):
        """Sets the disable_polling of this DeviceFilterNoMetadata.


        :param disable_polling: The disable_polling of this DeviceFilterNoMetadata.  # noqa: E501
        :type: bool
        """

        self._disable_polling = disable_polling

    @property
    def disable_concurrent_polling(self):
        """Gets the disable_concurrent_polling of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The disable_concurrent_polling of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._disable_concurrent_polling

    @disable_concurrent_polling.setter
    def disable_concurrent_polling(self, disable_concurrent_polling):
        """Sets the disable_concurrent_polling of this DeviceFilterNoMetadata.


        :param disable_concurrent_polling: The disable_concurrent_polling of this DeviceFilterNoMetadata.  # noqa: E501
        :type: bool
        """

        self._disable_concurrent_polling = disable_concurrent_polling

    @property
    def disable_thresholding(self):
        """Gets the disable_thresholding of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The disable_thresholding of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._disable_thresholding

    @disable_thresholding.setter
    def disable_thresholding(self, disable_thresholding):
        """Sets the disable_thresholding of this DeviceFilterNoMetadata.


        :param disable_thresholding: The disable_thresholding of this DeviceFilterNoMetadata.  # noqa: E501
        :type: bool
        """

        self._disable_thresholding = disable_thresholding

    @property
    def in_device_group_ids(self):
        """Gets the in_device_group_ids of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The in_device_group_ids of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: list[int]
        """
        return self._in_device_group_ids

    @in_device_group_ids.setter
    def in_device_group_ids(self, in_device_group_ids):
        """Sets the in_device_group_ids of this DeviceFilterNoMetadata.


        :param in_device_group_ids: The in_device_group_ids of this DeviceFilterNoMetadata.  # noqa: E501
        :type: list[int]
        """

        self._in_device_group_ids = in_device_group_ids

    @property
    def not_in_device_group_ids(self):
        """Gets the not_in_device_group_ids of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The not_in_device_group_ids of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: list[int]
        """
        return self._not_in_device_group_ids

    @not_in_device_group_ids.setter
    def not_in_device_group_ids(self, not_in_device_group_ids):
        """Sets the not_in_device_group_ids of this DeviceFilterNoMetadata.


        :param not_in_device_group_ids: The not_in_device_group_ids of this DeviceFilterNoMetadata.  # noqa: E501
        :type: list[int]
        """

        self._not_in_device_group_ids = not_in_device_group_ids

    @property
    def plugin_manager_id(self):
        """Gets the plugin_manager_id of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The plugin_manager_id of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: int
        """
        return self._plugin_manager_id

    @plugin_manager_id.setter
    def plugin_manager_id(self, plugin_manager_id):
        """Sets the plugin_manager_id of this DeviceFilterNoMetadata.


        :param plugin_manager_id: The plugin_manager_id of this DeviceFilterNoMetadata.  # noqa: E501
        :type: int
        """

        self._plugin_manager_id = plugin_manager_id

    @property
    def allow_delete(self):
        """Gets the allow_delete of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The allow_delete of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._allow_delete

    @allow_delete.setter
    def allow_delete(self, allow_delete):
        """Sets the allow_delete of this DeviceFilterNoMetadata.


        :param allow_delete: The allow_delete of this DeviceFilterNoMetadata.  # noqa: E501
        :type: bool
        """

        self._allow_delete = allow_delete

    @property
    def num_elements(self):
        """Gets the num_elements of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The num_elements of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: int
        """
        return self._num_elements

    @num_elements.setter
    def num_elements(self, num_elements):
        """Sets the num_elements of this DeviceFilterNoMetadata.


        :param num_elements: The num_elements of this DeviceFilterNoMetadata.  # noqa: E501
        :type: int
        """

        self._num_elements = num_elements

    @property
    def is_queued_for_deletion(self):
        """Gets the is_queued_for_deletion of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The is_queued_for_deletion of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_queued_for_deletion

    @is_queued_for_deletion.setter
    def is_queued_for_deletion(self, is_queued_for_deletion):
        """Sets the is_queued_for_deletion of this DeviceFilterNoMetadata.


        :param is_queued_for_deletion: The is_queued_for_deletion of this DeviceFilterNoMetadata.  # noqa: E501
        :type: bool
        """

        self._is_queued_for_deletion = is_queued_for_deletion

    @property
    def metadata(self):
        """Gets the metadata of this DeviceFilterNoMetadata.  # noqa: E501

        Key-value pair, the key is namespaceName.attributeName, e.g. {system}.sysName  # noqa: E501

        :return: The metadata of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DeviceFilterNoMetadata.

        Key-value pair, the key is namespaceName.attributeName, e.g. {system}.sysName  # noqa: E501

        :param metadata: The metadata of this DeviceFilterNoMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def plugins(self):
        """Gets the plugins of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The plugins of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: list[PluginFilterDtoNoMetadata]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this DeviceFilterNoMetadata.


        :param plugins: The plugins of this DeviceFilterNoMetadata.  # noqa: E501
        :type: list[PluginFilterDtoNoMetadata]
        """

        self._plugins = plugins

    @property
    def new(self):
        """Gets the new of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The new of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._new

    @new.setter
    def new(self, new):
        """Sets the new of this DeviceFilterNoMetadata.


        :param new: The new of this DeviceFilterNoMetadata.  # noqa: E501
        :type: bool
        """

        self._new = new

    @property
    def deleted(self):
        """Gets the deleted of this DeviceFilterNoMetadata.  # noqa: E501


        :return: The deleted of this DeviceFilterNoMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DeviceFilterNoMetadata.


        :param deleted: The deleted of this DeviceFilterNoMetadata.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

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
        if issubclass(DeviceFilterNoMetadata, dict):
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
        if not isinstance(other, DeviceFilterNoMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
