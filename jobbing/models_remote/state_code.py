# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class StateCode(Model):
	def __init__(self,
			id_state_code:int = None,
			state_code:str = None,
			state_name:str = None,
			id_country_code:int = None): # noqa: E501

		self.swagger_types = {
			'id_state_code': int,
			'state_code': str,
			'state_name': str,
			'id_country_code': int
		}

		self.attribute_map = {
			'id_state_code': 'id_state_code',
			'state_code': 'state_code',
			'state_name': 'state_name',
			'id_country_code': 'id_country_code'
		}

		self._id_state_code = id_state_code
		self._state_code = state_code
		self._state_name = state_name
		self._id_country_code = id_country_code

	@classmethod
	def from_dict(cls, dikt) -> 'StateCode':
		return util.deserialize_model(dikt, cls)

	@property
	def id_state_code(self) -> int:
		return self._id_state_code

	@id_state_code.setter
	def id_state_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_state_code`, must not be `None`")  # noqa: E501
		self._id_state_code = param

	@property
	def state_code(self) -> str:
		return self._state_code

	@state_code.setter
	def state_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `state_code`, must not be `None`")  # noqa: E501
		self._state_code = param

	@property
	def state_name(self) -> str:
		return self._state_name

	@state_name.setter
	def state_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `state_name`, must not be `None`")  # noqa: E501
		self._state_name = param

	@property
	def id_country_code(self) -> int:
		return self._id_country_code

	@id_country_code.setter
	def id_country_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_country_code`, must not be `None`")  # noqa: E501
		self._id_country_code = param

