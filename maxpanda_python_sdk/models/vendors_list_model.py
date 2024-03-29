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

class VendorsListModel(object):
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
        'site_ref': 'list[SiteRef]',
        'vendor_id': 'int',
        'name': 'str',
        'phone': 'str',
        'email': 'str',
        'invited': 'str',
        'building_ref': 'list[BuildingDetails]',
        'location_ref': 'list[LocationRef]',
        'notes': 'str',
        'contract_start_date': 'datetime',
        'contract_end_date': 'datetime',
        'vendor_address': 'AddressAPIModel'
    }

    attribute_map = {
        'site_ref': 'SiteRef',
        'vendor_id': 'VendorId',
        'name': 'Name',
        'phone': 'Phone',
        'email': 'Email',
        'invited': 'Invited',
        'building_ref': 'BuildingRef',
        'location_ref': 'LocationRef',
        'notes': 'Notes',
        'contract_start_date': 'ContractStartDate',
        'contract_end_date': 'ContractEndDate',
        'vendor_address': 'VendorAddress'
    }

    def __init__(self, site_ref=None, vendor_id=None, name=None, phone=None, email=None, invited=None, building_ref=None, location_ref=None, notes=None, contract_start_date=None, contract_end_date=None, vendor_address=None):  # noqa: E501
        """VendorsListModel - a model defined in Swagger"""  # noqa: E501
        self._site_ref = None
        self._vendor_id = None
        self._name = None
        self._phone = None
        self._email = None
        self._invited = None
        self._building_ref = None
        self._location_ref = None
        self._notes = None
        self._contract_start_date = None
        self._contract_end_date = None
        self._vendor_address = None
        self.discriminator = None
        if site_ref is not None:
            self.site_ref = site_ref
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if invited is not None:
            self.invited = invited
        if building_ref is not None:
            self.building_ref = building_ref
        if location_ref is not None:
            self.location_ref = location_ref
        if notes is not None:
            self.notes = notes
        if contract_start_date is not None:
            self.contract_start_date = contract_start_date
        if contract_end_date is not None:
            self.contract_end_date = contract_end_date
        if vendor_address is not None:
            self.vendor_address = vendor_address

    @property
    def site_ref(self):
        """Gets the site_ref of this VendorsListModel.  # noqa: E501


        :return: The site_ref of this VendorsListModel.  # noqa: E501
        :rtype: list[SiteRef]
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this VendorsListModel.


        :param site_ref: The site_ref of this VendorsListModel.  # noqa: E501
        :type: list[SiteRef]
        """

        self._site_ref = site_ref

    @property
    def vendor_id(self):
        """Gets the vendor_id of this VendorsListModel.  # noqa: E501


        :return: The vendor_id of this VendorsListModel.  # noqa: E501
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this VendorsListModel.


        :param vendor_id: The vendor_id of this VendorsListModel.  # noqa: E501
        :type: int
        """

        self._vendor_id = vendor_id

    @property
    def name(self):
        """Gets the name of this VendorsListModel.  # noqa: E501


        :return: The name of this VendorsListModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VendorsListModel.


        :param name: The name of this VendorsListModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this VendorsListModel.  # noqa: E501


        :return: The phone of this VendorsListModel.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this VendorsListModel.


        :param phone: The phone of this VendorsListModel.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this VendorsListModel.  # noqa: E501


        :return: The email of this VendorsListModel.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this VendorsListModel.


        :param email: The email of this VendorsListModel.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def invited(self):
        """Gets the invited of this VendorsListModel.  # noqa: E501


        :return: The invited of this VendorsListModel.  # noqa: E501
        :rtype: str
        """
        return self._invited

    @invited.setter
    def invited(self, invited):
        """Sets the invited of this VendorsListModel.


        :param invited: The invited of this VendorsListModel.  # noqa: E501
        :type: str
        """

        self._invited = invited

    @property
    def building_ref(self):
        """Gets the building_ref of this VendorsListModel.  # noqa: E501


        :return: The building_ref of this VendorsListModel.  # noqa: E501
        :rtype: list[BuildingDetails]
        """
        return self._building_ref

    @building_ref.setter
    def building_ref(self, building_ref):
        """Sets the building_ref of this VendorsListModel.


        :param building_ref: The building_ref of this VendorsListModel.  # noqa: E501
        :type: list[BuildingDetails]
        """

        self._building_ref = building_ref

    @property
    def location_ref(self):
        """Gets the location_ref of this VendorsListModel.  # noqa: E501


        :return: The location_ref of this VendorsListModel.  # noqa: E501
        :rtype: list[LocationRef]
        """
        return self._location_ref

    @location_ref.setter
    def location_ref(self, location_ref):
        """Sets the location_ref of this VendorsListModel.


        :param location_ref: The location_ref of this VendorsListModel.  # noqa: E501
        :type: list[LocationRef]
        """

        self._location_ref = location_ref

    @property
    def notes(self):
        """Gets the notes of this VendorsListModel.  # noqa: E501


        :return: The notes of this VendorsListModel.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this VendorsListModel.


        :param notes: The notes of this VendorsListModel.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def contract_start_date(self):
        """Gets the contract_start_date of this VendorsListModel.  # noqa: E501


        :return: The contract_start_date of this VendorsListModel.  # noqa: E501
        :rtype: datetime
        """
        return self._contract_start_date

    @contract_start_date.setter
    def contract_start_date(self, contract_start_date):
        """Sets the contract_start_date of this VendorsListModel.


        :param contract_start_date: The contract_start_date of this VendorsListModel.  # noqa: E501
        :type: datetime
        """

        self._contract_start_date = contract_start_date

    @property
    def contract_end_date(self):
        """Gets the contract_end_date of this VendorsListModel.  # noqa: E501


        :return: The contract_end_date of this VendorsListModel.  # noqa: E501
        :rtype: datetime
        """
        return self._contract_end_date

    @contract_end_date.setter
    def contract_end_date(self, contract_end_date):
        """Sets the contract_end_date of this VendorsListModel.


        :param contract_end_date: The contract_end_date of this VendorsListModel.  # noqa: E501
        :type: datetime
        """

        self._contract_end_date = contract_end_date

    @property
    def vendor_address(self):
        """Gets the vendor_address of this VendorsListModel.  # noqa: E501


        :return: The vendor_address of this VendorsListModel.  # noqa: E501
        :rtype: AddressAPIModel
        """
        return self._vendor_address

    @vendor_address.setter
    def vendor_address(self, vendor_address):
        """Sets the vendor_address of this VendorsListModel.


        :param vendor_address: The vendor_address of this VendorsListModel.  # noqa: E501
        :type: AddressAPIModel
        """

        self._vendor_address = vendor_address

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
        if issubclass(VendorsListModel, dict):
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
        if not isinstance(other, VendorsListModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
