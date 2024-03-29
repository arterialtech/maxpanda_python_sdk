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

class POAddressModelAPI(object):
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
        'address_id': 'int',
        'title': 'str',
        'ship_to': 'str',
        'email': 'str',
        'phone': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'city': 'str',
        'region': 'str',
        'country': 'str',
        'postal_code': 'str',
        'po_box': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'site_ref': 'SiteRef',
        'address_id': 'AddressId',
        'title': 'Title',
        'ship_to': 'ShipTo',
        'email': 'Email',
        'phone': 'Phone',
        'address_line1': 'AddressLine1',
        'address_line2': 'AddressLine2',
        'city': 'City',
        'region': 'Region',
        'country': 'Country',
        'postal_code': 'PostalCode',
        'po_box': 'POBox',
        'sort_order': 'SortOrder'
    }

    def __init__(self, site_ref=None, address_id=None, title=None, ship_to=None, email=None, phone=None, address_line1=None, address_line2=None, city=None, region=None, country=None, postal_code=None, po_box=None, sort_order=None):  # noqa: E501
        """POAddressModelAPI - a model defined in Swagger"""  # noqa: E501
        self._site_ref = None
        self._address_id = None
        self._title = None
        self._ship_to = None
        self._email = None
        self._phone = None
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._region = None
        self._country = None
        self._postal_code = None
        self._po_box = None
        self._sort_order = None
        self.discriminator = None
        if site_ref is not None:
            self.site_ref = site_ref
        self.address_id = address_id
        if title is not None:
            self.title = title
        if ship_to is not None:
            self.ship_to = ship_to
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if country is not None:
            self.country = country
        if postal_code is not None:
            self.postal_code = postal_code
        if po_box is not None:
            self.po_box = po_box
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def site_ref(self):
        """Gets the site_ref of this POAddressModelAPI.  # noqa: E501


        :return: The site_ref of this POAddressModelAPI.  # noqa: E501
        :rtype: SiteRef
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this POAddressModelAPI.


        :param site_ref: The site_ref of this POAddressModelAPI.  # noqa: E501
        :type: SiteRef
        """

        self._site_ref = site_ref

    @property
    def address_id(self):
        """Gets the address_id of this POAddressModelAPI.  # noqa: E501


        :return: The address_id of this POAddressModelAPI.  # noqa: E501
        :rtype: int
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """Sets the address_id of this POAddressModelAPI.


        :param address_id: The address_id of this POAddressModelAPI.  # noqa: E501
        :type: int
        """
        if address_id is None:
            raise ValueError("Invalid value for `address_id`, must not be `None`")  # noqa: E501

        self._address_id = address_id

    @property
    def title(self):
        """Gets the title of this POAddressModelAPI.  # noqa: E501


        :return: The title of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this POAddressModelAPI.


        :param title: The title of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def ship_to(self):
        """Gets the ship_to of this POAddressModelAPI.  # noqa: E501


        :return: The ship_to of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """Sets the ship_to of this POAddressModelAPI.


        :param ship_to: The ship_to of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._ship_to = ship_to

    @property
    def email(self):
        """Gets the email of this POAddressModelAPI.  # noqa: E501


        :return: The email of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this POAddressModelAPI.


        :param email: The email of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this POAddressModelAPI.  # noqa: E501


        :return: The phone of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this POAddressModelAPI.


        :param phone: The phone of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def address_line1(self):
        """Gets the address_line1 of this POAddressModelAPI.  # noqa: E501


        :return: The address_line1 of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this POAddressModelAPI.


        :param address_line1: The address_line1 of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this POAddressModelAPI.  # noqa: E501


        :return: The address_line2 of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this POAddressModelAPI.


        :param address_line2: The address_line2 of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this POAddressModelAPI.  # noqa: E501


        :return: The city of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this POAddressModelAPI.


        :param city: The city of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def region(self):
        """Gets the region of this POAddressModelAPI.  # noqa: E501


        :return: The region of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this POAddressModelAPI.


        :param region: The region of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def country(self):
        """Gets the country of this POAddressModelAPI.  # noqa: E501


        :return: The country of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this POAddressModelAPI.


        :param country: The country of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def postal_code(self):
        """Gets the postal_code of this POAddressModelAPI.  # noqa: E501


        :return: The postal_code of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this POAddressModelAPI.


        :param postal_code: The postal_code of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def po_box(self):
        """Gets the po_box of this POAddressModelAPI.  # noqa: E501


        :return: The po_box of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._po_box

    @po_box.setter
    def po_box(self, po_box):
        """Sets the po_box of this POAddressModelAPI.


        :param po_box: The po_box of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._po_box = po_box

    @property
    def sort_order(self):
        """Gets the sort_order of this POAddressModelAPI.  # noqa: E501


        :return: The sort_order of this POAddressModelAPI.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this POAddressModelAPI.


        :param sort_order: The sort_order of this POAddressModelAPI.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

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
        if issubclass(POAddressModelAPI, dict):
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
        if not isinstance(other, POAddressModelAPI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
