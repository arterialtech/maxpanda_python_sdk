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

class CreateTaskTemplateField(object):
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
        'field_name': 'str',
        'field_type': 'int',
        'field_value': 'str',
        'sort_order': 'int',
        'is_required': 'bool',
        'task_id': 'int'
    }

    attribute_map = {
        'field_name': 'FieldName',
        'field_type': 'FieldType',
        'field_value': 'FieldValue',
        'sort_order': 'SortOrder',
        'is_required': 'IsRequired',
        'task_id': 'TaskId'
    }

    def __init__(self, field_name=None, field_type=None, field_value=None, sort_order=None, is_required=None, task_id=None):  # noqa: E501
        """CreateTaskTemplateField - a model defined in Swagger"""  # noqa: E501
        self._field_name = None
        self._field_type = None
        self._field_value = None
        self._sort_order = None
        self._is_required = None
        self._task_id = None
        self.discriminator = None
        self.field_name = field_name
        self.field_type = field_type
        if field_value is not None:
            self.field_value = field_value
        if sort_order is not None:
            self.sort_order = sort_order
        self.is_required = is_required
        self.task_id = task_id

    @property
    def field_name(self):
        """Gets the field_name of this CreateTaskTemplateField.  # noqa: E501

        Name of the Task Field  # noqa: E501

        :return: The field_name of this CreateTaskTemplateField.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this CreateTaskTemplateField.

        Name of the Task Field  # noqa: E501

        :param field_name: The field_name of this CreateTaskTemplateField.  # noqa: E501
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501

        self._field_name = field_name

    @property
    def field_type(self):
        """Gets the field_type of this CreateTaskTemplateField.  # noqa: E501

        Type of the Task Field  # noqa: E501

        :return: The field_type of this CreateTaskTemplateField.  # noqa: E501
        :rtype: int
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this CreateTaskTemplateField.

        Type of the Task Field  # noqa: E501

        :param field_type: The field_type of this CreateTaskTemplateField.  # noqa: E501
        :type: int
        """
        if field_type is None:
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501

        self._field_type = field_type

    @property
    def field_value(self):
        """Gets the field_value of this CreateTaskTemplateField.  # noqa: E501

        Value of the Task Field  # noqa: E501

        :return: The field_value of this CreateTaskTemplateField.  # noqa: E501
        :rtype: str
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        """Sets the field_value of this CreateTaskTemplateField.

        Value of the Task Field  # noqa: E501

        :param field_value: The field_value of this CreateTaskTemplateField.  # noqa: E501
        :type: str
        """

        self._field_value = field_value

    @property
    def sort_order(self):
        """Gets the sort_order of this CreateTaskTemplateField.  # noqa: E501

        Order of Sorting  # noqa: E501

        :return: The sort_order of this CreateTaskTemplateField.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this CreateTaskTemplateField.

        Order of Sorting  # noqa: E501

        :param sort_order: The sort_order of this CreateTaskTemplateField.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def is_required(self):
        """Gets the is_required of this CreateTaskTemplateField.  # noqa: E501

        Set true if the field is mandatory  # noqa: E501

        :return: The is_required of this CreateTaskTemplateField.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this CreateTaskTemplateField.

        Set true if the field is mandatory  # noqa: E501

        :param is_required: The is_required of this CreateTaskTemplateField.  # noqa: E501
        :type: bool
        """
        if is_required is None:
            raise ValueError("Invalid value for `is_required`, must not be `None`")  # noqa: E501

        self._is_required = is_required

    @property
    def task_id(self):
        """Gets the task_id of this CreateTaskTemplateField.  # noqa: E501

        Id of Task.Task Id can be found in your Maxpanda Task Library Index or Task API.  # noqa: E501

        :return: The task_id of this CreateTaskTemplateField.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CreateTaskTemplateField.

        Id of Task.Task Id can be found in your Maxpanda Task Library Index or Task API.  # noqa: E501

        :param task_id: The task_id of this CreateTaskTemplateField.  # noqa: E501
        :type: int
        """
        if task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501

        self._task_id = task_id

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
        if issubclass(CreateTaskTemplateField, dict):
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
        if not isinstance(other, CreateTaskTemplateField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
