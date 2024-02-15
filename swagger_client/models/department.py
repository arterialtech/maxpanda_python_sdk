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

class Department(object):
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
        'building_group_id': 'int',
        'name': 'str',
        'site_ref': 'list[SiteRef]'
    }

    attribute_map = {
        'building_group_id': 'BuildingGroupId',
        'name': 'Name',
        'site_ref': 'SiteRef'
    }

    def __init__(self, building_group_id=None, name=None, site_ref=None):  # noqa: E501
        """Department - a model defined in Swagger"""  # noqa: E501
        self._building_group_id = None
        self._name = None
        self._site_ref = None
        self.discriminator = None
        if building_group_id is not None:
            self.building_group_id = building_group_id
        if name is not None:
            self.name = name
        if site_ref is not None:
            self.site_ref = site_ref

    @property
    def building_group_id(self):
        """Gets the building_group_id of this Department.  # noqa: E501


        :return: The building_group_id of this Department.  # noqa: E501
        :rtype: int
        """
        return self._building_group_id

    @building_group_id.setter
    def building_group_id(self, building_group_id):
        """Sets the building_group_id of this Department.


        :param building_group_id: The building_group_id of this Department.  # noqa: E501
        :type: int
        """

        self._building_group_id = building_group_id

    @property
    def name(self):
        """Gets the name of this Department.  # noqa: E501


        :return: The name of this Department.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Department.


        :param name: The name of this Department.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def site_ref(self):
        """Gets the site_ref of this Department.  # noqa: E501


        :return: The site_ref of this Department.  # noqa: E501
        :rtype: list[SiteRef]
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this Department.


        :param site_ref: The site_ref of this Department.  # noqa: E501
        :type: list[SiteRef]
        """

        self._site_ref = site_ref

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
        if issubclass(Department, dict):
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
        if not isinstance(other, Department):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
