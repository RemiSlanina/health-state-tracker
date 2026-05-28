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

def create_entry(
        energy_level,
        pain_level,
        sensory_load,
        food_tolerance,
        note
):
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

