from pydantic import BaseModel

class HealthEntryRequest(BaseModel):
    energy_level: int
    pain_level: int
    sensory_load: int
    food_tolerance: str
    note: str

