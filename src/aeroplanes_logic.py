
class Aeroplane:
    __slots__ = ('country', 'callsign', 'velocity', 'vertical_rate', 'geo_altitude')

    def __init__(self, country, callsign, velocity, vertical_rate,  geo_altitude):
        self.country = country
        self.callsign = callsign
        self.velocity = velocity
        self.vertical_rate = vertical_rate
        self.geo_altitude = geo_altitude
        self.__validity_check()

    @staticmethod
    def cast_to_object_list(data):
        result = []
        for obj in data:
            new_aeroplane = {
                'country': obj[2],
                'callsign': obj[1],
                'velocity': obj[9],
                'vertical_rate': obj[11],
                'geo_altitude': obj[13]
            }

            result.append(new_aeroplane)

        return result

    def __add__(self, other):
        return self.geo_altitude + other.geo_altitude

    def __lt__(self, other):
        return self.geo_altitude < other.geo_altitude

    def __le__(self, other):
        return self.geo_altitude <= other.geo_altitude

    def __gt__(self, other):
        return self.geo_altitude > other.geo_altitude

    def __ge__(self, other):
        return self.geo_altitude >= other.geo_altitude

    def __validity_check(self):
        if isinstance(self.country, str) and isinstance(self.callsign, str) and isinstance(self.velocity, float) and isinstance(self.vertical_rate, float) and isinstance(self.geo_altitude, float):
            pass
        else:
            raise TypeError('Введены некоректные данные при создании объекта')
