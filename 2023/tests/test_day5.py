import pytest

from aoc2023.day5 import RangeMap, get_destination

def test_range_map_get_destination():
    range_map = RangeMap(source_range_start=50, destination_source_start=52, range_length=48)
    assert range_map.get_destination(79) == 81

# @pytest.mark.skip
def test_get_destination():
    range_maps = [
        RangeMap(source_range_start=98, destination_source_start=50, range_length=2),
        RangeMap(source_range_start=50, destination_source_start=52, range_length=48),
    ]
    seed = 79

    result = get_destination(seed, range_maps)
    assert result == 81

