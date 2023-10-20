# coding: utf-8

"""
    Python API wrapper for Jellyfish Media Server

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from jellyfish._openapi_client.models.component import Component
from jellyfish._openapi_client.models.peer import Peer
from jellyfish._openapi_client.models.room_config import RoomConfig


class Room(BaseModel):
    """
    Description of the room state
    """

    components: conlist(Component) = Field(...)
    config: RoomConfig = Field(...)
    id: StrictStr = Field(..., description="Room ID")
    peers: conlist(Peer) = Field(...)
    __properties = ["components", "config", "id", "peers"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Room:
        """Create an instance of Room from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item in self.components:
                if _item:
                    _items.append(_item.to_dict())
            _dict["components"] = _items
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict["config"] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in peers (list)
        _items = []
        if self.peers:
            for _item in self.peers:
                if _item:
                    _items.append(_item.to_dict())
            _dict["peers"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Room:
        """Create an instance of Room from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Room.parse_obj(obj)

        _obj = Room.parse_obj(
            {
                "components": [
                    Component.from_dict(_item) for _item in obj.get("components")
                ]
                if obj.get("components") is not None
                else None,
                "config": RoomConfig.from_dict(obj.get("config"))
                if obj.get("config") is not None
                else None,
                "id": obj.get("id"),
                "peers": [Peer.from_dict(_item) for _item in obj.get("peers")]
                if obj.get("peers") is not None
                else None,
            }
        )
        return _obj
