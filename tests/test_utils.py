import pytest
from src import utils


def test_get_time_period(time_periods):
    for period in time_periods:
        date, result = period
        assert utils.get_time_period(date) == result


# @pytest.mark.parametrize("invalid_data", ['', '2020-10-10', '10:10:10', '03.12.2020'])
# def test_invalid_get_time_period(invalid_data):
#     with pytest.raises(ValueError):
#         utils.get_time_period(invalid_data)


def test_get_operations_in_period(operations_in_period):
    for inputs in operations_in_period:
        operations, date, result = inputs
        assert utils.get_operations_in_period(operations, date) == result
    assert utils.get_operations_in_period([], '2020-10-20 10:10:10') == []


# @pytest.mark.parametrize('invalid_data', [
#     ([], ''),
#     ([], '2020-10-10'),
#     ([], '10:10:10'),
#     ([], '03.12.2020')
# ])
# def test_invalid_get_operations_in_period(invalid_data):
#     operations, date = invalid_data
#     with pytest.raises(ValueError):
#         utils.get_operations_in_period(operations, date)


def test_get_greetings_by_date(greetings):
    for data in greetings:
        date, result = data
        assert utils.get_greetings_by_date(date) == result


# @pytest.mark.parametrize('invalid_data', ['', '2020-10-10', '10:10:10', '03.12.2020'])
# def test_invalid_get_greetings_by_date(invalid_data):
#     with pytest.raises(ValueError):
#         utils.get_greetings_by_date(invalid_data)


def test_get_cards_info(cards_info):
    operations, result = cards_info
    assert utils.get_cards_info(operations) == result
    assert utils.get_cards_info([]) == []


# def test_invalid_get_cards_info():
#     with pytest.raises(ValueError):
#         utils.get_cards_info('')
