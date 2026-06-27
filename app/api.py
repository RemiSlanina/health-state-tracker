from fastapi import  FastAPI
from app.db import (get_entries, create_entry, delete_entry, update_entry,
                    get_entry, search_notes, search_food_tolerance, get_entries_by_energy, get_entries_by_pain,)
from app.HealthEntryRequest import HealthEntryRequest
from app.models import HealthEntry

app = FastAPI()
@app.get("/")
def root():
    return {"message": "Health State Tracker API"}

@app.get("/entries")
def get_entries_api():
    #print("Hello from api")
    return get_entries()

@app.get("/entries/{entry_id}")
def get_entry_api(entry_id: int):
    print(entry_id)
    return get_entry(entry_id)

@app.post("/entries")
def create_entry_api(entry: HealthEntryRequest):
    #print(entry)
    create_entry(HealthEntry(
        entry.energy_level,
         entry.pain_level,
         entry.sensory_load,
         entry.food_tolerance,
         entry.note))
    return entry

@app.delete("/entries/{entry_id}")
def delete_entry_api(entry_id: int):
    delete_entry(entry_id)
    return {"message": "Entry Deleted"}

@app.put("/entries/{entry_id}")
def update_entry_api(entry_id: int, entry: HealthEntryRequest):
    update_entry( HealthEntry(
        entry.energy_level,
        entry.pain_level,
        entry.sensory_load,
        entry.food_tolerance,
        entry.note,
        entry_id
    ))
    return {"message": "Entry Updated"}

# SEARCH endpoints

# difference:
# ?keyword=noise is a query parameter. like
# http://127.0.0.1:8000/entries/search/note?keyword=noise
# /energy/7 is a path parameter. For example:
# http://127.0.0.1:8000/entries/search/energy/4

@app.get("/entries/search/note")
def search_notes_api(keyword: str):
    # FastAPI sees keyword: str and automatically knows to read it from the query string.
    return search_notes(keyword)

@app.get("/entries/search/food")
def search_food_api(keyword: str):
    return search_food_tolerance(keyword)

@app.get("/entries/search/energy/{level}")
def search_energy_api(level:int):
    return get_entries_by_energy(level)

@app.get("/entries/search/pain/{level}")
def search_pain_api(level:int):
    return get_entries_by_pain(level)