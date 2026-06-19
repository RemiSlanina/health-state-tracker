from app.db import convert_tuple_into_health_entry, convert_tuples_into_health_entries
from app.models import HealthEntry
from unittest.mock import MagicMock, patch
from app.db import get_entry

def test_get_entry():
    fake_connection = MagicMock()
    fake_cursor = MagicMock()

    # `with` calls __enter__(), so we mock the object returned by it.
    # Without `with`: fake_connection.cursor.return_value = fake_cursor
    fake_connection.cursor.return_value.__enter__.return_value = fake_cursor
    fake_connection.__enter__.return_value = fake_connection

    fake_cursor.fetchone.return_value = (
        123,
        "2026-06-12",
        4,
        5,
        6,
        "apples",
        "forgot taking my meds"
    )

    with patch("app.db.get_connection", return_value=fake_connection):
        result = get_entry(123)

    assert result.id == 123
    assert result.timestamp == "2026-06-12"
    assert result.energy_level == 4
    assert result.pain_level == 5
    assert result.sensory_load == 6
    assert result.food_tolerance ==  "apples"
    assert result.note == "forgot taking my meds"

def test_convert_tuple_into_health_entry():
    row  = (
        123,
        "2026-06-12",
        4,
        5,
        6,
        "toast",
        "noise"
    )

    result = convert_tuple_into_health_entry(row)

    #assert type(result) == HealthEntry more better in python:
    assert isinstance(result, HealthEntry)

    assert result.id == 123
    assert result.timestamp == "2026-06-12"
    assert result.energy_level == 4
    assert result.pain_level == 5
    assert result.sensory_load == 6
    assert result.food_tolerance == "toast"
    assert result.note == "noise"


def test_convert_tuples_into_health_entries():
    rows = [
        (
            1,
            "2026-06-12",
            4,
            5,
            6,
            "toast",
            "noise"),
        (
            2,
            "2026-06-13",
            7,
            8,
            9,
            "rice",
            "light"
        )
    ]

    results = convert_tuples_into_health_entries(rows)

    assert len(results) == len(rows)
    assert results[0].id == 1
    assert results[0].timestamp == "2026-06-12"
    assert results[0].energy_level == 4
    assert results[0].pain_level == 5
    assert results[0].sensory_load == 6
    assert results[0].food_tolerance == "toast"
    assert results[0].note == "noise"

    assert results[1].id == 2
    assert results[1].timestamp == "2026-06-13"
    assert results[1].energy_level == 7
    assert results[1].pain_level == 8
    assert results[1].sensory_load == 9
    assert results[1].food_tolerance == "rice"
    assert results[1].note == "light"
