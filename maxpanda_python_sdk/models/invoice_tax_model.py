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

class InvoiceTaxModel(object):
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
        'invoice_tax_id': 'int',
        'tax_rate': 'float'
    }

    attribute_map = {
        'invoice_tax_id': 'InvoiceTaxId',
        'tax_rate': 'TaxRate'
    }

    def __init__(self, invoice_tax_id=None, tax_rate=None):  # noqa: E501
        """InvoiceTaxModel - a model defined in Swagger"""  # noqa: E501
        self._invoice_tax_id = None
        self._tax_rate = None
        self.discriminator = None
        self.invoice_tax_id = invoice_tax_id
        self.tax_rate = tax_rate

    @property
    def invoice_tax_id(self):
        """Gets the invoice_tax_id of this InvoiceTaxModel.  # noqa: E501


        :return: The invoice_tax_id of this InvoiceTaxModel.  # noqa: E501
        :rtype: int
        """
        return self._invoice_tax_id

    @invoice_tax_id.setter
    def invoice_tax_id(self, invoice_tax_id):
        """Sets the invoice_tax_id of this InvoiceTaxModel.


        :param invoice_tax_id: The invoice_tax_id of this InvoiceTaxModel.  # noqa: E501
        :type: int
        """
        if invoice_tax_id is None:
            raise ValueError("Invalid value for `invoice_tax_id`, must not be `None`")  # noqa: E501

        self._invoice_tax_id = invoice_tax_id

    @property
    def tax_rate(self):
        """Gets the tax_rate of this InvoiceTaxModel.  # noqa: E501


        :return: The tax_rate of this InvoiceTaxModel.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this InvoiceTaxModel.


        :param tax_rate: The tax_rate of this InvoiceTaxModel.  # noqa: E501
        :type: float
        """
        if tax_rate is None:
            raise ValueError("Invalid value for `tax_rate`, must not be `None`")  # noqa: E501

        self._tax_rate = tax_rate

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
        if issubclass(InvoiceTaxModel, dict):
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
        if not isinstance(other, InvoiceTaxModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other