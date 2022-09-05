# coding: utf-8

"""
    SevOne API Documentation

    Supported endpoints by the new RESTful API  # noqa: E501

    OpenAPI spec version: 2.1.42, Hash: 719f8be
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.net_flow_api import NetFlowApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNetFlowApi(unittest.TestCase):
    """NetFlowApi unit test stubs"""

    def setUp(self):
        self.api = NetFlowApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_application(self):
        """Test case for create_application

        Create application  # noqa: E501
        """
        pass

    def test_create_device_mappings(self):
        """Test case for create_device_mappings

        Create device mapping  # noqa: E501
        """
        pass

    def test_create_filter(self):
        """Test case for create_filter

        Create Netflow filters  # noqa: E501
        """
        pass

    def test_create_filter_entities(self):
        """Test case for create_filter_entities

        Create Netflow filters rules  # noqa: E501
        """
        pass

    def test_create_mappings(self):
        """Test case for create_mappings

        Create object mapping  # noqa: E501
        """
        pass

    def test_create_service_profile(self):
        """Test case for create_service_profile

        Create service profile  # noqa: E501
        """
        pass

    def test_create_subnet(self):
        """Test case for create_subnet

        Create subnet  # noqa: E501
        """
        pass

    def test_create_subnet_category(self):
        """Test case for create_subnet_category

        Create Network Segment  # noqa: E501
        """
        pass

    def test_delet_subnet_by_id(self):
        """Test case for delet_subnet_by_id

        Delete subnet  # noqa: E501
        """
        pass

    def test_delet_subnet_category_by_id(self):
        """Test case for delet_subnet_category_by_id

        Delete Network Segment  # noqa: E501
        """
        pass

    def test_delete_application(self):
        """Test case for delete_application

        Delete application  # noqa: E501
        """
        pass

    def test_delete_device_mapping_by_id(self):
        """Test case for delete_device_mapping_by_id

        Delete Device Mapping by Id  # noqa: E501
        """
        pass

    def test_delete_filter(self):
        """Test case for delete_filter

        Delete Netflow filter  # noqa: E501
        """
        pass

    def test_delete_filter_entity(self):
        """Test case for delete_filter_entity

        Delete Netflow filter rule  # noqa: E501
        """
        pass

    def test_delete_interface(self):
        """Test case for delete_interface

        Delete interface by deviceId, interfaceId, direction.  # noqa: E501
        """
        pass

    def test_delete_object_mapping_by_id(self):
        """Test case for delete_object_mapping_by_id

        Delete Object Mapping by Id  # noqa: E501
        """
        pass

    def test_delete_service_profile(self):
        """Test case for delete_service_profile

        Delete service profile  # noqa: E501
        """
        pass

    def test_filter_net_flow_device_interfaces(self):
        """Test case for filter_net_flow_device_interfaces

        Get NetFlow device interfaces  # noqa: E501
        """
        pass

    def test_filter_net_flow_devices(self):
        """Test case for filter_net_flow_devices

        Get all NetFlow devices  # noqa: E501
        """
        pass

    def test_filter_netflow_fields(self):
        """Test case for filter_netflow_fields

        Filter netflow fields  # noqa: E501
        """
        pass

    def test_filter_netflow_views(self):
        """Test case for filter_netflow_views

        Filter views  # noqa: E501
        """
        pass

    def test_filter_view_indicators(self):
        """Test case for filter_view_indicators

        Filter netflow view fields  # noqa: E501
        """
        pass

    def test_get_device_mappings(self):
        """Test case for get_device_mappings

        Get flow interface to device mappings  # noqa: E501
        """
        pass

    def test_get_directions(self):
        """Test case for get_directions

        Get directions by NetFlow device id and interface id  # noqa: E501
        """
        pass

    def test_get_filter_by_id(self):
        """Test case for get_filter_by_id

        Get Netflow filters  # noqa: E501
        """
        pass

    def test_get_filter_entities_by_id(self):
        """Test case for get_filter_entities_by_id

        Get Netflow filter rules  # noqa: E501
        """
        pass

    def test_get_filters(self):
        """Test case for get_filters

        Get Netflow filters  # noqa: E501
        """
        pass

    def test_get_interfaces(self):
        """Test case for get_interfaces

        Get interfaces by NetFlow device id  # noqa: E501
        """
        pass

    def test_get_mapping_by_indicator(self):
        """Test case for get_mapping_by_indicator

        Get flow interface to device indicator mapping by indicators  # noqa: E501
        """
        pass

    def test_get_mapping_by_interfaces(self):
        """Test case for get_mapping_by_interfaces

        Get flow interface to device indicator mapping by interface  # noqa: E501
        """
        pass

    def test_get_mappings(self):
        """Test case for get_mappings

        Get flow interface to device indicator mappings  # noqa: E501
        """
        pass

    def test_get_net_flow_devices(self):
        """Test case for get_net_flow_devices

        Get all NetFlow devices  # noqa: E501
        """
        pass

    def test_get_net_flow_modes(self):
        """Test case for get_net_flow_modes

        Get the status of NetFlow settings  # noqa: E501
        """
        pass

    def test_get_netflow_categories(self):
        """Test case for get_netflow_categories

        Get netflow view categories  # noqa: E501
        """
        pass

    def test_get_netflow_fields(self):
        """Test case for get_netflow_fields

        Get netflow fields  # noqa: E501
        """
        pass

    def test_get_network_segments(self):
        """Test case for get_network_segments

        Get Network Segments  # noqa: E501
        """
        pass

    def test_get_protocols(self):
        """Test case for get_protocols

        Get protocols  # noqa: E501
        """
        pass

    def test_get_report_columns(self):
        """Test case for get_report_columns

        """
        pass

    def test_get_service_profiles(self):
        """Test case for get_service_profiles

        Get service profiles  # noqa: E501
        """
        pass

    def test_get_services_by_port(self):
        """Test case for get_services_by_port

        Get services by port  # noqa: E501
        """
        pass

    def test_get_services_by_service_profile_id(self):
        """Test case for get_services_by_service_profile_id

        Get services by service profile Id  # noqa: E501
        """
        pass

    def test_get_subnet_category_by_id(self):
        """Test case for get_subnet_category_by_id

        Get Network Segment By Id  # noqa: E501
        """
        pass

    def test_get_subnets(self):
        """Test case for get_subnets

        Get subnets  # noqa: E501
        """
        pass

    def test_get_subnets_by_category_id(self):
        """Test case for get_subnets_by_category_id

        Get subnets  # noqa: E501
        """
        pass

    def test_get_view_indicators(self):
        """Test case for get_view_indicators

        Get the keys and metrics in a FlowFalcon view  # noqa: E501
        """
        pass

    def test_get_views(self):
        """Test case for get_views

        Get views  # noqa: E501
        """
        pass

    def test_update_application(self):
        """Test case for update_application

        Update application  # noqa: E501
        """
        pass

    def test_update_device_mappings(self):
        """Test case for update_device_mappings

        Update device mapping  # noqa: E501
        """
        pass

    def test_update_interface(self):
        """Test case for update_interface

        Update interface  # noqa: E501
        """
        pass

    def test_update_service_profile(self):
        """Test case for update_service_profile

        Update service profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
