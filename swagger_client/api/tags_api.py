# coding: utf-8

"""
    SevOne API Documentation

    Supported endpoints by the new RESTful API  # noqa: E501

    OpenAPI spec version: 2.1.42, Hash: 719f8be
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_tags(self, options, **kwargs):  # noqa: E501
        """Get all Tags  # noqa: E501

        Endpoint for retrieving all Tags that supports pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags(options, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PageAndSortOptions options: (required)
        :param str name: Name of the tag
        :return: PagerTagsDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tags_with_http_info(options, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tags_with_http_info(options, **kwargs)  # noqa: E501
            return data

    def get_tags_with_http_info(self, options, **kwargs):  # noqa: E501
        """Get all Tags  # noqa: E501

        Endpoint for retrieving all Tags that supports pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags_with_http_info(options, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PageAndSortOptions options: (required)
        :param str name: Name of the tag
        :return: PagerTagsDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['options', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'options' is set
        if ('options' not in params or
                params['options'] is None):
            raise ValueError("Missing the required parameter `options` when calling `get_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'options' in params:
            query_params.append(('options', params['options']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagerTagsDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tags1(self, name, **kwargs):  # noqa: E501
        """Get Indicator Types Based On Tag Name   # noqa: E501

        Endpoint for retrieving all Indicator Types Based On Tag Name that supports pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags1(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the tag (required)
        :param int page: The number of the requested page, defaults to 0
        :param int size: The size of the requested page, defaults to 20
        :return: PagerTagIndicatorTypesDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tags1_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tags1_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_tags1_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get Indicator Types Based On Tag Name   # noqa: E501

        Endpoint for retrieving all Indicator Types Based On Tag Name that supports pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags1_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the tag (required)
        :param int page: The number of the requested page, defaults to 0
        :param int size: The size of the requested page, defaults to 20
        :return: PagerTagIndicatorTypesDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'page', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tags1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_tags1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/tags/{name}/indicatortypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagerTagIndicatorTypesDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
