# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'message': 'str',
        'update_available': 'bool'
    }

    attribute_map = {
        'message': 'message',
        'update_available': 'updateAvailable'
    }

    def __init__(self, message=None, update_available=None):
        """
        UpdateMessage - a model defined in Swagger
        """

        self._message = None
        self._update_available = None
        self.discriminator = None

        if message is not None:
          self.message = message
        if update_available is not None:
          self.update_available = update_available

    @property
    def message(self):
        """
        Gets the message of this UpdateMessage.

        :return: The message of this UpdateMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this UpdateMessage.

        :param message: The message of this UpdateMessage.
        :type: str
        """

        self._message = message

    @property
    def update_available(self):
        """
        Gets the update_available of this UpdateMessage.

        :return: The update_available of this UpdateMessage.
        :rtype: bool
        """
        return self._update_available

    @update_available.setter
    def update_available(self, update_available):
        """
        Sets the update_available of this UpdateMessage.

        :param update_available: The update_available of this UpdateMessage.
        :type: bool
        """

        self._update_available = update_available

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UpdateMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
