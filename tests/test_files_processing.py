from src.files_processing import JSONSaver
from src.aeroplanes_logic import Aeroplane
import pytest
import json


@pytest.fixture
def aeroplane():
    test_aeroplane = Aeroplane("test", "test", 1.0, 1.0, 1.0)
    return test_aeroplane


@pytest.fixture
def saver():
    test_saver = JSONSaver(file_path="tests/test_file.json")
    return test_saver


@pytest.fixture
def aeroplane_dict():
    teat_dict = {
        "country": "test",
        "callsign": "test",
        "velocity": 1.0,
        "vertical_rate": 1.0,
        "geo_altitude": 1.0,
    }
    return teat_dict


@pytest.fixture
def data():
    data_list = [
        {
            "country": "test4",
            "callsign": "test4",
            "velocity": 1.0,
            "vertical_rate": 4.0,
            "geo_altitude": 1.0,
        },
        {
            "country": "test2",
            "callsign": "test2",
            "velocity": 1.0,
            "vertical_rate": 2.0,
            "geo_altitude": 1.0,
        },
        {
            "country": "test1",
            "callsign": "test1",
            "velocity": 1.0,
            "vertical_rate": 1.0,
            "geo_altitude": 1.0,
        },
        {
            "country": "test3",
            "callsign": "test3",
            "velocity": 1.0,
            "vertical_rate": 3.0,
            "geo_altitude": 1.0,
        },
    ]
    return data_list


def test_add_aeroplane(aeroplane, saver, aeroplane_dict):
    saver.add_aeroplane(aeroplane)
    with open("tests/test_file.json", encoding="utf-8") as file:
        test_file = json.load(file)
        assert test_file == [aeroplane_dict]


def test_get_json_data(saver):
    result = saver.get_json_data()
    with open("tests/test_file.json", encoding="utf-8") as file:
        test_file = json.load(file)
        assert test_file == result


def test_del_aeroplanes(saver, aeroplane):
    saver.del_aeroplane(aeroplane)
    with open("tests/test_file.json", encoding="utf-8") as file:
        test_file = json.load(file)
        assert test_file == []


def test_get_top_by_height(data, saver):
    result = saver.get_top_by_height(data, 2)
    assert result == [
        {
            "country": "test1",
            "callsign": "test1",
            "velocity": 1.0,
            "vertical_rate": 1.0,
            "geo_altitude": 1.0,
        },
        {
            "country": "test2",
            "callsign": "test2",
            "velocity": 1.0,
            "vertical_rate": 2.0,
            "geo_altitude": 1.0,
        },
    ]
