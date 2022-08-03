# stitch everythin together #

def enough_fuel(curr_fuel, distance_inbetween):
    return curr_fuel > distance_inbetween


def fill_up(FULL):
    curr_fuel = FULL
    return curr_fuel


def not_enough(FULL, distance_inbetween):
    return FULL < distance_inbetween


def fuel_left(curr_fuel, distance_inbetween):
    return curr_fuel - distance_inbetween


def gas_stations(disance, tank_size, stations):
    DISTANCE = disance
    FULL = tank_size
    result = []
    LAST_STOP = len(stations)
    for index in range(len(stations)):

        if index == 0:
            dist = stations[0]
            dist_forward = stations[1] - stations[0]
            curr_fuel = FULL
            if not_enough(FULL, dist):
                result = []
                break
            if not_enough(FULL, dist_forward):
                result = []
                break
            curr_fuel = fuel_left(curr_fuel, dist)
            if not enough_fuel(curr_fuel, dist_forward):
                curr_fuel = fill_up(FULL)
                result.append(stations[0])

        elif index == LAST_STOP - 1:
            dist = stations[index] - stations[index - 1]
            curr_fuel = fuel_left(curr_fuel, dist)
            dist_forward = DISTANCE - stations[index]
            if not_enough(FULL, dist_forward):
                result = []
                break
            if not enough_fuel(curr_fuel, dist_forward):
                curr_fuel = fill_up(FULL)
                result.append(stations[index])

        else:
            if stations[index + 1] > DISTANCE:
                continue
            dist_forward = stations[index + 1] - stations[index]
            dist = stations[index] - stations[index - 1]
            if not_enough(FULL, dist):
                result = []
                break
            curr_fuel = fuel_left(curr_fuel, dist)

            if not enough_fuel(curr_fuel, dist_forward):
                curr_fuel = fill_up(FULL)
                result.append(stations[index])

    return result


tests = [
    (320, 90, [50, 80, 140, 180, 220, 290], [80, 140, 220, 290]),
    (390, 80, [70, 90, 140, 210, 240, 280, 350], [70, 140, 210, 280, 350]),
    (100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150], [40, 80]),
    (100, 50, [10, 90], []),
]

for test, test2, test3, expected in tests:
    print(expected == gas_stations(test, test2, test3))
