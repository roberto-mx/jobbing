# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class ZipCode(Model):
	def __init__(self,
			id_zip_code:int = None,
			zip_code:str = None): # noqa: E501

		self.swagger_types = {
			'id_zip_code': int,
			'zip_code': str
		}

		self.attribute_map = {
			'id_zip_code': 'id_zip_code',
			'zip_code': 'zip_code'
		}

		self._id_zip_code = id_zip_code
		self._zip_code = zip_code

	@classmethod
	def from_dict(cls, dikt) -> 'ZipCode':
		return util.deserialize_model(dikt, cls)

	@property
	def id_zip_code(self) -> int:
		return self._id_zip_code

	@id_zip_code.setter
	def id_zip_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `id_zip_code`, must not be `None`")  # noqa: E501
		self._id_zip_code = param

	@property
	def zip_code(self) -> str:
		return self._zip_code

	@zip_code.setter
	def zip_code(self, param):
		if param is None:
			raise ValueError("Invalid value for `zip_code`, must not be `None`")  # noqa: E501
		self._zip_code = param

