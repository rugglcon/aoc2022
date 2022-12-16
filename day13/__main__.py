from functools import cmp_to_key
import json
from pprint import pprint

CORRECT = -1
NO_RESULT = 0
INCORRECT = 1

def get_pairs(lines):
    pairs = []
    left = None
    right = None
    for line in lines:
        if not line:
            pairs.append({"left": left, "right": right})
            left = None
            right = None
        elif left is None:
            left = json.loads(line)
        elif right is None:
            right = json.loads(line)

    return pairs


def compare_packets(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: return CORRECT
        elif right < left: return INCORRECT
        else: return NO_RESULT
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            res = compare_packets(left[i], right[i])
            if res != NO_RESULT:
                return res
        
        if len(left) < len(right):
            return CORRECT
        elif len(right) < len(left):
            return INCORRECT
        else:
            return NO_RESULT
    else:
        return compare_packets(
            left if isinstance(left, list) else [left],
            right if isinstance(right, list) else [right]
        )
    

def part_one(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        pairs = get_pairs(lines)
        good_indices = []

        for idx, pair in enumerate(pairs):
            result = compare_packets(pair["left"], pair["right"])
            if result == CORRECT:
                good_indices.append(idx + 1)
    
    return sum(good_indices)


def part_two(filename):
    with open(filename) as f:
        lines = [json.loads(l.strip()) for l in f.readlines() if l.strip()]
        lines.sort(key=cmp_to_key(compare_packets))
    
    return (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    print("part 1 test")
    assert part_one(f"{cur_dir}/test.txt") == 13
    print("part 2 test")
    part_2_test = part_two(f"{cur_dir}/test.txt")
    print(part_2_test)
    assert part_2_test == 140
    print("part 1 real")
    real_part_1 = part_one(f"{cur_dir}/input.txt")
    print(real_part_1)
    print("part 2 real")
    real_part_2 = part_two(f"{cur_dir}/input.txt")
    print(real_part_2)