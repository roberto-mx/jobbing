# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Album(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, album_id: int=None, title: str=None, description: str=None):  # noqa: E501
        """Album - a model defined in Swagger

        :param album_id: The album_id of this Album.  # noqa: E501
        :type album_id: int
        :param title: The title of this Album.  # noqa: E501
        :type title: str
        :param description: The description of this Album.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'album_id': int,
            'title': str,
            'description': str
        }

        self.attribute_map = {
            'album_id': 'albumId',
            'title': 'title',
            'description': 'description'
        }
        self._album_id = album_id
        self._title = title
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Album':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Album of this Album.  # noqa: E501
        :rtype: Album
        """
        return util.deserialize_model(dikt, cls)

    @property
    def album_id(self) -> int:
        """Gets the album_id of this Album.

        Primary key  # noqa: E501

        :return: The album_id of this Album.
        :rtype: int
        """
        return self._album_id

    @album_id.setter
    def album_id(self, album_id: int):
        """Sets the album_id of this Album.

        Primary key  # noqa: E501

        :param album_id: The album_id of this Album.
        :type album_id: int
        """

        self._album_id = album_id

    @property
    def title(self) -> str:
        """Gets the title of this Album.

        Title of the album content  # noqa: E501

        :return: The title of this Album.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Album.

        Title of the album content  # noqa: E501

        :param title: The title of this Album.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this Album.

        describe the content of the album  # noqa: E501

        :return: The description of this Album.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Album.

        describe the content of the album  # noqa: E501

        :param description: The description of this Album.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description
