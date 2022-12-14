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

class StatusMapDto(object):
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
        'name': 'str',
        'image_id': 'int',
        'image_mime_type': 'str',
        'image_size': 'int',
        'image_name': 'str',
        'nodes': 'list[NodeDto]',
        'connections': 'list[ConnectionDto]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'image_id': 'imageId',
        'image_mime_type': 'imageMimeType',
        'image_size': 'imageSize',
        'image_name': 'imageName',
        'nodes': 'nodes',
        'connections': 'connections'
    }

    def __init__(self, id=None, name=None, image_id=None, image_mime_type=None, image_size=None, image_name=None, nodes=None, connections=None):  # noqa: E501
        """StatusMapDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._image_id = None
        self._image_mime_type = None
        self._image_size = None
        self._image_name = None
        self._nodes = None
        self._connections = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if image_id is not None:
            self.image_id = image_id
        if image_mime_type is not None:
            self.image_mime_type = image_mime_type
        if image_size is not None:
            self.image_size = image_size
        if image_name is not None:
            self.image_name = image_name
        if nodes is not None:
            self.nodes = nodes
        if connections is not None:
            self.connections = connections

    @property
    def id(self):
        """Gets the id of this StatusMapDto.  # noqa: E501


        :return: The id of this StatusMapDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StatusMapDto.


        :param id: The id of this StatusMapDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StatusMapDto.  # noqa: E501


        :return: The name of this StatusMapDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StatusMapDto.


        :param name: The name of this StatusMapDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def image_id(self):
        """Gets the image_id of this StatusMapDto.  # noqa: E501


        :return: The image_id of this StatusMapDto.  # noqa: E501
        :rtype: int
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this StatusMapDto.


        :param image_id: The image_id of this StatusMapDto.  # noqa: E501
        :type: int
        """

        self._image_id = image_id

    @property
    def image_mime_type(self):
        """Gets the image_mime_type of this StatusMapDto.  # noqa: E501


        :return: The image_mime_type of this StatusMapDto.  # noqa: E501
        :rtype: str
        """
        return self._image_mime_type

    @image_mime_type.setter
    def image_mime_type(self, image_mime_type):
        """Sets the image_mime_type of this StatusMapDto.


        :param image_mime_type: The image_mime_type of this StatusMapDto.  # noqa: E501
        :type: str
        """

        self._image_mime_type = image_mime_type

    @property
    def image_size(self):
        """Gets the image_size of this StatusMapDto.  # noqa: E501


        :return: The image_size of this StatusMapDto.  # noqa: E501
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this StatusMapDto.


        :param image_size: The image_size of this StatusMapDto.  # noqa: E501
        :type: int
        """

        self._image_size = image_size

    @property
    def image_name(self):
        """Gets the image_name of this StatusMapDto.  # noqa: E501


        :return: The image_name of this StatusMapDto.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this StatusMapDto.


        :param image_name: The image_name of this StatusMapDto.  # noqa: E501
        :type: str
        """

        self._image_name = image_name

    @property
    def nodes(self):
        """Gets the nodes of this StatusMapDto.  # noqa: E501


        :return: The nodes of this StatusMapDto.  # noqa: E501
        :rtype: list[NodeDto]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this StatusMapDto.


        :param nodes: The nodes of this StatusMapDto.  # noqa: E501
        :type: list[NodeDto]
        """

        self._nodes = nodes

    @property
    def connections(self):
        """Gets the connections of this StatusMapDto.  # noqa: E501


        :return: The connections of this StatusMapDto.  # noqa: E501
        :rtype: list[ConnectionDto]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this StatusMapDto.


        :param connections: The connections of this StatusMapDto.  # noqa: E501
        :type: list[ConnectionDto]
        """

        self._connections = connections

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
        if issubclass(StatusMapDto, dict):
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
        if not isinstance(other, StatusMapDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
