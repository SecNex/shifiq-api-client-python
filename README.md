# Shifiq API Client for Python

This is a Python client for the ShifIQ API. It allows you to interact with the ShifIQ API to manage your players and their configurations and more.

## Installation

```bash
pip install shifiq-api-client
```

## Usage

```python
from shifiq.api.player import Player, PlayerConfiguration
from shifiq.api.location import Location, LocationGroup, LocationConfiguration, LocationGroupConfiguration
from shifiq.client import ApiClient

client = ApiClient(api_key="your_api_key")

player = Player(client)
location = Location(client)
location_group = LocationGroup(client)

# Player
player.get_all_players()
player.get_player(player_id="123")
player.get_player_by_unique_name(unique_name="unique_name")

# Location
location.get_all_locations()
location.get_location(location_id="123")
location.get_location_by_unique_name(unique_name="unique_name")

# Location Group
location_group.get_all_location_groups()
location_group.get_location_group(location_group_id="123")
location_group.get_location_group_by_unique_name(unique_name="unique_name")
```
