# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: protos/fishjam/peer_notifications.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class PeerMessage(betterproto.Message):
    """Defines any type of message sent between FJ and a peer"""

    authenticated: "PeerMessageAuthenticated" = betterproto.message_field(
        1, group="content"
    )
    auth_request: "PeerMessageAuthRequest" = betterproto.message_field(
        2, group="content"
    )
    media_event: "PeerMessageMediaEvent" = betterproto.message_field(3, group="content")


@dataclass(eq=False, repr=False)
class PeerMessageAuthenticated(betterproto.Message):
    """Response sent by FJ, confirming successfull authentication"""

    pass


@dataclass(eq=False, repr=False)
class PeerMessageAuthRequest(betterproto.Message):
    """Request sent by peer, to authenticate to FJ server"""

    token: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class PeerMessageMediaEvent(betterproto.Message):
    """Any type of WebRTC messages passed betweend FJ and peer"""

    data: str = betterproto.string_field(1)
