from math import floor, prod


class Monkey():
    def __init__(self, number, items, op_factor, op_func, test, true_monkey, false_monkey):
        self.number = number
        self.items = items
        self.op_func = op_func
        self.op_factor = op_factor
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.num_inspections = 0


def get_monkeys(lines):
    monkeys = []
    num = None
    items = None
    op_func = None
    op_factor = None
    test = None
    true_monkey = None
    false_monkey = None
    for line in lines:
        if "Monkey" in line:
            num = int(line[line.index(":") - 1])
        if "Starting" in line:
            items = [int(i) for i in line[line.index(":") + 2:].split(", ")]
        if "Operation" in line:
            op_func = sum if line[line.index("old") + 4] == "+" else prod
            op_factor = line.split(" ")[-1]
        if "Test" in line:
            test = int(line.split(" ")[-1])
        if "true" in line:
            true_monkey = int(line.split(" ")[-1])
        if "false" in line:
            false_monkey = int(line.split(" ")[-1])

        if not line:
            monkeys.append(
                Monkey(num, items, op_factor, op_func, test, true_monkey, false_monkey)
            )

    monkeys.append(
        Monkey(num, items, op_factor, op_func, test, true_monkey, false_monkey)
    )
    
    return monkeys


def part_one(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        monkeys = get_monkeys(lines)
        for r in range(20):
            for monkey in monkeys:
                monkey.num_inspections += len(monkey.items)
                items = [i for i in monkey.items]
                for i, item in enumerate(items):
                    item = monkey.op_func([item, int(monkey.op_factor) if monkey.op_factor != "old" else item])
                    item = floor(item / 3)
                    if not item % monkey.test:
                        monkeys[monkey.true_monkey].items.append(item) 
                    else:
                        monkeys[monkey.false_monkey].items.append(item)
                    
                monkey.items = []
            
    return prod(sorted([m.num_inspections for m in monkeys], reverse=True)[0:2])


def part_two(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        monkeys = get_monkeys(lines)
        divisor = prod([m.test for m in monkeys])
        for r in range(10000):
            for monkey in monkeys:
                monkey.num_inspections += len(monkey.items)
                for item in monkey.items:
                    item = monkey.op_func([item, int(monkey.op_factor) if monkey.op_factor != "old" else item])
                    item = item % divisor
                    if not item % monkey.test:
                        monkeys[monkey.true_monkey].items.append(item) 
                    else:
                        monkeys[monkey.false_monkey].items.append(item)
                    
                monkey.items = []
            
    print(prod(sorted([m.num_inspections for m in monkeys], reverse=True)[0:2]))
    return prod(sorted([m.num_inspections for m in monkeys], reverse=True)[0:2])


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == 10605
    assert part_two(f"{cur_dir}/test.txt") == 2713310158
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))