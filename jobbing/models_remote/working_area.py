# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class WorkingArea(Model):
	def __init__(self,
			working_area_id:int = None,
			working_area_municipality:int = None): # noqa: E501

		self.swagger_types = {
			'working_area_id': int,
			'working_area_municipality': int
		}

		self.attribute_map = {
			'working_area_id': 'working_area_id',
			'working_area_municipality': 'working_area_municipality'
		}

		self._working_area_id = working_area_id
		self._working_area_municipality = working_area_municipality

	@classmethod
	def from_dict(cls, dikt) -> 'WorkingArea':
		return util.deserialize_model(dikt, cls)

	@property
	def working_area_id(self) -> int:
		return self._working_area_id

	@working_area_id.setter
	def working_area_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `working_area_id`, must not be `None`")  # noqa: E501
		self._working_area_id = param

	@property
	def working_area_municipality(self) -> int:
		return self._working_area_municipality

	@working_area_municipality.setter
	def working_area_municipality(self, param):
		if param is None:
			raise ValueError("Invalid value for `working_area_municipality`, must not be `None`")  # noqa: E501
		self._working_area_municipality = param

