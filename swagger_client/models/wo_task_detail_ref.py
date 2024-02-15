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

class WOTaskDetailRef(object):
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
        'description': 'str',
        'priority_ref': 'TaskPriorityDetails',
        'comment': 'str',
        'status_ref': 'TaskStatusAPIListModel',
        'notify_users': 'str',
        'vendor': 'VendorDetail',
        'staff': 'UserDetail',
        'sort_order': 'int',
        'fields': 'list[WOTaskFieldDetail]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'priority_ref': 'PriorityRef',
        'comment': 'Comment',
        'status_ref': 'StatusRef',
        'notify_users': 'NotifyUsers',
        'vendor': 'Vendor',
        'staff': 'Staff',
        'sort_order': 'SortOrder',
        'fields': 'Fields'
    }

    def __init__(self, id=None, name=None, description=None, priority_ref=None, comment=None, status_ref=None, notify_users=None, vendor=None, staff=None, sort_order=None, fields=None):  # noqa: E501
        """WOTaskDetailRef - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._priority_ref = None
        self._comment = None
        self._status_ref = None
        self._notify_users = None
        self._vendor = None
        self._staff = None
        self._sort_order = None
        self._fields = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if priority_ref is not None:
            self.priority_ref = priority_ref
        if comment is not None:
            self.comment = comment
        if status_ref is not None:
            self.status_ref = status_ref
        if notify_users is not None:
            self.notify_users = notify_users
        if vendor is not None:
            self.vendor = vendor
        if staff is not None:
            self.staff = staff
        if sort_order is not None:
            self.sort_order = sort_order
        if fields is not None:
            self.fields = fields

    @property
    def id(self):
        """Gets the id of this WOTaskDetailRef.  # noqa: E501


        :return: The id of this WOTaskDetailRef.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WOTaskDetailRef.


        :param id: The id of this WOTaskDetailRef.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WOTaskDetailRef.  # noqa: E501


        :return: The name of this WOTaskDetailRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WOTaskDetailRef.


        :param name: The name of this WOTaskDetailRef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this WOTaskDetailRef.  # noqa: E501


        :return: The description of this WOTaskDetailRef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WOTaskDetailRef.


        :param description: The description of this WOTaskDetailRef.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def priority_ref(self):
        """Gets the priority_ref of this WOTaskDetailRef.  # noqa: E501


        :return: The priority_ref of this WOTaskDetailRef.  # noqa: E501
        :rtype: TaskPriorityDetails
        """
        return self._priority_ref

    @priority_ref.setter
    def priority_ref(self, priority_ref):
        """Sets the priority_ref of this WOTaskDetailRef.


        :param priority_ref: The priority_ref of this WOTaskDetailRef.  # noqa: E501
        :type: TaskPriorityDetails
        """

        self._priority_ref = priority_ref

    @property
    def comment(self):
        """Gets the comment of this WOTaskDetailRef.  # noqa: E501


        :return: The comment of this WOTaskDetailRef.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this WOTaskDetailRef.


        :param comment: The comment of this WOTaskDetailRef.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def status_ref(self):
        """Gets the status_ref of this WOTaskDetailRef.  # noqa: E501


        :return: The status_ref of this WOTaskDetailRef.  # noqa: E501
        :rtype: TaskStatusAPIListModel
        """
        return self._status_ref

    @status_ref.setter
    def status_ref(self, status_ref):
        """Sets the status_ref of this WOTaskDetailRef.


        :param status_ref: The status_ref of this WOTaskDetailRef.  # noqa: E501
        :type: TaskStatusAPIListModel
        """

        self._status_ref = status_ref

    @property
    def notify_users(self):
        """Gets the notify_users of this WOTaskDetailRef.  # noqa: E501


        :return: The notify_users of this WOTaskDetailRef.  # noqa: E501
        :rtype: str
        """
        return self._notify_users

    @notify_users.setter
    def notify_users(self, notify_users):
        """Sets the notify_users of this WOTaskDetailRef.


        :param notify_users: The notify_users of this WOTaskDetailRef.  # noqa: E501
        :type: str
        """

        self._notify_users = notify_users

    @property
    def vendor(self):
        """Gets the vendor of this WOTaskDetailRef.  # noqa: E501


        :return: The vendor of this WOTaskDetailRef.  # noqa: E501
        :rtype: VendorDetail
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this WOTaskDetailRef.


        :param vendor: The vendor of this WOTaskDetailRef.  # noqa: E501
        :type: VendorDetail
        """

        self._vendor = vendor

    @property
    def staff(self):
        """Gets the staff of this WOTaskDetailRef.  # noqa: E501


        :return: The staff of this WOTaskDetailRef.  # noqa: E501
        :rtype: UserDetail
        """
        return self._staff

    @staff.setter
    def staff(self, staff):
        """Sets the staff of this WOTaskDetailRef.


        :param staff: The staff of this WOTaskDetailRef.  # noqa: E501
        :type: UserDetail
        """

        self._staff = staff

    @property
    def sort_order(self):
        """Gets the sort_order of this WOTaskDetailRef.  # noqa: E501


        :return: The sort_order of this WOTaskDetailRef.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this WOTaskDetailRef.


        :param sort_order: The sort_order of this WOTaskDetailRef.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def fields(self):
        """Gets the fields of this WOTaskDetailRef.  # noqa: E501


        :return: The fields of this WOTaskDetailRef.  # noqa: E501
        :rtype: list[WOTaskFieldDetail]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this WOTaskDetailRef.


        :param fields: The fields of this WOTaskDetailRef.  # noqa: E501
        :type: list[WOTaskFieldDetail]
        """

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
        if issubclass(WOTaskDetailRef, dict):
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
        if not isinstance(other, WOTaskDetailRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other