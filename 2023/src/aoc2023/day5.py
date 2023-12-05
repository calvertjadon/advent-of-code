import re
import sys

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from pprint import pprint


class Category(str, Enum):
    SEEDS = "seeds"
    SOIL = "soil"
    FERTILIZER = "fertilizer"
    WATER = "water"
    LIGHT = "light"
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    LOCATION = "location"


class MapName(str, Enum):
    SEED_TO_SOIL = "seed-to-soil"
    SOIL_TO_FERTILIZER = "soil-to-fertilizer"
    FERTILIZER_TO_WATER = "fertilizer-to-water"
    WATER_TO_LIGHT = "water-to-light"
    LIGHT_TO_TEMPERATURE = "light-to-temperature"
    TEMPERATURE_TO_HUMIDITY = "temperature-to-humidity"
    HUMIDITY_TO_LOCATION = "humidity-to-location"

    @property
    def source(self) -> Category:
        if self == MapName.SEED_TO_SOIL:
            return Category.SEEDS
        return Category(self.value.split("-to-")[0])

    @property
    def destination(self) -> Category:
        return Category(self.value.split("-to-")[1])


map_names = iter(MapName)


@dataclass
class MapEntry:
    def __init__(
        self, destination_range_start: int, source_range_start: int, range_length: int
    ) -> None:
        self._source_range = range(
            source_range_start, source_range_start + range_length
        )
        self._destination_range = range(
            destination_range_start, destination_range_start + range_length
        )

    @property
    def source_range(self) -> range:
        return self._source_range

    @property
    def destination_range(self) -> range:
        return self._destination_range

    def get_destination(self, source: int) -> int:
        return source - self.source_range.start + self.destination_range.start


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        almanac = f.read().strip()

    map_entries: dict[MapName, list[MapEntry]] = defaultdict(list)
    map_results: dict[Category, list[range]] = defaultdict(list)

    for match in re.finditer(r"(.+):\s([\d\s]+)", almanac, re.MULTILINE):
        header = match.group(1).strip().split()[0]
        if header == Category.SEEDS:
            seed_data = iter(list(map(int, match.group(2).strip().split())))
            for seed_range_start in seed_data:
                range_length = next(seed_data)
                map_results[Category.SEEDS].append(
                    range(seed_range_start, seed_range_start + range_length)
                )

        else:
            map_name = MapName(header)
            map_entries[map_name] = [
                MapEntry(*map(int, line.split()))
                for line in match.group(2).strip().splitlines()
            ]

    for map_name in map_names:
        while len(map_results[map_name.source]) > 0:
            seed_range = map_results[map_name.source].pop()

            for map_entry in map_entries[map_name]:
                overlap_start = max(seed_range.start, map_entry.source_range.start)
                overlap_end = min(seed_range.stop, map_entry.source_range.stop)

                if overlap_start < overlap_end:
                    map_results[map_name.destination].append(
                        range(
                            map_entry.get_destination(overlap_start),
                            map_entry.get_destination(overlap_end)
                        )
                    )

                    if overlap_start > seed_range.start:
                        map_results[map_name.source].append(
                            range(seed_range.start, overlap_start)
                        )

                    if seed_range.stop > overlap_end:
                        map_results[map_name.source].append(
                            range(overlap_end, seed_range.stop)
                        )

                    break
            else:
                map_results[map_name.destination].append(
                    range(seed_range.start, seed_range.stop)
                )

    pprint(min(r.start for r in map_results[Category.LOCATION]))

