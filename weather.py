from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather


def main(address: str):
    coordinates = get_gps_coordinates(address)
    weather = get_weather(coordinates)
    print(format_weather(weather))


if __name__ == '__main__':
    address = 'Samara'
    main(address)
