# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Status(Model):
	def __init__(self,
			status_id:int = None,
			status_name:str = None,
			status_updated_date:str = None): # noqa: E501

		self.swagger_types = {
			'status_id': int,
			'status_name': str,
			'status_updated_date': str
		}

		self.attribute_map = {
			'status_id': 'status_id',
			'status_name': 'status_name',
			'status_updated_date': 'status_updated_date'
		}

		self._status_id = status_id
		self._status_name = status_name
		self._status_updated_date = status_updated_date

	@classmethod
	def from_dict(cls, dikt) -> 'Status':
		return util.deserialize_model(dikt, cls)

	@property
	def status_id(self) -> int:
		return self._status_id

	@status_id.setter
	def status_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `status_id`, must not be `None`")  # noqa: E501
		self._status_id = param

	@property
	def status_name(self) -> str:
		return self._status_name

	@status_name.setter
	def status_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `status_name`, must not be `None`")  # noqa: E501
		self._status_name = param

	@property
	def status_updated_date(self) -> str:
		return self._status_updated_date

	@status_updated_date.setter
	def status_updated_date(self, param):
		if param is None:
			raise ValueError("Invalid value for `status_updated_date`, must not be `None`")  # noqa: E501
		self._status_updated_date = param

