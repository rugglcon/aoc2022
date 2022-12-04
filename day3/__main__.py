from itertools import accumulate
import string


def part_one(filename):
    with open(filename) as f:
        return list(
            accumulate(
                string.ascii_letters.index(
                    [
                        s
                        for s in line[: len(line) // 2]
                        if s in line[len(line) // 2 :]
                    ][0]
                )
                + 1
                for line in [l.strip() for l in f.readlines()]
            )
        )[-1]


def part_two(filename):
    letters = []
    with open(filename) as f:
        input = [l.strip() for l in f.readlines()]
        for i in range(0, len(input) - 2, 3):
            elf1, elf2, elf3 = input[i:i + 3]
            letter = [c for c in elf1 if c in elf2 and c in elf3][0]
            letters.append(string.ascii_letters.index(letter) + 1)

    return sum(letters)

if __name__ == "__main__":
    assert part_one("day3/test.txt") == 157
    assert part_two("day3/test.txt") == 70
    print(part_one("day3/input.txt"), part_two("day3/input.txt"))
