from itertools import takewhile


def get_moves(lines):
    for line in lines:
        move = (
            int(line.split(" ")[1]),
            int(line.split(" ")[3]),
            int(line.split(" ")[5])
        )
        yield move


def part_one(filename):
    crates = []
    with open(filename) as f:
        lines = [l for l in f.readlines()]
        crate_lines = [
            line for line in takewhile(lambda x: x.strip(), lines)
        ]
        crate_lines.reverse() # process lines backward so we get the order correct
        for crate in crate_lines[0]:
            if crate.strip():
                crates.append([]) # prepare the crates

        crate_lines = crate_lines[1:]
        moves = [l.strip() for l in lines[len(crate_lines) + 2:]]

        for line in crate_lines:
            for crate, idx in enumerate(range(0, len(line), 4)):
                item = line[idx : idx + 4].strip()
                if item:
                    crates[crate].append(item)

        # now do moves
        for num_moved, from_crate, to_crate in get_moves(moves):
            popped_items = 0
            while popped_items < num_moved:
                crates[to_crate - 1].append(
                    crates[from_crate - 1].pop()
                )
                popped_items += 1
        
        # get the top items
        return "".join([crate.pop()[1] for crate in crates])


def part_two(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        pass


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == "CMZ"
    assert part_two(f"{cur_dir}/test.txt") == None
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))