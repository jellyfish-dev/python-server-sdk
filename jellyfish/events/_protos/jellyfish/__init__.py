# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: protos/jellyfish/server_notifications.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


class ServerMessageEventType(betterproto.Enum):
    EVENT_TYPE_UNSPECIFIED = 0
    EVENT_TYPE_SERVER_NOTIFICATION = 1
    EVENT_TYPE_METRICS = 2


@dataclass(eq=False, repr=False)
class ServerMessage(betterproto.Message):
    room_crashed: "ServerMessageRoomCrashed" = betterproto.message_field(1, group="content")
    peer_connected: "ServerMessagePeerConnected" = betterproto.message_field(2, group="content")
    peer_disconnected: "ServerMessagePeerDisconnected" = betterproto.message_field(
        3, group="content"
    )
    peer_crashed: "ServerMessagePeerCrashed" = betterproto.message_field(4, group="content")
    component_crashed: "ServerMessageComponentCrashed" = betterproto.message_field(
        5, group="content"
    )
    authenticated: "ServerMessageAuthenticated" = betterproto.message_field(6, group="content")
    auth_request: "ServerMessageAuthRequest" = betterproto.message_field(7, group="content")
    subscribe_request: "ServerMessageSubscribeRequest" = betterproto.message_field(
        8, group="content"
    )
    subscribe_response: "ServerMessageSubscribeResponse" = betterproto.message_field(
        9, group="content"
    )
    room_created: "ServerMessageRoomCreated" = betterproto.message_field(10, group="content")
    room_deleted: "ServerMessageRoomDeleted" = betterproto.message_field(11, group="content")
    metrics_report: "ServerMessageMetricsReport" = betterproto.message_field(12, group="content")
    hls_playable: "ServerMessageHlsPlayable" = betterproto.message_field(13, group="content")


@dataclass(eq=False, repr=False)
class ServerMessageRoomCrashed(betterproto.Message):
    room_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessagePeerConnected(betterproto.Message):
    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessagePeerDisconnected(betterproto.Message):
    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessagePeerCrashed(betterproto.Message):
    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessageComponentCrashed(betterproto.Message):
    room_id: str = betterproto.string_field(1)
    component_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessageAuthenticated(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ServerMessageAuthRequest(betterproto.Message):
    token: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageSubscribeRequest(betterproto.Message):
    event_type: "ServerMessageEventType" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageSubscribeResponse(betterproto.Message):
    event_type: "ServerMessageEventType" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageRoomCreated(betterproto.Message):
    room_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageRoomDeleted(betterproto.Message):
    room_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageMetricsReport(betterproto.Message):
    metrics: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageHlsPlayable(betterproto.Message):
    room_id: str = betterproto.string_field(1)
    component_id: str = betterproto.string_field(2)
