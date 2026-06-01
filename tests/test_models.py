from app.models import HealthEntry
import pytest

def test_health_entry_creation():
    entry = HealthEntry(
        energy_level=4,
        pain_level=4,
        sensory_load=7,
        food_tolerance="bread",
        note="noise"
    )
    assert entry.energy_level == 4
    assert entry.pain_level == 4
    assert entry.note == "noise"