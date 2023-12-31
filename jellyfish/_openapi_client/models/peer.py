from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.peer_status import PeerStatus

T = TypeVar("T", bound="Peer")


@_attrs_define
class Peer:
    """Describes peer status"""

    id: str
    """Assigned peer id"""
    status: PeerStatus
    """Informs about the peer status"""
    type: str
    """Peer type"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        id = self.id
        status = self.status.value

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        id = d.pop("id")

        status = PeerStatus(d.pop("status"))

        type = d.pop("type")

        peer = cls(
            id=id,
            status=status,
            type=type,
        )

        peer.additional_properties = d
        return peer

    @property
    def additional_keys(self) -> List[str]:
        """@private"""
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
