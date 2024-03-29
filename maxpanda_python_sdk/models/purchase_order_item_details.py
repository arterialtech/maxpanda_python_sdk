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

class PurchaseOrderItemDetails(object):
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
        'purchase_order_item_id': 'int',
        'name': 'str',
        'part_number': 'str',
        'mfr_part_number': 'str',
        'bin_loc_num': 'str',
        'bin_name': 'str',
        'update_bin_quantity_to_inventory': 'bool',
        'unit_price': 'float',
        'ordered_quantity': 'float',
        'total_ordered_amount': 'float'
    }

    attribute_map = {
        'purchase_order_item_id': 'PurchaseOrderItemId',
        'name': 'Name',
        'part_number': 'PartNumber',
        'mfr_part_number': 'MfrPartNumber',
        'bin_loc_num': 'BinLocNum',
        'bin_name': 'BinName',
        'update_bin_quantity_to_inventory': 'UpdateBinQuantityToInventory',
        'unit_price': 'UnitPrice',
        'ordered_quantity': 'OrderedQuantity',
        'total_ordered_amount': 'TotalOrderedAmount'
    }

    def __init__(self, purchase_order_item_id=None, name=None, part_number=None, mfr_part_number=None, bin_loc_num=None, bin_name=None, update_bin_quantity_to_inventory=None, unit_price=None, ordered_quantity=None, total_ordered_amount=None):  # noqa: E501
        """PurchaseOrderItemDetails - a model defined in Swagger"""  # noqa: E501
        self._purchase_order_item_id = None
        self._name = None
        self._part_number = None
        self._mfr_part_number = None
        self._bin_loc_num = None
        self._bin_name = None
        self._update_bin_quantity_to_inventory = None
        self._unit_price = None
        self._ordered_quantity = None
        self._total_ordered_amount = None
        self.discriminator = None
        if purchase_order_item_id is not None:
            self.purchase_order_item_id = purchase_order_item_id
        if name is not None:
            self.name = name
        if part_number is not None:
            self.part_number = part_number
        if mfr_part_number is not None:
            self.mfr_part_number = mfr_part_number
        if bin_loc_num is not None:
            self.bin_loc_num = bin_loc_num
        if bin_name is not None:
            self.bin_name = bin_name
        if update_bin_quantity_to_inventory is not None:
            self.update_bin_quantity_to_inventory = update_bin_quantity_to_inventory
        if unit_price is not None:
            self.unit_price = unit_price
        if ordered_quantity is not None:
            self.ordered_quantity = ordered_quantity
        if total_ordered_amount is not None:
            self.total_ordered_amount = total_ordered_amount

    @property
    def purchase_order_item_id(self):
        """Gets the purchase_order_item_id of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The purchase_order_item_id of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: int
        """
        return self._purchase_order_item_id

    @purchase_order_item_id.setter
    def purchase_order_item_id(self, purchase_order_item_id):
        """Sets the purchase_order_item_id of this PurchaseOrderItemDetails.


        :param purchase_order_item_id: The purchase_order_item_id of this PurchaseOrderItemDetails.  # noqa: E501
        :type: int
        """

        self._purchase_order_item_id = purchase_order_item_id

    @property
    def name(self):
        """Gets the name of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The name of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PurchaseOrderItemDetails.


        :param name: The name of this PurchaseOrderItemDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def part_number(self):
        """Gets the part_number of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The part_number of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this PurchaseOrderItemDetails.


        :param part_number: The part_number of this PurchaseOrderItemDetails.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def mfr_part_number(self):
        """Gets the mfr_part_number of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The mfr_part_number of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: str
        """
        return self._mfr_part_number

    @mfr_part_number.setter
    def mfr_part_number(self, mfr_part_number):
        """Sets the mfr_part_number of this PurchaseOrderItemDetails.


        :param mfr_part_number: The mfr_part_number of this PurchaseOrderItemDetails.  # noqa: E501
        :type: str
        """

        self._mfr_part_number = mfr_part_number

    @property
    def bin_loc_num(self):
        """Gets the bin_loc_num of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The bin_loc_num of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: str
        """
        return self._bin_loc_num

    @bin_loc_num.setter
    def bin_loc_num(self, bin_loc_num):
        """Sets the bin_loc_num of this PurchaseOrderItemDetails.


        :param bin_loc_num: The bin_loc_num of this PurchaseOrderItemDetails.  # noqa: E501
        :type: str
        """

        self._bin_loc_num = bin_loc_num

    @property
    def bin_name(self):
        """Gets the bin_name of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The bin_name of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: str
        """
        return self._bin_name

    @bin_name.setter
    def bin_name(self, bin_name):
        """Sets the bin_name of this PurchaseOrderItemDetails.


        :param bin_name: The bin_name of this PurchaseOrderItemDetails.  # noqa: E501
        :type: str
        """

        self._bin_name = bin_name

    @property
    def update_bin_quantity_to_inventory(self):
        """Gets the update_bin_quantity_to_inventory of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The update_bin_quantity_to_inventory of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: bool
        """
        return self._update_bin_quantity_to_inventory

    @update_bin_quantity_to_inventory.setter
    def update_bin_quantity_to_inventory(self, update_bin_quantity_to_inventory):
        """Sets the update_bin_quantity_to_inventory of this PurchaseOrderItemDetails.


        :param update_bin_quantity_to_inventory: The update_bin_quantity_to_inventory of this PurchaseOrderItemDetails.  # noqa: E501
        :type: bool
        """

        self._update_bin_quantity_to_inventory = update_bin_quantity_to_inventory

    @property
    def unit_price(self):
        """Gets the unit_price of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The unit_price of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this PurchaseOrderItemDetails.


        :param unit_price: The unit_price of this PurchaseOrderItemDetails.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def ordered_quantity(self):
        """Gets the ordered_quantity of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The ordered_quantity of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: float
        """
        return self._ordered_quantity

    @ordered_quantity.setter
    def ordered_quantity(self, ordered_quantity):
        """Sets the ordered_quantity of this PurchaseOrderItemDetails.


        :param ordered_quantity: The ordered_quantity of this PurchaseOrderItemDetails.  # noqa: E501
        :type: float
        """

        self._ordered_quantity = ordered_quantity

    @property
    def total_ordered_amount(self):
        """Gets the total_ordered_amount of this PurchaseOrderItemDetails.  # noqa: E501


        :return: The total_ordered_amount of this PurchaseOrderItemDetails.  # noqa: E501
        :rtype: float
        """
        return self._total_ordered_amount

    @total_ordered_amount.setter
    def total_ordered_amount(self, total_ordered_amount):
        """Sets the total_ordered_amount of this PurchaseOrderItemDetails.


        :param total_ordered_amount: The total_ordered_amount of this PurchaseOrderItemDetails.  # noqa: E501
        :type: float
        """

        self._total_ordered_amount = total_ordered_amount

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
        if issubclass(PurchaseOrderItemDetails, dict):
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
        if not isinstance(other, PurchaseOrderItemDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
