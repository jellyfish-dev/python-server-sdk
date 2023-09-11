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



from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.peer_options import PeerOptions

class AddPeerRequest(BaseModel):
    """
    AddPeerRequest
    """
    options: PeerOptions = Field(...)
    type: StrictStr = Field(..., description="Peer type")
    __properties = ["options", "type"]

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
    def from_json(cls, json_str: str) -> AddPeerRequest:
        """Create an instance of AddPeerRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddPeerRequest:
        """Create an instance of AddPeerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddPeerRequest.parse_obj(obj)

        _obj = AddPeerRequest.parse_obj({
            "options": PeerOptions.from_dict(obj.get("options")) if obj.get("options") is not None else None,
            "type": obj.get("type")
        })
        return _obj


