def should_tail_move(head, tail):
    return abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1


def move_tail(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if x_diff == 1 and y_diff == 2:
        return (1, 1)
    elif x_diff == 2 and y_diff == 1:
        return (1, 1)
    elif x_diff == -1 and y_diff == 2:
        return (-1, 1)
    elif x_diff == 2 and y_diff == -1:
        return (1, -1)
    elif x_diff == -1 and y_diff == -2:
        return (-1, -1)
    elif x_diff == -2 and y_diff == -1:
        return (-1, -1)
    elif x_diff == 2 and y_diff == 0:
        return (1, 0)
    elif x_diff == 0 and y_diff == 2:
        return (0, 1)
    elif x_diff == -2 and y_diff == 0:
        return (-1, 0)
    elif x_diff == 0 and y_diff == -2:
        return (0, -1)
    elif x_diff == -2 and y_diff == 1:
        return (-1, 1)
    elif x_diff == 1 and y_diff == -2:
        return (1, -1)
    elif x_diff == 2 and y_diff == 2:
        return (1, 1)
    elif x_diff == -2 and y_diff == -2:
        return (-1, -1)
    elif x_diff == 2 and y_diff == -2:
        return (1, -1)
    elif x_diff == -2 and y_diff == 2:
        return (-1, 1)


def part_one(filename):
    head = [0, 0]
    tail = [0, 0]
    points_visited = [(0, 0)]
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            [dir, steps] = line.split(" ")
            if dir == "R":
                head_step = 1
                head_point = 0
            elif dir == "U":
                head_step = 1
                head_point = 1
            elif dir == "L":
                head_step = -1
                head_point = 0
            elif dir == "D":
                head_step = -1
                head_point = 1

            for _ in range(0, int(steps)):
                head[head_point] += head_step

                if should_tail_move(head, tail):
                    tail_moves = move_tail(head, tail)
                    tail[0] += tail_moves[0]
                    tail[1] += tail_moves[1]
                    points_visited.append((tail[0], tail[1]))

    return len(set(points_visited))


def part_two(filename):
    knots = [[0, 0] for _ in range(0, 10)]
    points_visited = [(0, 0)]
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        for line in lines:
            [dir, steps] = line.split(" ")
            if dir == "R":
                head_step = 1
                head_point = 0
            elif dir == "U":
                head_step = 1
                head_point = 1
            elif dir == "L":
                head_step = -1
                head_point = 0
            elif dir == "D":
                head_step = -1
                head_point = 1
            
            for _ in range(0, int(steps)):
                knots[0][head_point] += head_step

                for i in range(1, len(knots)):
                    if should_tail_move(knots[i - 1], knots[i]):
                        tail_moves = move_tail(knots[i - 1], knots[i])
                        knots[i][0] += tail_moves[0]
                        knots[i][1] += tail_moves[1]
                        if i == len(knots) - 1: # last tail
                            points_visited.append((knots[i][0], knots[i][1]))

    return len(set(points_visited))


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test_1.txt") == 13
    assert part_two(f"{cur_dir}/test_2.txt") == 36
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))