import re
import sys

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from multiprocessing.pool import ThreadPool


class DestinationMap(str, Enum):
    SEEDS = "seeds"
    SEED_TO_SOIL = "seed-to-soil"
    SOIL_TO_FERTILIZER = "soil-to-fertilizer"
    FERTILIZER_TO_WATER = "fertilizer-to-water"
    WATER_TO_LIGHT = "water-to-light"
    LIGHT_TO_TEMPERATURE = "light-to-temperature"
    TEMPERATURE_TO_HUMIDITY = "temperature-to-humidity"
    HUMIDITY_TO_LOCATION = "humidity-to-location"


@dataclass
class RangeMap:
    source_range_start: int
    destination_source_start: int
    range_length: int

    def in_source_range(self, value: int) -> bool:
        return self.source_range_start <= value < self.source_range_start + self.range_length

    def get_destination(self, source: int) -> int | None:
        if self.in_source_range(source):
            return self.destination_source_start + source - self.source_range_start
        return None


def read_input(almanac: str) -> tuple[list[range], dict[DestinationMap, list[RangeMap]]]:
    seed_ranges = []
    range_maps: dict[DestinationMap, list[RangeMap]] = defaultdict(list)

    for match in re.finditer(r"(.+):\s([\d\s]+)", almanac, re.MULTILINE):
        header = match.group(1).strip().split()[0]
        data = [
            [int(n) for n in line.split()]
            for line in match.group(2).strip().splitlines()
        ]

        if header == DestinationMap.SEEDS:
            seed_iter = iter(data[0])
            for start in seed_iter:
                range_len = next(seed_iter)
                seed_ranges.append(range(start, start+range_len))
            continue

        for dst_rng_st, src_rng_st, rng_len in data:
            range_maps[DestinationMap(header)].append(
                RangeMap(
                    source_range_start=src_rng_st,
                    destination_source_start=dst_rng_st,
                    range_length=rng_len,
                )
            )

    return seed_ranges, range_maps


def get_destination(source: int, ranges: list[RangeMap]) -> int:
    for range_map in ranges:
        if range_map.in_source_range(source):
            dest = range_map.get_destination(source)
            if not dest:
                raise Exception("something broke")
            return dest
    return source


def get_seed_location(
    seed: int, range_maps: dict[DestinationMap, list[RangeMap]]
) -> int:
    soil = get_destination(seed, range_maps[DestinationMap.SEED_TO_SOIL])
    fertilizer = get_destination(soil, range_maps[DestinationMap.SOIL_TO_FERTILIZER])
    water = get_destination(fertilizer, range_maps[DestinationMap.FERTILIZER_TO_WATER])
    light = get_destination(water, range_maps[DestinationMap.WATER_TO_LIGHT])
    temp = get_destination(light, range_maps[DestinationMap.LIGHT_TO_TEMPERATURE])
    humidity = get_destination(temp, range_maps[DestinationMap.TEMPERATURE_TO_HUMIDITY])
    location = get_destination(
        humidity, range_maps[DestinationMap.HUMIDITY_TO_LOCATION]
    )
    return location


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        almanac = f.read().strip()

    seed_ranges, range_maps = read_input(almanac)

    locations = []
    threads = []

    pool = ThreadPool(processes=4)
    print(seed_ranges)
    # sys.exit()

    for seed_range in seed_ranges:
        for seed in seed_range:
            thread = pool.apply_async(func=get_seed_location, args=(seed, range_maps))
            threads.append(thread)

            # locations.append(get_seed_location(seed, range_maps))

    for thread in threads:
        location = thread.get()
        locations.append(location)

    print(f"nearest seed location: {min(locations)}")

