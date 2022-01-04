# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Colony(Model):
	def __init__(self,
			id_colony_code:int = None,
			colony_name:str = None,
			id_municipality:int = None,
			id_zip_code:int = None): # noqa: E501

		self.swagger_types = {
			'id_colony_code': int,
			'colony_name': str,
			'id_municipality': int,
			'id_zip_code': int
		}

		self.attribute_map = {
			'id_colony_code': 'id_colony_code',
			'colony_name': 'colony_name',
			'id_municipality': 'id_municipality',
			'id_zip_code': 'id_zip_code'
		}

		self._id_colony_code = id_colony_code
		self._colony_name = colony_name
		self._id_municipality = id_municipality
		self._id_zip_code = id_zip_code

	@classmethod
	def from_dict(cls, dikt) -> 'Colony':
		return util.deserialize_model(dikt, cls)

	@property
	def id_colony_code(self) -> int:
		return self._id_colony_code

	@id_colony_code.setter
	def id_colony_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_colony_code`, must not be `None`")  # noqa: E501
		self._id_colony_code = param

	@property
	def colony_name(self) -> str:
		return self._colony_name

	@colony_name.setter
	def colony_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `colony_name`, must not be `None`")  # noqa: E501
		self._colony_name = param

	@property
	def id_municipality(self) -> int:
		return self._id_municipality

	@id_municipality.setter
	def id_municipality(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_municipality`, must not be `None`")  # noqa: E501
		self._id_municipality = param

	@property
	def id_zip_code(self) -> int:
		return self._id_zip_code

	@id_zip_code.setter
	def id_zip_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_zip_code`, must not be `None`")  # noqa: E501
		self._id_zip_code = param

