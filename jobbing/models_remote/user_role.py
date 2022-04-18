# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class UserRole(Model):
	def __init__(self,
			user_role_id:int = None,
			user_role_name:str = None,
			user_role_updated_date:str = None): # noqa: E501

		self.swagger_types = {
			'user_role_id': int,
			'user_role_name': str,
			'user_role_updated_date': str
		}

		self.attribute_map = {
			'user_role_id': 'user_role_id',
			'user_role_name': 'user_role_name',
			'user_role_updated_date': 'user_role_updated_date'
		}

		self._user_role_id = user_role_id
		self._user_role_name = user_role_name
		self._user_role_updated_date = user_role_updated_date

	@classmethod
	def from_dict(cls, dikt) -> 'UserRole':
		return util.deserialize_model(dikt, cls)

	@property
	def user_role_id(self) -> int:
		return self._user_role_id

	@user_role_id.setter
	def user_role_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_role_id`, must not be `None`")  # noqa: E501
		self._user_role_id = param

	@property
	def user_role_name(self) -> str:
		return self._user_role_name

	@user_role_name.setter
	def user_role_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_role_name`, must not be `None`")  # noqa: E501
		self._user_role_name = param

	@property
	def user_role_updated_date(self) -> str:
		return self._user_role_updated_date

	@user_role_updated_date.setter
	def user_role_updated_date(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_role_updated_date`, must not be `None`")  # noqa: E501
		self._user_role_updated_date = param

