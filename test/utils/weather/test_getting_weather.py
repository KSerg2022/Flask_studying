import pytest
import requests

from utils.weather.getting_weather import get_weather, main


class TestGettingWeather:

    def setup_method(self):
        self.city = 'Mariupol'
        self.api_id = '402d150cc39854f9d464c714a56dcf36'
        self.url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_id}&units=metric'

    def test_get_weather_200(self):
        response = requests.get(self.url)
        assert response.status_code == 200

    def test_get_weather_error(self):
        city = "Kyev"
        with pytest.raises(RuntimeError, match='openweathermap.org returned non-200 code'):
            get_weather(city, self.api_id)

        api_id = self.api_id + '1'
        with pytest.raises(RuntimeError, match='openweathermap.org returned non-200 code'):
            get_weather(self.city, api_id)

    def test_main(self):
        result = main(self.city)
        assert isinstance(result, dict) is True

    def test_main_error(self):
        city = "Kyev"
        result = main(city)
        assert 'City not found' in result['error']


if __name__ == '__main__':
    pytest.main()
