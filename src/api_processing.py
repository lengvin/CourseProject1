from abc import ABC, abstractmethod
import requests


class APIAdapter(ABC):

    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_api_data(self, country):
        pass


class GetAirplanes(APIAdapter):

    def __init__(self):
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = 'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None
        super().__init__()

    def get_api_data(self, country):
        headers_nominatim = {
            'User-Agent': 'test-app',
        }

        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        response = requests.get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()

        geo_coordinates = data[0].get('boundingbox')

        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = requests.get(url=self.opensky_url, params=params)

        self.aeroplanes = response.json()

        return self.aeroplanes


api = GetAirplanes()

print(api.get_api_data('Canada'))
