def part_one(filename):
    cycle = 1
    register = 1
    cycle_vals = []
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            instrs = line.split(" ")
            if len(instrs) == 1:
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    cycle_vals.append((cycle, register))
            else:
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    cycle_vals.append((cycle, register))
                cycle += 1
                register += int(instrs[1])
                if cycle in [20, 60, 100, 140, 180, 220]:
                    cycle_vals.append((cycle, register))

    return sum([cycle * register for (cycle, register) in cycle_vals])


def part_two(filename):
    cycle = 0
    register = 1
    sprite = (register - 1, register, register + 1)
    CRT = ""
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            instrs = line.split(" ")
            if (cycle % 40) in sprite:
                CRT += "#"
            else:
                CRT += "."
            cycle += 1


            if len(instrs) == 2:
                if (cycle % 40) in sprite:
                    CRT += "#"
                else:
                    CRT += "."

                register += int(instrs[1])
                sprite = (register - 1, register, register + 1)
                cycle += 1

    for i in range(0, len(CRT), 40):
        print(CRT[i:i + 40])


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == 13140
    part_two(f"{cur_dir}/test.txt")
    print("test")
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))
