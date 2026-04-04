from abc import ABC, abstractmethod
import json


class BaseJSONSaver(ABC):

    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def add_aeroplane(self, aeroplane):
        pass

    @abstractmethod
    def get_json_data(self):
        pass

    @abstractmethod
    def del_aeroplane(self, aeroplane):
        pass


class JSONSaver(BaseJSONSaver):

    def __init__(self, file_path='../data/aeroplanes_data.json'):
        self.__file_path = file_path
        super().__init__()

    def __rewrite_file(self, new_json_file):
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_json_file, file, indent=4)

    def add_aeroplane(self, aeroplane):
        json_file = self.get_json_data()
        json_file.append({
            'country': aeroplane.country,
            'callsign': aeroplane.callsign,
            'velocity': aeroplane.velocity,
            'vertical_rate': aeroplane.vertical_rate,
            'geo_altitude': aeroplane.geo_altitude
        })
        self.__rewrite_file(json_file)

    def get_json_data(self):
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                json_file = json.load(file)
        except (FileNotFoundError, TypeError, json.JSONDecodeError, ValueError) as e:
            print(e)
            return []
        else:
            return json_file

    def del_aeroplane(self, aeroplane):
        json_file = self.get_json_data()
        aeroplane_dict = {
            'country': aeroplane.country,
            'callsign': aeroplane.callsign,
            'velocity': aeroplane.velocity,
            'vertical_rate': aeroplane.vertical_rate,
            'geo_altitude': aeroplane.geo_altitude
        }
        json_file.remove(aeroplane_dict)
        self.__rewrite_file(json_file)

    def get_by_criteria_from_json(self, criteria, value):
        json_file = self.get_json_data()
        result = []
        for aeroplane in json_file:
            if aeroplane[criteria] == value:
                result.append(aeroplane)

        return result
