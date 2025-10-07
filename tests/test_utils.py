import pytest
from src import utils


def test_get_time_period(time_periods):
    for period in time_periods:
        date, result = period
        assert utils.get_time_period(date) == result


def test_get_operations_in_period(operations_in_period):
    for inputs in operations_in_period:
        operations, date, result = inputs
        assert utils.get_operations_in_period(operations, date, 'M') == result
    assert utils.get_operations_in_period([], '2020-10-20 10:10:10', 'M') == []


def test_get_greetings_by_date(greetings):
    for data in greetings:
        date, result = data
        assert utils.get_greetings_by_date(date) == result


def test_get_cards_info(cards_info):
    operations, result = cards_info
    assert utils.get_cards_info(operations) == result
    assert utils.get_cards_info([]) == []
