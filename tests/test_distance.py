# tests/test_lib.py
from mlproject.distance import haversine

def test_type_distance():
    assert type(haversine(3,1,5,-1)) == float