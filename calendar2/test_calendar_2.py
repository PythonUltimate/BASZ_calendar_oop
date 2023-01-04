from datetime import datetime, timedelta
from unittest.mock import Mock
import pytest

from calendar2.calendar2 import Calendar
from event import Event


@pytest.fixture
def events():
    event_1 = Event(1, datetime.now() + timedelta(days=2), 15, 'test1', 'desc1', 'owner1')
    event_2 = Event(2, datetime.now() + timedelta(days=35), 15, 'test2', 'desc2', 'owner2')
    event_3 = Event(3, datetime.now() + timedelta(days=2), 25, 'test3', 'desc3', 'owner3')
    return [event_1, event_2, event_3]


@pytest.fixture
def calendar(events):
    return Calendar(events)

def test_add_event_positive(events):
    calendar = Calendar()
    calendar.events = events[0]
    assert len(calendar) == 1


def test_add_invalid_event_should_raise_error():
    calendar = Calendar()
    with pytest.raises(TypeError) as excinfo:
        calendar.events = 'test_event'
        assert 'Wrong data type:' in str(excinfo.value)


def test_delete_event_positive(events, calendar):
    print(calendar)
    calendar.delete(3)
    assert len(calendar) == 1


def test_delete_negative(calendar, events):
    with pytest.raises(ValueError) as excinfo:
        calendar.delete(100)
        assert 'Event has been not found' in str(excinfo.value)


def test_filter_by_duration_with_correct_duration(calendar):
    result = calendar.filter_by_duration(25)
    assert len(result) == 1


def test_filter_by_duration_out_of_range(calendar):
    result = calendar.filter_by_duration(100)
    assert result == []


def test_filter_by_duration_in_positive_range(calendar):
    result = calendar.filter_by_duration(duration_min=12, duration_max=18)
    assert len(result) == 2


def test_filter_by_duration_in_out_of_range(calendar):
    result = calendar.filter_by_duration(duration_min=30, duration_max=40)
    assert len(result) == 0


def test_filter_by_data_positive(calendar):
    result = calendar.filter_by_data(start_date=datetime.now() + timedelta(days=1),
                                     end_date=datetime.now() + timedelta(days=3))
    assert len(result) == 2


def test_filter_by_data_negative(calendar):
    result = calendar.filter_by_data(start_date=datetime.now() + timedelta(days=100),
                                     end_date=datetime.now() + timedelta(days=300))
    assert len(result) == 0


def test_filter_by_title_positive(calendar):
    result = calendar.filter(filter_name='title', search_text='test1')
    assert len(result) == 1


def test_filter_by_title_negative(calendar):
    result = calendar.filter(filter_name='title', search_text='test_negative')
    assert len(result) == 0


def test_filter_by_owner_positive(calendar):
    result = calendar.filter(filter_name='owner', search_name='owner1')
    assert len(result) == 1


def test_filter_by_owner_negative(calendar):
    result = calendar.filter(filter_name='owner', search_name='owner_negative')
    assert len(result) == 0


def test_filter_by_description_positive(calendar):
    result = calendar.filter(filter_name='description', search_text='desc1')
    assert len(result) == 1


def test_filter_by_description_negative(calendar):
    result = calendar.filter(filter_name='description', search_text='desc_negative')
    assert len(result) == 0


def test_len_positive(calendar):
    assert len(calendar) == 3