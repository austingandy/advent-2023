with open("input.txt", "r") as file:
    lines = file.readlines()

maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

keys = "red green blue".split()

total = 0
for l in lines:
    gameNum = int(l[5:l.find(":")])
    print(gameNum)
    valid = True
    rounds = l[l.find(":")+2:].split(";")
    colors = [v.strip() for r in rounds for k in r for v in r.split(", ")]
    currMaxes = {k: 0 for k in keys}
    for c in colors:
        s = c.split()
        count = int(s[0])
        currColor = s[1]
        currMaxes[currColor] = max(currMaxes[currColor], count)
    power = 1
    for v in currMaxes.values():
        power *= v
    total += power

print(total)
