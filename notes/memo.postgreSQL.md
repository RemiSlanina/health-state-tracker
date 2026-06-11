# PostgreSQL Learning Memo

## What I Set Up

Installed PostgreSQL on Ubuntu:

```bash
sudo apt install postgresql postgresql-contrib
```

Checked service status:

```bash
sudo systemctl status postgresql
```

Connected as postgres admin user:

```bash
sudo -u postgres psql
```

Exited psql:

```sql
\q
```

Created my own user:

```sql
CREATE USER remi WITH PASSWORD 'mypassword';
ALTER USER remi CREATEDB;
```

Created my own database:

```sql
CREATE DATABASE remidb OWNER remi;
```

Connected as my own user:

```bash
psql -U remi -d remidb
```

---

# Useful psql Commands

List databases:

```sql
\l
```

List users/roles:

```sql
\du
```

Describe table structure:

```sql
\d cats
```

Quit psql:

```sql
\q
```

---

# First Table

Created table:

```sql
CREATE TABLE cats (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    favorite_food TEXT
);
```

Concepts:

* TABLE = category/type
* ROW = one instance
* COLUMN = attribute/property

`SERIAL`

* auto-incrementing integer IDs
* usually: 1, 2, 3, 4...

`PRIMARY KEY`

* unique identifier
* cannot duplicate
* usually used for relationships

`NOT NULL`

* field is required

---

# Insert Data

Insert one row:

```sql
INSERT INTO cats (name, age, favorite_food)
VALUES ('Tilo', 7, 'forbidden oleander water');
```

---

# Read Data

Select all:

```sql
SELECT * FROM cats;
```

Select specific columns:

```sql
SELECT name FROM cats;
```

Filter rows:

```sql
SELECT * FROM cats
WHERE age > 7;
```

Sort ascending:

```sql
SELECT * FROM cats
ORDER BY age ASC;
```

Sort descending:

```sql
SELECT * FROM cats
ORDER BY age DESC;
```

---

# Update Data

Inspect first:

```sql
SELECT * FROM cats
WHERE name = 'Tilo';
```

Update safely:

```sql
UPDATE cats
SET age = 8
WHERE name = 'Tilo';
```

Dangerous:

```sql
UPDATE cats
SET age = 999;
```

Without WHERE:
updates ALL rows.

---

# Delete Data

Inspect first:

```sql
SELECT * FROM cats
WHERE name = 'Mira';
```

Delete safely:

```sql
DELETE FROM cats
WHERE name = 'Mira';
```

Dangerous:

```sql
DELETE FROM cats;
```

Without WHERE:
deletes ALL rows.

---

# Transactions

Start temporary state:

```sql
BEGIN;
```

Prompt changes:

```text
remidb=*>
```

Inside transaction:
changes are NOT final yet.

Accept changes permanently:

```sql
COMMIT;
```

Undo changes:

```sql
ROLLBACK;
```

---

# Relationships / Foreign Keys

Created owners table:

```sql
CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
```

Added relationship column:

```sql
ALTER TABLE cats
ADD COLUMN owner_id INTEGER;
```

Added foreign key constraint:

```sql
ALTER TABLE cats
ADD CONSTRAINT fk_owner
FOREIGN KEY (owner_id)
REFERENCES owners(id);
```

Meaning:

* cats.owner_id must reference real owners.id
* database enforces relational integrity

---

# JOIN

INNER JOIN:
only matched rows survive.

```sql
SELECT
    cats.name AS cat_name,
    owners.name AS owner_name
FROM cats
JOIN owners
ON cats.owner_id = owners.id;
```

LEFT JOIN:
keep ALL rows from left table,
even if no match exists.

```sql
SELECT
    cats.name AS cat_name,
    owners.name AS owner_name
FROM cats
LEFT JOIN owners
ON cats.owner_id = owners.id;
```

---

# Important Mental Models

SQL is declarative:

* describe WHAT you want
* database decides HOW to execute

Database != application logic.
Database = structured persistent state.

Foreign keys = relational rules.

Transactions = temporary reality bubble.

Always be cautious with:

* UPDATE
* DELETE

Especially without WHERE clauses.

---

# Important Commands To Learn Next

Aggregation:

```sql
COUNT()
SUM()
AVG()
MIN()
MAX()
GROUP BY
```

Null handling:

```sql
IS NULL
IS NOT NULL
```

Pattern matching:

```sql
LIKE
ILIKE
```

Indexes:

```sql
CREATE INDEX
```

Table deletion:

```sql
DROP TABLE
```

Changing table structure:

```sql
ALTER TABLE
```

Limiting rows:

```sql
LIMIT
```

Multiple conditions:

```sql
AND
OR
NOT
```

---

Mind psycopg string-literal-like parameter placeholders (%s %s): 

```sql
cur.execute(
    "INSERT INTO test VALUES (%s, %s)",
    ("hello", 42) # tuples, for one (42,)
)
```

And importantly:
psycopg handles:

escaping
quoting
type conversion
SQL injection protection

So this is GOOD:
```sql
VALUES (%s, %s)
```
This is BAD:
```sql
f"VALUES ({value1}, {value2})"
```
because manual string interpolation becomes dangerous later. 

---
CROSS JOIN and NULL:

CROSS JOIN matches everything with everything. 

If:
100 cats
100 owners
CROSS JOIN creates:
10,000 rows.

Another important thing:
missing matches become NULL.

NULL is not:
zero
empty string
false

NULL means:
“unknown / absent / undefined”

---

# Next Learning Steps

1. Connect PostgreSQL to DataGrip or VS Code
2. Connect Python to PostgreSQL
3. Learn SQLAlchemy basics
4. Build tiny real project
5. Learn FastAPI afterward

Possible project ideas:

* symptom tracker
* debugging knowledge base
* issue tracker
* tagging/search system
* medical observation system

