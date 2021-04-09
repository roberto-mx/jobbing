# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Neighborhood(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, neighborhood_id: int=None, name: str=None, zip_code: int=None, municipality_id: int=None):  # noqa: E501
        """Neighborhood - a model defined in Swagger

        :param neighborhood_id: The neighborhood_id of this Neighborhood.  # noqa: E501
        :type neighborhood_id: int
        :param name: The name of this Neighborhood.  # noqa: E501
        :type name: str
        :param zip_code: The zip_code of this Neighborhood.  # noqa: E501
        :type zip_code: int
        :param municipality_id: The municipality_id of this Neighborhood.  # noqa: E501
        :type municipality_id: int
        """
        self.swagger_types = {
            'neighborhood_id': int,
            'name': str,
            'zip_code': int,
            'municipality_id': int
        }

        self.attribute_map = {
            'neighborhood_id': 'neighborhoodId',
            'name': 'name',
            'zip_code': 'zipCode',
            'municipality_id': 'municipalityId'
        }
        self._neighborhood_id = neighborhood_id
        self._name = name
        self._zip_code = zip_code
        self._municipality_id = municipality_id

    @classmethod
    def from_dict(cls, dikt) -> 'Neighborhood':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Neighborhood of this Neighborhood.  # noqa: E501
        :rtype: Neighborhood
        """
        return util.deserialize_model(dikt, cls)

    @property
    def neighborhood_id(self) -> int:
        """Gets the neighborhood_id of this Neighborhood.


        :return: The neighborhood_id of this Neighborhood.
        :rtype: int
        """
        return self._neighborhood_id

    @neighborhood_id.setter
    def neighborhood_id(self, neighborhood_id: int):
        """Sets the neighborhood_id of this Neighborhood.


        :param neighborhood_id: The neighborhood_id of this Neighborhood.
        :type neighborhood_id: int
        """
        if neighborhood_id is None:
            raise ValueError("Invalid value for `neighborhood_id`, must not be `None`")  # noqa: E501

        self._neighborhood_id = neighborhood_id

    @property
    def name(self) -> str:
        """Gets the name of this Neighborhood.


        :return: The name of this Neighborhood.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Neighborhood.


        :param name: The name of this Neighborhood.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def zip_code(self) -> int:
        """Gets the zip_code of this Neighborhood.


        :return: The zip_code of this Neighborhood.
        :rtype: int
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code: int):
        """Sets the zip_code of this Neighborhood.


        :param zip_code: The zip_code of this Neighborhood.
        :type zip_code: int
        """
        if zip_code is None:
            raise ValueError("Invalid value for `zip_code`, must not be `None`")  # noqa: E501

        self._zip_code = zip_code

    @property
    def municipality_id(self) -> int:
        """Gets the municipality_id of this Neighborhood.


        :return: The municipality_id of this Neighborhood.
        :rtype: int
        """
        return self._municipality_id

    @municipality_id.setter
    def municipality_id(self, municipality_id: int):
        """Sets the municipality_id of this Neighborhood.


        :param municipality_id: The municipality_id of this Neighborhood.
        :type municipality_id: int
        """
        if municipality_id is None:
            raise ValueError("Invalid value for `municipality_id`, must not be `None`")  # noqa: E501

        self._municipality_id = municipality_id