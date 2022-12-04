def part_one(filename):
    num_pairs = 0
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            elf1, elf2 = line.split(",")
            if (
                int(elf1.split("-")[0]) >= int(elf2.split("-")[0]) and int(elf1.split("-")[1]) <= int(elf2.split("-")[1])
            ) or (
                int(elf2.split("-")[0]) >= int(elf1.split("-")[0]) and int(elf2.split("-")[1]) <= int(elf1.split("-")[1])
            ):
                num_pairs += 1

    return num_pairs


def part_two(filename):
    num_pairs = 0
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            elf1, elf2 = line.split(",")
            if (
                int(elf1.split("-")[0]) >= int(elf2.split("-")[0]) and int(elf1.split("-")[0]) <= int(elf2.split("-")[1])
            ) or (
                int(elf2.split("-")[0]) >= int(elf1.split("-")[0]) and int(elf2.split("-")[0]) <= int(elf1.split("-")[1])
            ):
                num_pairs += 1

    return num_pairs


if __name__ == "__main__":
    assert part_one("day4/test.txt") == 2
    assert part_two("day4/test.txt") == 4
    print(part_one("day4/input.txt"), part_two("day4/input.txt"))