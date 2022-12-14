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

class StatusMapAttachmentRequestDto(object):
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
        'resources': 'StatusMapAttachmentResource',
        'visualization': 'StatusMapAttachmentVisualization'
    }

    attribute_map = {
        'name': 'name',
        'resources': 'resources',
        'visualization': 'visualization'
    }

    def __init__(self, name=None, resources=None, visualization=None):  # noqa: E501
        """StatusMapAttachmentRequestDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._resources = None
        self._visualization = None
        self.discriminator = None
        self.name = name
        self.resources = resources
        if visualization is not None:
            self.visualization = visualization

    @property
    def name(self):
        """Gets the name of this StatusMapAttachmentRequestDto.  # noqa: E501


        :return: The name of this StatusMapAttachmentRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StatusMapAttachmentRequestDto.


        :param name: The name of this StatusMapAttachmentRequestDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resources(self):
        """Gets the resources of this StatusMapAttachmentRequestDto.  # noqa: E501


        :return: The resources of this StatusMapAttachmentRequestDto.  # noqa: E501
        :rtype: StatusMapAttachmentResource
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this StatusMapAttachmentRequestDto.


        :param resources: The resources of this StatusMapAttachmentRequestDto.  # noqa: E501
        :type: StatusMapAttachmentResource
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")  # noqa: E501

        self._resources = resources

    @property
    def visualization(self):
        """Gets the visualization of this StatusMapAttachmentRequestDto.  # noqa: E501


        :return: The visualization of this StatusMapAttachmentRequestDto.  # noqa: E501
        :rtype: StatusMapAttachmentVisualization
        """
        return self._visualization

    @visualization.setter
    def visualization(self, visualization):
        """Sets the visualization of this StatusMapAttachmentRequestDto.


        :param visualization: The visualization of this StatusMapAttachmentRequestDto.  # noqa: E501
        :type: StatusMapAttachmentVisualization
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
        if issubclass(StatusMapAttachmentRequestDto, dict):
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
        if not isinstance(other, StatusMapAttachmentRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
