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

class PageResult(object):
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
        'is_success': 'bool',
        'message': 'str',
        'status': 'str',
        'status_code': 'int',
        'results': 'object'
    }

    attribute_map = {
        'is_success': 'IsSuccess',
        'message': 'Message',
        'status': 'Status',
        'status_code': 'StatusCode',
        'results': 'Results'
    }

    def __init__(self, is_success=None, message=None, status=None, status_code=None, results=None):  # noqa: E501
        """PageResult - a model defined in Swagger"""  # noqa: E501
        self._is_success = None
        self._message = None
        self._status = None
        self._status_code = None
        self._results = None
        self.discriminator = None
        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status
        if status_code is not None:
            self.status_code = status_code
        if results is not None:
            self.results = results

    @property
    def is_success(self):
        """Gets the is_success of this PageResult.  # noqa: E501

        It represents Success of an API request.  # noqa: E501

        :return: The is_success of this PageResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this PageResult.

        It represents Success of an API request.  # noqa: E501

        :param is_success: The is_success of this PageResult.  # noqa: E501
        :type: bool
        """

        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this PageResult.  # noqa: E501

        The Response represents the Response Message  of API  # noqa: E501

        :return: The message of this PageResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PageResult.

        The Response represents the Response Message  of API  # noqa: E501

        :param message: The message of this PageResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this PageResult.  # noqa: E501

        The Status represents the response status of API  # noqa: E501

        :return: The status of this PageResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PageResult.

        The Status represents the response status of API  # noqa: E501

        :param status: The status of this PageResult.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_code(self):
        """Gets the status_code of this PageResult.  # noqa: E501

        The Response represents the ResponseCode  of API  # noqa: E501

        :return: The status_code of this PageResult.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this PageResult.

        The Response represents the ResponseCode  of API  # noqa: E501

        :param status_code: The status_code of this PageResult.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def results(self):
        """Gets the results of this PageResult.  # noqa: E501

        The records this page represents.  # noqa: E501

        :return: The results of this PageResult.  # noqa: E501
        :rtype: object
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PageResult.

        The records this page represents.  # noqa: E501

        :param results: The results of this PageResult.  # noqa: E501
        :type: object
        """

        self._results = results

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
        if issubclass(PageResult, dict):
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
        if not isinstance(other, PageResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
