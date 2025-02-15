# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, time: str=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param time: The time of this InlineResponse200.  # noqa: E501
        :type time: str
        """
        self.swagger_types = {
            'time': str
        }

        self.attribute_map = {
            'time': 'time'
        }
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def time(self) -> str:
        """Gets the time of this InlineResponse200.


        :return: The time of this InlineResponse200.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """Sets the time of this InlineResponse200.


        :param time: The time of this InlineResponse200.
        :type time: str
        """

        self._time = time
