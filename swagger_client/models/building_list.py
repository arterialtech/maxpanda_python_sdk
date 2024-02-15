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

class BuildingList(object):
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
        'building_id': 'str',
        'name': 'str',
        'account_number': 'str',
        'description': 'str',
        'building_group_ref': 'DepartmentRef',
        'building_address': 'Address',
        'location_ref': 'list[LocationRef]'
    }

    attribute_map = {
        'site_ref': 'SiteRef',
        'building_id': 'BuildingId',
        'name': 'Name',
        'account_number': 'AccountNumber',
        'description': 'Description',
        'building_group_ref': 'BuildingGroupRef',
        'building_address': 'BuildingAddress',
        'location_ref': 'LocationRef'
    }

    def __init__(self, site_ref=None, building_id=None, name=None, account_number=None, description=None, building_group_ref=None, building_address=None, location_ref=None):  # noqa: E501
        """BuildingList - a model defined in Swagger"""  # noqa: E501
        self._site_ref = None
        self._building_id = None
        self._name = None
        self._account_number = None
        self._description = None
        self._building_group_ref = None
        self._building_address = None
        self._location_ref = None
        self.discriminator = None
        if site_ref is not None:
            self.site_ref = site_ref
        if building_id is not None:
            self.building_id = building_id
        if name is not None:
            self.name = name
        if account_number is not None:
            self.account_number = account_number
        if description is not None:
            self.description = description
        if building_group_ref is not None:
            self.building_group_ref = building_group_ref
        if building_address is not None:
            self.building_address = building_address
        if location_ref is not None:
            self.location_ref = location_ref

    @property
    def site_ref(self):
        """Gets the site_ref of this BuildingList.  # noqa: E501


        :return: The site_ref of this BuildingList.  # noqa: E501
        :rtype: SiteRef
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this BuildingList.


        :param site_ref: The site_ref of this BuildingList.  # noqa: E501
        :type: SiteRef
        """

        self._site_ref = site_ref

    @property
    def building_id(self):
        """Gets the building_id of this BuildingList.  # noqa: E501


        :return: The building_id of this BuildingList.  # noqa: E501
        :rtype: str
        """
        return self._building_id

    @building_id.setter
    def building_id(self, building_id):
        """Sets the building_id of this BuildingList.


        :param building_id: The building_id of this BuildingList.  # noqa: E501
        :type: str
        """

        self._building_id = building_id

    @property
    def name(self):
        """Gets the name of this BuildingList.  # noqa: E501


        :return: The name of this BuildingList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuildingList.


        :param name: The name of this BuildingList.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account_number(self):
        """Gets the account_number of this BuildingList.  # noqa: E501


        :return: The account_number of this BuildingList.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this BuildingList.


        :param account_number: The account_number of this BuildingList.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def description(self):
        """Gets the description of this BuildingList.  # noqa: E501


        :return: The description of this BuildingList.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BuildingList.


        :param description: The description of this BuildingList.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def building_group_ref(self):
        """Gets the building_group_ref of this BuildingList.  # noqa: E501


        :return: The building_group_ref of this BuildingList.  # noqa: E501
        :rtype: DepartmentRef
        """
        return self._building_group_ref

    @building_group_ref.setter
    def building_group_ref(self, building_group_ref):
        """Sets the building_group_ref of this BuildingList.


        :param building_group_ref: The building_group_ref of this BuildingList.  # noqa: E501
        :type: DepartmentRef
        """

        self._building_group_ref = building_group_ref

    @property
    def building_address(self):
        """Gets the building_address of this BuildingList.  # noqa: E501


        :return: The building_address of this BuildingList.  # noqa: E501
        :rtype: Address
        """
        return self._building_address

    @building_address.setter
    def building_address(self, building_address):
        """Sets the building_address of this BuildingList.


        :param building_address: The building_address of this BuildingList.  # noqa: E501
        :type: Address
        """

        self._building_address = building_address

    @property
    def location_ref(self):
        """Gets the location_ref of this BuildingList.  # noqa: E501


        :return: The location_ref of this BuildingList.  # noqa: E501
        :rtype: list[LocationRef]
        """
        return self._location_ref

    @location_ref.setter
    def location_ref(self, location_ref):
        """Sets the location_ref of this BuildingList.


        :param location_ref: The location_ref of this BuildingList.  # noqa: E501
        :type: list[LocationRef]
        """

        self._location_ref = location_ref

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
        if issubclass(BuildingList, dict):
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
        if not isinstance(other, BuildingList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
