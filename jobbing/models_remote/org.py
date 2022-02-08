# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Org(Model):
	def __init__(self,
			org_id:int = None,
			org_name:str = None,
			org_media_id:int = None): # noqa: E501

		self.swagger_types = {
			'org_id': int,
			'org_name': str,
			'org_media_id': int
		}

		self.attribute_map = {
			'org_id': 'org_id',
			'org_name': 'org_name',
			'org_media_id': 'org_media_id'
		}

		self._org_id = org_id
		self._org_name = org_name
		self._org_media_id = org_media_id

	@classmethod
	def from_dict(cls, dikt) -> 'Org':
		return util.deserialize_model(dikt, cls)

	@property
	def org_id(self) -> int:
		return self._org_id

	@org_id.setter
	def org_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501
		self._org_id = param

	@property
	def org_name(self) -> str:
		return self._org_name

	@org_name.setter
	def org_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `org_name`, must not be `None`")  # noqa: E501
		self._org_name = param

	@property
	def org_media_id(self) -> int:
		return self._org_media_id

	@org_media_id.setter
	def org_media_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `org_media_id`, must not be `None`")  # noqa: E501
		self._org_media_id = param

