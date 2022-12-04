def get_score_1(round):
    win = 6
    draw = 3
    lose = 0
    rock = 1
    paper = 2
    scissors = 3
    [them, me] = round.split(" ")
    if them == "A" and me == "X":
        # draw
        return draw + rock
    elif them == "A" and me == "Y":
        # win
        return win + paper
    elif them == "A" and me == "Z":
        # lose
        return lose + scissors
    elif them == "B" and me == "X":
        # lose
        return lose + rock
    elif them == "B" and me == "Y":
        # draw
        return draw + paper
    elif them == "B" and me == "Z":
        # win
        return win + scissors
    elif them == "C" and me == "X":
        # win
        return win + rock
    elif them == "C" and me == "Y":
        # lose
        return lose + paper
    elif them == "C" and me == "Z":
        # draw
        return draw + scissors


def get_score_2(round):
    win = 6
    draw = 3
    lose = 0
    rock = 1
    paper = 2
    scissors = 3
    [them, me] = round.split(" ")
    if them == "A" and me == "X":
        return lose + scissors
    elif them == "A" and me == "Y":
        return draw + rock
    elif them == "A" and me == "Z":
        return win + paper
    elif them == "B" and me == "X":
        return lose + rock
    elif them == "B" and me == "Y":
        return draw + paper
    elif them == "B" and me == "Z":
        return win + scissors
    elif them == "C" and me == "X":
        return lose + paper
    elif them == "C" and me == "Y":
        return draw + scissors
    elif them == "C" and me == "Z":
        return win + rock


def part_one(filename):
    with open(filename) as f:
        return sum([get_score_1(round.strip()) for round in f.readlines()])


def part_two(filename):
    with open(filename) as f:
        return sum([get_score_2(round.strip()) for round in f.readlines()])


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == 15
    assert part_two(f"{cur_dir}/test.txt") == 12
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))