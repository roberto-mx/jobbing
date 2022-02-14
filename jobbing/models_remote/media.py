# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Media(Model):
	def __init__(self,
			media_id:int = None,
			media_status_id:int = None,
			media_data:str = None,
			media_link:str = None,
			media_title:str = None,
			media_description:str = None,
			media_size:float = None,
			media_content_upload_date:str = None,
			media_content_updated_date:str = None): # noqa: E501

		self.swagger_types = {
			'media_id': int,
			'media_status_id': int,
			'media_data': str,
			'media_link': str,
			'media_title': str,
			'media_description': str,
			'media_size': float,
			'media_content_upload_date': str,
			'media_content_updated_date': str
		}

		self.attribute_map = {
			'media_id': 'media_id',
			'media_status_id': 'media_status_id',
			'media_data': 'media_data',
			'media_link': 'media_link',
			'media_title': 'media_title',
			'media_description': 'media_description',
			'media_size': 'media_size',
			'media_content_upload_date': 'media_content_upload_date',
			'media_content_updated_date': 'media_content_updated_date'
		}

		self._media_id = media_id
		self._media_status_id = media_status_id
		self._media_data = media_data
		self._media_link = media_link
		self._media_title = media_title
		self._media_description = media_description
		self._media_size = media_size
		self._media_content_upload_date = media_content_upload_date
		self._media_content_updated_date = media_content_updated_date

	@classmethod
	def from_dict(cls, dikt) -> 'Media':
		return util.deserialize_model(dikt, cls)

	@property
	def media_id(self) -> int:
		return self._media_id

	@media_id.setter
	def media_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `media_id`, must not be `None`")  # noqa: E501
		self._media_id = param

	@property
	def media_status_id(self) -> int:
		return self._media_status_id

	@media_status_id.setter
	def media_status_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `media_status_id`, must not be `None`")  # noqa: E501
		self._media_status_id = param

	@property
	def media_data(self) -> str:
		return self._media_data

	@media_data.setter
	def media_data(self, param):
		if param is None:
			raise ValueError("Invalid value for `media_data`, must not be `None`")  # noqa: E501
		self._media_data = param

	@property
	def media_link(self) -> str:
		return self._media_link

	@media_link.setter
	def media_link(self, param):
		if param is None:
			raise ValueError("Invalid value for `media_link`, must not be `None`")  # noqa: E501
		self._media_link = param

	@property
	def media_title(self) -> str:
		return self._media_title

	@media_title.setter
	def media_title(self, param):
		if param is None:
			raise ValueError("Invalid value for `media_title`, must not be `None`")  # noqa: E501
		self._media_title = param

	@property
	def media_description(self) -> str:
		return self._media_description

	@media_description.setter
	def media_description(self, param):
		if param is None:
			raise ValueError("Invalid value for `media_description`, must not be `None`")  # noqa: E501
		self._media_description = param

	@property
	def media_size(self) -> float:
		return self._media_size

	@media_size.setter
	def media_size(self, param):
		if param is None:
			raise ValueError("Invalid value for `media_size`, must not be `None`")  # noqa: E501
		self._media_size = param

	@property
	def media_content_upload_date(self) -> str:
		return self._media_content_upload_date

	@media_content_upload_date.setter
	def media_content_upload_date(self, param):
		if param is None:
			raise ValueError("Invalid value for `media_content_upload_date`, must not be `None`")  # noqa: E501
		self._media_content_upload_date = param

	@property
	def media_content_updated_date(self) -> str:
		return self._media_content_updated_date

	@media_content_updated_date.setter
	def media_content_updated_date(self, param):
		if param is None:
			raise ValueError("Invalid value for `media_content_updated_date`, must not be `None`")  # noqa: E501
		self._media_content_updated_date = param

