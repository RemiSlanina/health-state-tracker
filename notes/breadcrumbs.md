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

## Testing Notes

- Verify returned values.
- Verify interactions with collaborators.
- Verify SQL parameter order when placeholders are positional.
- Use fixtures to remove repeated setup while keeping tests focused on behavior.

## Database Tests

Done:
- convert_tuple_into_health_entry()
- convert_tuples_into_health_entries()
- get_entry()
- get_entries()
- create_entry()
- update_entry()
- delete_entry()
- validation failure prevents database writes

Pending:
- search_notes()
- search_food_tolerance()
- get_entries_by_energy()
- get_entries_by_pain()

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
