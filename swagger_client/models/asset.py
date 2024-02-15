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

class Asset(object):
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
        'site_id': 'int',
        'name': 'str',
        'description': 'str',
        'model': 'str',
        'asset_type_id': 'int',
        'asset_status_id': 'int',
        'asset_tag': 'str',
        'serial_number': 'str',
        'manufacturer': 'str',
        'manufacturer_info': 'str',
        'preferred_vendor_id': 'int',
        'vendor_info': 'str',
        'installation_date': 'datetime',
        'warranty_date': 'datetime',
        'warranty_notes_parts': 'str',
        'warranty_notes_labor': 'str',
        'add_cc': 'str',
        'notes': 'str',
        'ip_mac_address': 'str',
        'is_mobile_asset': 'bool',
        'building_group_id': 'int',
        'building_id': 'int',
        'location_id': 'int',
        'assigned_user_id': 'int',
        'purchase_cost': 'float',
        'salvage_cost': 'float',
        'useful_life_in_years': 'float',
        'depreciation_rate': 'float',
        'parts_ids': 'list[int]',
        'metering_ids': 'list[int]'
    }

    attribute_map = {
        'site_id': 'siteId',
        'name': 'Name',
        'description': 'Description',
        'model': 'Model',
        'asset_type_id': 'AssetTypeId',
        'asset_status_id': 'AssetStatusId',
        'asset_tag': 'AssetTag',
        'serial_number': 'SerialNumber',
        'manufacturer': 'Manufacturer',
        'manufacturer_info': 'ManufacturerInfo',
        'preferred_vendor_id': 'PreferredVendorId',
        'vendor_info': 'VendorInfo',
        'installation_date': 'InstallationDate',
        'warranty_date': 'WarrantyDate',
        'warranty_notes_parts': 'WarrantyNotesParts',
        'warranty_notes_labor': 'WarrantyNotesLabor',
        'add_cc': 'AddCC',
        'notes': 'Notes',
        'ip_mac_address': 'IpMacAddress',
        'is_mobile_asset': 'IsMobileAsset',
        'building_group_id': 'BuildingGroupId',
        'building_id': 'BuildingId',
        'location_id': 'LocationId',
        'assigned_user_id': 'AssignedUserId',
        'purchase_cost': 'PurchaseCost',
        'salvage_cost': 'SalvageCost',
        'useful_life_in_years': 'UsefulLifeInYears',
        'depreciation_rate': 'DepreciationRate',
        'parts_ids': 'PartsIds',
        'metering_ids': 'MeteringIds'
    }

    def __init__(self, site_id=None, name=None, description=None, model=None, asset_type_id=None, asset_status_id=None, asset_tag=None, serial_number=None, manufacturer=None, manufacturer_info=None, preferred_vendor_id=None, vendor_info=None, installation_date=None, warranty_date=None, warranty_notes_parts=None, warranty_notes_labor=None, add_cc=None, notes=None, ip_mac_address=None, is_mobile_asset=None, building_group_id=None, building_id=None, location_id=None, assigned_user_id=None, purchase_cost=None, salvage_cost=None, useful_life_in_years=None, depreciation_rate=None, parts_ids=None, metering_ids=None):  # noqa: E501
        """Asset - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._name = None
        self._description = None
        self._model = None
        self._asset_type_id = None
        self._asset_status_id = None
        self._asset_tag = None
        self._serial_number = None
        self._manufacturer = None
        self._manufacturer_info = None
        self._preferred_vendor_id = None
        self._vendor_info = None
        self._installation_date = None
        self._warranty_date = None
        self._warranty_notes_parts = None
        self._warranty_notes_labor = None
        self._add_cc = None
        self._notes = None
        self._ip_mac_address = None
        self._is_mobile_asset = None
        self._building_group_id = None
        self._building_id = None
        self._location_id = None
        self._assigned_user_id = None
        self._purchase_cost = None
        self._salvage_cost = None
        self._useful_life_in_years = None
        self._depreciation_rate = None
        self._parts_ids = None
        self._metering_ids = None
        self.discriminator = None
        self.site_id = site_id
        self.name = name
        if description is not None:
            self.description = description
        if model is not None:
            self.model = model
        self.asset_type_id = asset_type_id
        self.asset_status_id = asset_status_id
        if asset_tag is not None:
            self.asset_tag = asset_tag
        if serial_number is not None:
            self.serial_number = serial_number
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if manufacturer_info is not None:
            self.manufacturer_info = manufacturer_info
        if preferred_vendor_id is not None:
            self.preferred_vendor_id = preferred_vendor_id
        if vendor_info is not None:
            self.vendor_info = vendor_info
        if installation_date is not None:
            self.installation_date = installation_date
        if warranty_date is not None:
            self.warranty_date = warranty_date
        if warranty_notes_parts is not None:
            self.warranty_notes_parts = warranty_notes_parts
        if warranty_notes_labor is not None:
            self.warranty_notes_labor = warranty_notes_labor
        if add_cc is not None:
            self.add_cc = add_cc
        if notes is not None:
            self.notes = notes
        if ip_mac_address is not None:
            self.ip_mac_address = ip_mac_address
        if is_mobile_asset is not None:
            self.is_mobile_asset = is_mobile_asset
        if building_group_id is not None:
            self.building_group_id = building_group_id
        if building_id is not None:
            self.building_id = building_id
        if location_id is not None:
            self.location_id = location_id
        if assigned_user_id is not None:
            self.assigned_user_id = assigned_user_id
        if purchase_cost is not None:
            self.purchase_cost = purchase_cost
        if salvage_cost is not None:
            self.salvage_cost = salvage_cost
        if useful_life_in_years is not None:
            self.useful_life_in_years = useful_life_in_years
        if depreciation_rate is not None:
            self.depreciation_rate = depreciation_rate
        if parts_ids is not None:
            self.parts_ids = parts_ids
        if metering_ids is not None:
            self.metering_ids = metering_ids

    @property
    def site_id(self):
        """Gets the site_id of this Asset.  # noqa: E501

        Site Id of the Asset. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :return: The site_id of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Asset.

        Site Id of the Asset. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :param site_id: The site_id of this Asset.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def name(self):
        """Gets the name of this Asset.  # noqa: E501

        Name of the Asset.  # noqa: E501

        :return: The name of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Asset.

        Name of the Asset.  # noqa: E501

        :param name: The name of this Asset.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Asset.  # noqa: E501

        Description of Asset.  # noqa: E501

        :return: The description of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Asset.

        Description of Asset.  # noqa: E501

        :param description: The description of this Asset.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def model(self):
        """Gets the model of this Asset.  # noqa: E501

        Model details of Asset  # noqa: E501

        :return: The model of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Asset.

        Model details of Asset  # noqa: E501

        :param model: The model of this Asset.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def asset_type_id(self):
        """Gets the asset_type_id of this Asset.  # noqa: E501

        Asset Type Id of the Asset. Asset Type Id can be found in your Maxpanda Company Asset Type Index or Asset Type Api  # noqa: E501

        :return: The asset_type_id of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._asset_type_id

    @asset_type_id.setter
    def asset_type_id(self, asset_type_id):
        """Sets the asset_type_id of this Asset.

        Asset Type Id of the Asset. Asset Type Id can be found in your Maxpanda Company Asset Type Index or Asset Type Api  # noqa: E501

        :param asset_type_id: The asset_type_id of this Asset.  # noqa: E501
        :type: int
        """
        if asset_type_id is None:
            raise ValueError("Invalid value for `asset_type_id`, must not be `None`")  # noqa: E501

        self._asset_type_id = asset_type_id

    @property
    def asset_status_id(self):
        """Gets the asset_status_id of this Asset.  # noqa: E501

        Asset Status Id of the Asset. Asset Status Id can be found in your Maxpanda Company Asset Status Index or Asset Status Api  # noqa: E501

        :return: The asset_status_id of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._asset_status_id

    @asset_status_id.setter
    def asset_status_id(self, asset_status_id):
        """Sets the asset_status_id of this Asset.

        Asset Status Id of the Asset. Asset Status Id can be found in your Maxpanda Company Asset Status Index or Asset Status Api  # noqa: E501

        :param asset_status_id: The asset_status_id of this Asset.  # noqa: E501
        :type: int
        """
        if asset_status_id is None:
            raise ValueError("Invalid value for `asset_status_id`, must not be `None`")  # noqa: E501

        self._asset_status_id = asset_status_id

    @property
    def asset_tag(self):
        """Gets the asset_tag of this Asset.  # noqa: E501

        Tag details of the Asset.  # noqa: E501

        :return: The asset_tag of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this Asset.

        Tag details of the Asset.  # noqa: E501

        :param asset_tag: The asset_tag of this Asset.  # noqa: E501
        :type: str
        """

        self._asset_tag = asset_tag

    @property
    def serial_number(self):
        """Gets the serial_number of this Asset.  # noqa: E501

        Serial Number of the Asset  # noqa: E501

        :return: The serial_number of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this Asset.

        Serial Number of the Asset  # noqa: E501

        :param serial_number: The serial_number of this Asset.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def manufacturer(self):
        """Gets the manufacturer of this Asset.  # noqa: E501

        Manufacturer details of the Asset.  # noqa: E501

        :return: The manufacturer of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this Asset.

        Manufacturer details of the Asset.  # noqa: E501

        :param manufacturer: The manufacturer of this Asset.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def manufacturer_info(self):
        """Gets the manufacturer_info of this Asset.  # noqa: E501

        Information of Manufacturer.  # noqa: E501

        :return: The manufacturer_info of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_info

    @manufacturer_info.setter
    def manufacturer_info(self, manufacturer_info):
        """Sets the manufacturer_info of this Asset.

        Information of Manufacturer.  # noqa: E501

        :param manufacturer_info: The manufacturer_info of this Asset.  # noqa: E501
        :type: str
        """

        self._manufacturer_info = manufacturer_info

    @property
    def preferred_vendor_id(self):
        """Gets the preferred_vendor_id of this Asset.  # noqa: E501

        Id of Preferred Vendor for the Asset. Preferred Vendor Id can be found in your Maxpanda Vendor Index or Vendor Api  # noqa: E501

        :return: The preferred_vendor_id of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._preferred_vendor_id

    @preferred_vendor_id.setter
    def preferred_vendor_id(self, preferred_vendor_id):
        """Sets the preferred_vendor_id of this Asset.

        Id of Preferred Vendor for the Asset. Preferred Vendor Id can be found in your Maxpanda Vendor Index or Vendor Api  # noqa: E501

        :param preferred_vendor_id: The preferred_vendor_id of this Asset.  # noqa: E501
        :type: int
        """

        self._preferred_vendor_id = preferred_vendor_id

    @property
    def vendor_info(self):
        """Gets the vendor_info of this Asset.  # noqa: E501

        Information about the vendor.  # noqa: E501

        :return: The vendor_info of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._vendor_info

    @vendor_info.setter
    def vendor_info(self, vendor_info):
        """Sets the vendor_info of this Asset.

        Information about the vendor.  # noqa: E501

        :param vendor_info: The vendor_info of this Asset.  # noqa: E501
        :type: str
        """

        self._vendor_info = vendor_info

    @property
    def installation_date(self):
        """Gets the installation_date of this Asset.  # noqa: E501

        Installation date of Asset  # noqa: E501

        :return: The installation_date of this Asset.  # noqa: E501
        :rtype: datetime
        """
        return self._installation_date

    @installation_date.setter
    def installation_date(self, installation_date):
        """Sets the installation_date of this Asset.

        Installation date of Asset  # noqa: E501

        :param installation_date: The installation_date of this Asset.  # noqa: E501
        :type: datetime
        """

        self._installation_date = installation_date

    @property
    def warranty_date(self):
        """Gets the warranty_date of this Asset.  # noqa: E501

        Warrenty date of Asset  # noqa: E501

        :return: The warranty_date of this Asset.  # noqa: E501
        :rtype: datetime
        """
        return self._warranty_date

    @warranty_date.setter
    def warranty_date(self, warranty_date):
        """Sets the warranty_date of this Asset.

        Warrenty date of Asset  # noqa: E501

        :param warranty_date: The warranty_date of this Asset.  # noqa: E501
        :type: datetime
        """

        self._warranty_date = warranty_date

    @property
    def warranty_notes_parts(self):
        """Gets the warranty_notes_parts of this Asset.  # noqa: E501

        Warranty Notes for Parts  # noqa: E501

        :return: The warranty_notes_parts of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._warranty_notes_parts

    @warranty_notes_parts.setter
    def warranty_notes_parts(self, warranty_notes_parts):
        """Sets the warranty_notes_parts of this Asset.

        Warranty Notes for Parts  # noqa: E501

        :param warranty_notes_parts: The warranty_notes_parts of this Asset.  # noqa: E501
        :type: str
        """

        self._warranty_notes_parts = warranty_notes_parts

    @property
    def warranty_notes_labor(self):
        """Gets the warranty_notes_labor of this Asset.  # noqa: E501

        Warranty Notes for Labor  # noqa: E501

        :return: The warranty_notes_labor of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._warranty_notes_labor

    @warranty_notes_labor.setter
    def warranty_notes_labor(self, warranty_notes_labor):
        """Sets the warranty_notes_labor of this Asset.

        Warranty Notes for Labor  # noqa: E501

        :param warranty_notes_labor: The warranty_notes_labor of this Asset.  # noqa: E501
        :type: str
        """

        self._warranty_notes_labor = warranty_notes_labor

    @property
    def add_cc(self):
        """Gets the add_cc of this Asset.  # noqa: E501

        Addition Email recievers  # noqa: E501

        :return: The add_cc of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._add_cc

    @add_cc.setter
    def add_cc(self, add_cc):
        """Sets the add_cc of this Asset.

        Addition Email recievers  # noqa: E501

        :param add_cc: The add_cc of this Asset.  # noqa: E501
        :type: str
        """

        self._add_cc = add_cc

    @property
    def notes(self):
        """Gets the notes of this Asset.  # noqa: E501

        Notes of the Asset  # noqa: E501

        :return: The notes of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Asset.

        Notes of the Asset  # noqa: E501

        :param notes: The notes of this Asset.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def ip_mac_address(self):
        """Gets the ip_mac_address of this Asset.  # noqa: E501

        IP / Mac Address of the Asset  # noqa: E501

        :return: The ip_mac_address of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._ip_mac_address

    @ip_mac_address.setter
    def ip_mac_address(self, ip_mac_address):
        """Sets the ip_mac_address of this Asset.

        IP / Mac Address of the Asset  # noqa: E501

        :param ip_mac_address: The ip_mac_address of this Asset.  # noqa: E501
        :type: str
        """

        self._ip_mac_address = ip_mac_address

    @property
    def is_mobile_asset(self):
        """Gets the is_mobile_asset of this Asset.  # noqa: E501

        Assets which are movable or can be moved from one location to another are called Mobile Assets  # noqa: E501

        :return: The is_mobile_asset of this Asset.  # noqa: E501
        :rtype: bool
        """
        return self._is_mobile_asset

    @is_mobile_asset.setter
    def is_mobile_asset(self, is_mobile_asset):
        """Sets the is_mobile_asset of this Asset.

        Assets which are movable or can be moved from one location to another are called Mobile Assets  # noqa: E501

        :param is_mobile_asset: The is_mobile_asset of this Asset.  # noqa: E501
        :type: bool
        """

        self._is_mobile_asset = is_mobile_asset

    @property
    def building_group_id(self):
        """Gets the building_group_id of this Asset.  # noqa: E501

        Building group of the Asset. Building Group Id can be found in your Maxpanda company Building Group or Department Api  # noqa: E501

        :return: The building_group_id of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._building_group_id

    @building_group_id.setter
    def building_group_id(self, building_group_id):
        """Sets the building_group_id of this Asset.

        Building group of the Asset. Building Group Id can be found in your Maxpanda company Building Group or Department Api  # noqa: E501

        :param building_group_id: The building_group_id of this Asset.  # noqa: E501
        :type: int
        """

        self._building_group_id = building_group_id

    @property
    def building_id(self):
        """Gets the building_id of this Asset.  # noqa: E501

        Building of the Asset. Building Id can be found in your Maxpanda Building index or Building Api  # noqa: E501

        :return: The building_id of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._building_id

    @building_id.setter
    def building_id(self, building_id):
        """Sets the building_id of this Asset.

        Building of the Asset. Building Id can be found in your Maxpanda Building index or Building Api  # noqa: E501

        :param building_id: The building_id of this Asset.  # noqa: E501
        :type: int
        """

        self._building_id = building_id

    @property
    def location_id(self):
        """Gets the location_id of this Asset.  # noqa: E501

        Location of the Asset. Location Id can be found in your Maxpanda Location index or Location Api  # noqa: E501

        :return: The location_id of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this Asset.

        Location of the Asset. Location Id can be found in your Maxpanda Location index or Location Api  # noqa: E501

        :param location_id: The location_id of this Asset.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def assigned_user_id(self):
        """Gets the assigned_user_id of this Asset.  # noqa: E501

        Currently assigned user of the Asset. User Id can be found in your Maxpanda User index or User Api  # noqa: E501

        :return: The assigned_user_id of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._assigned_user_id

    @assigned_user_id.setter
    def assigned_user_id(self, assigned_user_id):
        """Sets the assigned_user_id of this Asset.

        Currently assigned user of the Asset. User Id can be found in your Maxpanda User index or User Api  # noqa: E501

        :param assigned_user_id: The assigned_user_id of this Asset.  # noqa: E501
        :type: int
        """

        self._assigned_user_id = assigned_user_id

    @property
    def purchase_cost(self):
        """Gets the purchase_cost of this Asset.  # noqa: E501

        Purchase cost of the Asset  # noqa: E501

        :return: The purchase_cost of this Asset.  # noqa: E501
        :rtype: float
        """
        return self._purchase_cost

    @purchase_cost.setter
    def purchase_cost(self, purchase_cost):
        """Sets the purchase_cost of this Asset.

        Purchase cost of the Asset  # noqa: E501

        :param purchase_cost: The purchase_cost of this Asset.  # noqa: E501
        :type: float
        """

        self._purchase_cost = purchase_cost

    @property
    def salvage_cost(self):
        """Gets the salvage_cost of this Asset.  # noqa: E501

        Salvage cost of the Asset  # noqa: E501

        :return: The salvage_cost of this Asset.  # noqa: E501
        :rtype: float
        """
        return self._salvage_cost

    @salvage_cost.setter
    def salvage_cost(self, salvage_cost):
        """Sets the salvage_cost of this Asset.

        Salvage cost of the Asset  # noqa: E501

        :param salvage_cost: The salvage_cost of this Asset.  # noqa: E501
        :type: float
        """

        self._salvage_cost = salvage_cost

    @property
    def useful_life_in_years(self):
        """Gets the useful_life_in_years of this Asset.  # noqa: E501

        Number of years this Asset can be used  # noqa: E501

        :return: The useful_life_in_years of this Asset.  # noqa: E501
        :rtype: float
        """
        return self._useful_life_in_years

    @useful_life_in_years.setter
    def useful_life_in_years(self, useful_life_in_years):
        """Sets the useful_life_in_years of this Asset.

        Number of years this Asset can be used  # noqa: E501

        :param useful_life_in_years: The useful_life_in_years of this Asset.  # noqa: E501
        :type: float
        """

        self._useful_life_in_years = useful_life_in_years

    @property
    def depreciation_rate(self):
        """Gets the depreciation_rate of this Asset.  # noqa: E501

        Rate of Deprecation of the Asset  # noqa: E501

        :return: The depreciation_rate of this Asset.  # noqa: E501
        :rtype: float
        """
        return self._depreciation_rate

    @depreciation_rate.setter
    def depreciation_rate(self, depreciation_rate):
        """Sets the depreciation_rate of this Asset.

        Rate of Deprecation of the Asset  # noqa: E501

        :param depreciation_rate: The depreciation_rate of this Asset.  # noqa: E501
        :type: float
        """

        self._depreciation_rate = depreciation_rate

    @property
    def parts_ids(self):
        """Gets the parts_ids of this Asset.  # noqa: E501

        Parts of the Asset. Parts Id can be found in your Maxpanda Inventory Part Index or Parts Api  # noqa: E501

        :return: The parts_ids of this Asset.  # noqa: E501
        :rtype: list[int]
        """
        return self._parts_ids

    @parts_ids.setter
    def parts_ids(self, parts_ids):
        """Sets the parts_ids of this Asset.

        Parts of the Asset. Parts Id can be found in your Maxpanda Inventory Part Index or Parts Api  # noqa: E501

        :param parts_ids: The parts_ids of this Asset.  # noqa: E501
        :type: list[int]
        """

        self._parts_ids = parts_ids

    @property
    def metering_ids(self):
        """Gets the metering_ids of this Asset.  # noqa: E501

        Metering type of the Asset. Metering Type Id can be found in your Maxpanda Company MeteringType or Metering Types Api  # noqa: E501

        :return: The metering_ids of this Asset.  # noqa: E501
        :rtype: list[int]
        """
        return self._metering_ids

    @metering_ids.setter
    def metering_ids(self, metering_ids):
        """Sets the metering_ids of this Asset.

        Metering type of the Asset. Metering Type Id can be found in your Maxpanda Company MeteringType or Metering Types Api  # noqa: E501

        :param metering_ids: The metering_ids of this Asset.  # noqa: E501
        :type: list[int]
        """

        self._metering_ids = metering_ids

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
        if issubclass(Asset, dict):
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
        if not isinstance(other, Asset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
