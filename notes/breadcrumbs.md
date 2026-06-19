# Breadcrumbs

## FastAPI

FastAPI CRUD complete. 

Done: 
- Tests for convert tuples (db) 

Next candidates:
- 404 handling for missing entries
- split row conversion helpers
- one FastAPI test
- React prototype

Done:
- GET /entries
- POST /entries
- GET /entries/{id}
- DELETE /entries/{id}
- PUT /entries/{id}
Refactor:
- Split convert_rows_to_health_entries()


Next candidates:
- FastAPI endpoint tests
- 404 handling for missing entries 
- Return proper HTTP status codes
- Integration tests against PostgreSQL
- React frontend prototype
- Investigate FastAPI response models

Next steps:

- Tests for context managers (with get_connection() as...)

## Next Tests (pending...)

- create_entry() inserts row successfully
- update_entry() changes stored values
- delete_entry() removes row
- search_notes() returns matching entries
- search_food_tolerance() returns matching entries
- get_entries_by_energy() filters correctly
- get_entries_by_pain() filters correctly

## Integration Tests (pending...)

Requires PostgreSQL test database.

Investigate:

- temporary database
- test fixtures
- setup/teardown

## Psycopg / Context Managers

- Connection context managers automatically commit on success.
- Connection context managers automatically roll back on exceptions.
- Cursor context managers automatically close cursors.
- Resource management code can often be replaced with `with`.

## Debugging

- Verify assumptions from the terminal before blaming the IDE.
- A missing `.env` can look like a database bug.
- A project can be broken in several layers simultaneously.
