# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util

from jobbing.models_remote.profession import Profession
from jobbing.models_remote.working_area import WorkingArea

class UserModel(Model):
	def __init__(self,
			user_model_id:int = None,
			user_status_id:int = None,
			user_role_id:int = None,
			user_model_first_name:str = None,
			user_model_last_name:str = None,
			user_model_surname:str = None,
			user_model_birthday:str = None,
			user_model_phone_number:str = None,
			user_model_address_id:int = None,
			user_model_registry_date:str = None,
			user_model_updated_date:str = None,
			user_model_media_id:int = None,
			user_model_org:int = None,
			user_model_creator_id:int = None,
			user_model_description:str = None,
			user_model_professions:List[Profession] = None,
			user_model_working_areas:List[WorkingArea] = None): # noqa: E501

		self.swagger_types = {
			'user_model_id': int,
			'user_status_id': int,
			'user_role_id': int,
			'user_model_first_name': str,
			'user_model_last_name': str,
			'user_model_surname': str,
			'user_model_birthday': str,
			'user_model_phone_number': str,
			'user_model_address_id': int,
			'user_model_registry_date': str,
			'user_model_updated_date': str,
			'user_model_media_id': int,
			'user_model_org': int,
			'user_model_creator_id': int,
			'user_model_description': str,
			'user_model_professions': List[Profession],
			'user_model_working_areas': List[WorkingArea]
		}

		self.attribute_map = {
			'user_model_id': 'user_model_id',
			'user_status_id': 'user_status_id',
			'user_role_id': 'user_role_id',
			'user_model_first_name': 'user_model_first_name',
			'user_model_last_name': 'user_model_last_name',
			'user_model_surname': 'user_model_surname',
			'user_model_birthday': 'user_model_birthday',
			'user_model_phone_number': 'user_model_phone_number',
			'user_model_address_id': 'user_model_address_id',
			'user_model_registry_date': 'user_model_registry_date',
			'user_model_updated_date': 'user_model_updated_date',
			'user_model_media_id': 'user_model_media_id',
			'user_model_org': 'user_model_org',
			'user_model_creator_id': 'user_model_creator_id',
			'user_model_description': 'user_model_description',
			'user_model_professions': 'user_model_professions',
			'user_model_working_areas': 'user_model_working_areas'
		}

		self._user_model_id = user_model_id
		self._user_status_id = user_status_id
		self._user_role_id = user_role_id
		self._user_model_first_name = user_model_first_name
		self._user_model_last_name = user_model_last_name
		self._user_model_surname = user_model_surname
		self._user_model_birthday = user_model_birthday
		self._user_model_phone_number = user_model_phone_number
		self._user_model_address_id = user_model_address_id
		self._user_model_registry_date = user_model_registry_date
		self._user_model_updated_date = user_model_updated_date
		self._user_model_media_id = user_model_media_id
		self._user_model_org = user_model_org
		self._user_model_creator_id = user_model_creator_id
		self._user_model_description = user_model_description
		self._user_model_professions = user_model_professions
		self._user_model_working_areas = user_model_working_areas

	@classmethod
	def from_dict(cls, dikt) -> 'UserModel':
		return util.deserialize_model(dikt, cls)

	@property
	def user_model_id(self) -> int:
		return self._user_model_id

	@user_model_id.setter
	def user_model_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_id`, must not be `None`")  # noqa: E501
		self._user_model_id = param

	@property
	def user_status_id(self) -> int:
		return self._user_status_id

	@user_status_id.setter
	def user_status_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_status_id`, must not be `None`")  # noqa: E501
		self._user_status_id = param

	@property
	def user_role_id(self) -> int:
		return self._user_role_id

	@user_role_id.setter
	def user_role_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_role_id`, must not be `None`")  # noqa: E501
		self._user_role_id = param

	@property
	def user_model_first_name(self) -> str:
		return self._user_model_first_name

	@user_model_first_name.setter
	def user_model_first_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_first_name`, must not be `None`")  # noqa: E501
		self._user_model_first_name = param

	@property
	def user_model_last_name(self) -> str:
		return self._user_model_last_name

	@user_model_last_name.setter
	def user_model_last_name(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_last_name`, must not be `None`")  # noqa: E501
		self._user_model_last_name = param

	@property
	def user_model_surname(self) -> str:
		return self._user_model_surname

	@user_model_surname.setter
	def user_model_surname(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_surname`, must not be `None`")  # noqa: E501
		self._user_model_surname = param

	@property
	def user_model_birthday(self) -> str:
		return self._user_model_birthday

	@user_model_birthday.setter
	def user_model_birthday(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_birthday`, must not be `None`")  # noqa: E501
		self._user_model_birthday = param

	@property
	def user_model_phone_number(self) -> str:
		return self._user_model_phone_number

	@user_model_phone_number.setter
	def user_model_phone_number(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_phone_number`, must not be `None`")  # noqa: E501
		self._user_model_phone_number = param

	@property
	def user_model_address_id(self) -> int:
		return self._user_model_address_id

	@user_model_address_id.setter
	def user_model_address_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_address_id`, must not be `None`")  # noqa: E501
		self._user_model_address_id = param

	@property
	def user_model_registry_date(self) -> str:
		return self._user_model_registry_date

	@user_model_registry_date.setter
	def user_model_registry_date(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_registry_date`, must not be `None`")  # noqa: E501
		self._user_model_registry_date = param

	@property
	def user_model_updated_date(self) -> str:
		return self._user_model_updated_date

	@user_model_updated_date.setter
	def user_model_updated_date(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_updated_date`, must not be `None`")  # noqa: E501
		self._user_model_updated_date = param

	@property
	def user_model_media_id(self) -> int:
		return self._user_model_media_id

	@user_model_media_id.setter
	def user_model_media_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_media_id`, must not be `None`")  # noqa: E501
		self._user_model_media_id = param

	@property
	def user_model_org(self) -> int:
		return self._user_model_org

	@user_model_org.setter
	def user_model_org(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_org`, must not be `None`")  # noqa: E501
		self._user_model_org = param

	@property
	def user_model_creator_id(self) -> int:
		return self._user_model_creator_id

	@user_model_creator_id.setter
	def user_model_creator_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_creator_id`, must not be `None`")  # noqa: E501
		self._user_model_creator_id = param

	@property
	def user_model_description(self) -> str:
		return self._user_model_description

	@user_model_description.setter
	def user_model_description(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_description`, must not be `None`")  # noqa: E501
		self._user_model_description = param

	@property
	def user_model_professions(self) -> List[Profession]:
		return self._user_model_professions

	@user_model_professions.setter
	def user_model_professions(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_professions`, must not be `None`")  # noqa: E501
		self._user_model_professions = param

	@property
	def user_model_working_areas(self) -> List[WorkingArea]:
		return self._user_model_working_areas

	@user_model_working_areas.setter
	def user_model_working_areas(self, param):
		if param is None:
			raise ValueError("Invalid value for `user_model_working_areas`, must not be `None`")  # noqa: E501
		self._user_model_working_areas = param

