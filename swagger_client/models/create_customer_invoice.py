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

class CreateCustomerInvoice(object):
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
        'customer_id': 'int',
        'invoice_number': 'str',
        'archived': 'bool',
        'invoice_date': 'datetime',
        'due_date': 'datetime',
        'invoice_items': 'list[CreateInvoiceItemModel]',
        'invoice_taxes': 'list[InvoiceTaxModel]'
    }

    attribute_map = {
        'site_id': 'SiteId',
        'customer_id': 'CustomerId',
        'invoice_number': 'InvoiceNumber',
        'archived': 'Archived',
        'invoice_date': 'InvoiceDate',
        'due_date': 'DueDate',
        'invoice_items': 'InvoiceItems',
        'invoice_taxes': 'InvoiceTaxes'
    }

    def __init__(self, site_id=None, customer_id=None, invoice_number=None, archived=None, invoice_date=None, due_date=None, invoice_items=None, invoice_taxes=None):  # noqa: E501
        """CreateCustomerInvoice - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._customer_id = None
        self._invoice_number = None
        self._archived = None
        self._invoice_date = None
        self._due_date = None
        self._invoice_items = None
        self._invoice_taxes = None
        self.discriminator = None
        self.site_id = site_id
        self.customer_id = customer_id
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if archived is not None:
            self.archived = archived
        self.invoice_date = invoice_date
        if due_date is not None:
            self.due_date = due_date
        self.invoice_items = invoice_items
        self.invoice_taxes = invoice_taxes

    @property
    def site_id(self):
        """Gets the site_id of this CreateCustomerInvoice.  # noqa: E501

        Site Id of the Customer Invoice. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :return: The site_id of this CreateCustomerInvoice.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this CreateCustomerInvoice.

        Site Id of the Customer Invoice. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :param site_id: The site_id of this CreateCustomerInvoice.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def customer_id(self):
        """Gets the customer_id of this CreateCustomerInvoice.  # noqa: E501

        Id of the Customer. Customer Id can be found in your Maxpanda Customer Index or Customer API  # noqa: E501

        :return: The customer_id of this CreateCustomerInvoice.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CreateCustomerInvoice.

        Id of the Customer. Customer Id can be found in your Maxpanda Customer Index or Customer API  # noqa: E501

        :param customer_id: The customer_id of this CreateCustomerInvoice.  # noqa: E501
        :type: int
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def invoice_number(self):
        """Gets the invoice_number of this CreateCustomerInvoice.  # noqa: E501

        Invoice Number of Customer Invoice  # noqa: E501

        :return: The invoice_number of this CreateCustomerInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this CreateCustomerInvoice.

        Invoice Number of Customer Invoice  # noqa: E501

        :param invoice_number: The invoice_number of this CreateCustomerInvoice.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def archived(self):
        """Gets the archived of this CreateCustomerInvoice.  # noqa: E501


        :return: The archived of this CreateCustomerInvoice.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this CreateCustomerInvoice.


        :param archived: The archived of this CreateCustomerInvoice.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def invoice_date(self):
        """Gets the invoice_date of this CreateCustomerInvoice.  # noqa: E501

        Date of Customer Invoice  # noqa: E501

        :return: The invoice_date of this CreateCustomerInvoice.  # noqa: E501
        :rtype: datetime
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this CreateCustomerInvoice.

        Date of Customer Invoice  # noqa: E501

        :param invoice_date: The invoice_date of this CreateCustomerInvoice.  # noqa: E501
        :type: datetime
        """
        if invoice_date is None:
            raise ValueError("Invalid value for `invoice_date`, must not be `None`")  # noqa: E501

        self._invoice_date = invoice_date

    @property
    def due_date(self):
        """Gets the due_date of this CreateCustomerInvoice.  # noqa: E501

        Due date of Customer Invoice  # noqa: E501

        :return: The due_date of this CreateCustomerInvoice.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this CreateCustomerInvoice.

        Due date of Customer Invoice  # noqa: E501

        :param due_date: The due_date of this CreateCustomerInvoice.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def invoice_items(self):
        """Gets the invoice_items of this CreateCustomerInvoice.  # noqa: E501

        Details of Items of Customer Invoice  # noqa: E501

        :return: The invoice_items of this CreateCustomerInvoice.  # noqa: E501
        :rtype: list[CreateInvoiceItemModel]
        """
        return self._invoice_items

    @invoice_items.setter
    def invoice_items(self, invoice_items):
        """Sets the invoice_items of this CreateCustomerInvoice.

        Details of Items of Customer Invoice  # noqa: E501

        :param invoice_items: The invoice_items of this CreateCustomerInvoice.  # noqa: E501
        :type: list[CreateInvoiceItemModel]
        """
        if invoice_items is None:
            raise ValueError("Invalid value for `invoice_items`, must not be `None`")  # noqa: E501

        self._invoice_items = invoice_items

    @property
    def invoice_taxes(self):
        """Gets the invoice_taxes of this CreateCustomerInvoice.  # noqa: E501

        Taxes applied on Customer Invoice  # noqa: E501

        :return: The invoice_taxes of this CreateCustomerInvoice.  # noqa: E501
        :rtype: list[InvoiceTaxModel]
        """
        return self._invoice_taxes

    @invoice_taxes.setter
    def invoice_taxes(self, invoice_taxes):
        """Sets the invoice_taxes of this CreateCustomerInvoice.

        Taxes applied on Customer Invoice  # noqa: E501

        :param invoice_taxes: The invoice_taxes of this CreateCustomerInvoice.  # noqa: E501
        :type: list[InvoiceTaxModel]
        """
        if invoice_taxes is None:
            raise ValueError("Invalid value for `invoice_taxes`, must not be `None`")  # noqa: E501

        self._invoice_taxes = invoice_taxes

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
        if issubclass(CreateCustomerInvoice, dict):
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
        if not isinstance(other, CreateCustomerInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other