from dotenv import load_dotenv
import os
import psycopg

from app.models import HealthEntry

load_dotenv()

# ******************** CONNS ********************

def get_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

# ****************** HELPERS ******************
# helper for converting a single row
def convert_tuple_into_health_entry(row):
    return HealthEntry(
        id=row[0],
        timestamp=row[1],

        energy_level=row[2],
        pain_level=row[3],
        sensory_load=row[4],
        food_tolerance=row[5],
        note=row[6]
    )
# helper for converting rows
def convert_tuples_into_health_entries(rows):
    return [
        convert_tuple_into_health_entry(row) for row in rows
    ]
    # results = []
    # for row in rows:
    #     results.append(
    #         convert_tuple_into_health_entry(row)
    #     )
    # return results


# validation helper function
def is_valid_scale_value(value, field_name):
    if value < 0 or value > 10:
        raise ValueError(f"{field_name} must be between 0 and 10")

# ****************** ENTRY ******************

# create, get, update entries

def create_entry(entry:HealthEntry):
    is_valid_scale_value(entry.energy_level, "energy_level")
    is_valid_scale_value(entry.pain_level, "pain_level")
    is_valid_scale_value(entry.sensory_load, "sensory_load")
    with get_connection() as conn: 
        with conn.cursor() as cursor: 
            cursor.execute(
                """
                INSERT INTO health_entries (
                energy_level, 
                pain_level, 
                sensory_load, 
                food_tolerance, 
                note
                ) VALUES (%s, %s, %s, %s, %s)
                RETURNING * 
                """, (
                    entry.energy_level, 
                    entry.pain_level, 
                    entry.sensory_load, 
                    entry.food_tolerance, 
                    entry.note
                )
            )
            row = cursor.fetchone()
            return convert_tuple_into_health_entry(row)
            

def get_entries():
    with get_connection() as conn: 
        with conn.cursor() as cur: 
            cur.execute(
                """
                SELECT * FROM health_entries
                ORDER BY timestamp DESC 
                """
            )
            rows = cur.fetchall()
    return convert_tuples_into_health_entries(rows)

def get_entry(entry_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """SELECT * FROM health_entries 
                WHERE id = %s
                """,
                (entry_id, )
            )
            r = cur.fetchone()
    return convert_tuple_into_health_entry(r)

def update_entry(entry: HealthEntry):
    is_valid_scale_value(entry.energy_level, "energy_level")
    is_valid_scale_value(entry.pain_level, "pain_level")
    is_valid_scale_value(entry.sensory_load, "sensory_load")
    with get_connection() as conn: 
        with conn.cursor() as cur: 
            cur.execute(
                """
                UPDATE health_entries 
                SET energy_level = %s, 
                pain_level = %s, 
                sensory_load = %s, 
                food_tolerance = %s, 
                note = %s 
                WHERE id = %s
                RETURNING * 
                """, 
                (entry.energy_level, entry.pain_level, entry.sensory_load, 
                    entry.food_tolerance, entry.note, entry.id
                )
            )
            row = cur.fetchone()
            return convert_tuple_into_health_entry(row)

def delete_entry(entry_id):
    with get_connection() as conn: 
        with conn.cursor() as cur: 
            cur.execute(
                """
                DELETE FROM health_entries
                WHERE id = %s
                RETURNING * 
                """, 
                (entry_id, )
            )
            print(f"Deleted {cur.rowcount} rows")
            row = cur.fetchone()
            return convert_tuple_into_health_entry(row)


# ****************** SEARCH ******************
# search entries
def search_notes(keyword):
    keyword = keyword or "" # if None or empty 
    with get_connection() as conn: 
        with conn.cursor() as cur: 
            cur.execute(
                """SELECT * FROM health_entries
                WHERE note ILIKE %s
                ORDER BY timestamp DESC
                """, 
                #("%" + keyword + "%", ) # % = match any sequence of chars 
                (f"%{keyword}%",)
            ) 
            rows = cur.fetchall() 
    return convert_tuples_into_health_entries(rows) 
    # LIKE is case sensitive and slightly faster 
    # ILIKE is not case sensitive 

def search_food_tolerance(keyword):
    with get_connection() as conn: 
        with conn.cursor() as cur: 
            cur.execute(
                """SELECT * FROM health_entries 
                WHERE food_tolerance ILIKE %s
                ORDER BY timestamp DESC""", 
                (f"%{keyword}%",)
            )
            rows = cur.fetchall() 
    return convert_tuples_into_health_entries(rows) 


def get_entries_by_energy(level):
    is_valid_scale_value(level, "energy_level")
    with get_connection() as conn: 
        with conn.cursor() as cur: 
            cur.execute(
                """
                SELECT * FROM health_entries 
                WHERE energy_level = %s
                ORDER BY energy_level DESC
                """,
                (level,)
            )
            rows = cur.fetchall()
    return convert_tuples_into_health_entries(rows)



def get_entries_by_pain(level):
    is_valid_scale_value(level, "pain_level")
    with get_connection() as conn: 
        with conn.cursor() as cur: 
            cur.execute(
                """
                SELECT * FROM health_entries 
                WHERE pain_level = %s
                ORDER BY pain_level DESC
                """,
                (level,)
            )
            rows = cur.fetchall()
    return convert_tuples_into_health_entries(rows)

