# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Evidence(Model):
	def __init__(self,
			evidence_id:int = None,
			evidence_media:int = None): # noqa: E501

		self.swagger_types = {
			'evidence_id': int,
			'evidence_media': int
		}

		self.attribute_map = {
			'evidence_id': 'evidence_id',
			'evidence_media': 'evidence_media'
		}

		self._evidence_id = evidence_id
		self._evidence_media = evidence_media

	@classmethod
	def from_dict(cls, dikt) -> 'Evidence':
		return util.deserialize_model(dikt, cls)

	@property
	def evidence_id(self) -> int:
		return self._evidence_id

	@evidence_id.setter
	def evidence_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `evidence_id`, must not be `None`")  # noqa: E501
		self._evidence_id = param

	@property
	def evidence_media(self) -> int:
		return self._evidence_media

	@evidence_media.setter
	def evidence_media(self, param):
		if param is None:
			raise ValueError("Invalid value for `evidence_media`, must not be `None`")  # noqa: E501
		self._evidence_media = param

