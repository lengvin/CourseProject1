from abc import ABC, abstractmethod
import requests


class APIAdapter(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def _get_api_data(self, country: str) -> None:
        pass


class GetAeroplanes(APIAdapter):

    def __init__(self) -> None:
        self.__openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.__opensky_url = "https://opensky-network.org/api/states/all?"
        self.aeroplanes = None
        super().__init__()

    def _get_api_data(self, country: str) -> None:
        headers_nominatim = {
            "User-Agent": "test-app",
        }

        params_nominatim = {
            "country": country,
            "format": "json",
            "limit": 1,
        }

        response = requests.get(url=self.__openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()

        if response.ok:
            geo_coordinates = data[0].get("boundingbox")

            params = {
                "lamin": geo_coordinates[0],
                "lamax": geo_coordinates[1],
                "lomin": geo_coordinates[2],
                "lomax": geo_coordinates[3],
            }

            response = requests.get(url=self.__opensky_url, params=params)

            if response.ok:
                self.aeroplanes = response.json()
            else:
                self.aeroplanes = False
        else:
            self.aeroplanes = False

    def get_aeroplanes(self, country: str) -> dict:
        self._get_api_data(country)
        return self.aeroplanes
