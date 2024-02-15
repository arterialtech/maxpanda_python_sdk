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

class PartCategory(object):
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
        'part_category_id': 'int',
        'name': 'str',
        'account_number': 'str',
        'sort_order': 'int',
        'disabled': 'bool',
        'allowed_sites': 'list[SiteRef]'
    }

    attribute_map = {
        'part_category_id': 'PartCategoryId',
        'name': 'Name',
        'account_number': 'AccountNumber',
        'sort_order': 'SortOrder',
        'disabled': 'Disabled',
        'allowed_sites': 'AllowedSites'
    }

    def __init__(self, part_category_id=None, name=None, account_number=None, sort_order=None, disabled=None, allowed_sites=None):  # noqa: E501
        """PartCategory - a model defined in Swagger"""  # noqa: E501
        self._part_category_id = None
        self._name = None
        self._account_number = None
        self._sort_order = None
        self._disabled = None
        self._allowed_sites = None
        self.discriminator = None
        if part_category_id is not None:
            self.part_category_id = part_category_id
        if name is not None:
            self.name = name
        if account_number is not None:
            self.account_number = account_number
        if sort_order is not None:
            self.sort_order = sort_order
        if disabled is not None:
            self.disabled = disabled
        if allowed_sites is not None:
            self.allowed_sites = allowed_sites

    @property
    def part_category_id(self):
        """Gets the part_category_id of this PartCategory.  # noqa: E501


        :return: The part_category_id of this PartCategory.  # noqa: E501
        :rtype: int
        """
        return self._part_category_id

    @part_category_id.setter
    def part_category_id(self, part_category_id):
        """Sets the part_category_id of this PartCategory.


        :param part_category_id: The part_category_id of this PartCategory.  # noqa: E501
        :type: int
        """

        self._part_category_id = part_category_id

    @property
    def name(self):
        """Gets the name of this PartCategory.  # noqa: E501


        :return: The name of this PartCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartCategory.


        :param name: The name of this PartCategory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account_number(self):
        """Gets the account_number of this PartCategory.  # noqa: E501


        :return: The account_number of this PartCategory.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this PartCategory.


        :param account_number: The account_number of this PartCategory.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def sort_order(self):
        """Gets the sort_order of this PartCategory.  # noqa: E501


        :return: The sort_order of this PartCategory.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this PartCategory.


        :param sort_order: The sort_order of this PartCategory.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def disabled(self):
        """Gets the disabled of this PartCategory.  # noqa: E501


        :return: The disabled of this PartCategory.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this PartCategory.


        :param disabled: The disabled of this PartCategory.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def allowed_sites(self):
        """Gets the allowed_sites of this PartCategory.  # noqa: E501


        :return: The allowed_sites of this PartCategory.  # noqa: E501
        :rtype: list[SiteRef]
        """
        return self._allowed_sites

    @allowed_sites.setter
    def allowed_sites(self, allowed_sites):
        """Sets the allowed_sites of this PartCategory.


        :param allowed_sites: The allowed_sites of this PartCategory.  # noqa: E501
        :type: list[SiteRef]
        """

        self._allowed_sites = allowed_sites

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
        if issubclass(PartCategory, dict):
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
        if not isinstance(other, PartCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other