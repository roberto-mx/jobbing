# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Municipality(Model):
	def __init__(self,
			id_municipality:int = None,
			municipality_name:str = None,
			id_state_code:int = None): # noqa: E501

		self.swagger_types = {
			'id_municipality': int,
			'municipality_name': str,
			'id_state_code': int
		}

		self.attribute_map = {
			'id_municipality': 'id_municipality',
			'municipality_name': 'municipality_name',
			'id_state_code': 'id_state_code'
		}

		self._id_municipality = id_municipality
		self._municipality_name = municipality_name
		self._id_state_code = id_state_code

	@classmethod
	def from_dict(cls, dikt) -> 'Municipality':
		return util.deserialize_model(dikt, cls)

	@property
	def id_municipality(self) -> int:
		return self._id_municipality

	@id_municipality.setter
	def id_municipality(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_municipality`, must not be `None`")  # noqa: E501
		self._id_municipality = param

	@property
	def municipality_name(self) -> str:
		return self._municipality_name

	@municipality_name.setter
	def municipality_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `municipality_name`, must not be `None`")  # noqa: E501
		self._municipality_name = param

	@property
	def id_state_code(self) -> int:
		return self._id_state_code

	@id_state_code.setter
	def id_state_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_state_code`, must not be `None`")  # noqa: E501
		self._id_state_code = param

