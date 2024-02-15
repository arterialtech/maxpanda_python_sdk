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

class TaskFieldRef(object):
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
        'field_name': 'str',
        'field_type': 'int',
        'field_type_name': 'str',
        'is_required': 'bool',
        'is_range_defined': 'bool',
        'range_min_value': 'str',
        'range_max_value': 'str',
        'sort_order': 'int'
    }

    attribute_map = {
        'id': 'Id',
        'field_name': 'FieldName',
        'field_type': 'FieldType',
        'field_type_name': 'FieldTypeName',
        'is_required': 'IsRequired',
        'is_range_defined': 'IsRangeDefined',
        'range_min_value': 'RangeMinValue',
        'range_max_value': 'RangeMaxValue',
        'sort_order': 'SortOrder'
    }

    def __init__(self, id=None, field_name=None, field_type=None, field_type_name=None, is_required=None, is_range_defined=None, range_min_value=None, range_max_value=None, sort_order=None):  # noqa: E501
        """TaskFieldRef - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._field_name = None
        self._field_type = None
        self._field_type_name = None
        self._is_required = None
        self._is_range_defined = None
        self._range_min_value = None
        self._range_max_value = None
        self._sort_order = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if field_name is not None:
            self.field_name = field_name
        if field_type is not None:
            self.field_type = field_type
        if field_type_name is not None:
            self.field_type_name = field_type_name
        if is_required is not None:
            self.is_required = is_required
        if is_range_defined is not None:
            self.is_range_defined = is_range_defined
        if range_min_value is not None:
            self.range_min_value = range_min_value
        if range_max_value is not None:
            self.range_max_value = range_max_value
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def id(self):
        """Gets the id of this TaskFieldRef.  # noqa: E501


        :return: The id of this TaskFieldRef.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskFieldRef.


        :param id: The id of this TaskFieldRef.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def field_name(self):
        """Gets the field_name of this TaskFieldRef.  # noqa: E501


        :return: The field_name of this TaskFieldRef.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this TaskFieldRef.


        :param field_name: The field_name of this TaskFieldRef.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def field_type(self):
        """Gets the field_type of this TaskFieldRef.  # noqa: E501


        :return: The field_type of this TaskFieldRef.  # noqa: E501
        :rtype: int
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this TaskFieldRef.


        :param field_type: The field_type of this TaskFieldRef.  # noqa: E501
        :type: int
        """

        self._field_type = field_type

    @property
    def field_type_name(self):
        """Gets the field_type_name of this TaskFieldRef.  # noqa: E501


        :return: The field_type_name of this TaskFieldRef.  # noqa: E501
        :rtype: str
        """
        return self._field_type_name

    @field_type_name.setter
    def field_type_name(self, field_type_name):
        """Sets the field_type_name of this TaskFieldRef.


        :param field_type_name: The field_type_name of this TaskFieldRef.  # noqa: E501
        :type: str
        """

        self._field_type_name = field_type_name

    @property
    def is_required(self):
        """Gets the is_required of this TaskFieldRef.  # noqa: E501


        :return: The is_required of this TaskFieldRef.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this TaskFieldRef.


        :param is_required: The is_required of this TaskFieldRef.  # noqa: E501
        :type: bool
        """

        self._is_required = is_required

    @property
    def is_range_defined(self):
        """Gets the is_range_defined of this TaskFieldRef.  # noqa: E501


        :return: The is_range_defined of this TaskFieldRef.  # noqa: E501
        :rtype: bool
        """
        return self._is_range_defined

    @is_range_defined.setter
    def is_range_defined(self, is_range_defined):
        """Sets the is_range_defined of this TaskFieldRef.


        :param is_range_defined: The is_range_defined of this TaskFieldRef.  # noqa: E501
        :type: bool
        """

        self._is_range_defined = is_range_defined

    @property
    def range_min_value(self):
        """Gets the range_min_value of this TaskFieldRef.  # noqa: E501


        :return: The range_min_value of this TaskFieldRef.  # noqa: E501
        :rtype: str
        """
        return self._range_min_value

    @range_min_value.setter
    def range_min_value(self, range_min_value):
        """Sets the range_min_value of this TaskFieldRef.


        :param range_min_value: The range_min_value of this TaskFieldRef.  # noqa: E501
        :type: str
        """

        self._range_min_value = range_min_value

    @property
    def range_max_value(self):
        """Gets the range_max_value of this TaskFieldRef.  # noqa: E501


        :return: The range_max_value of this TaskFieldRef.  # noqa: E501
        :rtype: str
        """
        return self._range_max_value

    @range_max_value.setter
    def range_max_value(self, range_max_value):
        """Sets the range_max_value of this TaskFieldRef.


        :param range_max_value: The range_max_value of this TaskFieldRef.  # noqa: E501
        :type: str
        """

        self._range_max_value = range_max_value

    @property
    def sort_order(self):
        """Gets the sort_order of this TaskFieldRef.  # noqa: E501


        :return: The sort_order of this TaskFieldRef.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this TaskFieldRef.


        :param sort_order: The sort_order of this TaskFieldRef.  # noqa: E501
        :type: int
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
        if issubclass(TaskFieldRef, dict):
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
        if not isinstance(other, TaskFieldRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
