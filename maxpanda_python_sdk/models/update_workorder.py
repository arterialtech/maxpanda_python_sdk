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

class UpdateWorkorder(object):
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
        'workorder_id': 'int',
        'title': 'str',
        'referenced_id': 'str',
        'workorder_category_id': 'int',
        'workorder_priority_id': 'int',
        'short_description': 'str',
        'notes': 'str',
        'private_notes': 'str',
        'comments': 'str',
        'primary_contact': 'str',
        'alternate_contact': 'str',
        'add_cc': 'str',
        'enter_work_area': 'str',
        'all_day_event': 'bool',
        'start_date': 'datetime',
        'due_date': 'datetime',
        'completed_date': 'datetime',
        'closed_date': 'datetime',
        'customer_id': 'int',
        'building_group_id': 'int',
        'building_id': 'int',
        'locations_id': 'list[int]',
        'assets_id': 'list[int]',
        'vendor_id': 'list[int]',
        'tasks_id': 'list[int]',
        'workorder_staffs_ref': 'list[WorkorderStaffsRef]',
        'customer_invoices_id': 'list[int]',
        'vendor_invoices_id': 'list[int]',
        'work_order_part_refs': 'list[WorkOrderPartsRef]',
        'workorder_status': 'int'
    }

    attribute_map = {
        'site_id': 'SiteId',
        'workorder_id': 'WorkorderId',
        'title': 'Title',
        'referenced_id': 'ReferencedId',
        'workorder_category_id': 'WorkorderCategoryId',
        'workorder_priority_id': 'WorkorderPriorityId',
        'short_description': 'ShortDescription',
        'notes': 'Notes',
        'private_notes': 'PrivateNotes',
        'comments': 'Comments',
        'primary_contact': 'PrimaryContact',
        'alternate_contact': 'AlternateContact',
        'add_cc': 'AddCC',
        'enter_work_area': 'EnterWorkArea',
        'all_day_event': 'AllDayEvent',
        'start_date': 'StartDate',
        'due_date': 'DueDate',
        'completed_date': 'CompletedDate',
        'closed_date': 'ClosedDate',
        'customer_id': 'CustomerId',
        'building_group_id': 'BuildingGroupId',
        'building_id': 'BuildingId',
        'locations_id': 'LocationsId',
        'assets_id': 'AssetsId',
        'vendor_id': 'VendorId',
        'tasks_id': 'TasksId',
        'workorder_staffs_ref': 'WorkorderStaffsRef',
        'customer_invoices_id': 'CustomerInvoicesId',
        'vendor_invoices_id': 'VendorInvoicesId',
        'work_order_part_refs': 'workOrderPartRefs',
        'workorder_status': 'WorkorderStatus'
    }

    def __init__(self, site_id=None, workorder_id=None, title=None, referenced_id=None, workorder_category_id=None, workorder_priority_id=None, short_description=None, notes=None, private_notes=None, comments=None, primary_contact=None, alternate_contact=None, add_cc=None, enter_work_area=None, all_day_event=None, start_date=None, due_date=None, completed_date=None, closed_date=None, customer_id=None, building_group_id=None, building_id=None, locations_id=None, assets_id=None, vendor_id=None, tasks_id=None, workorder_staffs_ref=None, customer_invoices_id=None, vendor_invoices_id=None, work_order_part_refs=None, workorder_status=None):  # noqa: E501
        """UpdateWorkorder - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._workorder_id = None
        self._title = None
        self._referenced_id = None
        self._workorder_category_id = None
        self._workorder_priority_id = None
        self._short_description = None
        self._notes = None
        self._private_notes = None
        self._comments = None
        self._primary_contact = None
        self._alternate_contact = None
        self._add_cc = None
        self._enter_work_area = None
        self._all_day_event = None
        self._start_date = None
        self._due_date = None
        self._completed_date = None
        self._closed_date = None
        self._customer_id = None
        self._building_group_id = None
        self._building_id = None
        self._locations_id = None
        self._assets_id = None
        self._vendor_id = None
        self._tasks_id = None
        self._workorder_staffs_ref = None
        self._customer_invoices_id = None
        self._vendor_invoices_id = None
        self._work_order_part_refs = None
        self._workorder_status = None
        self.discriminator = None
        self.site_id = site_id
        self.workorder_id = workorder_id
        self.title = title
        if referenced_id is not None:
            self.referenced_id = referenced_id
        self.workorder_category_id = workorder_category_id
        self.workorder_priority_id = workorder_priority_id
        if short_description is not None:
            self.short_description = short_description
        if notes is not None:
            self.notes = notes
        if private_notes is not None:
            self.private_notes = private_notes
        if comments is not None:
            self.comments = comments
        if primary_contact is not None:
            self.primary_contact = primary_contact
        if alternate_contact is not None:
            self.alternate_contact = alternate_contact
        if add_cc is not None:
            self.add_cc = add_cc
        self.enter_work_area = enter_work_area
        if all_day_event is not None:
            self.all_day_event = all_day_event
        self.start_date = start_date
        if due_date is not None:
            self.due_date = due_date
        if completed_date is not None:
            self.completed_date = completed_date
        if closed_date is not None:
            self.closed_date = closed_date
        if customer_id is not None:
            self.customer_id = customer_id
        if building_group_id is not None:
            self.building_group_id = building_group_id
        if building_id is not None:
            self.building_id = building_id
        if locations_id is not None:
            self.locations_id = locations_id
        if assets_id is not None:
            self.assets_id = assets_id
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if tasks_id is not None:
            self.tasks_id = tasks_id
        if workorder_staffs_ref is not None:
            self.workorder_staffs_ref = workorder_staffs_ref
        if customer_invoices_id is not None:
            self.customer_invoices_id = customer_invoices_id
        if vendor_invoices_id is not None:
            self.vendor_invoices_id = vendor_invoices_id
        if work_order_part_refs is not None:
            self.work_order_part_refs = work_order_part_refs
        self.workorder_status = workorder_status

    @property
    def site_id(self):
        """Gets the site_id of this UpdateWorkorder.  # noqa: E501

        Site Id of the WorkOrder. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :return: The site_id of this UpdateWorkorder.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this UpdateWorkorder.

        Site Id of the WorkOrder. Site Id can be found in your Maxpanda Site Index or Site API  # noqa: E501

        :param site_id: The site_id of this UpdateWorkorder.  # noqa: E501
        :type: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def workorder_id(self):
        """Gets the workorder_id of this UpdateWorkorder.  # noqa: E501

        Id of the WorkOrder. Workorder Id can be found in your Maxpanda Workorder List View or Workorder API  # noqa: E501

        :return: The workorder_id of this UpdateWorkorder.  # noqa: E501
        :rtype: int
        """
        return self._workorder_id

    @workorder_id.setter
    def workorder_id(self, workorder_id):
        """Sets the workorder_id of this UpdateWorkorder.

        Id of the WorkOrder. Workorder Id can be found in your Maxpanda Workorder List View or Workorder API  # noqa: E501

        :param workorder_id: The workorder_id of this UpdateWorkorder.  # noqa: E501
        :type: int
        """
        if workorder_id is None:
            raise ValueError("Invalid value for `workorder_id`, must not be `None`")  # noqa: E501

        self._workorder_id = workorder_id

    @property
    def title(self):
        """Gets the title of this UpdateWorkorder.  # noqa: E501

        Name or Title of the WorkOrder  # noqa: E501

        :return: The title of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateWorkorder.

        Name or Title of the WorkOrder  # noqa: E501

        :param title: The title of this UpdateWorkorder.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def referenced_id(self):
        """Gets the referenced_id of this UpdateWorkorder.  # noqa: E501

        Reference Id of the WorkOrder  # noqa: E501

        :return: The referenced_id of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._referenced_id

    @referenced_id.setter
    def referenced_id(self, referenced_id):
        """Sets the referenced_id of this UpdateWorkorder.

        Reference Id of the WorkOrder  # noqa: E501

        :param referenced_id: The referenced_id of this UpdateWorkorder.  # noqa: E501
        :type: str
        """

        self._referenced_id = referenced_id

    @property
    def workorder_category_id(self):
        """Gets the workorder_category_id of this UpdateWorkorder.  # noqa: E501

        Category Id of the WorkOrder. Category Id can be found in your Maxpanda Company WorkOrderCategory or WorkOrderCategory API  # noqa: E501

        :return: The workorder_category_id of this UpdateWorkorder.  # noqa: E501
        :rtype: int
        """
        return self._workorder_category_id

    @workorder_category_id.setter
    def workorder_category_id(self, workorder_category_id):
        """Sets the workorder_category_id of this UpdateWorkorder.

        Category Id of the WorkOrder. Category Id can be found in your Maxpanda Company WorkOrderCategory or WorkOrderCategory API  # noqa: E501

        :param workorder_category_id: The workorder_category_id of this UpdateWorkorder.  # noqa: E501
        :type: int
        """
        if workorder_category_id is None:
            raise ValueError("Invalid value for `workorder_category_id`, must not be `None`")  # noqa: E501

        self._workorder_category_id = workorder_category_id

    @property
    def workorder_priority_id(self):
        """Gets the workorder_priority_id of this UpdateWorkorder.  # noqa: E501

        Priority Id of the WorkOrder. Priotiy Id can be found in your Maxpanda Company WorkOrderPriority or WorkOrderPriority API  # noqa: E501

        :return: The workorder_priority_id of this UpdateWorkorder.  # noqa: E501
        :rtype: int
        """
        return self._workorder_priority_id

    @workorder_priority_id.setter
    def workorder_priority_id(self, workorder_priority_id):
        """Sets the workorder_priority_id of this UpdateWorkorder.

        Priority Id of the WorkOrder. Priotiy Id can be found in your Maxpanda Company WorkOrderPriority or WorkOrderPriority API  # noqa: E501

        :param workorder_priority_id: The workorder_priority_id of this UpdateWorkorder.  # noqa: E501
        :type: int
        """
        if workorder_priority_id is None:
            raise ValueError("Invalid value for `workorder_priority_id`, must not be `None`")  # noqa: E501

        self._workorder_priority_id = workorder_priority_id

    @property
    def short_description(self):
        """Gets the short_description of this UpdateWorkorder.  # noqa: E501

        Short Description about the WorkOrder  # noqa: E501

        :return: The short_description of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this UpdateWorkorder.

        Short Description about the WorkOrder  # noqa: E501

        :param short_description: The short_description of this UpdateWorkorder.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def notes(self):
        """Gets the notes of this UpdateWorkorder.  # noqa: E501

        Notes for the Staff  # noqa: E501

        :return: The notes of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UpdateWorkorder.

        Notes for the Staff  # noqa: E501

        :param notes: The notes of this UpdateWorkorder.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def private_notes(self):
        """Gets the private_notes of this UpdateWorkorder.  # noqa: E501

        Private Notes  # noqa: E501

        :return: The private_notes of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._private_notes

    @private_notes.setter
    def private_notes(self, private_notes):
        """Sets the private_notes of this UpdateWorkorder.

        Private Notes  # noqa: E501

        :param private_notes: The private_notes of this UpdateWorkorder.  # noqa: E501
        :type: str
        """

        self._private_notes = private_notes

    @property
    def comments(self):
        """Gets the comments of this UpdateWorkorder.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this UpdateWorkorder.

        Comments  # noqa: E501

        :param comments: The comments of this UpdateWorkorder.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def primary_contact(self):
        """Gets the primary_contact of this UpdateWorkorder.  # noqa: E501

        Primary Contact Number  # noqa: E501

        :return: The primary_contact of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._primary_contact

    @primary_contact.setter
    def primary_contact(self, primary_contact):
        """Sets the primary_contact of this UpdateWorkorder.

        Primary Contact Number  # noqa: E501

        :param primary_contact: The primary_contact of this UpdateWorkorder.  # noqa: E501
        :type: str
        """

        self._primary_contact = primary_contact

    @property
    def alternate_contact(self):
        """Gets the alternate_contact of this UpdateWorkorder.  # noqa: E501

        Alternate Contact Number  # noqa: E501

        :return: The alternate_contact of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._alternate_contact

    @alternate_contact.setter
    def alternate_contact(self, alternate_contact):
        """Sets the alternate_contact of this UpdateWorkorder.

        Alternate Contact Number  # noqa: E501

        :param alternate_contact: The alternate_contact of this UpdateWorkorder.  # noqa: E501
        :type: str
        """

        self._alternate_contact = alternate_contact

    @property
    def add_cc(self):
        """Gets the add_cc of this UpdateWorkorder.  # noqa: E501

        Add external Email Recipients  # noqa: E501

        :return: The add_cc of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._add_cc

    @add_cc.setter
    def add_cc(self, add_cc):
        """Sets the add_cc of this UpdateWorkorder.

        Add external Email Recipients  # noqa: E501

        :param add_cc: The add_cc of this UpdateWorkorder.  # noqa: E501
        :type: str
        """

        self._add_cc = add_cc

    @property
    def enter_work_area(self):
        """Gets the enter_work_area of this UpdateWorkorder.  # noqa: E501

        Allow to enter in Work Area. Enter boolean value.  # noqa: E501

        :return: The enter_work_area of this UpdateWorkorder.  # noqa: E501
        :rtype: str
        """
        return self._enter_work_area

    @enter_work_area.setter
    def enter_work_area(self, enter_work_area):
        """Sets the enter_work_area of this UpdateWorkorder.

        Allow to enter in Work Area. Enter boolean value.  # noqa: E501

        :param enter_work_area: The enter_work_area of this UpdateWorkorder.  # noqa: E501
        :type: str
        """
        if enter_work_area is None:
            raise ValueError("Invalid value for `enter_work_area`, must not be `None`")  # noqa: E501

        self._enter_work_area = enter_work_area

    @property
    def all_day_event(self):
        """Gets the all_day_event of this UpdateWorkorder.  # noqa: E501

        Is this an All day event  # noqa: E501

        :return: The all_day_event of this UpdateWorkorder.  # noqa: E501
        :rtype: bool
        """
        return self._all_day_event

    @all_day_event.setter
    def all_day_event(self, all_day_event):
        """Sets the all_day_event of this UpdateWorkorder.

        Is this an All day event  # noqa: E501

        :param all_day_event: The all_day_event of this UpdateWorkorder.  # noqa: E501
        :type: bool
        """

        self._all_day_event = all_day_event

    @property
    def start_date(self):
        """Gets the start_date of this UpdateWorkorder.  # noqa: E501

        Date on which WorkOrder was Started  # noqa: E501

        :return: The start_date of this UpdateWorkorder.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this UpdateWorkorder.

        Date on which WorkOrder was Started  # noqa: E501

        :param start_date: The start_date of this UpdateWorkorder.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def due_date(self):
        """Gets the due_date of this UpdateWorkorder.  # noqa: E501

        Due Date of WorkOrder  # noqa: E501

        :return: The due_date of this UpdateWorkorder.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this UpdateWorkorder.

        Due Date of WorkOrder  # noqa: E501

        :param due_date: The due_date of this UpdateWorkorder.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def completed_date(self):
        """Gets the completed_date of this UpdateWorkorder.  # noqa: E501

        Date on which WorkOrder was Completed  # noqa: E501

        :return: The completed_date of this UpdateWorkorder.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """Sets the completed_date of this UpdateWorkorder.

        Date on which WorkOrder was Completed  # noqa: E501

        :param completed_date: The completed_date of this UpdateWorkorder.  # noqa: E501
        :type: datetime
        """

        self._completed_date = completed_date

    @property
    def closed_date(self):
        """Gets the closed_date of this UpdateWorkorder.  # noqa: E501

        Date on which WorkOrder was Closed  # noqa: E501

        :return: The closed_date of this UpdateWorkorder.  # noqa: E501
        :rtype: datetime
        """
        return self._closed_date

    @closed_date.setter
    def closed_date(self, closed_date):
        """Sets the closed_date of this UpdateWorkorder.

        Date on which WorkOrder was Closed  # noqa: E501

        :param closed_date: The closed_date of this UpdateWorkorder.  # noqa: E501
        :type: datetime
        """

        self._closed_date = closed_date

    @property
    def customer_id(self):
        """Gets the customer_id of this UpdateWorkorder.  # noqa: E501

        Customer Id of the WorkOrder. Customer Id can be found in your Maxpanda Customer Index or Customer API  # noqa: E501

        :return: The customer_id of this UpdateWorkorder.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this UpdateWorkorder.

        Customer Id of the WorkOrder. Customer Id can be found in your Maxpanda Customer Index or Customer API  # noqa: E501

        :param customer_id: The customer_id of this UpdateWorkorder.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def building_group_id(self):
        """Gets the building_group_id of this UpdateWorkorder.  # noqa: E501

        Building Group Id of the WorkOrder. Building Group Id can be found in your Maxpanda Company Building Group or Department API  # noqa: E501

        :return: The building_group_id of this UpdateWorkorder.  # noqa: E501
        :rtype: int
        """
        return self._building_group_id

    @building_group_id.setter
    def building_group_id(self, building_group_id):
        """Sets the building_group_id of this UpdateWorkorder.

        Building Group Id of the WorkOrder. Building Group Id can be found in your Maxpanda Company Building Group or Department API  # noqa: E501

        :param building_group_id: The building_group_id of this UpdateWorkorder.  # noqa: E501
        :type: int
        """

        self._building_group_id = building_group_id

    @property
    def building_id(self):
        """Gets the building_id of this UpdateWorkorder.  # noqa: E501

        Building Id of the WorkOrder. Building Id can be found in your Maxpanda Building Index or Buildings API  # noqa: E501

        :return: The building_id of this UpdateWorkorder.  # noqa: E501
        :rtype: int
        """
        return self._building_id

    @building_id.setter
    def building_id(self, building_id):
        """Sets the building_id of this UpdateWorkorder.

        Building Id of the WorkOrder. Building Id can be found in your Maxpanda Building Index or Buildings API  # noqa: E501

        :param building_id: The building_id of this UpdateWorkorder.  # noqa: E501
        :type: int
        """

        self._building_id = building_id

    @property
    def locations_id(self):
        """Gets the locations_id of this UpdateWorkorder.  # noqa: E501

        Location Id of the WorkOrder. Location Id can be found in your Maxpanda Location Index or Locations API  # noqa: E501

        :return: The locations_id of this UpdateWorkorder.  # noqa: E501
        :rtype: list[int]
        """
        return self._locations_id

    @locations_id.setter
    def locations_id(self, locations_id):
        """Sets the locations_id of this UpdateWorkorder.

        Location Id of the WorkOrder. Location Id can be found in your Maxpanda Location Index or Locations API  # noqa: E501

        :param locations_id: The locations_id of this UpdateWorkorder.  # noqa: E501
        :type: list[int]
        """

        self._locations_id = locations_id

    @property
    def assets_id(self):
        """Gets the assets_id of this UpdateWorkorder.  # noqa: E501

        Asset Id of the WorkOrder. Asset Id can be found in your Maxpanda Asset Index or Assets API  # noqa: E501

        :return: The assets_id of this UpdateWorkorder.  # noqa: E501
        :rtype: list[int]
        """
        return self._assets_id

    @assets_id.setter
    def assets_id(self, assets_id):
        """Sets the assets_id of this UpdateWorkorder.

        Asset Id of the WorkOrder. Asset Id can be found in your Maxpanda Asset Index or Assets API  # noqa: E501

        :param assets_id: The assets_id of this UpdateWorkorder.  # noqa: E501
        :type: list[int]
        """

        self._assets_id = assets_id

    @property
    def vendor_id(self):
        """Gets the vendor_id of this UpdateWorkorder.  # noqa: E501

        Vendor Id of the WorkOrder. Vendor Id can be found in your Maxpanda Vendor Index or Vendors API  # noqa: E501

        :return: The vendor_id of this UpdateWorkorder.  # noqa: E501
        :rtype: list[int]
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this UpdateWorkorder.

        Vendor Id of the WorkOrder. Vendor Id can be found in your Maxpanda Vendor Index or Vendors API  # noqa: E501

        :param vendor_id: The vendor_id of this UpdateWorkorder.  # noqa: E501
        :type: list[int]
        """

        self._vendor_id = vendor_id

    @property
    def tasks_id(self):
        """Gets the tasks_id of this UpdateWorkorder.  # noqa: E501

        Task Id of the WorkOrder. Task Id can be found in your Maxpanda Task Index or Task API  # noqa: E501

        :return: The tasks_id of this UpdateWorkorder.  # noqa: E501
        :rtype: list[int]
        """
        return self._tasks_id

    @tasks_id.setter
    def tasks_id(self, tasks_id):
        """Sets the tasks_id of this UpdateWorkorder.

        Task Id of the WorkOrder. Task Id can be found in your Maxpanda Task Index or Task API  # noqa: E501

        :param tasks_id: The tasks_id of this UpdateWorkorder.  # noqa: E501
        :type: list[int]
        """

        self._tasks_id = tasks_id

    @property
    def workorder_staffs_ref(self):
        """Gets the workorder_staffs_ref of this UpdateWorkorder.  # noqa: E501

        Staff details of the WorkOrder. Staff details can be found in your Maxpanda Users Index or Users API  # noqa: E501

        :return: The workorder_staffs_ref of this UpdateWorkorder.  # noqa: E501
        :rtype: list[WorkorderStaffsRef]
        """
        return self._workorder_staffs_ref

    @workorder_staffs_ref.setter
    def workorder_staffs_ref(self, workorder_staffs_ref):
        """Sets the workorder_staffs_ref of this UpdateWorkorder.

        Staff details of the WorkOrder. Staff details can be found in your Maxpanda Users Index or Users API  # noqa: E501

        :param workorder_staffs_ref: The workorder_staffs_ref of this UpdateWorkorder.  # noqa: E501
        :type: list[WorkorderStaffsRef]
        """

        self._workorder_staffs_ref = workorder_staffs_ref

    @property
    def customer_invoices_id(self):
        """Gets the customer_invoices_id of this UpdateWorkorder.  # noqa: E501

        Customer Invoice Id of the WorkOrder. Customer Invoice Id can be found in your Maxpanda Customer Invoice Index or Customer Invoices API  # noqa: E501

        :return: The customer_invoices_id of this UpdateWorkorder.  # noqa: E501
        :rtype: list[int]
        """
        return self._customer_invoices_id

    @customer_invoices_id.setter
    def customer_invoices_id(self, customer_invoices_id):
        """Sets the customer_invoices_id of this UpdateWorkorder.

        Customer Invoice Id of the WorkOrder. Customer Invoice Id can be found in your Maxpanda Customer Invoice Index or Customer Invoices API  # noqa: E501

        :param customer_invoices_id: The customer_invoices_id of this UpdateWorkorder.  # noqa: E501
        :type: list[int]
        """

        self._customer_invoices_id = customer_invoices_id

    @property
    def vendor_invoices_id(self):
        """Gets the vendor_invoices_id of this UpdateWorkorder.  # noqa: E501

        Vendor Invoices Id of the WorkOrder. Vendor Invoices Id can be found in your Maxpanda Inventory Invoices Index or Vendor Invoices API  # noqa: E501

        :return: The vendor_invoices_id of this UpdateWorkorder.  # noqa: E501
        :rtype: list[int]
        """
        return self._vendor_invoices_id

    @vendor_invoices_id.setter
    def vendor_invoices_id(self, vendor_invoices_id):
        """Sets the vendor_invoices_id of this UpdateWorkorder.

        Vendor Invoices Id of the WorkOrder. Vendor Invoices Id can be found in your Maxpanda Inventory Invoices Index or Vendor Invoices API  # noqa: E501

        :param vendor_invoices_id: The vendor_invoices_id of this UpdateWorkorder.  # noqa: E501
        :type: list[int]
        """

        self._vendor_invoices_id = vendor_invoices_id

    @property
    def work_order_part_refs(self):
        """Gets the work_order_part_refs of this UpdateWorkorder.  # noqa: E501


        :return: The work_order_part_refs of this UpdateWorkorder.  # noqa: E501
        :rtype: list[WorkOrderPartsRef]
        """
        return self._work_order_part_refs

    @work_order_part_refs.setter
    def work_order_part_refs(self, work_order_part_refs):
        """Sets the work_order_part_refs of this UpdateWorkorder.


        :param work_order_part_refs: The work_order_part_refs of this UpdateWorkorder.  # noqa: E501
        :type: list[WorkOrderPartsRef]
        """

        self._work_order_part_refs = work_order_part_refs

    @property
    def workorder_status(self):
        """Gets the workorder_status of this UpdateWorkorder.  # noqa: E501


        :return: The workorder_status of this UpdateWorkorder.  # noqa: E501
        :rtype: int
        """
        return self._workorder_status

    @workorder_status.setter
    def workorder_status(self, workorder_status):
        """Sets the workorder_status of this UpdateWorkorder.


        :param workorder_status: The workorder_status of this UpdateWorkorder.  # noqa: E501
        :type: int
        """
        if workorder_status is None:
            raise ValueError("Invalid value for `workorder_status`, must not be `None`")  # noqa: E501

        self._workorder_status = workorder_status

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
        if issubclass(UpdateWorkorder, dict):
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
        if not isinstance(other, UpdateWorkorder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
