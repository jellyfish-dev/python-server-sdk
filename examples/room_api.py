import os

from jellyfish import ComponentOptionsHLS, PeerOptionsWebRTC, RoomApi

HOST = "jellyfish" if os.getenv("DOCKER_TEST") == "TRUE" else "localhost"
SERVER_ADDRESS = f"{HOST}:5002"

# Create a room
room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token="development")

jellyfish_address, room = room_api.create_room(
    video_codec="h264", webhook_url="http://localhost:5000/webhook"
)
print((jellyfish_address, room))

# Add peer to the room
peer_token, peer_webrtc = room_api.add_peer(room.id, options=PeerOptionsWebRTC())
print((peer_token, peer_webrtc))

# Add component to the room
component_hls = room_api.add_component(room.id, options=ComponentOptionsHLS())
print(component_hls)
