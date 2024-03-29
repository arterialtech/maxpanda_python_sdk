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

class CreateTaskModel(object):
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
        'name': 'str',
        'task_priority_id': 'int',
        'sites_id': 'list[int]',
        'description': 'str',
        'fields': 'list[CreateTaskField]'
    }

    attribute_map = {
        'name': 'Name',
        'task_priority_id': 'TaskPriorityId',
        'sites_id': 'SitesId',
        'description': 'Description',
        'fields': 'Fields'
    }

    def __init__(self, name=None, task_priority_id=None, sites_id=None, description=None, fields=None):  # noqa: E501
        """CreateTaskModel - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._task_priority_id = None
        self._sites_id = None
        self._description = None
        self._fields = None
        self.discriminator = None
        self.name = name
        if task_priority_id is not None:
            self.task_priority_id = task_priority_id
        self.sites_id = sites_id
        self.description = description
        self.fields = fields

    @property
    def name(self):
        """Gets the name of this CreateTaskModel.  # noqa: E501

        Name of the Task  # noqa: E501

        :return: The name of this CreateTaskModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTaskModel.

        Name of the Task  # noqa: E501

        :param name: The name of this CreateTaskModel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def task_priority_id(self):
        """Gets the task_priority_id of this CreateTaskModel.  # noqa: E501

        Priority of the Task. Task Priority Id can be found in your Maxpanda Company Task Priority or Task Priority API  # noqa: E501

        :return: The task_priority_id of this CreateTaskModel.  # noqa: E501
        :rtype: int
        """
        return self._task_priority_id

    @task_priority_id.setter
    def task_priority_id(self, task_priority_id):
        """Sets the task_priority_id of this CreateTaskModel.

        Priority of the Task. Task Priority Id can be found in your Maxpanda Company Task Priority or Task Priority API  # noqa: E501

        :param task_priority_id: The task_priority_id of this CreateTaskModel.  # noqa: E501
        :type: int
        """

        self._task_priority_id = task_priority_id

    @property
    def sites_id(self):
        """Gets the sites_id of this CreateTaskModel.  # noqa: E501

        Site Id of the Task. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :return: The sites_id of this CreateTaskModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._sites_id

    @sites_id.setter
    def sites_id(self, sites_id):
        """Sets the sites_id of this CreateTaskModel.

        Site Id of the Task. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :param sites_id: The sites_id of this CreateTaskModel.  # noqa: E501
        :type: list[int]
        """
        if sites_id is None:
            raise ValueError("Invalid value for `sites_id`, must not be `None`")  # noqa: E501

        self._sites_id = sites_id

    @property
    def description(self):
        """Gets the description of this CreateTaskModel.  # noqa: E501

        Description about the Task  # noqa: E501

        :return: The description of this CreateTaskModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTaskModel.

        Description about the Task  # noqa: E501

        :param description: The description of this CreateTaskModel.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def fields(self):
        """Gets the fields of this CreateTaskModel.  # noqa: E501


        :return: The fields of this CreateTaskModel.  # noqa: E501
        :rtype: list[CreateTaskField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CreateTaskModel.


        :param fields: The fields of this CreateTaskModel.  # noqa: E501
        :type: list[CreateTaskField]
        """
        if fields is None:
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

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
        if issubclass(CreateTaskModel, dict):
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
        if not isinstance(other, CreateTaskModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
