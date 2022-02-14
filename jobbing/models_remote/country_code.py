# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class CountryCode(Model):
	def __init__(self,
			id_country_code:int = None,
			country_code:int = None,
			country_name:str = None): # noqa: E501

		self.swagger_types = {
			'id_country_code': int,
			'country_code': int,
			'country_name': str
		}

		self.attribute_map = {
			'id_country_code': 'id_country_code',
			'country_code': 'country_code',
			'country_name': 'country_name'
		}

		self._id_country_code = id_country_code
		self._country_code = country_code
		self._country_name = country_name

	@classmethod
	def from_dict(cls, dikt) -> 'CountryCode':
		return util.deserialize_model(dikt, cls)

	@property
	def id_country_code(self) -> int:
		return self._id_country_code

	@id_country_code.setter
	def id_country_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_country_code`, must not be `None`")  # noqa: E501
		self._id_country_code = param

	@property
	def country_code(self) -> int:
		return self._country_code

	@country_code.setter
	def country_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501
		self._country_code = param

	@property
	def country_name(self) -> str:
		return self._country_name

	@country_name.setter
	def country_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `country_name`, must not be `None`")  # noqa: E501
		self._country_name = param

