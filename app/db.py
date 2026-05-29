from dotenv import load_dotenv
import os
import psycopg

load_dotenv()

def get_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

# validation helper function
def is_valid_scale_value(value, field_name):
    if value < 0 or value > 10:
        raise ValueError(f"{field_name} must be between 0 and 10")

# create, get, update entries

def create_entry(
        energy_level,
        pain_level,
        sensory_load,
        food_tolerance,
        note
):
    is_valid_scale_value(energy_level, "energy_level")
    is_valid_scale_value(pain_level, "pain_level")
    is_valid_scale_value(sensory_load, "sensory_load")
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO health_entries (
        energy_level, 
        pain_level, 
        sensory_load, 
        food_tolerance, 
        note
        ) VALUES (%s, %s, %s, %s, %s)
        """, (
        energy_level,
        pain_level,
        sensory_load,
        food_tolerance,
        note
        )
    )

    conn.commit()
    cur.close()
    conn.close()

def get_entries():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM health_entries
        ORDER BY timestamp DESC
        """
    )

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_entry(
        entry_id,
        energy_level
):
    is_valid_scale_value(energy_level, "energy_level")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE health_entries 
        SET energy_level = %s
        WHERE id = %s
        """,
        (energy_level, entry_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_entry(entry_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        DELETE FROM health_entries 
        WHERE id = %s 
        """,
        (entry_id,)
    )
    print(cur.rowcount)
    conn.commit()
    cur.close()
    conn.close()

# search entries

def search_notes(keyword):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * FROM health_entries
        WHERE note ILIKE %s 
        ORDER BY timestamp DESC
        """,
        (f"%{keyword}%",)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def search_food_tolerance(keyword):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM health_entries
        WHERE food_tolerance ILIKE %s 
        ORDER BY timestamp DESC
        """,
        (f"%{keyword}%",)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_entries_by_energy(level):
    is_valid_scale_value(level, "energy_level")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM health_entries 
        WHERE energy_level = %s
        ORDER BY energy_level DESC
        """,
        (level,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_entries_by_pain(level):
    is_valid_scale_value(level, "pain_level")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM health_entries 
        WHERE pain_level = %s
        ORDER BY pain_level DESC
        """,
        (level,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

