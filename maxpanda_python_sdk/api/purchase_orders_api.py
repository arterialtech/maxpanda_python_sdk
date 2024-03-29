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


class PurchaseOrdersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def purchase_order_get(self, site_id, request_complete_information, **kwargs):  # noqa: E501
        """Get a paged list of Purchase Orders  # noqa: E501

        The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_get(site_id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :param int page: Page number to start retrieving data (similar to List View pagification)
        :param int page_size: Number of records per page (max=100)
        :return: PurchaseOrderResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purchase_order_get_with_http_info(site_id, request_complete_information, **kwargs)  # noqa: E501
        else:
            (data) = self.purchase_order_get_with_http_info(site_id, request_complete_information, **kwargs)  # noqa: E501
            return data

    def purchase_order_get_with_http_info(self, site_id, request_complete_information, **kwargs):  # noqa: E501
        """Get a paged list of Purchase Orders  # noqa: E501

        The default list will return the first 25 records.  The NextPageUrl property will return the next page of records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_get_with_http_info(site_id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :param int page: Page number to start retrieving data (similar to List View pagification)
        :param int page_size: Number of records per page (max=100)
        :return: PurchaseOrderResponseModel
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
                    " to method purchase_order_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `purchase_order_get`")  # noqa: E501
        # verify the required parameter 'request_complete_information' is set
        if ('request_complete_information' not in params or
                params['request_complete_information'] is None):
            raise ValueError("Missing the required parameter `request_complete_information` when calling `purchase_order_get`")  # noqa: E501

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
            '/v1/PurchaseOrder', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PurchaseOrderResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def purchase_order_get_0(self, id, site_id, request_complete_information, **kwargs):  # noqa: E501
        """Get a specific Purchase Order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_get_0(id, site_id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The Purchase Order id to retrieve (required)
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :return: PurchaseOrderResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purchase_order_get_0_with_http_info(id, site_id, request_complete_information, **kwargs)  # noqa: E501
        else:
            (data) = self.purchase_order_get_0_with_http_info(id, site_id, request_complete_information, **kwargs)  # noqa: E501
            return data

    def purchase_order_get_0_with_http_info(self, id, site_id, request_complete_information, **kwargs):  # noqa: E501
        """Get a specific Purchase Order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_get_0_with_http_info(id, site_id, request_complete_information, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The Purchase Order id to retrieve (required)
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param bool request_complete_information: True option provides all the data fields. False will only return required fields (required)
        :return: PurchaseOrderResponseModel
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
                    " to method purchase_order_get_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `purchase_order_get_0`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `purchase_order_get_0`")  # noqa: E501
        # verify the required parameter 'request_complete_information' is set
        if ('request_complete_information' not in params or
                params['request_complete_information'] is None):
            raise ValueError("Missing the required parameter `request_complete_information` when calling `purchase_order_get_0`")  # noqa: E501

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
            '/v1/PurchaseOrder/id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PurchaseOrderResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def purchase_order_get_po_status(self, **kwargs):  # noqa: E501
        """Get Purchase Order Statuses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_get_po_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PageResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purchase_order_get_po_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.purchase_order_get_po_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def purchase_order_get_po_status_with_http_info(self, **kwargs):  # noqa: E501
        """Get Purchase Order Statuses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_get_po_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PageResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method purchase_order_get_po_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/v1/PurchaseOrderStatus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def purchase_order_post(self, body, **kwargs):  # noqa: E501
        """Create a new Purchase Order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePurchaseOrder body: Details of new Purchase Order (required)
        :return: POCreateUpdateResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purchase_order_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.purchase_order_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def purchase_order_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new Purchase Order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePurchaseOrder body: Details of new Purchase Order (required)
        :return: POCreateUpdateResponseModel
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
                    " to method purchase_order_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `purchase_order_post`")  # noqa: E501

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
            '/v1/PurchaseOrder', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POCreateUpdateResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def purchase_order_put(self, body, **kwargs):  # noqa: E501
        """Update a Purchase Order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_put(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePurchaseOrder body: Details of Purchase Order (required)
        :return: POCreateUpdateResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purchase_order_put_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.purchase_order_put_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def purchase_order_put_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update a Purchase Order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_put_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePurchaseOrder body: Details of Purchase Order (required)
        :return: POCreateUpdateResponseModel
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
                    " to method purchase_order_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `purchase_order_put`")  # noqa: E501

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
            '/v1/PurchaseOrder', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POCreateUpdateResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def purchase_order_put_0(self, purchase_order_id, site_id, new_status, **kwargs):  # noqa: E501
        """Update Status of Purchase Order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_put_0(purchase_order_id, site_id, new_status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int purchase_order_id: Purchase Order Id (required)
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param int new_status: Status ID can be found in Purchase Order Status API (required)
        :return: POCreateUpdateResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.purchase_order_put_0_with_http_info(purchase_order_id, site_id, new_status, **kwargs)  # noqa: E501
        else:
            (data) = self.purchase_order_put_0_with_http_info(purchase_order_id, site_id, new_status, **kwargs)  # noqa: E501
            return data

    def purchase_order_put_0_with_http_info(self, purchase_order_id, site_id, new_status, **kwargs):  # noqa: E501
        """Update Status of Purchase Order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.purchase_order_put_0_with_http_info(purchase_order_id, site_id, new_status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int purchase_order_id: Purchase Order Id (required)
        :param int site_id: Site ID can be found in your Maxpanda Site index or Sites API (required)
        :param int new_status: Status ID can be found in Purchase Order Status API (required)
        :return: POCreateUpdateResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['purchase_order_id', 'site_id', 'new_status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method purchase_order_put_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'purchase_order_id' is set
        if ('purchase_order_id' not in params or
                params['purchase_order_id'] is None):
            raise ValueError("Missing the required parameter `purchase_order_id` when calling `purchase_order_put_0`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `purchase_order_put_0`")  # noqa: E501
        # verify the required parameter 'new_status' is set
        if ('new_status' not in params or
                params['new_status'] is None):
            raise ValueError("Missing the required parameter `new_status` when calling `purchase_order_put_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'purchase_order_id' in params:
            query_params.append(('PurchaseOrderId', params['purchase_order_id']))  # noqa: E501
        if 'site_id' in params:
            query_params.append(('SiteId', params['site_id']))  # noqa: E501
        if 'new_status' in params:
            query_params.append(('NewStatus', params['new_status']))  # noqa: E501

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
            '/v1/UpdatePurchaseOrderStatus', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POCreateUpdateResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
