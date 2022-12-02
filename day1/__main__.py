from itertools import groupby


def part_one():
    with open("day1/input.txt") as f:
        return max(
            [
                sum([int(x) for x in list(n)])
                for a, n in groupby(
                    [l.strip() for l in f.readlines()], key=lambda x: len(x)
                )
                if a
            ]
        )


def part_two():
    with open("day1/input.txt") as f:
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
    print((part_one(), part_two()))