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

class POTemplateResponseModel(object):
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
        'results': 'list[POTemplate]',
        'is_success': 'bool',
        'message': 'str',
        'status': 'str',
        'status_code': 'int',
        'page_number': 'int',
        'page_size': 'int',
        'total_number_of_pages': 'int',
        'total_number_of_records': 'int',
        'next_page_url': 'str'
    }

    attribute_map = {
        'results': 'Results',
        'is_success': 'IsSuccess',
        'message': 'Message',
        'status': 'Status',
        'status_code': 'StatusCode',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'total_number_of_pages': 'TotalNumberOfPages',
        'total_number_of_records': 'TotalNumberOfRecords',
        'next_page_url': 'NextPageUrl'
    }

    def __init__(self, results=None, is_success=None, message=None, status=None, status_code=None, page_number=None, page_size=None, total_number_of_pages=None, total_number_of_records=None, next_page_url=None):  # noqa: E501
        """POTemplateResponseModel - a model defined in Swagger"""  # noqa: E501
        self._results = None
        self._is_success = None
        self._message = None
        self._status = None
        self._status_code = None
        self._page_number = None
        self._page_size = None
        self._total_number_of_pages = None
        self._total_number_of_records = None
        self._next_page_url = None
        self.discriminator = None
        if results is not None:
            self.results = results
        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status
        if status_code is not None:
            self.status_code = status_code
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if total_number_of_pages is not None:
            self.total_number_of_pages = total_number_of_pages
        if total_number_of_records is not None:
            self.total_number_of_records = total_number_of_records
        if next_page_url is not None:
            self.next_page_url = next_page_url

    @property
    def results(self):
        """Gets the results of this POTemplateResponseModel.  # noqa: E501


        :return: The results of this POTemplateResponseModel.  # noqa: E501
        :rtype: list[POTemplate]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this POTemplateResponseModel.


        :param results: The results of this POTemplateResponseModel.  # noqa: E501
        :type: list[POTemplate]
        """

        self._results = results

    @property
    def is_success(self):
        """Gets the is_success of this POTemplateResponseModel.  # noqa: E501

        It represents Success of an API request.  # noqa: E501

        :return: The is_success of this POTemplateResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this POTemplateResponseModel.

        It represents Success of an API request.  # noqa: E501

        :param is_success: The is_success of this POTemplateResponseModel.  # noqa: E501
        :type: bool
        """

        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this POTemplateResponseModel.  # noqa: E501

        The Response represents the Response Message  of API  # noqa: E501

        :return: The message of this POTemplateResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this POTemplateResponseModel.

        The Response represents the Response Message  of API  # noqa: E501

        :param message: The message of this POTemplateResponseModel.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this POTemplateResponseModel.  # noqa: E501

        The Status represents the response status of API  # noqa: E501

        :return: The status of this POTemplateResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this POTemplateResponseModel.

        The Status represents the response status of API  # noqa: E501

        :param status: The status of this POTemplateResponseModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_code(self):
        """Gets the status_code of this POTemplateResponseModel.  # noqa: E501

        The Response represents the ResponseCode  of API  # noqa: E501

        :return: The status_code of this POTemplateResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this POTemplateResponseModel.

        The Response represents the ResponseCode  of API  # noqa: E501

        :param status_code: The status_code of this POTemplateResponseModel.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def page_number(self):
        """Gets the page_number of this POTemplateResponseModel.  # noqa: E501

        The page number this page represents.  # noqa: E501

        :return: The page_number of this POTemplateResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this POTemplateResponseModel.

        The page number this page represents.  # noqa: E501

        :param page_number: The page_number of this POTemplateResponseModel.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this POTemplateResponseModel.  # noqa: E501

        The number of records returned in a page.  # noqa: E501

        :return: The page_size of this POTemplateResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this POTemplateResponseModel.

        The number of records returned in a page.  # noqa: E501

        :param page_size: The page_size of this POTemplateResponseModel.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_number_of_pages(self):
        """Gets the total_number_of_pages of this POTemplateResponseModel.  # noqa: E501

        The total number of pages available.  # noqa: E501

        :return: The total_number_of_pages of this POTemplateResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_pages

    @total_number_of_pages.setter
    def total_number_of_pages(self, total_number_of_pages):
        """Sets the total_number_of_pages of this POTemplateResponseModel.

        The total number of pages available.  # noqa: E501

        :param total_number_of_pages: The total_number_of_pages of this POTemplateResponseModel.  # noqa: E501
        :type: int
        """

        self._total_number_of_pages = total_number_of_pages

    @property
    def total_number_of_records(self):
        """Gets the total_number_of_records of this POTemplateResponseModel.  # noqa: E501

        The total number of records available.  # noqa: E501

        :return: The total_number_of_records of this POTemplateResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_records

    @total_number_of_records.setter
    def total_number_of_records(self, total_number_of_records):
        """Sets the total_number_of_records of this POTemplateResponseModel.

        The total number of records available.  # noqa: E501

        :param total_number_of_records: The total_number_of_records of this POTemplateResponseModel.  # noqa: E501
        :type: int
        """

        self._total_number_of_records = total_number_of_records

    @property
    def next_page_url(self):
        """Gets the next_page_url of this POTemplateResponseModel.  # noqa: E501

        The URL to the next page - if null, there are no more pages.  # noqa: E501

        :return: The next_page_url of this POTemplateResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._next_page_url

    @next_page_url.setter
    def next_page_url(self, next_page_url):
        """Sets the next_page_url of this POTemplateResponseModel.

        The URL to the next page - if null, there are no more pages.  # noqa: E501

        :param next_page_url: The next_page_url of this POTemplateResponseModel.  # noqa: E501
        :type: str
        """

        self._next_page_url = next_page_url

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
        if issubclass(POTemplateResponseModel, dict):
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
        if not isinstance(other, POTemplateResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
