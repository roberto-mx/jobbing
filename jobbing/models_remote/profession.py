# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util
from jobbing.models_remote.evidence import Evidence

class Profession(Model):
	def __init__(self,
			profession_id:int = None,
			profession_skill:int = None,
			profession_evidences:List[Evidence] = None): # noqa: E501

		self.swagger_types = {
			'profession_id': int,
			'profession_skill': int,
			'profession_evidences': List[Evidence]
		}

		self.attribute_map = {
			'profession_id': 'profession_id',
			'profession_skill': 'profession_skill',
			'profession_evidences': 'profession_evidences'
		}

		self._profession_id = profession_id
		self._profession_skill = profession_skill
		self._profession_evidences = profession_evidences

	@classmethod
	def from_dict(cls, dikt) -> 'Profession':
		return util.deserialize_model(dikt, cls)

	@property
	def profession_id(self) -> int:
		return self._profession_id

	@profession_id.setter
	def profession_id(self, param):
		if param is None:
			raise ValueError("Invalid value for `profession_id`, must not be `None`")  # noqa: E501
		self._profession_id = param

	@property
	def profession_skill(self) -> int:
		return self._profession_skill

	@profession_skill.setter
	def profession_skill(self, param):
		if param is None:
			raise ValueError("Invalid value for `profession_skill`, must not be `None`")  # noqa: E501
		self._profession_skill = param

	@property
	def profession_evidences(self) -> List[Evidence]:
		return self._profession_evidences

	@profession_evidences.setter
	def profession_evidences(self, param):
		if param is None:
			raise ValueError("Invalid value for `profession_evidences`, must not be `None`")  # noqa: E501
		self._profession_evidences = param

