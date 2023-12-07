import math
import sys

from collections import defaultdict, namedtuple

Race = namedtuple("Race", "duration record")



if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        puzzle_input = f.read().strip()

    races = []
    duration_deets, record_deets = puzzle_input.splitlines()
    duration = int("".join(duration_deets.split(":")[1].strip().split()))
    record = int("".join(record_deets.split(":")[1].strip().split()))
    race = Race(duration, record)


    results: list[int] = []
    new_records: list[int] = []

    for milliseconds_held in range(race.duration):
        # hold button for <durration> milliseconds
        # +1 speed for each millisecond held
        speed = milliseconds_held
        remaining_time = race.duration - milliseconds_held
        distance = speed * remaining_time

        if distance > race.record:
            new_records.append(distance)

        print(f"speed={speed}, distance={distance}")

    ways_to_win = len(new_records)
    results.append(ways_to_win)

    print(math.prod(results))

