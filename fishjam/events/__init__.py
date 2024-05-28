"""
.. include:: ../../docs/server_notifications.md
"""

# Exported messages
from fishjam.events._protos.fishjam import (
    ServerMessageComponentCrashed,
    ServerMessageHlsPlayable,
    ServerMessageMetricsReport,
    ServerMessagePeerAdded,
    ServerMessagePeerConnected,
    ServerMessagePeerCrashed,
    ServerMessagePeerDeleted,
    ServerMessagePeerDisconnected,
    ServerMessageRoomCrashed,
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageTrack,
    ServerMessageTrackAdded,
    ServerMessageTrackMetadataUpdated,
    ServerMessageTrackRemoved,
    ServerMessageTrackType,
)

__all__ = [
    "ServerMessageRoomCreated",
    "ServerMessageRoomDeleted",
    "ServerMessageRoomCrashed",
    "ServerMessagePeerAdded",
    "ServerMessagePeerConnected",
    "ServerMessagePeerDeleted",
    "ServerMessagePeerDisconnected",
    "ServerMessagePeerCrashed",
    "ServerMessageComponentCrashed",
    "ServerMessageTrack",
    "ServerMessageTrackType",
    "ServerMessageTrackAdded",
    "ServerMessageTrackMetadataUpdated",
    "ServerMessageTrackRemoved",
    "ServerMessageHlsPlayable",
    "ServerMessageMetricsReport",
]