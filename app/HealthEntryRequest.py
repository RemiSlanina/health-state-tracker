from pydantic import BaseModel, Field

class HealthEntryRequest(BaseModel):
    energy_level: int = Field(ge=0, le=10) # ge greater than or equal
    pain_level: int = Field(ge=0, le=10)   # le less than or equal
    sensory_load: int = Field(ge=0, le=10)
    food_tolerance: str
    note: str

