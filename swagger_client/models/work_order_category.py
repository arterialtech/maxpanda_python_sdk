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

class WorkOrderCategory(object):
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
        'work_order_category_id': 'int',
        'name': 'str',
        'site_ref': 'list[SiteRef]'
    }

    attribute_map = {
        'work_order_category_id': 'WorkOrderCategoryId',
        'name': 'Name',
        'site_ref': 'SiteRef'
    }

    def __init__(self, work_order_category_id=None, name=None, site_ref=None):  # noqa: E501
        """WorkOrderCategory - a model defined in Swagger"""  # noqa: E501
        self._work_order_category_id = None
        self._name = None
        self._site_ref = None
        self.discriminator = None
        if work_order_category_id is not None:
            self.work_order_category_id = work_order_category_id
        if name is not None:
            self.name = name
        if site_ref is not None:
            self.site_ref = site_ref

    @property
    def work_order_category_id(self):
        """Gets the work_order_category_id of this WorkOrderCategory.  # noqa: E501


        :return: The work_order_category_id of this WorkOrderCategory.  # noqa: E501
        :rtype: int
        """
        return self._work_order_category_id

    @work_order_category_id.setter
    def work_order_category_id(self, work_order_category_id):
        """Sets the work_order_category_id of this WorkOrderCategory.


        :param work_order_category_id: The work_order_category_id of this WorkOrderCategory.  # noqa: E501
        :type: int
        """

        self._work_order_category_id = work_order_category_id

    @property
    def name(self):
        """Gets the name of this WorkOrderCategory.  # noqa: E501


        :return: The name of this WorkOrderCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkOrderCategory.


        :param name: The name of this WorkOrderCategory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def site_ref(self):
        """Gets the site_ref of this WorkOrderCategory.  # noqa: E501


        :return: The site_ref of this WorkOrderCategory.  # noqa: E501
        :rtype: list[SiteRef]
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this WorkOrderCategory.


        :param site_ref: The site_ref of this WorkOrderCategory.  # noqa: E501
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
        if issubclass(WorkOrderCategory, dict):
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
        if not isinstance(other, WorkOrderCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
