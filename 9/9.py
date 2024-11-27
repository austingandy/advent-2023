with open("input.txt", "r") as file:
    s = file.readlines()

inputs = []
for line in s:
    inputs.append([int(n) for n in line.split(' ')])

input = inputs[0]
print(input)


def diffs(nums):
    return [next - first for first, next in zip(nums, nums[1:])]


def calc_tree(input):
    curr = input
    tree = [curr]
    while (not all(n == 0 for n in curr)) and len(curr) > 0:
        curr = diffs(curr)
        tree.append(curr)
    return tree


def calc_next(tree):
    # skip the 0th layer because we already know what it's gonna look like
    rev_tree = tree[::-1][1:]
    diff_val = 0
    for l in rev_tree:
        diff_val = l[0] - diff_val
    return diff_val


s = 0
for input in inputs:
    s += calc_next(calc_tree(input))

print(s)




