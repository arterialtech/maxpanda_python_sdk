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

class WOPartRef(object):
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
        'id': 'int',
        'name': 'str',
        'on_hand': 'float',
        'used': 'float',
        'allocated': 'float'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'on_hand': 'OnHand',
        'used': 'Used',
        'allocated': 'Allocated'
    }

    def __init__(self, id=None, name=None, on_hand=None, used=None, allocated=None):  # noqa: E501
        """WOPartRef - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._on_hand = None
        self._used = None
        self._allocated = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if on_hand is not None:
            self.on_hand = on_hand
        if used is not None:
            self.used = used
        if allocated is not None:
            self.allocated = allocated

    @property
    def id(self):
        """Gets the id of this WOPartRef.  # noqa: E501


        :return: The id of this WOPartRef.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WOPartRef.


        :param id: The id of this WOPartRef.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WOPartRef.  # noqa: E501


        :return: The name of this WOPartRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WOPartRef.


        :param name: The name of this WOPartRef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def on_hand(self):
        """Gets the on_hand of this WOPartRef.  # noqa: E501


        :return: The on_hand of this WOPartRef.  # noqa: E501
        :rtype: float
        """
        return self._on_hand

    @on_hand.setter
    def on_hand(self, on_hand):
        """Sets the on_hand of this WOPartRef.


        :param on_hand: The on_hand of this WOPartRef.  # noqa: E501
        :type: float
        """

        self._on_hand = on_hand

    @property
    def used(self):
        """Gets the used of this WOPartRef.  # noqa: E501


        :return: The used of this WOPartRef.  # noqa: E501
        :rtype: float
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this WOPartRef.


        :param used: The used of this WOPartRef.  # noqa: E501
        :type: float
        """

        self._used = used

    @property
    def allocated(self):
        """Gets the allocated of this WOPartRef.  # noqa: E501


        :return: The allocated of this WOPartRef.  # noqa: E501
        :rtype: float
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this WOPartRef.


        :param allocated: The allocated of this WOPartRef.  # noqa: E501
        :type: float
        """

        self._allocated = allocated

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
        if issubclass(WOPartRef, dict):
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
        if not isinstance(other, WOPartRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
