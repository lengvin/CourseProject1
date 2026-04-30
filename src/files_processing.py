from abc import ABC, abstractmethod
import json
from typing import Union
from src.aeroplanes_logic import Aeroplane


class BaseJSONSaver(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def add_aeroplane(self, aeroplane: "Aeroplane"):
        pass

    @abstractmethod
    def get_json_data(self):
        pass

    @abstractmethod
    def del_aeroplane(self, aeroplane):
        pass


class JSONSaver(BaseJSONSaver):

    def __init__(self, file_path="data/aeroplanes_data.json"):
        self.__file_path = file_path
        super().__init__()

    def __rewrite_file(self, new_json_file: list) -> None:
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(new_json_file, file, indent=4)

    def add_aeroplane(self, aeroplane):
        json_file = self.get_json_data()
        json_file.append(
            {
                "country": aeroplane.country,
                "callsign": aeroplane.callsign,
                "velocity": aeroplane.velocity,
                "vertical_rate": aeroplane.vertical_rate,
                "geo_altitude": aeroplane.geo_altitude,
            }
        )
        self.__rewrite_file(json_file)

    def get_json_data(self) -> list:
        with open(self.__file_path, encoding="utf-8") as file:
            json_file = json.load(file)
            return json_file

    def del_aeroplane(self, aeroplane: "Aeroplane") -> None:
        json_file = self.get_json_data()
        aeroplane_dict = {
            "country": aeroplane.country,
            "callsign": aeroplane.callsign,
            "velocity": aeroplane.velocity,
            "vertical_rate": aeroplane.vertical_rate,
            "geo_altitude": aeroplane.geo_altitude,
        }
        json_file.remove(aeroplane_dict)
        self.__rewrite_file(json_file)

    def get_by_criterion_from_json(self, criteria: str, value: Union[str, float]) -> list:
        json_file = self.get_json_data()
        result = []
        for aeroplane in json_file:
            if aeroplane[criteria] == value:
                result.append(aeroplane)

        return result

    @staticmethod
    def get_top_by_height(data: list, top: int) -> list:
        if len(data) >= top:
            for aeroplane in data:
                if aeroplane["vertical_rate"] is None:
                    aeroplane["vertical_rate"] = -1000000

            sorted_data = sorted(data, key=lambda x: x["vertical_rate"])

            for aeroplane in sorted_data:
                if aeroplane["vertical_rate"] == -1000000:
                    aeroplane["vertical_rate"] = None

            return sorted_data[:top]
        else:
            raise ValueError("Число элементов в списке меньше запрашеваемого")
