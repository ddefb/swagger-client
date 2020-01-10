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


class EntityTypeFilter(object):
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
        'relation_type': 'str',
        'entity_types': 'list[str]'
    }

    attribute_map = {
        'relation_type': 'relationType',
        'entity_types': 'entityTypes'
    }

    def __init__(self, relation_type=None, entity_types=None):
        """
        EntityTypeFilter - a model defined in Swagger
        """

        self._relation_type = None
        self._entity_types = None
        self.discriminator = None

        self.relation_type = relation_type
        self.entity_types = entity_types

    @property
    def relation_type(self):
        """
        Gets the relation_type of this EntityTypeFilter.

        :return: The relation_type of this EntityTypeFilter.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """
        Sets the relation_type of this EntityTypeFilter.

        :param relation_type: The relation_type of this EntityTypeFilter.
        :type: str
        """
        if relation_type is None:
            raise ValueError("Invalid value for `relation_type`, must not be `None`")

        self._relation_type = relation_type

    @property
    def entity_types(self):
        """
        Gets the entity_types of this EntityTypeFilter.

        :return: The entity_types of this EntityTypeFilter.
        :rtype: list[str]
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """
        Sets the entity_types of this EntityTypeFilter.

        :param entity_types: The entity_types of this EntityTypeFilter.
        :type: list[str]
        """
        if entity_types is None:
            raise ValueError("Invalid value for `entity_types`, must not be `None`")
        allowed_values = ["TENANT", "CUSTOMER", "USER", "RULE", "PLUGIN", "DASHBOARD", "ASSET", "DEVICE", "ALARM"]
        if not set(entity_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `entity_types` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(entity_types)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._entity_types = entity_types

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
        if not isinstance(other, EntityTypeFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
