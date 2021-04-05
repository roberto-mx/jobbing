# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Role(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, role_id: int=None, name: str=None, status: str=None):  # noqa: E501
        """Role - a model defined in Swagger

        :param role_id: The role_id of this Role.  # noqa: E501
        :type role_id: int
        :param name: The name of this Role.  # noqa: E501
        :type name: str
        :param status: The status of this Role.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'role_id': int,
            'name': str,
            'status': str
        }

        self.attribute_map = {
            'role_id': 'roleId',
            'name': 'name',
            'status': 'status'
        }
        self._role_id = role_id
        self._name = name
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Role':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Role of this Role.  # noqa: E501
        :rtype: Role
        """
        return util.deserialize_model(dikt, cls)

    @property
    def role_id(self) -> int:
        """Gets the role_id of this Role.

        Access roles  # noqa: E501

        :return: The role_id of this Role.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id: int):
        """Sets the role_id of this Role.

        Access roles  # noqa: E501

        :param role_id: The role_id of this Role.
        :type role_id: int
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def name(self) -> str:
        """Gets the name of this Role.

        Name of the role  # noqa: E501

        :return: The name of this Role.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Role.

        Name of the role  # noqa: E501

        :param name: The name of this Role.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self) -> str:
        """Gets the status of this Role.

        Defines if role is active or not  # noqa: E501

        :return: The status of this Role.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Role.

        Defines if role is active or not  # noqa: E501

        :param status: The status of this Role.
        :type status: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
