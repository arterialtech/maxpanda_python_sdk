# coding: utf-8

"""
    Maxpanda API V1

    The Maxpanda API documentation for version 1  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreatePurchaseOrder(object):
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
        'site_id': 'int',
        'vendor_id': 'int',
        'title': 'str',
        'account': 'str',
        'shipping_address_id': 'int',
        'request_approvers_id': 'list[int]',
        'received': 'datetime',
        'ordered': 'datetime',
        'notes': 'str',
        'comment': 'str',
        'items': 'list[PurchaseOrderItem]'
    }

    attribute_map = {
        'site_id': 'SiteId',
        'vendor_id': 'VendorId',
        'title': 'Title',
        'account': 'Account',
        'shipping_address_id': 'ShippingAddressId',
        'request_approvers_id': 'RequestApproversId',
        'received': 'Received',
        'ordered': 'Ordered',
        'notes': 'Notes',
        'comment': 'Comment',
        'items': 'Items'
    }

    def __init__(self, site_id=None, vendor_id=None, title=None, account=None, shipping_address_id=None, request_approvers_id=None, received=None, ordered=None, notes=None, comment=None, items=None):  # noqa: E501
        """CreatePurchaseOrder - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._vendor_id = None
        self._title = None
        self._account = None
        self._shipping_address_id = None
        self._request_approvers_id = None
        self._received = None
        self._ordered = None
        self._notes = None
        self._comment = None
        self._items = None
        self.discriminator = None
        self.site_id = site_id
        self.vendor_id = vendor_id
        self.title = title
        if account is not None:
            self.account = account
        self.shipping_address_id = shipping_address_id
        self.request_approvers_id = request_approvers_id
        if received is not None:
            self.received = received
        if ordered is not None:
            self.ordered = ordered
        if notes is not None:
            self.notes = notes
        if comment is not None:
            self.comment = comment
        if items is not None:
            self.items = items

    @property
    def site_id(self):
        """Gets the site_id of this CreatePurchaseOrder.  # noqa: E501

        Site Id of the Purchase Order. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :return: The site_id of this CreatePurchaseOrder.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this CreatePurchaseOrder.

        Site Id of the Purchase Order. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :param site_id: The site_id of this CreatePurchaseOrder.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def vendor_id(self):
        """Gets the vendor_id of this CreatePurchaseOrder.  # noqa: E501

        Vendor Id of the Purchase Order. Vendor Id can be found in your Maxpanda Vendor Index or Vendor API  # noqa: E501

        :return: The vendor_id of this CreatePurchaseOrder.  # noqa: E501
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this CreatePurchaseOrder.

        Vendor Id of the Purchase Order. Vendor Id can be found in your Maxpanda Vendor Index or Vendor API  # noqa: E501

        :param vendor_id: The vendor_id of this CreatePurchaseOrder.  # noqa: E501
        :type: int
        """
        if vendor_id is None:
            raise ValueError("Invalid value for `vendor_id`, must not be `None`")  # noqa: E501

        self._vendor_id = vendor_id

    @property
    def title(self):
        """Gets the title of this CreatePurchaseOrder.  # noqa: E501

        Title of Purchase Order  # noqa: E501

        :return: The title of this CreatePurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreatePurchaseOrder.

        Title of Purchase Order  # noqa: E501

        :param title: The title of this CreatePurchaseOrder.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def account(self):
        """Gets the account of this CreatePurchaseOrder.  # noqa: E501

        Account details  # noqa: E501

        :return: The account of this CreatePurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this CreatePurchaseOrder.

        Account details  # noqa: E501

        :param account: The account of this CreatePurchaseOrder.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def shipping_address_id(self):
        """Gets the shipping_address_id of this CreatePurchaseOrder.  # noqa: E501

        Shipping Address Id of the Purchase Order. Shipping Id can be found in your Maxpanda Company PO Address or PO Address API  # noqa: E501

        :return: The shipping_address_id of this CreatePurchaseOrder.  # noqa: E501
        :rtype: int
        """
        return self._shipping_address_id

    @shipping_address_id.setter
    def shipping_address_id(self, shipping_address_id):
        """Sets the shipping_address_id of this CreatePurchaseOrder.

        Shipping Address Id of the Purchase Order. Shipping Id can be found in your Maxpanda Company PO Address or PO Address API  # noqa: E501

        :param shipping_address_id: The shipping_address_id of this CreatePurchaseOrder.  # noqa: E501
        :type: int
        """
        if shipping_address_id is None:
            raise ValueError("Invalid value for `shipping_address_id`, must not be `None`")  # noqa: E501

        self._shipping_address_id = shipping_address_id

    @property
    def request_approvers_id(self):
        """Gets the request_approvers_id of this CreatePurchaseOrder.  # noqa: E501

        Approvers Id of the Purchase Order. User Id can be found in your Maxpanda User Index or User API  # noqa: E501

        :return: The request_approvers_id of this CreatePurchaseOrder.  # noqa: E501
        :rtype: list[int]
        """
        return self._request_approvers_id

    @request_approvers_id.setter
    def request_approvers_id(self, request_approvers_id):
        """Sets the request_approvers_id of this CreatePurchaseOrder.

        Approvers Id of the Purchase Order. User Id can be found in your Maxpanda User Index or User API  # noqa: E501

        :param request_approvers_id: The request_approvers_id of this CreatePurchaseOrder.  # noqa: E501
        :type: list[int]
        """
        if request_approvers_id is None:
            raise ValueError("Invalid value for `request_approvers_id`, must not be `None`")  # noqa: E501

        self._request_approvers_id = request_approvers_id

    @property
    def received(self):
        """Gets the received of this CreatePurchaseOrder.  # noqa: E501

        Date of Item Receiving  # noqa: E501

        :return: The received of this CreatePurchaseOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._received

    @received.setter
    def received(self, received):
        """Sets the received of this CreatePurchaseOrder.

        Date of Item Receiving  # noqa: E501

        :param received: The received of this CreatePurchaseOrder.  # noqa: E501
        :type: datetime
        """

        self._received = received

    @property
    def ordered(self):
        """Gets the ordered of this CreatePurchaseOrder.  # noqa: E501

        Date of Item Order  # noqa: E501

        :return: The ordered of this CreatePurchaseOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._ordered

    @ordered.setter
    def ordered(self, ordered):
        """Sets the ordered of this CreatePurchaseOrder.

        Date of Item Order  # noqa: E501

        :param ordered: The ordered of this CreatePurchaseOrder.  # noqa: E501
        :type: datetime
        """

        self._ordered = ordered

    @property
    def notes(self):
        """Gets the notes of this CreatePurchaseOrder.  # noqa: E501

        Notes about Purchase Order  # noqa: E501

        :return: The notes of this CreatePurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreatePurchaseOrder.

        Notes about Purchase Order  # noqa: E501

        :param notes: The notes of this CreatePurchaseOrder.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def comment(self):
        """Gets the comment of this CreatePurchaseOrder.  # noqa: E501

        Comment  # noqa: E501

        :return: The comment of this CreatePurchaseOrder.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreatePurchaseOrder.

        Comment  # noqa: E501

        :param comment: The comment of this CreatePurchaseOrder.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def items(self):
        """Gets the items of this CreatePurchaseOrder.  # noqa: E501

        Parts ordered in Purchase Order.  # noqa: E501

        :return: The items of this CreatePurchaseOrder.  # noqa: E501
        :rtype: list[PurchaseOrderItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CreatePurchaseOrder.

        Parts ordered in Purchase Order.  # noqa: E501

        :param items: The items of this CreatePurchaseOrder.  # noqa: E501
        :type: list[PurchaseOrderItem]
        """

        self._items = items

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
        if issubclass(CreatePurchaseOrder, dict):
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
        if not isinstance(other, CreatePurchaseOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
