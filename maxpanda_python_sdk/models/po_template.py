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

class POTemplate(object):
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
        'site_ref': 'SiteRef',
        'purchase_order_template_id': 'int',
        'vendor_ref': 'VendorRef',
        'title': 'str',
        'account': 'str',
        'shipping_address': 'POAddress',
        'request_approver_ref': 'list[UserRef]',
        'private_notes': 'str',
        'comment': 'str',
        'purchase_order_item_ref': 'list[PurchaseOrderItemDetails]'
    }

    attribute_map = {
        'site_ref': 'SiteRef',
        'purchase_order_template_id': 'PurchaseOrderTemplateId',
        'vendor_ref': 'VendorRef',
        'title': 'Title',
        'account': 'Account',
        'shipping_address': 'ShippingAddress',
        'request_approver_ref': 'RequestApproverRef',
        'private_notes': 'PrivateNotes',
        'comment': 'Comment',
        'purchase_order_item_ref': 'PurchaseOrderItemRef'
    }

    def __init__(self, site_ref=None, purchase_order_template_id=None, vendor_ref=None, title=None, account=None, shipping_address=None, request_approver_ref=None, private_notes=None, comment=None, purchase_order_item_ref=None):  # noqa: E501
        """POTemplate - a model defined in Swagger"""  # noqa: E501
        self._site_ref = None
        self._purchase_order_template_id = None
        self._vendor_ref = None
        self._title = None
        self._account = None
        self._shipping_address = None
        self._request_approver_ref = None
        self._private_notes = None
        self._comment = None
        self._purchase_order_item_ref = None
        self.discriminator = None
        if site_ref is not None:
            self.site_ref = site_ref
        if purchase_order_template_id is not None:
            self.purchase_order_template_id = purchase_order_template_id
        if vendor_ref is not None:
            self.vendor_ref = vendor_ref
        if title is not None:
            self.title = title
        if account is not None:
            self.account = account
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if request_approver_ref is not None:
            self.request_approver_ref = request_approver_ref
        if private_notes is not None:
            self.private_notes = private_notes
        if comment is not None:
            self.comment = comment
        if purchase_order_item_ref is not None:
            self.purchase_order_item_ref = purchase_order_item_ref

    @property
    def site_ref(self):
        """Gets the site_ref of this POTemplate.  # noqa: E501


        :return: The site_ref of this POTemplate.  # noqa: E501
        :rtype: SiteRef
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this POTemplate.


        :param site_ref: The site_ref of this POTemplate.  # noqa: E501
        :type: SiteRef
        """

        self._site_ref = site_ref

    @property
    def purchase_order_template_id(self):
        """Gets the purchase_order_template_id of this POTemplate.  # noqa: E501


        :return: The purchase_order_template_id of this POTemplate.  # noqa: E501
        :rtype: int
        """
        return self._purchase_order_template_id

    @purchase_order_template_id.setter
    def purchase_order_template_id(self, purchase_order_template_id):
        """Sets the purchase_order_template_id of this POTemplate.


        :param purchase_order_template_id: The purchase_order_template_id of this POTemplate.  # noqa: E501
        :type: int
        """

        self._purchase_order_template_id = purchase_order_template_id

    @property
    def vendor_ref(self):
        """Gets the vendor_ref of this POTemplate.  # noqa: E501


        :return: The vendor_ref of this POTemplate.  # noqa: E501
        :rtype: VendorRef
        """
        return self._vendor_ref

    @vendor_ref.setter
    def vendor_ref(self, vendor_ref):
        """Sets the vendor_ref of this POTemplate.


        :param vendor_ref: The vendor_ref of this POTemplate.  # noqa: E501
        :type: VendorRef
        """

        self._vendor_ref = vendor_ref

    @property
    def title(self):
        """Gets the title of this POTemplate.  # noqa: E501


        :return: The title of this POTemplate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this POTemplate.


        :param title: The title of this POTemplate.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def account(self):
        """Gets the account of this POTemplate.  # noqa: E501


        :return: The account of this POTemplate.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this POTemplate.


        :param account: The account of this POTemplate.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def shipping_address(self):
        """Gets the shipping_address of this POTemplate.  # noqa: E501


        :return: The shipping_address of this POTemplate.  # noqa: E501
        :rtype: POAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this POTemplate.


        :param shipping_address: The shipping_address of this POTemplate.  # noqa: E501
        :type: POAddress
        """

        self._shipping_address = shipping_address

    @property
    def request_approver_ref(self):
        """Gets the request_approver_ref of this POTemplate.  # noqa: E501


        :return: The request_approver_ref of this POTemplate.  # noqa: E501
        :rtype: list[UserRef]
        """
        return self._request_approver_ref

    @request_approver_ref.setter
    def request_approver_ref(self, request_approver_ref):
        """Sets the request_approver_ref of this POTemplate.


        :param request_approver_ref: The request_approver_ref of this POTemplate.  # noqa: E501
        :type: list[UserRef]
        """

        self._request_approver_ref = request_approver_ref

    @property
    def private_notes(self):
        """Gets the private_notes of this POTemplate.  # noqa: E501


        :return: The private_notes of this POTemplate.  # noqa: E501
        :rtype: str
        """
        return self._private_notes

    @private_notes.setter
    def private_notes(self, private_notes):
        """Sets the private_notes of this POTemplate.


        :param private_notes: The private_notes of this POTemplate.  # noqa: E501
        :type: str
        """

        self._private_notes = private_notes

    @property
    def comment(self):
        """Gets the comment of this POTemplate.  # noqa: E501


        :return: The comment of this POTemplate.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this POTemplate.


        :param comment: The comment of this POTemplate.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def purchase_order_item_ref(self):
        """Gets the purchase_order_item_ref of this POTemplate.  # noqa: E501


        :return: The purchase_order_item_ref of this POTemplate.  # noqa: E501
        :rtype: list[PurchaseOrderItemDetails]
        """
        return self._purchase_order_item_ref

    @purchase_order_item_ref.setter
    def purchase_order_item_ref(self, purchase_order_item_ref):
        """Sets the purchase_order_item_ref of this POTemplate.


        :param purchase_order_item_ref: The purchase_order_item_ref of this POTemplate.  # noqa: E501
        :type: list[PurchaseOrderItemDetails]
        """

        self._purchase_order_item_ref = purchase_order_item_ref

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
        if issubclass(POTemplate, dict):
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
        if not isinstance(other, POTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other