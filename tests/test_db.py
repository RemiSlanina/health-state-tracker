from _pytest import fixtures

from app.db import convert_tuple_into_health_entry, convert_tuples_into_health_entries
from app.models import HealthEntry
from unittest.mock import MagicMock, patch
import pytest
from app.db import get_entry, delete_entry, get_entries, create_entry, update_entry
from contextlib import ExitStack

@pytest.fixture
def fake_db():
    fake_connection = MagicMock()
    fake_cursor = MagicMock()

    # `with` calls __enter__(), so we mock the object returned by it.
    # Without `with`: fake_connection.cursor.return_value = fake_cursor
    fake_connection.cursor.return_value.__enter__.return_value = fake_cursor
    fake_connection.__enter__.return_value = fake_connection

    with patch("app.db.get_connection", return_value=fake_connection):
        yield fake_cursor

    # no return with ExitStack, yield instead
    #return fake_connection, fake_cursor

@pytest.fixture
def valid_health_entry():
    return HealthEntry(
        energy_level=0,
            pain_level=10,
            sensory_load=7,
            food_tolerance="toast",
            note="noise",
            id=1,
    )

@pytest.fixture
def invalid_health_entry():
    return HealthEntry(
        energy_level=99,
            pain_level=10,
            sensory_load=7,
            food_tolerance="toast",
            note="noise",
            id=1,
    )

def test_get_entries(fake_db):
    # no unpacking with ExitStack
    #fake_connection, fake_cursor = fake_db


    fake_db.fetchall.return_value = [
        (
            123,
            "2026-06-12",
            4,
            5,
            6,
            "apples",
            "forgot taking my meds"
        ),
        (
            456,
            "2026-06-17",
            7,
            8,
            9,
            "potatoes",
            "took too many meds"
        )
    ]

    # with patch("app.db.get_connection", return_value=fake_connection):
    result = get_entries()

    print(result)
    print(len(result))
    print(fake_db.fetchall.call_count)
    print(fake_db.fetchall.call_args)

    assert result[0].id == 123
    assert result[0].timestamp == "2026-06-12"
    assert result[0].energy_level == 4
    assert result[0].pain_level == 5
    assert result[0].sensory_load == 6
    assert result[0].food_tolerance == "apples"
    assert result[0].note == "forgot taking my meds"

    assert result[1].id == 456
    assert result[1].timestamp == "2026-06-17"
    assert result[1].energy_level == 7
    assert result[1].pain_level == 8
    assert result[1].sensory_load == 9
    assert result[1].food_tolerance == "potatoes"
    assert result[1].note == "took too many meds"

    fake_db.execute.assert_called_once()
    fake_db.fetchall.assert_called_once()

    query,  = fake_db.execute.call_args.args
    # Or index it:
    #
    # query = fake_cursor.execute.call_args.args[0]

    assert "SELECT * FROM health_entries" in query
    assert "ORDER BY timestamp DESC" in query
    # params are empty


def test_get_entry(fake_db):
    #fake_connection, fake_cursor = fake_db

    fake_db.fetchone.return_value = (
        123,
        "2026-06-12",
        4,
        5,
        6,
        "apples",
        "forgot taking my meds"
    )

    #with patch("app.db.get_connection", return_value=fake_connection):
    result = get_entry(123)

    assert result.id == 123
    assert result.timestamp == "2026-06-12"
    assert result.energy_level == 4
    assert result.pain_level == 5
    assert result.sensory_load == 6
    assert result.food_tolerance ==  "apples"
    assert result.note == "forgot taking my meds"

    fake_db.execute.assert_called_once()
    fake_db.fetchone.assert_called_once()

    query, params = fake_db.execute.call_args.args
    assert "SELECT * FROM health_entries" in query
    assert "WHERE id = %s" in query
    assert params == (123,)


def test_delete_entry(fake_db):
    #fake_connection, fake_cursor = fake_db

    #with patch("app.db.get_connection", return_value=fake_connection):
    delete_entry(123)

    fake_db.execute.assert_called_once()
    query, params = fake_db.execute.call_args.args
    assert "DELETE FROM health_entries" in query
    assert "WHERE id = %s" in query
    assert params == (123,)

def test_create_entry(fake_db, valid_health_entry):
    #fake_connection, fake_cursor = fake_db

    # entry = valid_health_entry()

    #with patch("app.db.get_connection", return_value=fake_connection):
    create_entry(valid_health_entry)

    fake_db.execute.assert_called_once()
    query, params = fake_db.execute.call_args.args
    assert "INSERT INTO health_entries" in query
    assert "VALUES (%s, %s, %s, %s, %s)" in query

    assert params == (
        0,
        10,
        7,
        "toast",
        "noise",
    )


def test_update_entry(fake_db, valid_health_entry):
    update_entry(valid_health_entry)

    fake_db.execute.assert_called_once()
    query, params = fake_db.execute.call_args.args
    assert "UPDATE health_entries" in query
    assert "SET" in query
    assert "WHERE id = %s" in query
    # order matters with SQL placeholders
    assert params == (
        0,
        10,
        7,
        "toast",
        "noise",
        1,
    )


def test_attempt_create_entry_fail(fake_db, invalid_health_entry):
    #fake_connection, fake_cursor = fake_db

    # entry = HealthEntry(
    #     energy_level=99,
    #         pain_level=10,
    #         sensory_load=7,
    #         food_tolerance="toast",
    #         note="noise",
    #         id=1
    # )

    with pytest.raises(ValueError):
        create_entry(invalid_health_entry)

    fake_db.execute.assert_not_called()

def test_attempt_update_entry_fail(fake_db, invalid_health_entry):
    #fake_connection, fake_cursor = fake_db

    # entry = HealthEntry(
    #     energy_level=99,
    #         pain_level=10,
    #         sensory_load=7,
    #         food_tolerance="toast",
    #         note="noise",
    #         id=1
    # )

    with pytest.raises(ValueError):
        update_entry(invalid_health_entry)

    fake_db.execute.assert_not_called()



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



