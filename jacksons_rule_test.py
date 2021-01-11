"""
This program is to test (not prove) the jacksons rule.
Basically you have 2 machines with jobs taking varying amounts of time on each machine
Think of a washing machine/ drying machine job
Whats the best way to schedule these jobs?
Jackson's rule says that we should put the job with the shortest wash first and the shortest dry last
keep repeating this until we no longer have any more loads
Algorithms to Live By Page 107
"""

# Loads in the format of a list of tuples [(wash_time,dry_time)]
# loads is a really bad variable name ik


import random


def calcualte_total_time(ordered_loads):
    total_time = ordered_loads[0][0]
    prev_dry = ordered_loads[0][1]
    for i in range(1, len(ordered_loads)):
        wash, dry = ordered_loads[i]
        total_time += max(prev_dry, wash)
        prev_dry = dry
    total_time += dry

    return total_time


def jacksons_rule(loads):
    # prob faster to sort and do smtn clever but im not clever
    starting_loads = []
    ending_loads = []

    while loads:
        shortest_wash = min(loads, key=lambda x: x[0])
        shortest_dry = min(loads, key=lambda x: x[1])

        if shortest_wash[0] <= shortest_dry[1]:
            starting_loads.append(shortest_wash)
            loads.pop(loads.index(shortest_wash))
        else:
            ending_loads.append(shortest_dry)
            loads.pop(loads.index(shortest_dry))

    return starting_loads + list(reversed(ending_loads))


def greedy_rule(loads):
    # shortest wash time then the next load becomes max wash time less than the prev dry time
    start = min(loads, key=lambda x: x[0])
    load_order = [start]
    loads.pop(loads.index(start))
    prev_dry = start[1]

    while loads:
        all_less = list(filter(lambda x: x[0] <= prev_dry, loads))
        if all_less:
            next_load = max(all_less, key=lambda y: y[0])

        else:
            next_load = max(loads, key=lambda y: y[0])
        loads.pop(loads.index(next_load))
        load_order.append(next_load)

    return load_order


def generate_data():
    data = []
    for i in range(random.randint(500, 1000)):
        data.append((random.randint(1, 500), random.randint(1, 500)))
    return data


if __name__ == "__main__":
    jackson_count = 0
    greedy_count = 0
    tie_count = 0
    greedy_diff = 0
    jackson_diff = 0
    for i in range(1000):
        wash_data = generate_data()

        jackson = calcualte_total_time(jacksons_rule(wash_data.copy()))
        greedy = calcualte_total_time(greedy_rule(wash_data.copy()))

        if jackson > greedy:
            jackson_count += 1
            jackson_diff += jackson - greedy
        elif greedy > jackson:
            greedy_count += 1
            greedy_diff += greedy - jackson
        else:
            tie_count += 1

    print("jackson: " + str(jackson_count))
    print("greedy: " + str(greedy_count))
    print("tie: " + str(tie_count))
    print("jackson_avg: " + str(jackson_diff/jackson_count))
    print("greedy_avg: " + str(greedy_diff/greedy_count))
