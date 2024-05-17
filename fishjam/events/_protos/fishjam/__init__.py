# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: protos/fishjam/server_notifications.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


class ServerMessageEventType(betterproto.Enum):
    """Defines message groups for which client can subscribe"""

    EVENT_TYPE_UNSPECIFIED = 0
    EVENT_TYPE_SERVER_NOTIFICATION = 1
    EVENT_TYPE_METRICS = 2


class ServerMessageTrackType(betterproto.Enum):
    """Defines types of tracks being published by peers and component"""

    TRACK_TYPE_UNSPECIFIED = 0
    TRACK_TYPE_VIDEO = 1
    TRACK_TYPE_AUDIO = 2


@dataclass(eq=False, repr=False)
class ServerMessage(betterproto.Message):
    """Defines any type of message passed between FJ and server client"""

    room_crashed: "ServerMessageRoomCrashed" = betterproto.message_field(
        1, group="content"
    )
    peer_connected: "ServerMessagePeerConnected" = betterproto.message_field(
        2, group="content"
    )
    peer_disconnected: "ServerMessagePeerDisconnected" = betterproto.message_field(
        3, group="content"
    )
    peer_crashed: "ServerMessagePeerCrashed" = betterproto.message_field(
        4, group="content"
    )
    component_crashed: "ServerMessageComponentCrashed" = betterproto.message_field(
        5, group="content"
    )
    authenticated: "ServerMessageAuthenticated" = betterproto.message_field(
        6, group="content"
    )
    auth_request: "ServerMessageAuthRequest" = betterproto.message_field(
        7, group="content"
    )
    subscribe_request: "ServerMessageSubscribeRequest" = betterproto.message_field(
        8, group="content"
    )
    subscribe_response: "ServerMessageSubscribeResponse" = betterproto.message_field(
        9, group="content"
    )
    room_created: "ServerMessageRoomCreated" = betterproto.message_field(
        10, group="content"
    )
    room_deleted: "ServerMessageRoomDeleted" = betterproto.message_field(
        11, group="content"
    )
    metrics_report: "ServerMessageMetricsReport" = betterproto.message_field(
        12, group="content"
    )
    hls_playable: "ServerMessageHlsPlayable" = betterproto.message_field(
        13, group="content"
    )
    hls_uploaded: "ServerMessageHlsUploaded" = betterproto.message_field(
        14, group="content"
    )
    hls_upload_crashed: "ServerMessageHlsUploadCrashed" = betterproto.message_field(
        15, group="content"
    )
    peer_metadata_updated: "ServerMessagePeerMetadataUpdated" = (
        betterproto.message_field(16, group="content")
    )
    track_added: "ServerMessageTrackAdded" = betterproto.message_field(
        17, group="content"
    )
    track_removed: "ServerMessageTrackRemoved" = betterproto.message_field(
        18, group="content"
    )
    track_metadata_updated: "ServerMessageTrackMetadataUpdated" = (
        betterproto.message_field(19, group="content")
    )
    peer_added: "ServerMessagePeerAdded" = betterproto.message_field(
        20, group="content"
    )
    peer_deleted: "ServerMessagePeerDeleted" = betterproto.message_field(
        21, group="content"
    )


@dataclass(eq=False, repr=False)
class ServerMessageRoomCrashed(betterproto.Message):
    """Notification sent when a room crashes"""

    room_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessagePeerAdded(betterproto.Message):
    """Notification sent when a peer is added"""

    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessagePeerDeleted(betterproto.Message):
    """Notification sent when a peer is removed"""

    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessagePeerConnected(betterproto.Message):
    """Notification sent when a peer connects"""

    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessagePeerDisconnected(betterproto.Message):
    """Notification sent when a peer disconnects from FJ"""

    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessagePeerCrashed(betterproto.Message):
    """Notification sent when a peer crashes"""

    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2)
    reason: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class ServerMessageComponentCrashed(betterproto.Message):
    """Notification sent when a component crashes"""

    room_id: str = betterproto.string_field(1)
    component_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessageAuthenticated(betterproto.Message):
    """Response sent by FJ, confirming successfull authentication"""

    pass


@dataclass(eq=False, repr=False)
class ServerMessageAuthRequest(betterproto.Message):
    """Request sent by client, to authenticate to FJ server"""

    token: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageSubscribeRequest(betterproto.Message):
    """Request sent by client to subsribe for certain message type"""

    event_type: "ServerMessageEventType" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageSubscribeResponse(betterproto.Message):
    """Response sent by FJ, confirming subscription for message type"""

    event_type: "ServerMessageEventType" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageRoomCreated(betterproto.Message):
    """Notification sent when a room is created"""

    room_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageRoomDeleted(betterproto.Message):
    """Notification sent when a room is deleted"""

    room_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageMetricsReport(betterproto.Message):
    """Message containing WebRTC metrics from FJ"""

    metrics: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageHlsPlayable(betterproto.Message):
    """Notification sent when the HLS stream becomes available in a room"""

    room_id: str = betterproto.string_field(1)
    component_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ServerMessageHlsUploaded(betterproto.Message):
    """
    Notification sent when the HLS recording is successfully uploded to AWS S3
    """

    room_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessageHlsUploadCrashed(betterproto.Message):
    """Notification sent when the upload of HLS recording to AWS S3 fails"""

    room_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ServerMessagePeerMetadataUpdated(betterproto.Message):
    """Notification sent when peer updates its metadata"""

    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2)
    metadata: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class ServerMessageTrack(betterproto.Message):
    """Describes a media track"""

    id: str = betterproto.string_field(1)
    type: "ServerMessageTrackType" = betterproto.enum_field(2)
    metadata: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class ServerMessageTrackAdded(betterproto.Message):
    """Notification sent when peer or component adds new track"""

    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2, group="endpoint_info")
    component_id: str = betterproto.string_field(3, group="endpoint_info")
    track: "ServerMessageTrack" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ServerMessageTrackRemoved(betterproto.Message):
    """Notification sent when a track is removed"""

    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2, group="endpoint_info")
    component_id: str = betterproto.string_field(3, group="endpoint_info")
    track: "ServerMessageTrack" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ServerMessageTrackMetadataUpdated(betterproto.Message):
    """Notification sent when metadata of a multimedia track is updated"""

    room_id: str = betterproto.string_field(1)
    peer_id: str = betterproto.string_field(2, group="endpoint_info")
    component_id: str = betterproto.string_field(3, group="endpoint_info")
    track: "ServerMessageTrack" = betterproto.message_field(4)
