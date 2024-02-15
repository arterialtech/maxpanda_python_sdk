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

class AssetList(object):
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
        'asset_id': 'int',
        'name': 'str',
        'model': 'str',
        'asset_type_ref': 'AssetTypeRef',
        'asset_status_ref': 'AssetStatusRef',
        'asset_tag': 'str',
        'serial_number': 'str',
        'manufacture': 'str',
        'manufacture_info': 'str',
        'preferred_supplier': 'VendorRef',
        'vendor_info': 'str',
        'installation_date': 'datetime',
        'warranty_date': 'datetime',
        'warranty_notes_labor': 'str',
        'warranty_notes_parts': 'str',
        'notes': 'str',
        'ip_mac_address': 'str',
        'building_group_ref': 'DepartmentRef',
        'building_ref': 'BuildingRef',
        'location_ref': 'LocationRef',
        'user_ref': 'list[AssetStaffRef]',
        'part_ref': 'list[PartRef]',
        'metering_type_ref': 'list[MerteringRef]',
        'asset_audits_ref': 'list[AssetAuditModel]'
    }

    attribute_map = {
        'site_ref': 'SiteRef',
        'asset_id': 'AssetId',
        'name': 'Name',
        'model': 'Model',
        'asset_type_ref': 'AssetTypeRef',
        'asset_status_ref': 'AssetStatusRef',
        'asset_tag': 'AssetTag',
        'serial_number': 'SerialNumber',
        'manufacture': 'Manufacture',
        'manufacture_info': 'ManufactureInfo',
        'preferred_supplier': 'PreferredSupplier',
        'vendor_info': 'VendorInfo',
        'installation_date': 'InstallationDate',
        'warranty_date': 'WarrantyDate',
        'warranty_notes_labor': 'WarrantyNotesLabor',
        'warranty_notes_parts': 'WarrantyNotesParts',
        'notes': 'Notes',
        'ip_mac_address': 'IpMacAddress',
        'building_group_ref': 'BuildingGroupRef',
        'building_ref': 'BuildingRef',
        'location_ref': 'LocationRef',
        'user_ref': 'UserRef',
        'part_ref': 'PartRef',
        'metering_type_ref': 'MeteringTypeRef',
        'asset_audits_ref': 'AssetAuditsRef'
    }

    def __init__(self, site_ref=None, asset_id=None, name=None, model=None, asset_type_ref=None, asset_status_ref=None, asset_tag=None, serial_number=None, manufacture=None, manufacture_info=None, preferred_supplier=None, vendor_info=None, installation_date=None, warranty_date=None, warranty_notes_labor=None, warranty_notes_parts=None, notes=None, ip_mac_address=None, building_group_ref=None, building_ref=None, location_ref=None, user_ref=None, part_ref=None, metering_type_ref=None, asset_audits_ref=None):  # noqa: E501
        """AssetList - a model defined in Swagger"""  # noqa: E501
        self._site_ref = None
        self._asset_id = None
        self._name = None
        self._model = None
        self._asset_type_ref = None
        self._asset_status_ref = None
        self._asset_tag = None
        self._serial_number = None
        self._manufacture = None
        self._manufacture_info = None
        self._preferred_supplier = None
        self._vendor_info = None
        self._installation_date = None
        self._warranty_date = None
        self._warranty_notes_labor = None
        self._warranty_notes_parts = None
        self._notes = None
        self._ip_mac_address = None
        self._building_group_ref = None
        self._building_ref = None
        self._location_ref = None
        self._user_ref = None
        self._part_ref = None
        self._metering_type_ref = None
        self._asset_audits_ref = None
        self.discriminator = None
        if site_ref is not None:
            self.site_ref = site_ref
        if asset_id is not None:
            self.asset_id = asset_id
        if name is not None:
            self.name = name
        if model is not None:
            self.model = model
        if asset_type_ref is not None:
            self.asset_type_ref = asset_type_ref
        if asset_status_ref is not None:
            self.asset_status_ref = asset_status_ref
        if asset_tag is not None:
            self.asset_tag = asset_tag
        if serial_number is not None:
            self.serial_number = serial_number
        if manufacture is not None:
            self.manufacture = manufacture
        if manufacture_info is not None:
            self.manufacture_info = manufacture_info
        if preferred_supplier is not None:
            self.preferred_supplier = preferred_supplier
        if vendor_info is not None:
            self.vendor_info = vendor_info
        if installation_date is not None:
            self.installation_date = installation_date
        if warranty_date is not None:
            self.warranty_date = warranty_date
        if warranty_notes_labor is not None:
            self.warranty_notes_labor = warranty_notes_labor
        if warranty_notes_parts is not None:
            self.warranty_notes_parts = warranty_notes_parts
        if notes is not None:
            self.notes = notes
        if ip_mac_address is not None:
            self.ip_mac_address = ip_mac_address
        if building_group_ref is not None:
            self.building_group_ref = building_group_ref
        if building_ref is not None:
            self.building_ref = building_ref
        if location_ref is not None:
            self.location_ref = location_ref
        if user_ref is not None:
            self.user_ref = user_ref
        if part_ref is not None:
            self.part_ref = part_ref
        if metering_type_ref is not None:
            self.metering_type_ref = metering_type_ref
        if asset_audits_ref is not None:
            self.asset_audits_ref = asset_audits_ref

    @property
    def site_ref(self):
        """Gets the site_ref of this AssetList.  # noqa: E501


        :return: The site_ref of this AssetList.  # noqa: E501
        :rtype: SiteRef
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this AssetList.


        :param site_ref: The site_ref of this AssetList.  # noqa: E501
        :type: SiteRef
        """

        self._site_ref = site_ref

    @property
    def asset_id(self):
        """Gets the asset_id of this AssetList.  # noqa: E501


        :return: The asset_id of this AssetList.  # noqa: E501
        :rtype: int
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this AssetList.


        :param asset_id: The asset_id of this AssetList.  # noqa: E501
        :type: int
        """

        self._asset_id = asset_id

    @property
    def name(self):
        """Gets the name of this AssetList.  # noqa: E501


        :return: The name of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetList.


        :param name: The name of this AssetList.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def model(self):
        """Gets the model of this AssetList.  # noqa: E501


        :return: The model of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this AssetList.


        :param model: The model of this AssetList.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def asset_type_ref(self):
        """Gets the asset_type_ref of this AssetList.  # noqa: E501


        :return: The asset_type_ref of this AssetList.  # noqa: E501
        :rtype: AssetTypeRef
        """
        return self._asset_type_ref

    @asset_type_ref.setter
    def asset_type_ref(self, asset_type_ref):
        """Sets the asset_type_ref of this AssetList.


        :param asset_type_ref: The asset_type_ref of this AssetList.  # noqa: E501
        :type: AssetTypeRef
        """

        self._asset_type_ref = asset_type_ref

    @property
    def asset_status_ref(self):
        """Gets the asset_status_ref of this AssetList.  # noqa: E501


        :return: The asset_status_ref of this AssetList.  # noqa: E501
        :rtype: AssetStatusRef
        """
        return self._asset_status_ref

    @asset_status_ref.setter
    def asset_status_ref(self, asset_status_ref):
        """Sets the asset_status_ref of this AssetList.


        :param asset_status_ref: The asset_status_ref of this AssetList.  # noqa: E501
        :type: AssetStatusRef
        """

        self._asset_status_ref = asset_status_ref

    @property
    def asset_tag(self):
        """Gets the asset_tag of this AssetList.  # noqa: E501


        :return: The asset_tag of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this AssetList.


        :param asset_tag: The asset_tag of this AssetList.  # noqa: E501
        :type: str
        """

        self._asset_tag = asset_tag

    @property
    def serial_number(self):
        """Gets the serial_number of this AssetList.  # noqa: E501


        :return: The serial_number of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this AssetList.


        :param serial_number: The serial_number of this AssetList.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def manufacture(self):
        """Gets the manufacture of this AssetList.  # noqa: E501


        :return: The manufacture of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._manufacture

    @manufacture.setter
    def manufacture(self, manufacture):
        """Sets the manufacture of this AssetList.


        :param manufacture: The manufacture of this AssetList.  # noqa: E501
        :type: str
        """

        self._manufacture = manufacture

    @property
    def manufacture_info(self):
        """Gets the manufacture_info of this AssetList.  # noqa: E501


        :return: The manufacture_info of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._manufacture_info

    @manufacture_info.setter
    def manufacture_info(self, manufacture_info):
        """Sets the manufacture_info of this AssetList.


        :param manufacture_info: The manufacture_info of this AssetList.  # noqa: E501
        :type: str
        """

        self._manufacture_info = manufacture_info

    @property
    def preferred_supplier(self):
        """Gets the preferred_supplier of this AssetList.  # noqa: E501


        :return: The preferred_supplier of this AssetList.  # noqa: E501
        :rtype: VendorRef
        """
        return self._preferred_supplier

    @preferred_supplier.setter
    def preferred_supplier(self, preferred_supplier):
        """Sets the preferred_supplier of this AssetList.


        :param preferred_supplier: The preferred_supplier of this AssetList.  # noqa: E501
        :type: VendorRef
        """

        self._preferred_supplier = preferred_supplier

    @property
    def vendor_info(self):
        """Gets the vendor_info of this AssetList.  # noqa: E501


        :return: The vendor_info of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._vendor_info

    @vendor_info.setter
    def vendor_info(self, vendor_info):
        """Sets the vendor_info of this AssetList.


        :param vendor_info: The vendor_info of this AssetList.  # noqa: E501
        :type: str
        """

        self._vendor_info = vendor_info

    @property
    def installation_date(self):
        """Gets the installation_date of this AssetList.  # noqa: E501


        :return: The installation_date of this AssetList.  # noqa: E501
        :rtype: datetime
        """
        return self._installation_date

    @installation_date.setter
    def installation_date(self, installation_date):
        """Sets the installation_date of this AssetList.


        :param installation_date: The installation_date of this AssetList.  # noqa: E501
        :type: datetime
        """

        self._installation_date = installation_date

    @property
    def warranty_date(self):
        """Gets the warranty_date of this AssetList.  # noqa: E501


        :return: The warranty_date of this AssetList.  # noqa: E501
        :rtype: datetime
        """
        return self._warranty_date

    @warranty_date.setter
    def warranty_date(self, warranty_date):
        """Sets the warranty_date of this AssetList.


        :param warranty_date: The warranty_date of this AssetList.  # noqa: E501
        :type: datetime
        """

        self._warranty_date = warranty_date

    @property
    def warranty_notes_labor(self):
        """Gets the warranty_notes_labor of this AssetList.  # noqa: E501


        :return: The warranty_notes_labor of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._warranty_notes_labor

    @warranty_notes_labor.setter
    def warranty_notes_labor(self, warranty_notes_labor):
        """Sets the warranty_notes_labor of this AssetList.


        :param warranty_notes_labor: The warranty_notes_labor of this AssetList.  # noqa: E501
        :type: str
        """

        self._warranty_notes_labor = warranty_notes_labor

    @property
    def warranty_notes_parts(self):
        """Gets the warranty_notes_parts of this AssetList.  # noqa: E501


        :return: The warranty_notes_parts of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._warranty_notes_parts

    @warranty_notes_parts.setter
    def warranty_notes_parts(self, warranty_notes_parts):
        """Sets the warranty_notes_parts of this AssetList.


        :param warranty_notes_parts: The warranty_notes_parts of this AssetList.  # noqa: E501
        :type: str
        """

        self._warranty_notes_parts = warranty_notes_parts

    @property
    def notes(self):
        """Gets the notes of this AssetList.  # noqa: E501


        :return: The notes of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AssetList.


        :param notes: The notes of this AssetList.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def ip_mac_address(self):
        """Gets the ip_mac_address of this AssetList.  # noqa: E501


        :return: The ip_mac_address of this AssetList.  # noqa: E501
        :rtype: str
        """
        return self._ip_mac_address

    @ip_mac_address.setter
    def ip_mac_address(self, ip_mac_address):
        """Sets the ip_mac_address of this AssetList.


        :param ip_mac_address: The ip_mac_address of this AssetList.  # noqa: E501
        :type: str
        """

        self._ip_mac_address = ip_mac_address

    @property
    def building_group_ref(self):
        """Gets the building_group_ref of this AssetList.  # noqa: E501


        :return: The building_group_ref of this AssetList.  # noqa: E501
        :rtype: DepartmentRef
        """
        return self._building_group_ref

    @building_group_ref.setter
    def building_group_ref(self, building_group_ref):
        """Sets the building_group_ref of this AssetList.


        :param building_group_ref: The building_group_ref of this AssetList.  # noqa: E501
        :type: DepartmentRef
        """

        self._building_group_ref = building_group_ref

    @property
    def building_ref(self):
        """Gets the building_ref of this AssetList.  # noqa: E501


        :return: The building_ref of this AssetList.  # noqa: E501
        :rtype: BuildingRef
        """
        return self._building_ref

    @building_ref.setter
    def building_ref(self, building_ref):
        """Sets the building_ref of this AssetList.


        :param building_ref: The building_ref of this AssetList.  # noqa: E501
        :type: BuildingRef
        """

        self._building_ref = building_ref

    @property
    def location_ref(self):
        """Gets the location_ref of this AssetList.  # noqa: E501


        :return: The location_ref of this AssetList.  # noqa: E501
        :rtype: LocationRef
        """
        return self._location_ref

    @location_ref.setter
    def location_ref(self, location_ref):
        """Sets the location_ref of this AssetList.


        :param location_ref: The location_ref of this AssetList.  # noqa: E501
        :type: LocationRef
        """

        self._location_ref = location_ref

    @property
    def user_ref(self):
        """Gets the user_ref of this AssetList.  # noqa: E501


        :return: The user_ref of this AssetList.  # noqa: E501
        :rtype: list[AssetStaffRef]
        """
        return self._user_ref

    @user_ref.setter
    def user_ref(self, user_ref):
        """Sets the user_ref of this AssetList.


        :param user_ref: The user_ref of this AssetList.  # noqa: E501
        :type: list[AssetStaffRef]
        """

        self._user_ref = user_ref

    @property
    def part_ref(self):
        """Gets the part_ref of this AssetList.  # noqa: E501


        :return: The part_ref of this AssetList.  # noqa: E501
        :rtype: list[PartRef]
        """
        return self._part_ref

    @part_ref.setter
    def part_ref(self, part_ref):
        """Sets the part_ref of this AssetList.


        :param part_ref: The part_ref of this AssetList.  # noqa: E501
        :type: list[PartRef]
        """

        self._part_ref = part_ref

    @property
    def metering_type_ref(self):
        """Gets the metering_type_ref of this AssetList.  # noqa: E501


        :return: The metering_type_ref of this AssetList.  # noqa: E501
        :rtype: list[MerteringRef]
        """
        return self._metering_type_ref

    @metering_type_ref.setter
    def metering_type_ref(self, metering_type_ref):
        """Sets the metering_type_ref of this AssetList.


        :param metering_type_ref: The metering_type_ref of this AssetList.  # noqa: E501
        :type: list[MerteringRef]
        """

        self._metering_type_ref = metering_type_ref

    @property
    def asset_audits_ref(self):
        """Gets the asset_audits_ref of this AssetList.  # noqa: E501


        :return: The asset_audits_ref of this AssetList.  # noqa: E501
        :rtype: list[AssetAuditModel]
        """
        return self._asset_audits_ref

    @asset_audits_ref.setter
    def asset_audits_ref(self, asset_audits_ref):
        """Sets the asset_audits_ref of this AssetList.


        :param asset_audits_ref: The asset_audits_ref of this AssetList.  # noqa: E501
        :type: list[AssetAuditModel]
        """

        self._asset_audits_ref = asset_audits_ref

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
        if issubclass(AssetList, dict):
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
        if not isinstance(other, AssetList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other