from app.db import is_valid_scale_value
import pytest

def test_valid_scale_value():
    is_valid_scale_value(5, "energy_level")

def test_invalid_scale_value():
    with pytest.raises(ValueError):
        is_valid_scale_value(55, "energy_level")

def test_negative_scale_value():
    with pytest.raises(ValueError):
        is_valid_scale_value(-5, "energy_level")