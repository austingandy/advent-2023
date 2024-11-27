with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]  # Strip newlines

s = 0
counts = dict()
for i in range(len(lines)):
    counts[i] = 1

for i, l in enumerate(lines):
    c, rest = l.split(": ")
    winning, ours = rest.split(" | ")
    winning = {int(i) for i in winning.split(" ") if not i == ''}
    ours = [int(i) for i in ours.split(" ") if not i == '']
    count = 0
    for n in ours:
        if n in winning:
            count += 1
    for j in range(i+1,i+count+1):
        if j in counts:
            counts[j] += counts[i]
    print(f"{i+1=}")
    print(f"{count=}")
    print(f"{counts[i]=}")
    print()
s = 0
for k in counts:
    s += counts[k]
print(s)
