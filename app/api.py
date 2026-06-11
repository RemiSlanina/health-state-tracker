from fastapi import  FastAPI
from app.db import get_entries, create_entry, delete_entry, update_entry
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