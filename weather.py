from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import ApiServiceError, CantGetCoordinates


def main(address: str):
    try:
        coordinates = get_gps_coordinates(address)
    except CantGetCoordinates:
        print('Не смог получить GPS координаты')
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print('Не смог получить погоду в API-сервиса погода')
        exit(1)
    print(format_weather(weather))


if __name__ == '__main__':
    address = 'Samara'
    main(address)
