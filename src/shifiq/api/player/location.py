from ...client import ApiClient

class LocationConfiguration:
    id: str
    name: str
    unique_name: str
    description: str

class LocationGroupConfiguration:
    id: str
    name: str
    unique_name: str
    description: str
    locations: list[LocationConfiguration]

class Location:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    def get_all_locations(self) -> list[LocationConfiguration]:
        __response = self.api_client.request("GET", "locations")
        return [LocationConfiguration(**location) for location in __response]
    
    def get_location(self, location_id: str) -> LocationConfiguration:
        __response = self.api_client.request("GET", f"locations/{location_id}")
        return LocationConfiguration(**__response)

    def get_location_by_unique_name(self, unique_name: str) -> LocationConfiguration:
        __response = self.api_client.request("GET", f"locations?unique_name={unique_name}")
        return LocationConfiguration(**__response)
    

class LocationGroup:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    def get_all_location_groups(self) -> list[LocationGroupConfiguration]:
        __response = self.api_client.request("GET", "location-groups")
        return [LocationGroupConfiguration(**location_group) for location_group in __response]
    
    def get_location_group(self, location_group_id: str) -> LocationGroupConfiguration:
        __response = self.api_client.request("GET", f"location-groups/{location_group_id}")
        return LocationGroupConfiguration(**__response)

    def get_location_group_by_unique_name(self, unique_name: str) -> LocationGroupConfiguration:
        __response = self.api_client.request("GET", f"location-groups?unique_name={unique_name}")
        return LocationGroupConfiguration(**__response)