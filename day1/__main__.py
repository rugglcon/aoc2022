from itertools import groupby


def part_one(filename):
    with open(filename) as f:
        return max(
            [
                sum([int(x) for x in list(n)])
                for a, n in groupby(
                    [l.strip() for l in f.readlines()], key=lambda x: len(x)
                )
                if a
            ]
        )


def part_two(filename):
    with open(filename) as f:
        return sum(
            sorted(
                [
                    sum([int(x) for x in list(n)])
                    for a, n in groupby(
                        [l.strip() for l in f.readlines()], key=lambda x: len(x)
                    )
                    if a
                ],
                reverse=True
            )[:3]
        )


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == 24000
    assert part_two(f"{cur_dir}/test.txt") == 45000
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))