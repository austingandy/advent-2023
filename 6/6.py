import math

with open("input.txt", "r") as file:
    s = file.read()
s = s.split("\n")
times, distances = s[0], s[1]
times = [int(s) for s in times.split(" ")[1:] if len(s) > 0]
distances = [int(s) for s in distances.split(" ")[1:] if len(s) > 0]
print(times)
print(distances)

def ways_to_beat(time, dist, curr_speed, can_hold):
    if time == 0:
        return 0
    if not can_hold:
        return 1 if time * curr_speed > dist else 0
    else:
        # initiate launch sequence or keep holding
        launch_now = ways_to_beat(time - 1, dist - curr_speed, curr_speed, False)
        keep_holding = ways_to_beat(time - 1, dist, curr_speed + 1, True)
        return launch_now + keep_holding


def fast_ways_to_beat(time, dist):
    inner = time**2 - 4*dist
    if inner < 0:
        return 0
    first_term = math.sqrt(inner)
    left = (-1*time + first_term)/-2.0
    right = (-1*time - first_term)/-2.0
    high = max(left, right)
    low = min(left, right)
    num_vals = int(high) - int(low)
    if int(low) == low:
        num_vals -= 1
    return max(0, num_vals)


q = 1
for t, d in zip(times, distances):
    answer = fast_ways_to_beat(t, d)
    print(f"{answer=}")
    q *= answer

print(q)

# part 2
new_s = [l.replace(" ", "") for l in s]
time = int(new_s[0].split(":")[1])
dist = int(new_s[1].split(":")[1])
print(time, dist)
print(fast_ways_to_beat(time, dist))
