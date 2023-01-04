from datetime import datetime, timedelta

import pytest

from event import Event


@pytest.fixture
def event():
    return Event(1, datetime.now() + timedelta(days=2), 15, '', '', '')


def test_duration_less_than_10min_raise_error():
    with pytest.raises(ValueError) as excinfo:
        Event(1, datetime.now() + timedelta(days=2), 9, '', '', '')
        assert 'can not be shorter than 10 minutes.' in str(excinfo.value)


def test_change_duration_less_10min_raise_error(event):
    with pytest.raises(ValueError) as excinfo:
        event.duration = 5
        assert 'can not be shorter than 10 minutes.' in str(excinfo.value)


def test_positive_duration(event):
    assert event.duration == 15


def test_duration_invalid_type_should_raise_error():
    with pytest.raises(TypeError) as excinfo:
        Event(1, datetime.now() + timedelta(days=2), '15', '', '', '')
        assert 'duration should be a positive digit.' in str(excinfo.value)


def test_start_date_with_less_than_1_hour_raise_error():
    with pytest.raises(ValueError) as excinfo:
        Event(1, datetime.now() + timedelta(minutes=30), 15, '', '', '')
        assert 'should not start in less than a hour' in str(excinfo.value)


def test_start_date_change_with_less_than_1_hour_raise_error(event):
    with pytest.raises(ValueError) as excinfo:
        event.start_date = datetime.now() + timedelta(minutes=30)
        assert 'should not start in less than a hour' in str(excinfo.value)


def test_start_date_invalid_type_should_raise_error():
    with pytest.raises(TypeError) as excinfo:
        Event(1, 'niedziela', '15', '', '', '')
        assert 'new date must be date or time:' in str(excinfo.value)


def test_positive_start_date(event):
    assert f'{event.start_date:%A %b %y %H:%M}' == f'{datetime.now() + timedelta(days=2):%A %b %y %H:%M}'
