from src.aeroplanes_logic import Aeroplane
import pytest


@pytest.fixture
def aeroplane():
    test_aeroplane = Aeroplane("test", "test", 1.0, 1.0, 1.0)
    return test_aeroplane


def test_aeroplane_init(aeroplane):
    assert aeroplane.country == "test"
    assert aeroplane.callsign == "test"
    assert aeroplane.velocity == 1.0
    assert aeroplane.vertical_rate == 1.0
    assert aeroplane.geo_altitude == 1.0


def test_cast_to_object_list(aeroplane):
    test_list = [["test", "test", "test", 1, 1, 1.0, 1.0, 1.0, False, 1.0, 1.0, 1.0, "null", 1.0, "test", False, 0]]
    result = Aeroplane.cast_to_object_list(test_list)[0]
    assert result.country == aeroplane.country
    assert result.callsign == aeroplane.callsign
    assert result.velocity == aeroplane.velocity
    assert result.vertical_rate == aeroplane.vertical_rate
    assert result.geo_altitude == aeroplane.geo_altitude


def test_invalid_data():
    with pytest.raises(TypeError):
        test_invalid_aeroplane = Aeroplane(1, 1, 1, 1, 1)
