# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Skills(Model):
	def __init__(self,
			skills_id:int = None,
			skills_name:str = None,
			skills_media_id:int = None,
			skills_description:str = None,
			skills_updated_date:str = None): # noqa: E501

		self.swagger_types = {
			'skills_id': int,
			'skills_name': str,
			'skills_media_id': int,
			'skills_description': str,
			'skills_updated_date': str
		}

		self.attribute_map = {
			'skills_id': 'skills_id',
			'skills_name': 'skills_name',
			'skills_media_id': 'skills_media_id',
			'skills_description': 'skills_description',
			'skills_updated_date': 'skills_updated_date'
		}

		self._skills_id = skills_id
		self._skills_name = skills_name
		self._skills_media_id = skills_media_id
		self._skills_description = skills_description
		self._skills_updated_date = skills_updated_date

	@classmethod
	def from_dict(cls, dikt) -> 'Skills':
		return util.deserialize_model(dikt, cls)

	@property
	def skills_id(self) -> int:
		return self._skills_id

	@skills_id.setter
	def skills_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `skills_id`, must not be `None`")  # noqa: E501
		self._skills_id = param

	@property
	def skills_name(self) -> str:
		return self._skills_name

	@skills_name.setter
	def skills_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `skills_name`, must not be `None`")  # noqa: E501
		self._skills_name = param

	@property
	def skills_media_id(self) -> int:
		return self._skills_media_id

	@skills_media_id.setter
	def skills_media_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `skills_media_id`, must not be `None`")  # noqa: E501
		self._skills_media_id = param

	@property
	def skills_description(self) -> str:
		return self._skills_description

	@skills_description.setter
	def skills_description(self, param):
		if param is None:
			raise ValueError("Invalid value for `skills_description`, must not be `None`")  # noqa: E501
		self._skills_description = param

	@property
	def skills_updated_date(self) -> str:
		return self._skills_updated_date

	@skills_updated_date.setter
	def skills_updated_date(self, param):
		if param is None:
			raise ValueError("Invalid value for `skills_updated_date`, must not be `None`")  # noqa: E501
		self._skills_updated_date = param

