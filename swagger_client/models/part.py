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

class Part(object):
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
        'part_id': 'int',
        'name': 'str',
        'part_number': 'str',
        'part_status_ref': 'PartStatusRef',
        'pat_type_ref': 'PartTypeRef',
        'part_category_ref': 'PartCategoryRef',
        'manufacture': 'str',
        'model_name': 'str',
        'upc': 'str',
        'preferred_supplier_ref': 'VendorRef',
        'unit_price': 'float',
        'current_part_cost': 'float',
        'last_part_cost': 'float',
        'average_part_cost': 'float',
        'oem': 'str',
        'oem1': 'str',
        'oem2': 'str',
        'oem3': 'str',
        'oem_supplier1_ref': 'VendorRef',
        'oem_supplier2_ref': 'VendorRef',
        'oem_supplier3_ref': 'VendorRef',
        'qty_in_bins': 'float',
        'qty_in_inventory': 'float',
        'qty_allocated': 'float',
        'qty_in_transit': 'float',
        'minimum_level': 'str',
        'maximum_level': 'str',
        'qty_on_order': 'float',
        'installation_date': 'datetime',
        'warranty_date': 'datetime',
        'warranty_notes_parts': 'str',
        'warranty_notes_labor': 'str',
        'notes': 'str',
        'storage_location_ref': 'LocationRef',
        'asset_ref': 'list[AssetRef]',
        'po_template_ref': 'list[POTemplateRef]',
        'bins_ref': 'list[BinRef]',
        'is_frozen': 'bool',
        'customer_warranty_start_date': 'datetime',
        'customer_warranty_end_date': 'datetime'
    }

    attribute_map = {
        'site_ref': 'SiteRef',
        'part_id': 'PartId',
        'name': 'Name',
        'part_number': 'PartNumber',
        'part_status_ref': 'PartStatusRef',
        'pat_type_ref': 'PatTypeRef',
        'part_category_ref': 'PartCategoryRef',
        'manufacture': 'Manufacture',
        'model_name': 'ModelName',
        'upc': 'UPC',
        'preferred_supplier_ref': 'PreferredSupplierRef',
        'unit_price': 'UnitPrice',
        'current_part_cost': 'CurrentPartCost',
        'last_part_cost': 'LastPartCost',
        'average_part_cost': 'AveragePartCost',
        'oem': 'OEM',
        'oem1': 'OEM1',
        'oem2': 'OEM2',
        'oem3': 'OEM3',
        'oem_supplier1_ref': 'OEMSupplier1Ref',
        'oem_supplier2_ref': 'OEMSupplier2Ref',
        'oem_supplier3_ref': 'OEMSupplier3Ref',
        'qty_in_bins': 'QtyInBins',
        'qty_in_inventory': 'QtyInInventory',
        'qty_allocated': 'QtyAllocated',
        'qty_in_transit': 'QtyInTransit',
        'minimum_level': 'MinimumLevel',
        'maximum_level': 'MaximumLevel',
        'qty_on_order': 'QtyOnOrder',
        'installation_date': 'InstallationDate',
        'warranty_date': 'WarrantyDate',
        'warranty_notes_parts': 'WarrantyNotesParts',
        'warranty_notes_labor': 'WarrantyNotesLabor',
        'notes': 'Notes',
        'storage_location_ref': 'StorageLocationRef',
        'asset_ref': 'AssetRef',
        'po_template_ref': 'POTemplateRef',
        'bins_ref': 'BinsRef',
        'is_frozen': 'IsFrozen',
        'customer_warranty_start_date': 'CustomerWarrantyStartDate',
        'customer_warranty_end_date': 'CustomerWarrantyEndDate'
    }

    def __init__(self, site_ref=None, part_id=None, name=None, part_number=None, part_status_ref=None, pat_type_ref=None, part_category_ref=None, manufacture=None, model_name=None, upc=None, preferred_supplier_ref=None, unit_price=None, current_part_cost=None, last_part_cost=None, average_part_cost=None, oem=None, oem1=None, oem2=None, oem3=None, oem_supplier1_ref=None, oem_supplier2_ref=None, oem_supplier3_ref=None, qty_in_bins=None, qty_in_inventory=None, qty_allocated=None, qty_in_transit=None, minimum_level=None, maximum_level=None, qty_on_order=None, installation_date=None, warranty_date=None, warranty_notes_parts=None, warranty_notes_labor=None, notes=None, storage_location_ref=None, asset_ref=None, po_template_ref=None, bins_ref=None, is_frozen=None, customer_warranty_start_date=None, customer_warranty_end_date=None):  # noqa: E501
        """Part - a model defined in Swagger"""  # noqa: E501
        self._site_ref = None
        self._part_id = None
        self._name = None
        self._part_number = None
        self._part_status_ref = None
        self._pat_type_ref = None
        self._part_category_ref = None
        self._manufacture = None
        self._model_name = None
        self._upc = None
        self._preferred_supplier_ref = None
        self._unit_price = None
        self._current_part_cost = None
        self._last_part_cost = None
        self._average_part_cost = None
        self._oem = None
        self._oem1 = None
        self._oem2 = None
        self._oem3 = None
        self._oem_supplier1_ref = None
        self._oem_supplier2_ref = None
        self._oem_supplier3_ref = None
        self._qty_in_bins = None
        self._qty_in_inventory = None
        self._qty_allocated = None
        self._qty_in_transit = None
        self._minimum_level = None
        self._maximum_level = None
        self._qty_on_order = None
        self._installation_date = None
        self._warranty_date = None
        self._warranty_notes_parts = None
        self._warranty_notes_labor = None
        self._notes = None
        self._storage_location_ref = None
        self._asset_ref = None
        self._po_template_ref = None
        self._bins_ref = None
        self._is_frozen = None
        self._customer_warranty_start_date = None
        self._customer_warranty_end_date = None
        self.discriminator = None
        if site_ref is not None:
            self.site_ref = site_ref
        if part_id is not None:
            self.part_id = part_id
        if name is not None:
            self.name = name
        if part_number is not None:
            self.part_number = part_number
        if part_status_ref is not None:
            self.part_status_ref = part_status_ref
        if pat_type_ref is not None:
            self.pat_type_ref = pat_type_ref
        if part_category_ref is not None:
            self.part_category_ref = part_category_ref
        if manufacture is not None:
            self.manufacture = manufacture
        if model_name is not None:
            self.model_name = model_name
        if upc is not None:
            self.upc = upc
        if preferred_supplier_ref is not None:
            self.preferred_supplier_ref = preferred_supplier_ref
        if unit_price is not None:
            self.unit_price = unit_price
        if current_part_cost is not None:
            self.current_part_cost = current_part_cost
        if last_part_cost is not None:
            self.last_part_cost = last_part_cost
        if average_part_cost is not None:
            self.average_part_cost = average_part_cost
        if oem is not None:
            self.oem = oem
        if oem1 is not None:
            self.oem1 = oem1
        if oem2 is not None:
            self.oem2 = oem2
        if oem3 is not None:
            self.oem3 = oem3
        if oem_supplier1_ref is not None:
            self.oem_supplier1_ref = oem_supplier1_ref
        if oem_supplier2_ref is not None:
            self.oem_supplier2_ref = oem_supplier2_ref
        if oem_supplier3_ref is not None:
            self.oem_supplier3_ref = oem_supplier3_ref
        if qty_in_bins is not None:
            self.qty_in_bins = qty_in_bins
        if qty_in_inventory is not None:
            self.qty_in_inventory = qty_in_inventory
        if qty_allocated is not None:
            self.qty_allocated = qty_allocated
        if qty_in_transit is not None:
            self.qty_in_transit = qty_in_transit
        if minimum_level is not None:
            self.minimum_level = minimum_level
        if maximum_level is not None:
            self.maximum_level = maximum_level
        if qty_on_order is not None:
            self.qty_on_order = qty_on_order
        if installation_date is not None:
            self.installation_date = installation_date
        if warranty_date is not None:
            self.warranty_date = warranty_date
        if warranty_notes_parts is not None:
            self.warranty_notes_parts = warranty_notes_parts
        if warranty_notes_labor is not None:
            self.warranty_notes_labor = warranty_notes_labor
        if notes is not None:
            self.notes = notes
        if storage_location_ref is not None:
            self.storage_location_ref = storage_location_ref
        if asset_ref is not None:
            self.asset_ref = asset_ref
        if po_template_ref is not None:
            self.po_template_ref = po_template_ref
        if bins_ref is not None:
            self.bins_ref = bins_ref
        if is_frozen is not None:
            self.is_frozen = is_frozen
        if customer_warranty_start_date is not None:
            self.customer_warranty_start_date = customer_warranty_start_date
        if customer_warranty_end_date is not None:
            self.customer_warranty_end_date = customer_warranty_end_date

    @property
    def site_ref(self):
        """Gets the site_ref of this Part.  # noqa: E501


        :return: The site_ref of this Part.  # noqa: E501
        :rtype: SiteRef
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this Part.


        :param site_ref: The site_ref of this Part.  # noqa: E501
        :type: SiteRef
        """

        self._site_ref = site_ref

    @property
    def part_id(self):
        """Gets the part_id of this Part.  # noqa: E501


        :return: The part_id of this Part.  # noqa: E501
        :rtype: int
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this Part.


        :param part_id: The part_id of this Part.  # noqa: E501
        :type: int
        """

        self._part_id = part_id

    @property
    def name(self):
        """Gets the name of this Part.  # noqa: E501


        :return: The name of this Part.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Part.


        :param name: The name of this Part.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def part_number(self):
        """Gets the part_number of this Part.  # noqa: E501


        :return: The part_number of this Part.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this Part.


        :param part_number: The part_number of this Part.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def part_status_ref(self):
        """Gets the part_status_ref of this Part.  # noqa: E501


        :return: The part_status_ref of this Part.  # noqa: E501
        :rtype: PartStatusRef
        """
        return self._part_status_ref

    @part_status_ref.setter
    def part_status_ref(self, part_status_ref):
        """Sets the part_status_ref of this Part.


        :param part_status_ref: The part_status_ref of this Part.  # noqa: E501
        :type: PartStatusRef
        """

        self._part_status_ref = part_status_ref

    @property
    def pat_type_ref(self):
        """Gets the pat_type_ref of this Part.  # noqa: E501


        :return: The pat_type_ref of this Part.  # noqa: E501
        :rtype: PartTypeRef
        """
        return self._pat_type_ref

    @pat_type_ref.setter
    def pat_type_ref(self, pat_type_ref):
        """Sets the pat_type_ref of this Part.


        :param pat_type_ref: The pat_type_ref of this Part.  # noqa: E501
        :type: PartTypeRef
        """

        self._pat_type_ref = pat_type_ref

    @property
    def part_category_ref(self):
        """Gets the part_category_ref of this Part.  # noqa: E501


        :return: The part_category_ref of this Part.  # noqa: E501
        :rtype: PartCategoryRef
        """
        return self._part_category_ref

    @part_category_ref.setter
    def part_category_ref(self, part_category_ref):
        """Sets the part_category_ref of this Part.


        :param part_category_ref: The part_category_ref of this Part.  # noqa: E501
        :type: PartCategoryRef
        """

        self._part_category_ref = part_category_ref

    @property
    def manufacture(self):
        """Gets the manufacture of this Part.  # noqa: E501


        :return: The manufacture of this Part.  # noqa: E501
        :rtype: str
        """
        return self._manufacture

    @manufacture.setter
    def manufacture(self, manufacture):
        """Sets the manufacture of this Part.


        :param manufacture: The manufacture of this Part.  # noqa: E501
        :type: str
        """

        self._manufacture = manufacture

    @property
    def model_name(self):
        """Gets the model_name of this Part.  # noqa: E501


        :return: The model_name of this Part.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this Part.


        :param model_name: The model_name of this Part.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def upc(self):
        """Gets the upc of this Part.  # noqa: E501


        :return: The upc of this Part.  # noqa: E501
        :rtype: str
        """
        return self._upc

    @upc.setter
    def upc(self, upc):
        """Sets the upc of this Part.


        :param upc: The upc of this Part.  # noqa: E501
        :type: str
        """

        self._upc = upc

    @property
    def preferred_supplier_ref(self):
        """Gets the preferred_supplier_ref of this Part.  # noqa: E501


        :return: The preferred_supplier_ref of this Part.  # noqa: E501
        :rtype: VendorRef
        """
        return self._preferred_supplier_ref

    @preferred_supplier_ref.setter
    def preferred_supplier_ref(self, preferred_supplier_ref):
        """Sets the preferred_supplier_ref of this Part.


        :param preferred_supplier_ref: The preferred_supplier_ref of this Part.  # noqa: E501
        :type: VendorRef
        """

        self._preferred_supplier_ref = preferred_supplier_ref

    @property
    def unit_price(self):
        """Gets the unit_price of this Part.  # noqa: E501


        :return: The unit_price of this Part.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this Part.


        :param unit_price: The unit_price of this Part.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def current_part_cost(self):
        """Gets the current_part_cost of this Part.  # noqa: E501


        :return: The current_part_cost of this Part.  # noqa: E501
        :rtype: float
        """
        return self._current_part_cost

    @current_part_cost.setter
    def current_part_cost(self, current_part_cost):
        """Sets the current_part_cost of this Part.


        :param current_part_cost: The current_part_cost of this Part.  # noqa: E501
        :type: float
        """

        self._current_part_cost = current_part_cost

    @property
    def last_part_cost(self):
        """Gets the last_part_cost of this Part.  # noqa: E501


        :return: The last_part_cost of this Part.  # noqa: E501
        :rtype: float
        """
        return self._last_part_cost

    @last_part_cost.setter
    def last_part_cost(self, last_part_cost):
        """Sets the last_part_cost of this Part.


        :param last_part_cost: The last_part_cost of this Part.  # noqa: E501
        :type: float
        """

        self._last_part_cost = last_part_cost

    @property
    def average_part_cost(self):
        """Gets the average_part_cost of this Part.  # noqa: E501


        :return: The average_part_cost of this Part.  # noqa: E501
        :rtype: float
        """
        return self._average_part_cost

    @average_part_cost.setter
    def average_part_cost(self, average_part_cost):
        """Sets the average_part_cost of this Part.


        :param average_part_cost: The average_part_cost of this Part.  # noqa: E501
        :type: float
        """

        self._average_part_cost = average_part_cost

    @property
    def oem(self):
        """Gets the oem of this Part.  # noqa: E501


        :return: The oem of this Part.  # noqa: E501
        :rtype: str
        """
        return self._oem

    @oem.setter
    def oem(self, oem):
        """Sets the oem of this Part.


        :param oem: The oem of this Part.  # noqa: E501
        :type: str
        """

        self._oem = oem

    @property
    def oem1(self):
        """Gets the oem1 of this Part.  # noqa: E501


        :return: The oem1 of this Part.  # noqa: E501
        :rtype: str
        """
        return self._oem1

    @oem1.setter
    def oem1(self, oem1):
        """Sets the oem1 of this Part.


        :param oem1: The oem1 of this Part.  # noqa: E501
        :type: str
        """

        self._oem1 = oem1

    @property
    def oem2(self):
        """Gets the oem2 of this Part.  # noqa: E501


        :return: The oem2 of this Part.  # noqa: E501
        :rtype: str
        """
        return self._oem2

    @oem2.setter
    def oem2(self, oem2):
        """Sets the oem2 of this Part.


        :param oem2: The oem2 of this Part.  # noqa: E501
        :type: str
        """

        self._oem2 = oem2

    @property
    def oem3(self):
        """Gets the oem3 of this Part.  # noqa: E501


        :return: The oem3 of this Part.  # noqa: E501
        :rtype: str
        """
        return self._oem3

    @oem3.setter
    def oem3(self, oem3):
        """Sets the oem3 of this Part.


        :param oem3: The oem3 of this Part.  # noqa: E501
        :type: str
        """

        self._oem3 = oem3

    @property
    def oem_supplier1_ref(self):
        """Gets the oem_supplier1_ref of this Part.  # noqa: E501


        :return: The oem_supplier1_ref of this Part.  # noqa: E501
        :rtype: VendorRef
        """
        return self._oem_supplier1_ref

    @oem_supplier1_ref.setter
    def oem_supplier1_ref(self, oem_supplier1_ref):
        """Sets the oem_supplier1_ref of this Part.


        :param oem_supplier1_ref: The oem_supplier1_ref of this Part.  # noqa: E501
        :type: VendorRef
        """

        self._oem_supplier1_ref = oem_supplier1_ref

    @property
    def oem_supplier2_ref(self):
        """Gets the oem_supplier2_ref of this Part.  # noqa: E501


        :return: The oem_supplier2_ref of this Part.  # noqa: E501
        :rtype: VendorRef
        """
        return self._oem_supplier2_ref

    @oem_supplier2_ref.setter
    def oem_supplier2_ref(self, oem_supplier2_ref):
        """Sets the oem_supplier2_ref of this Part.


        :param oem_supplier2_ref: The oem_supplier2_ref of this Part.  # noqa: E501
        :type: VendorRef
        """

        self._oem_supplier2_ref = oem_supplier2_ref

    @property
    def oem_supplier3_ref(self):
        """Gets the oem_supplier3_ref of this Part.  # noqa: E501


        :return: The oem_supplier3_ref of this Part.  # noqa: E501
        :rtype: VendorRef
        """
        return self._oem_supplier3_ref

    @oem_supplier3_ref.setter
    def oem_supplier3_ref(self, oem_supplier3_ref):
        """Sets the oem_supplier3_ref of this Part.


        :param oem_supplier3_ref: The oem_supplier3_ref of this Part.  # noqa: E501
        :type: VendorRef
        """

        self._oem_supplier3_ref = oem_supplier3_ref

    @property
    def qty_in_bins(self):
        """Gets the qty_in_bins of this Part.  # noqa: E501


        :return: The qty_in_bins of this Part.  # noqa: E501
        :rtype: float
        """
        return self._qty_in_bins

    @qty_in_bins.setter
    def qty_in_bins(self, qty_in_bins):
        """Sets the qty_in_bins of this Part.


        :param qty_in_bins: The qty_in_bins of this Part.  # noqa: E501
        :type: float
        """

        self._qty_in_bins = qty_in_bins

    @property
    def qty_in_inventory(self):
        """Gets the qty_in_inventory of this Part.  # noqa: E501


        :return: The qty_in_inventory of this Part.  # noqa: E501
        :rtype: float
        """
        return self._qty_in_inventory

    @qty_in_inventory.setter
    def qty_in_inventory(self, qty_in_inventory):
        """Sets the qty_in_inventory of this Part.


        :param qty_in_inventory: The qty_in_inventory of this Part.  # noqa: E501
        :type: float
        """

        self._qty_in_inventory = qty_in_inventory

    @property
    def qty_allocated(self):
        """Gets the qty_allocated of this Part.  # noqa: E501


        :return: The qty_allocated of this Part.  # noqa: E501
        :rtype: float
        """
        return self._qty_allocated

    @qty_allocated.setter
    def qty_allocated(self, qty_allocated):
        """Sets the qty_allocated of this Part.


        :param qty_allocated: The qty_allocated of this Part.  # noqa: E501
        :type: float
        """

        self._qty_allocated = qty_allocated

    @property
    def qty_in_transit(self):
        """Gets the qty_in_transit of this Part.  # noqa: E501


        :return: The qty_in_transit of this Part.  # noqa: E501
        :rtype: float
        """
        return self._qty_in_transit

    @qty_in_transit.setter
    def qty_in_transit(self, qty_in_transit):
        """Sets the qty_in_transit of this Part.


        :param qty_in_transit: The qty_in_transit of this Part.  # noqa: E501
        :type: float
        """

        self._qty_in_transit = qty_in_transit

    @property
    def minimum_level(self):
        """Gets the minimum_level of this Part.  # noqa: E501


        :return: The minimum_level of this Part.  # noqa: E501
        :rtype: str
        """
        return self._minimum_level

    @minimum_level.setter
    def minimum_level(self, minimum_level):
        """Sets the minimum_level of this Part.


        :param minimum_level: The minimum_level of this Part.  # noqa: E501
        :type: str
        """

        self._minimum_level = minimum_level

    @property
    def maximum_level(self):
        """Gets the maximum_level of this Part.  # noqa: E501


        :return: The maximum_level of this Part.  # noqa: E501
        :rtype: str
        """
        return self._maximum_level

    @maximum_level.setter
    def maximum_level(self, maximum_level):
        """Sets the maximum_level of this Part.


        :param maximum_level: The maximum_level of this Part.  # noqa: E501
        :type: str
        """

        self._maximum_level = maximum_level

    @property
    def qty_on_order(self):
        """Gets the qty_on_order of this Part.  # noqa: E501


        :return: The qty_on_order of this Part.  # noqa: E501
        :rtype: float
        """
        return self._qty_on_order

    @qty_on_order.setter
    def qty_on_order(self, qty_on_order):
        """Sets the qty_on_order of this Part.


        :param qty_on_order: The qty_on_order of this Part.  # noqa: E501
        :type: float
        """

        self._qty_on_order = qty_on_order

    @property
    def installation_date(self):
        """Gets the installation_date of this Part.  # noqa: E501


        :return: The installation_date of this Part.  # noqa: E501
        :rtype: datetime
        """
        return self._installation_date

    @installation_date.setter
    def installation_date(self, installation_date):
        """Sets the installation_date of this Part.


        :param installation_date: The installation_date of this Part.  # noqa: E501
        :type: datetime
        """

        self._installation_date = installation_date

    @property
    def warranty_date(self):
        """Gets the warranty_date of this Part.  # noqa: E501


        :return: The warranty_date of this Part.  # noqa: E501
        :rtype: datetime
        """
        return self._warranty_date

    @warranty_date.setter
    def warranty_date(self, warranty_date):
        """Sets the warranty_date of this Part.


        :param warranty_date: The warranty_date of this Part.  # noqa: E501
        :type: datetime
        """

        self._warranty_date = warranty_date

    @property
    def warranty_notes_parts(self):
        """Gets the warranty_notes_parts of this Part.  # noqa: E501


        :return: The warranty_notes_parts of this Part.  # noqa: E501
        :rtype: str
        """
        return self._warranty_notes_parts

    @warranty_notes_parts.setter
    def warranty_notes_parts(self, warranty_notes_parts):
        """Sets the warranty_notes_parts of this Part.


        :param warranty_notes_parts: The warranty_notes_parts of this Part.  # noqa: E501
        :type: str
        """

        self._warranty_notes_parts = warranty_notes_parts

    @property
    def warranty_notes_labor(self):
        """Gets the warranty_notes_labor of this Part.  # noqa: E501


        :return: The warranty_notes_labor of this Part.  # noqa: E501
        :rtype: str
        """
        return self._warranty_notes_labor

    @warranty_notes_labor.setter
    def warranty_notes_labor(self, warranty_notes_labor):
        """Sets the warranty_notes_labor of this Part.


        :param warranty_notes_labor: The warranty_notes_labor of this Part.  # noqa: E501
        :type: str
        """

        self._warranty_notes_labor = warranty_notes_labor

    @property
    def notes(self):
        """Gets the notes of this Part.  # noqa: E501


        :return: The notes of this Part.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Part.


        :param notes: The notes of this Part.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def storage_location_ref(self):
        """Gets the storage_location_ref of this Part.  # noqa: E501


        :return: The storage_location_ref of this Part.  # noqa: E501
        :rtype: LocationRef
        """
        return self._storage_location_ref

    @storage_location_ref.setter
    def storage_location_ref(self, storage_location_ref):
        """Sets the storage_location_ref of this Part.


        :param storage_location_ref: The storage_location_ref of this Part.  # noqa: E501
        :type: LocationRef
        """

        self._storage_location_ref = storage_location_ref

    @property
    def asset_ref(self):
        """Gets the asset_ref of this Part.  # noqa: E501


        :return: The asset_ref of this Part.  # noqa: E501
        :rtype: list[AssetRef]
        """
        return self._asset_ref

    @asset_ref.setter
    def asset_ref(self, asset_ref):
        """Sets the asset_ref of this Part.


        :param asset_ref: The asset_ref of this Part.  # noqa: E501
        :type: list[AssetRef]
        """

        self._asset_ref = asset_ref

    @property
    def po_template_ref(self):
        """Gets the po_template_ref of this Part.  # noqa: E501


        :return: The po_template_ref of this Part.  # noqa: E501
        :rtype: list[POTemplateRef]
        """
        return self._po_template_ref

    @po_template_ref.setter
    def po_template_ref(self, po_template_ref):
        """Sets the po_template_ref of this Part.


        :param po_template_ref: The po_template_ref of this Part.  # noqa: E501
        :type: list[POTemplateRef]
        """

        self._po_template_ref = po_template_ref

    @property
    def bins_ref(self):
        """Gets the bins_ref of this Part.  # noqa: E501


        :return: The bins_ref of this Part.  # noqa: E501
        :rtype: list[BinRef]
        """
        return self._bins_ref

    @bins_ref.setter
    def bins_ref(self, bins_ref):
        """Sets the bins_ref of this Part.


        :param bins_ref: The bins_ref of this Part.  # noqa: E501
        :type: list[BinRef]
        """

        self._bins_ref = bins_ref

    @property
    def is_frozen(self):
        """Gets the is_frozen of this Part.  # noqa: E501


        :return: The is_frozen of this Part.  # noqa: E501
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this Part.


        :param is_frozen: The is_frozen of this Part.  # noqa: E501
        :type: bool
        """

        self._is_frozen = is_frozen

    @property
    def customer_warranty_start_date(self):
        """Gets the customer_warranty_start_date of this Part.  # noqa: E501


        :return: The customer_warranty_start_date of this Part.  # noqa: E501
        :rtype: datetime
        """
        return self._customer_warranty_start_date

    @customer_warranty_start_date.setter
    def customer_warranty_start_date(self, customer_warranty_start_date):
        """Sets the customer_warranty_start_date of this Part.


        :param customer_warranty_start_date: The customer_warranty_start_date of this Part.  # noqa: E501
        :type: datetime
        """

        self._customer_warranty_start_date = customer_warranty_start_date

    @property
    def customer_warranty_end_date(self):
        """Gets the customer_warranty_end_date of this Part.  # noqa: E501


        :return: The customer_warranty_end_date of this Part.  # noqa: E501
        :rtype: datetime
        """
        return self._customer_warranty_end_date

    @customer_warranty_end_date.setter
    def customer_warranty_end_date(self, customer_warranty_end_date):
        """Sets the customer_warranty_end_date of this Part.


        :param customer_warranty_end_date: The customer_warranty_end_date of this Part.  # noqa: E501
        :type: datetime
        """

        self._customer_warranty_end_date = customer_warranty_end_date

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
        if issubclass(Part, dict):
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
        if not isinstance(other, Part):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other