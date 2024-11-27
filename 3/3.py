import re

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]  # Strip newlines

s = 0
added = set()
padded_lines = ["." * len(lines[0])] + lines + ["." * len(lines[0])]
for i in range(1, len(lines)-1):
    before, curr, after = padded_lines[i:i+3]
    for pos, c in enumerate(curr):
        if not c.isdigit() and not c == '.':
            for l in [before, after, curr]:
                for j in [pos+1, pos-1, pos]:
                    if 0 <= j < len(l) and l[j].isdigit():
                        # find the full number that has a digit at l[j]
                        start, end = j, j
                        while start >= 0 and l[start].isdigit():
                            start -= 1
                        while end < len(l) and l[end].isdigit():
                            end += 1
                        print(f"start: {start+1}, end: {end-1}")
                        print(f"adding val: {l[start+1:end]}")
                        if not (i, start+1, end) in added:
                            s += int(l[start+1:end])
                            added.add((i, start+1, end))
print(s)

