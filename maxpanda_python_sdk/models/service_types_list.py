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

class ServiceTypesList(object):
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
        'service_type_id': 'int',
        'name': 'str',
        'service_type_status_ref': 'PartStatusRef',
        'type_ref': 'PartTypeRef',
        'preferred_supplier_ref': 'VendorDetailsRef',
        'unit_price': 'float',
        'sales_price': 'float',
        'notes': 'str'
    }

    attribute_map = {
        'site_ref': 'SiteRef',
        'service_type_id': 'ServiceTypeId',
        'name': 'Name',
        'service_type_status_ref': 'ServiceTypeStatusRef',
        'type_ref': 'TypeRef',
        'preferred_supplier_ref': 'PreferredSupplierRef',
        'unit_price': 'UnitPrice',
        'sales_price': 'SalesPrice',
        'notes': 'Notes'
    }

    def __init__(self, site_ref=None, service_type_id=None, name=None, service_type_status_ref=None, type_ref=None, preferred_supplier_ref=None, unit_price=None, sales_price=None, notes=None):  # noqa: E501
        """ServiceTypesList - a model defined in Swagger"""  # noqa: E501
        self._site_ref = None
        self._service_type_id = None
        self._name = None
        self._service_type_status_ref = None
        self._type_ref = None
        self._preferred_supplier_ref = None
        self._unit_price = None
        self._sales_price = None
        self._notes = None
        self.discriminator = None
        if site_ref is not None:
            self.site_ref = site_ref
        if service_type_id is not None:
            self.service_type_id = service_type_id
        if name is not None:
            self.name = name
        if service_type_status_ref is not None:
            self.service_type_status_ref = service_type_status_ref
        if type_ref is not None:
            self.type_ref = type_ref
        if preferred_supplier_ref is not None:
            self.preferred_supplier_ref = preferred_supplier_ref
        if unit_price is not None:
            self.unit_price = unit_price
        if sales_price is not None:
            self.sales_price = sales_price
        if notes is not None:
            self.notes = notes

    @property
    def site_ref(self):
        """Gets the site_ref of this ServiceTypesList.  # noqa: E501


        :return: The site_ref of this ServiceTypesList.  # noqa: E501
        :rtype: SiteRef
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this ServiceTypesList.


        :param site_ref: The site_ref of this ServiceTypesList.  # noqa: E501
        :type: SiteRef
        """

        self._site_ref = site_ref

    @property
    def service_type_id(self):
        """Gets the service_type_id of this ServiceTypesList.  # noqa: E501


        :return: The service_type_id of this ServiceTypesList.  # noqa: E501
        :rtype: int
        """
        return self._service_type_id

    @service_type_id.setter
    def service_type_id(self, service_type_id):
        """Sets the service_type_id of this ServiceTypesList.


        :param service_type_id: The service_type_id of this ServiceTypesList.  # noqa: E501
        :type: int
        """

        self._service_type_id = service_type_id

    @property
    def name(self):
        """Gets the name of this ServiceTypesList.  # noqa: E501


        :return: The name of this ServiceTypesList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceTypesList.


        :param name: The name of this ServiceTypesList.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def service_type_status_ref(self):
        """Gets the service_type_status_ref of this ServiceTypesList.  # noqa: E501


        :return: The service_type_status_ref of this ServiceTypesList.  # noqa: E501
        :rtype: PartStatusRef
        """
        return self._service_type_status_ref

    @service_type_status_ref.setter
    def service_type_status_ref(self, service_type_status_ref):
        """Sets the service_type_status_ref of this ServiceTypesList.


        :param service_type_status_ref: The service_type_status_ref of this ServiceTypesList.  # noqa: E501
        :type: PartStatusRef
        """

        self._service_type_status_ref = service_type_status_ref

    @property
    def type_ref(self):
        """Gets the type_ref of this ServiceTypesList.  # noqa: E501


        :return: The type_ref of this ServiceTypesList.  # noqa: E501
        :rtype: PartTypeRef
        """
        return self._type_ref

    @type_ref.setter
    def type_ref(self, type_ref):
        """Sets the type_ref of this ServiceTypesList.


        :param type_ref: The type_ref of this ServiceTypesList.  # noqa: E501
        :type: PartTypeRef
        """

        self._type_ref = type_ref

    @property
    def preferred_supplier_ref(self):
        """Gets the preferred_supplier_ref of this ServiceTypesList.  # noqa: E501


        :return: The preferred_supplier_ref of this ServiceTypesList.  # noqa: E501
        :rtype: VendorDetailsRef
        """
        return self._preferred_supplier_ref

    @preferred_supplier_ref.setter
    def preferred_supplier_ref(self, preferred_supplier_ref):
        """Sets the preferred_supplier_ref of this ServiceTypesList.


        :param preferred_supplier_ref: The preferred_supplier_ref of this ServiceTypesList.  # noqa: E501
        :type: VendorDetailsRef
        """

        self._preferred_supplier_ref = preferred_supplier_ref

    @property
    def unit_price(self):
        """Gets the unit_price of this ServiceTypesList.  # noqa: E501


        :return: The unit_price of this ServiceTypesList.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this ServiceTypesList.


        :param unit_price: The unit_price of this ServiceTypesList.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def sales_price(self):
        """Gets the sales_price of this ServiceTypesList.  # noqa: E501


        :return: The sales_price of this ServiceTypesList.  # noqa: E501
        :rtype: float
        """
        return self._sales_price

    @sales_price.setter
    def sales_price(self, sales_price):
        """Sets the sales_price of this ServiceTypesList.


        :param sales_price: The sales_price of this ServiceTypesList.  # noqa: E501
        :type: float
        """

        self._sales_price = sales_price

    @property
    def notes(self):
        """Gets the notes of this ServiceTypesList.  # noqa: E501


        :return: The notes of this ServiceTypesList.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ServiceTypesList.


        :param notes: The notes of this ServiceTypesList.  # noqa: E501
        :type: str
        """

        self._notes = notes

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
        if issubclass(ServiceTypesList, dict):
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
        if not isinstance(other, ServiceTypesList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
