import re

with open("input.txt", "r") as file:
    lines = file.readlines()

numbers = "one two three four five six seven eight nine".split()
r = "|".join(numbers) + "|\\d"
r = "(?=(" + r + "))"
nMap = {n: str(i+1) for i, n in enumerate(numbers)}


def f(x):
    if x in nMap:
        return nMap[x]
    return x


s = 0
for l in lines:
    digits = re.findall(r, l)
    s += int(f(digits[0]) + f(digits[-1]))

print(s)
