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

class WorkOrderList(object):
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
        'workorder_id': 'int',
        'title': 'str',
        'reference_id': 'str',
        'category_ref': 'WorkorderCategoryRef',
        'priority_ref': 'WorkorderPriorityRef',
        'status_ref': 'WorkorderStatus',
        'workorder_type_ref': 'WorkorderTypeRef',
        'short_description': 'str',
        'notes': 'str',
        'private_notes': 'str',
        'comments': 'str',
        'primary_contact': 'str',
        'primary_phone': 'str',
        'alternate_contact': 'str',
        'alternate_phone': 'str',
        'external_emails': 'str',
        'start_date': 'datetime',
        'due_date': 'datetime',
        'planned_due_date': 'datetime',
        'completed_date': 'datetime',
        'closed_date': 'datetime',
        'approved_date': 'datetime',
        'enter_work_area': 'str',
        'customer_ref': 'list[CustomerRef]',
        'building_group_ref': 'DepartmentRef',
        'building_ref': 'BuildingRef',
        'location_ref': 'list[LocationRef]',
        'asset_ref': 'list[AssetRef]',
        'vendor_ref': 'list[VendorRef]',
        'task_ref': 'list[WOTaskDetailRef]',
        'part_ref': 'list[WOPartRef]',
        'staff_ref': 'list[StaffRef]',
        'customer_invoice_ref': 'list[InvoiceRef]',
        'vendor_invoice_ref': 'list[InvoiceRef]',
        'work_order_audit': 'list[WorkOrderAudit]',
        'total_hours': 'str',
        'total_cost': 'float',
        'total_parts_cost': 'float',
        'total_invoice_cost': 'float',
        'total_labour_cost': 'float'
    }

    attribute_map = {
        'site_ref': 'SiteRef',
        'workorder_id': 'WorkorderId',
        'title': 'Title',
        'reference_id': 'ReferenceID',
        'category_ref': 'CategoryRef',
        'priority_ref': 'PriorityRef',
        'status_ref': 'StatusRef',
        'workorder_type_ref': 'WorkorderTypeRef',
        'short_description': 'ShortDescription',
        'notes': 'Notes',
        'private_notes': 'PrivateNotes',
        'comments': 'Comments',
        'primary_contact': 'PrimaryContact',
        'primary_phone': 'PrimaryPhone',
        'alternate_contact': 'AlternateContact',
        'alternate_phone': 'AlternatePhone',
        'external_emails': 'ExternalEmails',
        'start_date': 'StartDate',
        'due_date': 'DueDate',
        'planned_due_date': 'PlannedDueDate',
        'completed_date': 'CompletedDate',
        'closed_date': 'ClosedDate',
        'approved_date': 'ApprovedDate',
        'enter_work_area': 'EnterWorkArea',
        'customer_ref': 'CustomerRef',
        'building_group_ref': 'BuildingGroupRef',
        'building_ref': 'BuildingRef',
        'location_ref': 'LocationRef',
        'asset_ref': 'AssetRef',
        'vendor_ref': 'VendorRef',
        'task_ref': 'TaskRef',
        'part_ref': 'PartRef',
        'staff_ref': 'StaffRef',
        'customer_invoice_ref': 'CustomerInvoiceRef',
        'vendor_invoice_ref': 'VendorInvoiceRef',
        'work_order_audit': 'WorkOrderAudit',
        'total_hours': 'TotalHours',
        'total_cost': 'TotalCost',
        'total_parts_cost': 'TotalPartsCost',
        'total_invoice_cost': 'TotalInvoiceCost',
        'total_labour_cost': 'TotalLabourCost'
    }

    def __init__(self, site_ref=None, workorder_id=None, title=None, reference_id=None, category_ref=None, priority_ref=None, status_ref=None, workorder_type_ref=None, short_description=None, notes=None, private_notes=None, comments=None, primary_contact=None, primary_phone=None, alternate_contact=None, alternate_phone=None, external_emails=None, start_date=None, due_date=None, planned_due_date=None, completed_date=None, closed_date=None, approved_date=None, enter_work_area=None, customer_ref=None, building_group_ref=None, building_ref=None, location_ref=None, asset_ref=None, vendor_ref=None, task_ref=None, part_ref=None, staff_ref=None, customer_invoice_ref=None, vendor_invoice_ref=None, work_order_audit=None, total_hours=None, total_cost=None, total_parts_cost=None, total_invoice_cost=None, total_labour_cost=None):  # noqa: E501
        """WorkOrderList - a model defined in Swagger"""  # noqa: E501
        self._site_ref = None
        self._workorder_id = None
        self._title = None
        self._reference_id = None
        self._category_ref = None
        self._priority_ref = None
        self._status_ref = None
        self._workorder_type_ref = None
        self._short_description = None
        self._notes = None
        self._private_notes = None
        self._comments = None
        self._primary_contact = None
        self._primary_phone = None
        self._alternate_contact = None
        self._alternate_phone = None
        self._external_emails = None
        self._start_date = None
        self._due_date = None
        self._planned_due_date = None
        self._completed_date = None
        self._closed_date = None
        self._approved_date = None
        self._enter_work_area = None
        self._customer_ref = None
        self._building_group_ref = None
        self._building_ref = None
        self._location_ref = None
        self._asset_ref = None
        self._vendor_ref = None
        self._task_ref = None
        self._part_ref = None
        self._staff_ref = None
        self._customer_invoice_ref = None
        self._vendor_invoice_ref = None
        self._work_order_audit = None
        self._total_hours = None
        self._total_cost = None
        self._total_parts_cost = None
        self._total_invoice_cost = None
        self._total_labour_cost = None
        self.discriminator = None
        if site_ref is not None:
            self.site_ref = site_ref
        if workorder_id is not None:
            self.workorder_id = workorder_id
        if title is not None:
            self.title = title
        if reference_id is not None:
            self.reference_id = reference_id
        if category_ref is not None:
            self.category_ref = category_ref
        if priority_ref is not None:
            self.priority_ref = priority_ref
        if status_ref is not None:
            self.status_ref = status_ref
        if workorder_type_ref is not None:
            self.workorder_type_ref = workorder_type_ref
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
        if primary_phone is not None:
            self.primary_phone = primary_phone
        if alternate_contact is not None:
            self.alternate_contact = alternate_contact
        if alternate_phone is not None:
            self.alternate_phone = alternate_phone
        if external_emails is not None:
            self.external_emails = external_emails
        if start_date is not None:
            self.start_date = start_date
        if due_date is not None:
            self.due_date = due_date
        if planned_due_date is not None:
            self.planned_due_date = planned_due_date
        if completed_date is not None:
            self.completed_date = completed_date
        if closed_date is not None:
            self.closed_date = closed_date
        if approved_date is not None:
            self.approved_date = approved_date
        if enter_work_area is not None:
            self.enter_work_area = enter_work_area
        if customer_ref is not None:
            self.customer_ref = customer_ref
        if building_group_ref is not None:
            self.building_group_ref = building_group_ref
        if building_ref is not None:
            self.building_ref = building_ref
        if location_ref is not None:
            self.location_ref = location_ref
        if asset_ref is not None:
            self.asset_ref = asset_ref
        if vendor_ref is not None:
            self.vendor_ref = vendor_ref
        if task_ref is not None:
            self.task_ref = task_ref
        if part_ref is not None:
            self.part_ref = part_ref
        if staff_ref is not None:
            self.staff_ref = staff_ref
        if customer_invoice_ref is not None:
            self.customer_invoice_ref = customer_invoice_ref
        if vendor_invoice_ref is not None:
            self.vendor_invoice_ref = vendor_invoice_ref
        if work_order_audit is not None:
            self.work_order_audit = work_order_audit
        if total_hours is not None:
            self.total_hours = total_hours
        if total_cost is not None:
            self.total_cost = total_cost
        if total_parts_cost is not None:
            self.total_parts_cost = total_parts_cost
        if total_invoice_cost is not None:
            self.total_invoice_cost = total_invoice_cost
        if total_labour_cost is not None:
            self.total_labour_cost = total_labour_cost

    @property
    def site_ref(self):
        """Gets the site_ref of this WorkOrderList.  # noqa: E501


        :return: The site_ref of this WorkOrderList.  # noqa: E501
        :rtype: SiteRef
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """Sets the site_ref of this WorkOrderList.


        :param site_ref: The site_ref of this WorkOrderList.  # noqa: E501
        :type: SiteRef
        """

        self._site_ref = site_ref

    @property
    def workorder_id(self):
        """Gets the workorder_id of this WorkOrderList.  # noqa: E501


        :return: The workorder_id of this WorkOrderList.  # noqa: E501
        :rtype: int
        """
        return self._workorder_id

    @workorder_id.setter
    def workorder_id(self, workorder_id):
        """Sets the workorder_id of this WorkOrderList.


        :param workorder_id: The workorder_id of this WorkOrderList.  # noqa: E501
        :type: int
        """

        self._workorder_id = workorder_id

    @property
    def title(self):
        """Gets the title of this WorkOrderList.  # noqa: E501


        :return: The title of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WorkOrderList.


        :param title: The title of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def reference_id(self):
        """Gets the reference_id of this WorkOrderList.  # noqa: E501


        :return: The reference_id of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this WorkOrderList.


        :param reference_id: The reference_id of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def category_ref(self):
        """Gets the category_ref of this WorkOrderList.  # noqa: E501


        :return: The category_ref of this WorkOrderList.  # noqa: E501
        :rtype: WorkorderCategoryRef
        """
        return self._category_ref

    @category_ref.setter
    def category_ref(self, category_ref):
        """Sets the category_ref of this WorkOrderList.


        :param category_ref: The category_ref of this WorkOrderList.  # noqa: E501
        :type: WorkorderCategoryRef
        """

        self._category_ref = category_ref

    @property
    def priority_ref(self):
        """Gets the priority_ref of this WorkOrderList.  # noqa: E501


        :return: The priority_ref of this WorkOrderList.  # noqa: E501
        :rtype: WorkorderPriorityRef
        """
        return self._priority_ref

    @priority_ref.setter
    def priority_ref(self, priority_ref):
        """Sets the priority_ref of this WorkOrderList.


        :param priority_ref: The priority_ref of this WorkOrderList.  # noqa: E501
        :type: WorkorderPriorityRef
        """

        self._priority_ref = priority_ref

    @property
    def status_ref(self):
        """Gets the status_ref of this WorkOrderList.  # noqa: E501


        :return: The status_ref of this WorkOrderList.  # noqa: E501
        :rtype: WorkorderStatus
        """
        return self._status_ref

    @status_ref.setter
    def status_ref(self, status_ref):
        """Sets the status_ref of this WorkOrderList.


        :param status_ref: The status_ref of this WorkOrderList.  # noqa: E501
        :type: WorkorderStatus
        """

        self._status_ref = status_ref

    @property
    def workorder_type_ref(self):
        """Gets the workorder_type_ref of this WorkOrderList.  # noqa: E501


        :return: The workorder_type_ref of this WorkOrderList.  # noqa: E501
        :rtype: WorkorderTypeRef
        """
        return self._workorder_type_ref

    @workorder_type_ref.setter
    def workorder_type_ref(self, workorder_type_ref):
        """Sets the workorder_type_ref of this WorkOrderList.


        :param workorder_type_ref: The workorder_type_ref of this WorkOrderList.  # noqa: E501
        :type: WorkorderTypeRef
        """

        self._workorder_type_ref = workorder_type_ref

    @property
    def short_description(self):
        """Gets the short_description of this WorkOrderList.  # noqa: E501


        :return: The short_description of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this WorkOrderList.


        :param short_description: The short_description of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def notes(self):
        """Gets the notes of this WorkOrderList.  # noqa: E501


        :return: The notes of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this WorkOrderList.


        :param notes: The notes of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def private_notes(self):
        """Gets the private_notes of this WorkOrderList.  # noqa: E501


        :return: The private_notes of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._private_notes

    @private_notes.setter
    def private_notes(self, private_notes):
        """Sets the private_notes of this WorkOrderList.


        :param private_notes: The private_notes of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._private_notes = private_notes

    @property
    def comments(self):
        """Gets the comments of this WorkOrderList.  # noqa: E501


        :return: The comments of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this WorkOrderList.


        :param comments: The comments of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def primary_contact(self):
        """Gets the primary_contact of this WorkOrderList.  # noqa: E501


        :return: The primary_contact of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._primary_contact

    @primary_contact.setter
    def primary_contact(self, primary_contact):
        """Sets the primary_contact of this WorkOrderList.


        :param primary_contact: The primary_contact of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._primary_contact = primary_contact

    @property
    def primary_phone(self):
        """Gets the primary_phone of this WorkOrderList.  # noqa: E501


        :return: The primary_phone of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._primary_phone

    @primary_phone.setter
    def primary_phone(self, primary_phone):
        """Sets the primary_phone of this WorkOrderList.


        :param primary_phone: The primary_phone of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._primary_phone = primary_phone

    @property
    def alternate_contact(self):
        """Gets the alternate_contact of this WorkOrderList.  # noqa: E501


        :return: The alternate_contact of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._alternate_contact

    @alternate_contact.setter
    def alternate_contact(self, alternate_contact):
        """Sets the alternate_contact of this WorkOrderList.


        :param alternate_contact: The alternate_contact of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._alternate_contact = alternate_contact

    @property
    def alternate_phone(self):
        """Gets the alternate_phone of this WorkOrderList.  # noqa: E501


        :return: The alternate_phone of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._alternate_phone

    @alternate_phone.setter
    def alternate_phone(self, alternate_phone):
        """Sets the alternate_phone of this WorkOrderList.


        :param alternate_phone: The alternate_phone of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._alternate_phone = alternate_phone

    @property
    def external_emails(self):
        """Gets the external_emails of this WorkOrderList.  # noqa: E501


        :return: The external_emails of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._external_emails

    @external_emails.setter
    def external_emails(self, external_emails):
        """Sets the external_emails of this WorkOrderList.


        :param external_emails: The external_emails of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._external_emails = external_emails

    @property
    def start_date(self):
        """Gets the start_date of this WorkOrderList.  # noqa: E501


        :return: The start_date of this WorkOrderList.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this WorkOrderList.


        :param start_date: The start_date of this WorkOrderList.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def due_date(self):
        """Gets the due_date of this WorkOrderList.  # noqa: E501


        :return: The due_date of this WorkOrderList.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this WorkOrderList.


        :param due_date: The due_date of this WorkOrderList.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def planned_due_date(self):
        """Gets the planned_due_date of this WorkOrderList.  # noqa: E501


        :return: The planned_due_date of this WorkOrderList.  # noqa: E501
        :rtype: datetime
        """
        return self._planned_due_date

    @planned_due_date.setter
    def planned_due_date(self, planned_due_date):
        """Sets the planned_due_date of this WorkOrderList.


        :param planned_due_date: The planned_due_date of this WorkOrderList.  # noqa: E501
        :type: datetime
        """

        self._planned_due_date = planned_due_date

    @property
    def completed_date(self):
        """Gets the completed_date of this WorkOrderList.  # noqa: E501


        :return: The completed_date of this WorkOrderList.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """Sets the completed_date of this WorkOrderList.


        :param completed_date: The completed_date of this WorkOrderList.  # noqa: E501
        :type: datetime
        """

        self._completed_date = completed_date

    @property
    def closed_date(self):
        """Gets the closed_date of this WorkOrderList.  # noqa: E501


        :return: The closed_date of this WorkOrderList.  # noqa: E501
        :rtype: datetime
        """
        return self._closed_date

    @closed_date.setter
    def closed_date(self, closed_date):
        """Sets the closed_date of this WorkOrderList.


        :param closed_date: The closed_date of this WorkOrderList.  # noqa: E501
        :type: datetime
        """

        self._closed_date = closed_date

    @property
    def approved_date(self):
        """Gets the approved_date of this WorkOrderList.  # noqa: E501


        :return: The approved_date of this WorkOrderList.  # noqa: E501
        :rtype: datetime
        """
        return self._approved_date

    @approved_date.setter
    def approved_date(self, approved_date):
        """Sets the approved_date of this WorkOrderList.


        :param approved_date: The approved_date of this WorkOrderList.  # noqa: E501
        :type: datetime
        """

        self._approved_date = approved_date

    @property
    def enter_work_area(self):
        """Gets the enter_work_area of this WorkOrderList.  # noqa: E501


        :return: The enter_work_area of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._enter_work_area

    @enter_work_area.setter
    def enter_work_area(self, enter_work_area):
        """Sets the enter_work_area of this WorkOrderList.


        :param enter_work_area: The enter_work_area of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._enter_work_area = enter_work_area

    @property
    def customer_ref(self):
        """Gets the customer_ref of this WorkOrderList.  # noqa: E501


        :return: The customer_ref of this WorkOrderList.  # noqa: E501
        :rtype: list[CustomerRef]
        """
        return self._customer_ref

    @customer_ref.setter
    def customer_ref(self, customer_ref):
        """Sets the customer_ref of this WorkOrderList.


        :param customer_ref: The customer_ref of this WorkOrderList.  # noqa: E501
        :type: list[CustomerRef]
        """

        self._customer_ref = customer_ref

    @property
    def building_group_ref(self):
        """Gets the building_group_ref of this WorkOrderList.  # noqa: E501


        :return: The building_group_ref of this WorkOrderList.  # noqa: E501
        :rtype: DepartmentRef
        """
        return self._building_group_ref

    @building_group_ref.setter
    def building_group_ref(self, building_group_ref):
        """Sets the building_group_ref of this WorkOrderList.


        :param building_group_ref: The building_group_ref of this WorkOrderList.  # noqa: E501
        :type: DepartmentRef
        """

        self._building_group_ref = building_group_ref

    @property
    def building_ref(self):
        """Gets the building_ref of this WorkOrderList.  # noqa: E501


        :return: The building_ref of this WorkOrderList.  # noqa: E501
        :rtype: BuildingRef
        """
        return self._building_ref

    @building_ref.setter
    def building_ref(self, building_ref):
        """Sets the building_ref of this WorkOrderList.


        :param building_ref: The building_ref of this WorkOrderList.  # noqa: E501
        :type: BuildingRef
        """

        self._building_ref = building_ref

    @property
    def location_ref(self):
        """Gets the location_ref of this WorkOrderList.  # noqa: E501


        :return: The location_ref of this WorkOrderList.  # noqa: E501
        :rtype: list[LocationRef]
        """
        return self._location_ref

    @location_ref.setter
    def location_ref(self, location_ref):
        """Sets the location_ref of this WorkOrderList.


        :param location_ref: The location_ref of this WorkOrderList.  # noqa: E501
        :type: list[LocationRef]
        """

        self._location_ref = location_ref

    @property
    def asset_ref(self):
        """Gets the asset_ref of this WorkOrderList.  # noqa: E501


        :return: The asset_ref of this WorkOrderList.  # noqa: E501
        :rtype: list[AssetRef]
        """
        return self._asset_ref

    @asset_ref.setter
    def asset_ref(self, asset_ref):
        """Sets the asset_ref of this WorkOrderList.


        :param asset_ref: The asset_ref of this WorkOrderList.  # noqa: E501
        :type: list[AssetRef]
        """

        self._asset_ref = asset_ref

    @property
    def vendor_ref(self):
        """Gets the vendor_ref of this WorkOrderList.  # noqa: E501


        :return: The vendor_ref of this WorkOrderList.  # noqa: E501
        :rtype: list[VendorRef]
        """
        return self._vendor_ref

    @vendor_ref.setter
    def vendor_ref(self, vendor_ref):
        """Sets the vendor_ref of this WorkOrderList.


        :param vendor_ref: The vendor_ref of this WorkOrderList.  # noqa: E501
        :type: list[VendorRef]
        """

        self._vendor_ref = vendor_ref

    @property
    def task_ref(self):
        """Gets the task_ref of this WorkOrderList.  # noqa: E501


        :return: The task_ref of this WorkOrderList.  # noqa: E501
        :rtype: list[WOTaskDetailRef]
        """
        return self._task_ref

    @task_ref.setter
    def task_ref(self, task_ref):
        """Sets the task_ref of this WorkOrderList.


        :param task_ref: The task_ref of this WorkOrderList.  # noqa: E501
        :type: list[WOTaskDetailRef]
        """

        self._task_ref = task_ref

    @property
    def part_ref(self):
        """Gets the part_ref of this WorkOrderList.  # noqa: E501


        :return: The part_ref of this WorkOrderList.  # noqa: E501
        :rtype: list[WOPartRef]
        """
        return self._part_ref

    @part_ref.setter
    def part_ref(self, part_ref):
        """Sets the part_ref of this WorkOrderList.


        :param part_ref: The part_ref of this WorkOrderList.  # noqa: E501
        :type: list[WOPartRef]
        """

        self._part_ref = part_ref

    @property
    def staff_ref(self):
        """Gets the staff_ref of this WorkOrderList.  # noqa: E501


        :return: The staff_ref of this WorkOrderList.  # noqa: E501
        :rtype: list[StaffRef]
        """
        return self._staff_ref

    @staff_ref.setter
    def staff_ref(self, staff_ref):
        """Sets the staff_ref of this WorkOrderList.


        :param staff_ref: The staff_ref of this WorkOrderList.  # noqa: E501
        :type: list[StaffRef]
        """

        self._staff_ref = staff_ref

    @property
    def customer_invoice_ref(self):
        """Gets the customer_invoice_ref of this WorkOrderList.  # noqa: E501


        :return: The customer_invoice_ref of this WorkOrderList.  # noqa: E501
        :rtype: list[InvoiceRef]
        """
        return self._customer_invoice_ref

    @customer_invoice_ref.setter
    def customer_invoice_ref(self, customer_invoice_ref):
        """Sets the customer_invoice_ref of this WorkOrderList.


        :param customer_invoice_ref: The customer_invoice_ref of this WorkOrderList.  # noqa: E501
        :type: list[InvoiceRef]
        """

        self._customer_invoice_ref = customer_invoice_ref

    @property
    def vendor_invoice_ref(self):
        """Gets the vendor_invoice_ref of this WorkOrderList.  # noqa: E501


        :return: The vendor_invoice_ref of this WorkOrderList.  # noqa: E501
        :rtype: list[InvoiceRef]
        """
        return self._vendor_invoice_ref

    @vendor_invoice_ref.setter
    def vendor_invoice_ref(self, vendor_invoice_ref):
        """Sets the vendor_invoice_ref of this WorkOrderList.


        :param vendor_invoice_ref: The vendor_invoice_ref of this WorkOrderList.  # noqa: E501
        :type: list[InvoiceRef]
        """

        self._vendor_invoice_ref = vendor_invoice_ref

    @property
    def work_order_audit(self):
        """Gets the work_order_audit of this WorkOrderList.  # noqa: E501


        :return: The work_order_audit of this WorkOrderList.  # noqa: E501
        :rtype: list[WorkOrderAudit]
        """
        return self._work_order_audit

    @work_order_audit.setter
    def work_order_audit(self, work_order_audit):
        """Sets the work_order_audit of this WorkOrderList.


        :param work_order_audit: The work_order_audit of this WorkOrderList.  # noqa: E501
        :type: list[WorkOrderAudit]
        """

        self._work_order_audit = work_order_audit

    @property
    def total_hours(self):
        """Gets the total_hours of this WorkOrderList.  # noqa: E501


        :return: The total_hours of this WorkOrderList.  # noqa: E501
        :rtype: str
        """
        return self._total_hours

    @total_hours.setter
    def total_hours(self, total_hours):
        """Sets the total_hours of this WorkOrderList.


        :param total_hours: The total_hours of this WorkOrderList.  # noqa: E501
        :type: str
        """

        self._total_hours = total_hours

    @property
    def total_cost(self):
        """Gets the total_cost of this WorkOrderList.  # noqa: E501


        :return: The total_cost of this WorkOrderList.  # noqa: E501
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this WorkOrderList.


        :param total_cost: The total_cost of this WorkOrderList.  # noqa: E501
        :type: float
        """

        self._total_cost = total_cost

    @property
    def total_parts_cost(self):
        """Gets the total_parts_cost of this WorkOrderList.  # noqa: E501


        :return: The total_parts_cost of this WorkOrderList.  # noqa: E501
        :rtype: float
        """
        return self._total_parts_cost

    @total_parts_cost.setter
    def total_parts_cost(self, total_parts_cost):
        """Sets the total_parts_cost of this WorkOrderList.


        :param total_parts_cost: The total_parts_cost of this WorkOrderList.  # noqa: E501
        :type: float
        """

        self._total_parts_cost = total_parts_cost

    @property
    def total_invoice_cost(self):
        """Gets the total_invoice_cost of this WorkOrderList.  # noqa: E501


        :return: The total_invoice_cost of this WorkOrderList.  # noqa: E501
        :rtype: float
        """
        return self._total_invoice_cost

    @total_invoice_cost.setter
    def total_invoice_cost(self, total_invoice_cost):
        """Sets the total_invoice_cost of this WorkOrderList.


        :param total_invoice_cost: The total_invoice_cost of this WorkOrderList.  # noqa: E501
        :type: float
        """

        self._total_invoice_cost = total_invoice_cost

    @property
    def total_labour_cost(self):
        """Gets the total_labour_cost of this WorkOrderList.  # noqa: E501


        :return: The total_labour_cost of this WorkOrderList.  # noqa: E501
        :rtype: float
        """
        return self._total_labour_cost

    @total_labour_cost.setter
    def total_labour_cost(self, total_labour_cost):
        """Sets the total_labour_cost of this WorkOrderList.


        :param total_labour_cost: The total_labour_cost of this WorkOrderList.  # noqa: E501
        :type: float
        """

        self._total_labour_cost = total_labour_cost

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
        if issubclass(WorkOrderList, dict):
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
        if not isinstance(other, WorkOrderList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other