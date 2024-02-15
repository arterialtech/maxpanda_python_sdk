# coding: utf-8

"""
    Maxpanda API V1

    The Maxpanda API documentation for version 1  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AssetStatusApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def asset_statuses_get(self, request_complete_information, **kwargs):  # noqa: E501
        """Get a paged list of Asset Status  # noqa: E501

        The default list will return the first 25 records.  The NextPageUrl property will return the next page of records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_statuses_get(request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :param int page: Page number to start retrieving data (similar to List View pagification)
        :param int page_size: Number of records per page (max=100)
        :return: AssetStatusResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_statuses_get_with_http_info(request_complete_information, **kwargs)  # noqa: E501
        else:
            (data) = self.asset_statuses_get_with_http_info(request_complete_information, **kwargs)  # noqa: E501
            return data

    def asset_statuses_get_with_http_info(self, request_complete_information, **kwargs):  # noqa: E501
        """Get a paged list of Asset Status  # noqa: E501

        The default list will return the first 25 records.  The NextPageUrl property will return the next page of records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_statuses_get_with_http_info(request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :param int page: Page number to start retrieving data (similar to List View pagification)
        :param int page_size: Number of records per page (max=100)
        :return: AssetStatusResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_complete_information', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_statuses_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request_complete_information' is set
        if ('request_complete_information' not in params or
                params['request_complete_information'] is None):
            raise ValueError("Missing the required parameter `request_complete_information` when calling `asset_statuses_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'request_complete_information' in params:
            query_params.append(('requestCompleteInformation', params['request_complete_information']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/Company/AssetStatuses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssetStatusResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def asset_statuses_get_0(self, id, request_complete_information, **kwargs):  # noqa: E501
        """Get a specific Asset Status record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_statuses_get_0(id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The Asset Status id to retrieve (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :return: AssetStatusResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.asset_statuses_get_0_with_http_info(id, request_complete_information, **kwargs)  # noqa: E501
        else:
            (data) = self.asset_statuses_get_0_with_http_info(id, request_complete_information, **kwargs)  # noqa: E501
            return data

    def asset_statuses_get_0_with_http_info(self, id, request_complete_information, **kwargs):  # noqa: E501
        """Get a specific Asset Status record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.asset_statuses_get_0_with_http_info(id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The Asset Status id to retrieve (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :return: AssetStatusResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'request_complete_information']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_statuses_get_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `asset_statuses_get_0`")  # noqa: E501
        # verify the required parameter 'request_complete_information' is set
        if ('request_complete_information' not in params or
                params['request_complete_information'] is None):
            raise ValueError("Missing the required parameter `request_complete_information` when calling `asset_statuses_get_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'request_complete_information' in params:
            query_params.append(('requestCompleteInformation', params['request_complete_information']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/Company/AssetStatuses/id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssetStatusResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
