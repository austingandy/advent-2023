with open("input.txt", "r") as file:
    s = file.read()

grid = [[c for c in l] for l in s.split("\n") if len(l) > 0]

print(grid)


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Grid:
    def __init__(self, grid):
        self.grid = grid
        if len(grid) == 0:
            self.width = 0
        else:
            self.width = len(self.grid[0])
        self.height = len(grid)
        for y in range(self.height):
            for x in range(self.width):
                p = Pos(x, y)
                if self.get(p) == 'S':
                    self.s = p

    def get(self, pos):
        return self.grid[pos.y][pos.x]

    def neighbors(self, pos):
        n = [Pos(pos.x + x, pos.y + y) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        return [p for p in n if 0 <= p.x < self.width and 0 <= p.y < self.height]

    def contiguous_neighbors(self, pos):
        neighbors = self.neighbors(pos)
        contiguous = []
        curr = self.get(pos)
        for n in neighbors:
            v = self.get(n)
            if curr == 'S':
                if n.x-pos.x == 1 and v in ['7', 'J', '-']:
                    contiguous.append(n)
                elif n.x-pos.x == -1 and v in ['F', 'L', '-']:
                    contiguous.append(n)
                elif n.y-pos.y == 1 and v in ['L', 'J', '|']:
                    contiguous.append(n)
                elif n.y-pos.y == -1 and v in ['7', 'F', '|']:
                    contiguous.append(n)
            else:
                if curr in ['-', 'L', 'F'] and n.x-pos.x == 1 and v in ['7', 'J', '-']:
                    contiguous.append(n)
                elif curr in ['-', 'J', '7'] and n.x-pos.x == -1 and v in ['F', 'L', '-']:
                    contiguous.append(n)
                elif curr in ['|', 'F', '7'] and n.y-pos.y == 1 and v in ['L', 'J', '|']:
                    contiguous.append(n)
                elif curr in ['|', 'L', 'J'] and n.y-pos.y == -1 and v in ['7', 'F', '|']:
                    contiguous.append(n)
        return contiguous

    def __len__(self):
        return self.height

    def find_loop_length(self, start):
        cpy = [[x for x in row] for row in self.grid]
        visited = set()
        frontier = {start}
        while len(frontier):
            next_frontier = set([l for p in frontier for l in self.contiguous_neighbors(p) if p not in visited])
            for p in frontier:
                visited.add(p)
            frontier = next_frontier
        for p in visited:
            cpy[p.y][p.x] = 'v'
        for r in cpy:
            print(''.join(r))
        return len(visited)


def find_s(grid):
    for y in range(grid.height):
        for x in range(grid.width):
            p = Pos(x, y)
            if grid.get(p) == 'S':
                return p


grid = Grid(grid)
print(grid.find_loop_length(grid.s)//2)

