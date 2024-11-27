with open("input.txt", "r") as file:
    s = file.read()

groups = s.split("\n\n")
seeds, rest = groups[0], groups[1:]
seeds = [int(i) for i in seeds.split(": ")[1].split(" ")]
maps = [r.split(":\n")[1] for r in rest]
maps = [r.split("\n") for r in maps]
final_maps = []
for row in maps:
    map_lines = []
    for line in row:
        l = [int(i) for i in line.split(" ") if not i == '']
        if len(l) == 3:
            map_lines.append(l)
    final_maps.append(map_lines)
maps = final_maps
m = float('inf')
i = 0
seed_ranges = []
while i + 1 < len(seeds):
    seed_ranges.append([seeds[i], seeds[i + 1]])
    i += 2

# part 1
for seed in seeds:
    curr = seed
    for map_type in maps:
        for map_range in map_type:
            sink, source, length = map_range
            if source <= curr < source + length:
                curr = curr + sink - source
                break
    m = min(m, curr)
print(m)


# part 2

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"({self.start},{self.end})"

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def combine_ranges(ranges):
    if len(ranges) == 1:
        return ranges
    ranges.sort(key=lambda x: x.start)
    prev = ranges[0]
    output = []
    for i in range(1, len(ranges)):
        # if there's overlap, combine the two
        if prev.start <= ranges[i].start <= prev.end:
            prev = Range(prev.start, max(ranges[i].end, prev.end))
        else:
            output.append(prev)
            prev = ranges[i]
    if len(output) == 0 or output[-1].start != prev.start or output[-1].end != prev.end:
        output.append(prev)
    return output


class Transform:
    def __init__(self, r, diff):
        self.range = r
        self.diff = diff

    def __str__(self):
        return f"range:{str(self.range)},diff:{self.diff}"


def transform_ranges(current_ranges, transforms):
    if not transforms:
        return current_ranges

    result = []
    for curr_range in current_ranges:
        unprocessed = [(curr_range, False)]

        for transform in transforms:
            new_unprocessed = []
            for range_to_process, _ in unprocessed:
                transformed_pieces = transform_range(range_to_process, transform.range, transform.diff)
                for piece, was_transformed in transformed_pieces:
                    if was_transformed:
                        result.append(piece)
                    else:
                        new_unprocessed.append((piece, False))
            unprocessed = new_unprocessed

        # Add any ranges that weren't transformed by any rule
        result.extend(piece for piece, _ in unprocessed)

    return combine_ranges(result)


def transform_range(curr, from_range, diff):
    if curr.end < from_range.start or curr.start > from_range.end:
        return [(curr, False)]
    ranges = []
    if curr.start < from_range.start:
        ranges.append((Range(curr.start, from_range.start-1), False))
    ranges.append(((Range(max(curr.start, from_range.start)+diff, min(curr.end, from_range.end)+diff)), True))
    if curr.end > from_range.end:
        ranges.append((Range(from_range.end+1, curr.end), False))
    return ranges


def part2(seed_ranges, maps):
    ranges = []
    transforms = []
    for map_type in maps:
        map_type_transforms = []
        for map_range in map_type:
            sink, source, length = map_range
            diff = sink - source
            from_range = Range(source, source + length - 1)
            map_type_transforms.append(Transform(from_range, diff))
        transforms.append(map_type_transforms)
    for r in seed_ranges:
        ranges.append(Range(r[0], r[0] + r[1] - 1))
    for t in transforms:
        ranges = transform_ranges(ranges, t)
    return ranges


final_ranges = part2(seed_ranges, maps)
m = float('inf')
print([str(f) for f in final_ranges])
for r in final_ranges:
    m = min(r.start, m)

print(m)
