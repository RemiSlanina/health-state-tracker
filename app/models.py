from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class HealthEntry:
    energy_level: int
    pain_level: int
    sensory_load: int
    food_tolerance: str
    note: str

    id: Optional[int] = None
    timestamp: Optional[datetime] = None

