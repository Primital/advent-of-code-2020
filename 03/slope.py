import functools


testdata = [
    ".#..#.....#....##..............",
    "...#.#...#...#.#..........#....",
    "#...###...#.#.....#.##.#.#...#.",
    "#.....#.#...##....#...#...#....",
    "##.......##.#.....#........##.#",
    "#..#....#......#..#......#...#."
]


def trees(right, down, map_data):
    height = len(map_data)
    width = len(map_data[0])
    vertical = 0
    horizontal = 0
    trees_hit = 0
    while(vertical < height):
        if map_data[vertical][horizontal] == '#':
            trees_hit += 1
        vertical += down
        horizontal = (horizontal + right) % width
    return trees_hit


assert(trees(3, 1, testdata) == 4)
assert(trees(9, 1, testdata) == 2)


map_data = []
with open('data1', 'r') as f:
    map_data = [x for x in f.read().split('\n') if len(x)]

# Part 1
print(trees(3, 1, map_data))

# Part 2
results = [trees(a, b, map_data) for (a, b) in [
    (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
]]
print(functools.reduce(lambda a, b: a*b, results))
