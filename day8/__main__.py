from pprint import pprint


def fill_out_grid(lines):
    """
    creates a list grid of the tree input.
    visualized, the grid this makes is actually
    the input rotated 90 degrees to the right
    """
    tree_grid = [[] for _ in range(0, len(lines))]
    for i, line in enumerate(lines):
        tree_grid[i].extend(int(l) for l in line)

    return tree_grid


def can_be_seen(tree, north, south, east, west):
    return any(
        [
            all([tree > n for n in north]),
            all([tree > s for s in south]),
            all([tree > e for e in east]),
            all([tree > w for w in west]),
        ]
    )


def part_one(filename):
    with open(filename) as f:
        tree_grid = fill_out_grid([l.strip() for l in f.readlines()])
        num_visible = (
            len(tree_grid) * 2 + len(tree_grid[0]) * 2
        ) - 4  # counted corners twice
        for i in range(1, len(tree_grid) - 1):
            for j in range(1, len(tree_grid[i]) - 1):
                if can_be_seen(
                    tree_grid[i][j],
                    [tree_grid[n][j] for n in range(0, i)],
                    [tree_grid[s][j] for s in range(i + 1, len(tree_grid))],
                    [tree_grid[i][e] for e in range(0, j)],
                    [tree_grid[i][w] for w in range(j + 1, len(tree_grid[i]))],
                ):
                    num_visible += 1

    return num_visible


def part_two(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        pass


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == 21
    # assert part_two(f"{cur_dir}/test.txt") == 0
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))
