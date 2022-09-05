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

class PagerDeviceGroupDtoNoMembers(object):
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
        'total_elements': 'int',
        'content': 'list[DeviceGroupDtoNoMembers]',
        'page_number': 'int',
        'page_size': 'int',
        'total_pages': 'int'
    }

    attribute_map = {
        'total_elements': 'totalElements',
        'content': 'content',
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'total_pages': 'totalPages'
    }

    def __init__(self, total_elements=None, content=None, page_number=None, page_size=None, total_pages=None):  # noqa: E501
        """PagerDeviceGroupDtoNoMembers - a model defined in Swagger"""  # noqa: E501
        self._total_elements = None
        self._content = None
        self._page_number = None
        self._page_size = None
        self._total_pages = None
        self.discriminator = None
        if total_elements is not None:
            self.total_elements = total_elements
        if content is not None:
            self.content = content
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if total_pages is not None:
            self.total_pages = total_pages

    @property
    def total_elements(self):
        """Gets the total_elements of this PagerDeviceGroupDtoNoMembers.  # noqa: E501


        :return: The total_elements of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this PagerDeviceGroupDtoNoMembers.


        :param total_elements: The total_elements of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :type: int
        """

        self._total_elements = total_elements

    @property
    def content(self):
        """Gets the content of this PagerDeviceGroupDtoNoMembers.  # noqa: E501


        :return: The content of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :rtype: list[DeviceGroupDtoNoMembers]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PagerDeviceGroupDtoNoMembers.


        :param content: The content of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :type: list[DeviceGroupDtoNoMembers]
        """

        self._content = content

    @property
    def page_number(self):
        """Gets the page_number of this PagerDeviceGroupDtoNoMembers.  # noqa: E501


        :return: The page_number of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this PagerDeviceGroupDtoNoMembers.


        :param page_number: The page_number of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this PagerDeviceGroupDtoNoMembers.  # noqa: E501


        :return: The page_size of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PagerDeviceGroupDtoNoMembers.


        :param page_size: The page_size of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_pages(self):
        """Gets the total_pages of this PagerDeviceGroupDtoNoMembers.  # noqa: E501


        :return: The total_pages of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PagerDeviceGroupDtoNoMembers.


        :param total_pages: The total_pages of this PagerDeviceGroupDtoNoMembers.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

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
        if issubclass(PagerDeviceGroupDtoNoMembers, dict):
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
        if not isinstance(other, PagerDeviceGroupDtoNoMembers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
