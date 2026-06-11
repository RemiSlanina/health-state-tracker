# What I learned

##  Thursday, 11 June 2026 

Install FastAPI qith uv:
```bash 
uv add fastapi
uv add uvicorn
```

Run FastAPI with 
```bash 
uv run uvicorn app.api:app --reload
```
Inspect with: 
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
or using Swagger UI
http://127.0.0.1:8000/docs 



## Tuesday, 9 June 2026

### Python Packaging

- Running a file directly and running a module are not equivalent.
- `python app/main.py` and `python -m app.main` resolve imports differently.
- Mixing `from db import ...` and `from app.db import ...` causes problems.

### uv

- `uv sync` recreates dependencies from pyproject.toml and uv.lock.
- A repository clone does not restore the virtual environment.

### Environment Variables

- `.env` is local configuration and is not stored in Git.
- Re-cloning a repository requires recreating `.env`.
- Missing database settings can produce misleading PostgreSQL errors.

### PostgreSQL

- `database "dbname" does not exist` can indicate missing configuration rather than a broken database server.

### Psycopg

- `with get_connection() as conn:` automatically commits on success and rolls back on exceptions.
- Context managers remove the need for manual close() calls.

# LIKE VS ILIKE

    # LIKE is case sensitive and slightly faster
    # ILIKE is not case sensitive
    # % = match any sequence of chars
    f.e ("%" + keyword + "%", ) or (f"%{keyword}%",)

Initially...

## PostgreSQL

- SERIAL does not reuse deleted IDs
- DELETE affects 0 rows if ID doesn't exist

### Python

- ValueError stops execution immediately
- dataclasses generate constructors automatically

### Git

- .env should be ignored
- force-push rewrites history
