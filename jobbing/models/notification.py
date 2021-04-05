# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jobbing.models.base_model_ import Model
from jobbing import util


class Notification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, notification_id: int=None, title: str=None, message: str=None, status: int=None, created: date=None, updated: date=None, account_id: int=None, notification_type_id: int=None, media_id: int=None):  # noqa: E501
        """Notification - a model defined in Swagger

        :param notification_id: The notification_id of this Notification.  # noqa: E501
        :type notification_id: int
        :param title: The title of this Notification.  # noqa: E501
        :type title: str
        :param message: The message of this Notification.  # noqa: E501
        :type message: str
        :param status: The status of this Notification.  # noqa: E501
        :type status: int
        :param created: The created of this Notification.  # noqa: E501
        :type created: date
        :param updated: The updated of this Notification.  # noqa: E501
        :type updated: date
        :param account_id: The account_id of this Notification.  # noqa: E501
        :type account_id: int
        :param notification_type_id: The notification_type_id of this Notification.  # noqa: E501
        :type notification_type_id: int
        :param media_id: The media_id of this Notification.  # noqa: E501
        :type media_id: int
        """
        self.swagger_types = {
            'notification_id': int,
            'title': str,
            'message': str,
            'status': int,
            'created': date,
            'updated': date,
            'account_id': int,
            'notification_type_id': int,
            'media_id': int
        }

        self.attribute_map = {
            'notification_id': 'notificationId',
            'title': 'title',
            'message': 'message',
            'status': 'status',
            'created': 'created',
            'updated': 'updated',
            'account_id': 'accountId',
            'notification_type_id': 'notificationTypeId',
            'media_id': 'mediaId'
        }
        self._notification_id = notification_id
        self._title = title
        self._message = message
        self._status = status
        self._created = created
        self._updated = updated
        self._account_id = account_id
        self._notification_type_id = notification_type_id
        self._media_id = media_id

    @classmethod
    def from_dict(cls, dikt) -> 'Notification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Notification of this Notification.  # noqa: E501
        :rtype: Notification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notification_id(self) -> int:
        """Gets the notification_id of this Notification.

        Primary key  # noqa: E501

        :return: The notification_id of this Notification.
        :rtype: int
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id: int):
        """Sets the notification_id of this Notification.

        Primary key  # noqa: E501

        :param notification_id: The notification_id of this Notification.
        :type notification_id: int
        """

        self._notification_id = notification_id

    @property
    def title(self) -> str:
        """Gets the title of this Notification.

        HO  # noqa: E501

        :return: The title of this Notification.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Notification.

        HO  # noqa: E501

        :param title: The title of this Notification.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def message(self) -> str:
        """Gets the message of this Notification.

        The message to notify about something  # noqa: E501

        :return: The message of this Notification.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Notification.

        The message to notify about something  # noqa: E501

        :param message: The message of this Notification.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def status(self) -> int:
        """Gets the status of this Notification.

        Status of the notification  # noqa: E501

        :return: The status of this Notification.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this Notification.

        Status of the notification  # noqa: E501

        :param status: The status of this Notification.
        :type status: int
        """

        self._status = status

    @property
    def created(self) -> date:
        """Gets the created of this Notification.

        Date when the notification was created  # noqa: E501

        :return: The created of this Notification.
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created: date):
        """Sets the created of this Notification.

        Date when the notification was created  # noqa: E501

        :param created: The created of this Notification.
        :type created: date
        """

        self._created = created

    @property
    def updated(self) -> date:
        """Gets the updated of this Notification.

        Date when the notification was updated  # noqa: E501

        :return: The updated of this Notification.
        :rtype: date
        """
        return self._updated

    @updated.setter
    def updated(self, updated: date):
        """Sets the updated of this Notification.

        Date when the notification was updated  # noqa: E501

        :param updated: The updated of this Notification.
        :type updated: date
        """

        self._updated = updated

    @property
    def account_id(self) -> int:
        """Gets the account_id of this Notification.

        Foreign key of the account that is associated to this notification  # noqa: E501

        :return: The account_id of this Notification.
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: int):
        """Sets the account_id of this Notification.

        Foreign key of the account that is associated to this notification  # noqa: E501

        :param account_id: The account_id of this Notification.
        :type account_id: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def notification_type_id(self) -> int:
        """Gets the notification_type_id of this Notification.

        Foreign key of the notification type tha is associated to this notification  # noqa: E501

        :return: The notification_type_id of this Notification.
        :rtype: int
        """
        return self._notification_type_id

    @notification_type_id.setter
    def notification_type_id(self, notification_type_id: int):
        """Sets the notification_type_id of this Notification.

        Foreign key of the notification type tha is associated to this notification  # noqa: E501

        :param notification_type_id: The notification_type_id of this Notification.
        :type notification_type_id: int
        """
        if notification_type_id is None:
            raise ValueError("Invalid value for `notification_type_id`, must not be `None`")  # noqa: E501

        self._notification_type_id = notification_type_id

    @property
    def media_id(self) -> int:
        """Gets the media_id of this Notification.

        Foreign key of the media that is associated to this notification  # noqa: E501

        :return: The media_id of this Notification.
        :rtype: int
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id: int):
        """Sets the media_id of this Notification.

        Foreign key of the media that is associated to this notification  # noqa: E501

        :param media_id: The media_id of this Notification.
        :type media_id: int
        """
        if media_id is None:
            raise ValueError("Invalid value for `media_id`, must not be `None`")  # noqa: E501

        self._media_id = media_id
