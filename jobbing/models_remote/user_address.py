# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class UserAddress(Model):
	def __init__(self,
			id_user_address:int = None,
			street_name:str = None,
			main_number:int = None,
			interior_number:int = None,
			id_colony_code:int = None,
			id_zip_code:int = None,
			id_state_code:int = None,
			id_municipality:int = None,
			id_country_code:int = None,
			date_added:str = None,
			last_update_date:str = None): # noqa: E501

		self.swagger_types = {
			'id_user_address': int,
			'street_name': str,
			'main_number': int,
			'interior_number': int,
			'id_colony_code': int,
			'id_zip_code': int,
			'id_state_code': int,
			'id_municipality': int,
			'id_country_code': int,
			'date_added': str,
			'last_update_date': str
		}

		self.attribute_map = {
			'id_user_address': 'id_user_address',
			'street_name': 'street_name',
			'main_number': 'main_number',
			'interior_number': 'interior_number',
			'id_colony_code': 'id_colony_code',
			'id_zip_code': 'id_zip_code',
			'id_state_code': 'id_state_code',
			'id_municipality': 'id_municipality',
			'id_country_code': 'id_country_code',
			'date_added': 'date_added',
			'last_update_date': 'last_update_date'
		}

		self._id_user_address = id_user_address
		self._street_name = street_name
		self._main_number = main_number
		self._interior_number = interior_number
		self._id_colony_code = id_colony_code
		self._id_zip_code = id_zip_code
		self._id_state_code = id_state_code
		self._id_municipality = id_municipality
		self._id_country_code = id_country_code
		self._date_added = date_added
		self._last_update_date = last_update_date

	@classmethod
	def from_dict(cls, dikt) -> 'UserAddress':
		return util.deserialize_model(dikt, cls)

	@property
	def id_user_address(self) -> int:
		return self._id_user_address

	@id_user_address.setter
	def id_user_address(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_user_address`, must not be `None`")  # noqa: E501
		self._id_user_address = param

	@property
	def street_name(self) -> str:
		return self._street_name

	@street_name.setter
	def street_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `street_name`, must not be `None`")  # noqa: E501
		self._street_name = param

	@property
	def main_number(self) -> int:
		return self._main_number

	@main_number.setter
	def main_number(self, param):
		if param is None:
			raise ValueError("Invalid value for `main_number`, must not be `None`")  # noqa: E501
		self._main_number = param

	@property
	def interior_number(self) -> int:
		return self._interior_number

	@interior_number.setter
	def interior_number(self, param):
		if param is None:
			raise ValueError("Invalid value for `interior_number`, must not be `None`")  # noqa: E501
		self._interior_number = param

	@property
	def id_colony_code(self) -> int:
		return self._id_colony_code

	@id_colony_code.setter
	def id_colony_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_colony_code`, must not be `None`")  # noqa: E501
		self._id_colony_code = param

	@property
	def id_zip_code(self) -> int:
		return self._id_zip_code

	@id_zip_code.setter
	def id_zip_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_zip_code`, must not be `None`")  # noqa: E501
		self._id_zip_code = param

	@property
	def id_state_code(self) -> int:
		return self._id_state_code

	@id_state_code.setter
	def id_state_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_state_code`, must not be `None`")  # noqa: E501
		self._id_state_code = param

	@property
	def id_municipality(self) -> int:
		return self._id_municipality

	@id_municipality.setter
	def id_municipality(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_municipality`, must not be `None`")  # noqa: E501
		self._id_municipality = param

	@property
	def id_country_code(self) -> int:
		return self._id_country_code

	@id_country_code.setter
	def id_country_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_country_code`, must not be `None`")  # noqa: E501
		self._id_country_code = param

	@property
	def date_added(self) -> str:
		return self._date_added

	@date_added.setter
	def date_added(self, param):
		if param is None:
			raise ValueError("Invalid value for `date_added`, must not be `None`")  # noqa: E501
		self._date_added = param

	@property
	def last_update_date(self) -> str:
		return self._last_update_date

	@last_update_date.setter
	def last_update_date(self, param):
		if param is None:
			raise ValueError("Invalid value for `last_update_date`, must not be `None`")  # noqa: E501
		self._last_update_date = param

