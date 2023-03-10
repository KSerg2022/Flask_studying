"""Test for modul country_codes.py"""
import pytest

from utils.weather.country_codes import *
from utils.weather.country_codes import URL_CODES_JSON


def test_get_codes():
    data = get_codes(URL_CODES_JSON)
    assert isinstance(data, list) is True


def test_get_codes_error():
    url = URL_CODES_JSON + '1'
    assert get_codes(url) is None


def test_read_codes_data_from_json():
    path_to_file = get_path_to_file_countries_codes()
    data = read_codes_data_from_json(path_to_file)
    assert isinstance(data, list) is True
    assert isinstance(data.pop(), dict) is True
    assert len(data.pop()) == 2
    assert 'code' in data.pop()
    assert 'name' in data.pop()


def test_write_codes_data_to_json():
    json_data = [
        {"code": "AL", "name": "Albania"},
        {"code": "DZ", "name": "Algeria"}
    ]
    assert write_codes_data_to_json(json_data) is True


def test_main():
    assert main(URL_CODES_JSON) is True


def test_main_error():
    url = URL_CODES_JSON + '1'
    with pytest.raises(RuntimeError, match='data not found'):
        main(url)
