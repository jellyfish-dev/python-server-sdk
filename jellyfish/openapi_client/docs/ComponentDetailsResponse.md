# ComponentDetailsResponse

Response containing component details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Component**](Component.md) |  | 

## Example

```python
from jellyfish_openapi_client.models.component_details_response import ComponentDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentDetailsResponse from a JSON string
component_details_response_instance = ComponentDetailsResponse.from_json(json)
# print the JSON string representation of the object
print ComponentDetailsResponse.to_json()

# convert the object into a dict
component_details_response_dict = component_details_response_instance.to_dict()
# create an instance of ComponentDetailsResponse from a dict
component_details_response_form_dict = component_details_response.from_dict(component_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

