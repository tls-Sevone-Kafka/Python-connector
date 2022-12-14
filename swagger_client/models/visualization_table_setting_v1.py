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

class VisualizationTableSettingV1(object):
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
        'data_presentation_setting': 'DataPresentationSetting',
        'column_setting': 'ColumnSetting',
        'csv_setting': 'CSVSetting',
        'table_setting': 'TableSetting'
    }

    attribute_map = {
        'data_presentation_setting': 'dataPresentationSetting',
        'column_setting': 'columnSetting',
        'csv_setting': 'csvSetting',
        'table_setting': 'tableSetting'
    }

    def __init__(self, data_presentation_setting=None, column_setting=None, csv_setting=None, table_setting=None):  # noqa: E501
        """VisualizationTableSettingV1 - a model defined in Swagger"""  # noqa: E501
        self._data_presentation_setting = None
        self._column_setting = None
        self._csv_setting = None
        self._table_setting = None
        self.discriminator = None
        if data_presentation_setting is not None:
            self.data_presentation_setting = data_presentation_setting
        if column_setting is not None:
            self.column_setting = column_setting
        if csv_setting is not None:
            self.csv_setting = csv_setting
        if table_setting is not None:
            self.table_setting = table_setting

    @property
    def data_presentation_setting(self):
        """Gets the data_presentation_setting of this VisualizationTableSettingV1.  # noqa: E501


        :return: The data_presentation_setting of this VisualizationTableSettingV1.  # noqa: E501
        :rtype: DataPresentationSetting
        """
        return self._data_presentation_setting

    @data_presentation_setting.setter
    def data_presentation_setting(self, data_presentation_setting):
        """Sets the data_presentation_setting of this VisualizationTableSettingV1.


        :param data_presentation_setting: The data_presentation_setting of this VisualizationTableSettingV1.  # noqa: E501
        :type: DataPresentationSetting
        """

        self._data_presentation_setting = data_presentation_setting

    @property
    def column_setting(self):
        """Gets the column_setting of this VisualizationTableSettingV1.  # noqa: E501


        :return: The column_setting of this VisualizationTableSettingV1.  # noqa: E501
        :rtype: ColumnSetting
        """
        return self._column_setting

    @column_setting.setter
    def column_setting(self, column_setting):
        """Sets the column_setting of this VisualizationTableSettingV1.


        :param column_setting: The column_setting of this VisualizationTableSettingV1.  # noqa: E501
        :type: ColumnSetting
        """

        self._column_setting = column_setting

    @property
    def csv_setting(self):
        """Gets the csv_setting of this VisualizationTableSettingV1.  # noqa: E501


        :return: The csv_setting of this VisualizationTableSettingV1.  # noqa: E501
        :rtype: CSVSetting
        """
        return self._csv_setting

    @csv_setting.setter
    def csv_setting(self, csv_setting):
        """Sets the csv_setting of this VisualizationTableSettingV1.


        :param csv_setting: The csv_setting of this VisualizationTableSettingV1.  # noqa: E501
        :type: CSVSetting
        """

        self._csv_setting = csv_setting

    @property
    def table_setting(self):
        """Gets the table_setting of this VisualizationTableSettingV1.  # noqa: E501


        :return: The table_setting of this VisualizationTableSettingV1.  # noqa: E501
        :rtype: TableSetting
        """
        return self._table_setting

    @table_setting.setter
    def table_setting(self, table_setting):
        """Sets the table_setting of this VisualizationTableSettingV1.


        :param table_setting: The table_setting of this VisualizationTableSettingV1.  # noqa: E501
        :type: TableSetting
        """

        self._table_setting = table_setting

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
        if issubclass(VisualizationTableSettingV1, dict):
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
        if not isinstance(other, VisualizationTableSettingV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
