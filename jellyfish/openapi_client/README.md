# jellyfish-openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.2.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import jellyfish_openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import jellyfish_openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import jellyfish_openapi_client
from jellyfish_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfish_openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authorization
configuration = jellyfish_openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with jellyfish_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfish_openapi_client.DefaultApi(api_client)
    room_id = 'room_id_example' # str | Room id
    filename = 'filename_example' # str | Name of the file
    range = 'range_example' # str | Byte range of partial segment (optional)
    hls_msn = 56 # int | Segment sequence number (optional)
    hls_part = 56 # int | Partial segment sequence number (optional)
    hls_skip = jellyfish_openapi_client.HlsSkip() # HlsSkip | Is delta manifest requested (optional)

    try:
        # Send file
        api_response = api_instance.jellyfish_web_hls_controller_index(room_id, filename, range=range, hls_msn=hls_msn, hls_part=hls_part, hls_skip=hls_skip)
        print("The response of DefaultApi->jellyfish_web_hls_controller_index:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->jellyfish_web_hls_controller_index: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**jellyfish_web_hls_controller_index**](docs/DefaultApi.md#jellyfish_web_hls_controller_index) | **GET** /hls/{room_id}/{filename} | Send file
*RoomApi* | [**add_component**](docs/RoomApi.md#add_component) | **POST** /room/{room_id}/component | Creates the component and adds it to the room
*RoomApi* | [**add_peer**](docs/RoomApi.md#add_peer) | **POST** /room/{room_id}/peer | Create peer
*RoomApi* | [**create_room**](docs/RoomApi.md#create_room) | **POST** /room | Creates a room
*RoomApi* | [**delete_component**](docs/RoomApi.md#delete_component) | **DELETE** /room/{room_id}/component/{id} | Delete the component from the room
*RoomApi* | [**delete_peer**](docs/RoomApi.md#delete_peer) | **DELETE** /room/{room_id}/peer/{id} | Delete peer
*RoomApi* | [**delete_room**](docs/RoomApi.md#delete_room) | **DELETE** /room/{room_id} | Delete the room
*RoomApi* | [**get_all_rooms**](docs/RoomApi.md#get_all_rooms) | **GET** /room | Show information about all rooms
*RoomApi* | [**get_room**](docs/RoomApi.md#get_room) | **GET** /room/{room_id} | Shows information about the room


## Documentation For Models

 - [AddComponentRequest](docs/AddComponentRequest.md)
 - [AddPeerRequest](docs/AddPeerRequest.md)
 - [Component](docs/Component.md)
 - [ComponentDetailsResponse](docs/ComponentDetailsResponse.md)
 - [ComponentMetadata](docs/ComponentMetadata.md)
 - [ComponentOptions](docs/ComponentOptions.md)
 - [ComponentOptionsRTSP](docs/ComponentOptionsRTSP.md)
 - [Error](docs/Error.md)
 - [HlsSkip](docs/HlsSkip.md)
 - [Peer](docs/Peer.md)
 - [PeerDetailsResponse](docs/PeerDetailsResponse.md)
 - [PeerDetailsResponseData](docs/PeerDetailsResponseData.md)
 - [PeerOptions](docs/PeerOptions.md)
 - [PeerOptionsWebRTC](docs/PeerOptionsWebRTC.md)
 - [PeerStatus](docs/PeerStatus.md)
 - [Room](docs/Room.md)
 - [RoomConfig](docs/RoomConfig.md)
 - [RoomCreateDetailsResponse](docs/RoomCreateDetailsResponse.md)
 - [RoomCreateDetailsResponseData](docs/RoomCreateDetailsResponseData.md)
 - [RoomDetailsResponse](docs/RoomDetailsResponse.md)
 - [RoomsListingResponse](docs/RoomsListingResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="authorization"></a>
### authorization

- **Type**: Bearer authentication


## Author



