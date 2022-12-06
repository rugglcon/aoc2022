def do_problem(filename, message_length):
    with open(filename) as f:
        subroutine = []
        line = [
            l.strip() for l in f.readlines()
        ][0]
        index = 0
        while len(subroutine) < message_length:
            subroutine.append(line[index])
            if len(set(subroutine)) < message_length and index >= message_length - 1:
                subroutine.reverse()
                subroutine.pop()
                subroutine.reverse()
            index += 1
    
    return index


def part_one(filename):
    return do_problem(filename, 4)


def part_two(filename):
    return do_problem(filename, 14)


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == 7
    assert part_two(f"{cur_dir}/test.txt") == 19
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))