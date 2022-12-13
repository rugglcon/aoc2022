from pprint import pprint


def fill_out_grid(lines):
    """
    creates a list grid of the tree input.
    visualized, the grid this makes is actually
    the input rotated 90 degrees to the right
    """
    tree_grid = [[] for _ in range(len(lines))]
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


def takewhile_inclusive(predicate, it):
    """
    needed to grab the element that takewhile
    drops - defined my own function to do it
    """
    for x in it:
        if predicate(x):
            yield x
        else:
            yield x
            break


def view_score(tree, north, south, east, west):
    right = [t for t in takewhile_inclusive(lambda t: t < tree, north)]
    left = [t for t in takewhile_inclusive(lambda t: t < tree, south)]
    down = [t for t in takewhile_inclusive(lambda t: t < tree, east)]
    up = [t for t in takewhile_inclusive(lambda t: t < tree, west)]
    score = 1
    score *= len(right) if right else 1
    score *= len(up) if up else 1
    score *= len(left) if left else 1
    score *= len(down) if down else 1
    return score


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
                    reversed([tree_grid[n][j] for n in range(i)]),
                    [tree_grid[s][j] for s in range(i + 1, len(tree_grid))],
                    [tree_grid[i][w] for w in range(j + 1, len(tree_grid[i]))],
                    reversed([tree_grid[i][e] for e in range(j)]),
                ):
                    num_visible += 1

    return num_visible


def part_two(filename):
    with open(filename) as f:
        tree_grid = fill_out_grid([l.strip() for l in f.readlines()])
        scores = []
        for i in range(1, len(tree_grid) - 1):
            for j in range(1, len(tree_grid[i]) - 1):
                scores.append(
                    view_score(
                        tree_grid[i][j],
                        reversed([tree_grid[n][j] for n in range(i)]),
                        [tree_grid[s][j] for s in range(i + 1, len(tree_grid))],
                        [tree_grid[i][w] for w in range(j + 1, len(tree_grid[i]))],
                        reversed([tree_grid[i][e] for e in range(j)]),
                    )
                )

    return max(scores)


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == 21
    assert part_two(f"{cur_dir}/test.txt") == 8
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))
