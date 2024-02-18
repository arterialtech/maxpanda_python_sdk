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

from maxpanda_python_sdk.api_client import ApiClient


class VendorInvoicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def vendor_invoice_get(self, site_id, request_complete_information, **kwargs):  # noqa: E501
        """Get a paged list of Vendor Invoice  # noqa: E501

        The default list will return the first 25 records.  The NextPageUrl property will return the next page of records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vendor_invoice_get(site_id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :param int page: Page number to start retrieving data (similar to List View pagification)
        :param int page_size: Number of records per page (max=100)
        :return: InvoiceResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vendor_invoice_get_with_http_info(site_id, request_complete_information, **kwargs)  # noqa: E501
        else:
            (data) = self.vendor_invoice_get_with_http_info(site_id, request_complete_information, **kwargs)  # noqa: E501
            return data

    def vendor_invoice_get_with_http_info(self, site_id, request_complete_information, **kwargs):  # noqa: E501
        """Get a paged list of Vendor Invoice  # noqa: E501

        The default list will return the first 25 records.  The NextPageUrl property will return the next page of records  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vendor_invoice_get_with_http_info(site_id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :param int page: Page number to start retrieving data (similar to List View pagification)
        :param int page_size: Number of records per page (max=100)
        :return: InvoiceResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id', 'request_complete_information', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vendor_invoice_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `vendor_invoice_get`")  # noqa: E501
        # verify the required parameter 'request_complete_information' is set
        if ('request_complete_information' not in params or
                params['request_complete_information'] is None):
            raise ValueError("Missing the required parameter `request_complete_information` when calling `vendor_invoice_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'site_id' in params:
            query_params.append(('siteId', params['site_id']))  # noqa: E501
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
        auth_settings = ['ApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/v1/VendorInvoices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InvoiceResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vendor_invoice_get_0(self, id, site_id, request_complete_information, **kwargs):  # noqa: E501
        """Get a specific Vendor Invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vendor_invoice_get_0(id, site_id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The Vendor Invoice id to retrieve (required)
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :return: InvoiceResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vendor_invoice_get_0_with_http_info(id, site_id, request_complete_information, **kwargs)  # noqa: E501
        else:
            (data) = self.vendor_invoice_get_0_with_http_info(id, site_id, request_complete_information, **kwargs)  # noqa: E501
            return data

    def vendor_invoice_get_0_with_http_info(self, id, site_id, request_complete_information, **kwargs):  # noqa: E501
        """Get a specific Vendor Invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vendor_invoice_get_0_with_http_info(id, site_id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The Vendor Invoice id to retrieve (required)
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :return: InvoiceResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'site_id', 'request_complete_information']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vendor_invoice_get_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `vendor_invoice_get_0`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `vendor_invoice_get_0`")  # noqa: E501
        # verify the required parameter 'request_complete_information' is set
        if ('request_complete_information' not in params or
                params['request_complete_information'] is None):
            raise ValueError("Missing the required parameter `request_complete_information` when calling `vendor_invoice_get_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'site_id' in params:
            query_params.append(('siteId', params['site_id']))  # noqa: E501
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
        auth_settings = ['ApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/v1/VendorInvoice/id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InvoiceResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vendor_invoice_post(self, body, **kwargs):  # noqa: E501
        """Create an Invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vendor_invoice_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateInvoiceModel body: Details of the new invoice (required)
        :return: InvoiceCreateUpdateResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vendor_invoice_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.vendor_invoice_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def vendor_invoice_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create an Invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vendor_invoice_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateInvoiceModel body: Details of the new invoice (required)
        :return: InvoiceCreateUpdateResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vendor_invoice_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `vendor_invoice_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/v1/VendorInvoice', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InvoiceCreateUpdateResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def vendor_invoice_put(self, body, **kwargs):  # noqa: E501
        """Update an Invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vendor_invoice_put(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateInvoiceModel body: Details of the Invoice (required)
        :return: InvoiceCreateUpdateResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.vendor_invoice_put_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.vendor_invoice_put_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def vendor_invoice_put_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update an Invoice  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.vendor_invoice_put_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateInvoiceModel body: Details of the Invoice (required)
        :return: InvoiceCreateUpdateResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vendor_invoice_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `vendor_invoice_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/v1/VendorInvoice', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InvoiceCreateUpdateResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
