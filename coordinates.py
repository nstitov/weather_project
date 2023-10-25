from dataclasses import dataclass

from geopy.geocoders import Nominatim

import config
from exceptions import CantGetCoordinates


@dataclass(frozen=True, slots=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates(address: str) -> Coordinates:
    coordinates = _get_gps_coords(address)
    return _round_coordinates(coordinates)


def _get_gps_coords(address: str) -> Coordinates:
    try:
        geolocator = Nominatim(user_agent='my_app')
        location = geolocator.geocode(address)
        latitude = location.latitude
        longitude = location.longitude
        return Coordinates(longitude=longitude, latitude=latitude)
    except AttributeError:
        raise CantGetCoordinates


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(lambda c: round(c, 1),
                            [coordinates.latitude, coordinates.longitude]))


if __name__ == '__main__':
    print(get_gps_coordinates('Самара'))