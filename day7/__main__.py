from typing import Dict, List


class Directory():
    parent: "Directory" = None
    name: str = None
    children: List["Directory"] = []
    size = 0

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
    
    def add_file(self, size):
        self.size += size
    
    def add_child_dir(self, dir):
        self.children.append(dir)
    
    def get_size(self):
        print(f"getting size for dir {self.name}")
        sizes = []
        for c in self.children:
            sizes.append(c.get_size())
        
        return sum(sizes) + self.size
    
    def __repr__(self) -> str:
        return self.name


def part_one(filename):
    dirs: Dict[str, Directory] = {}
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        prev_dir: Directory = None
        cur_dir: Directory = None
        for l in lines:
            args = l.split(" ")
            if args[0] == "$":
                if args[1] == "cd":
                    if args[2] == "..":
                        print(f"in {cur_dir}, going to {cur_dir.parent}")
                        cur_dir = cur_dir.parent
                        prev_dir = cur_dir.parent
                    else:
                        print(f"in {cur_dir}, entering {args[2]}")
                        if args[2] not in dirs:
                            print(f"adding dir {args[2]} from 'cd' command")
                            dirs[args[2]] = Directory(cur_dir, args[2])

                        prev_dir = cur_dir
                        cur_dir = dirs[args[2]]
                        print(f"entered {cur_dir} from {prev_dir}")
                elif args[1] == "ls":
                    print("ls")
                    continue
            else:
                if args[0].isnumeric():
                    cur_dir.add_file(int(args[0]))
                    print(f"added file {args[1]} to {cur_dir}")
                elif args[0] == "dir":
                    if args[1] not in dirs:
                        print(f"adding dir {args[1]} from 'dir' command")
                        dirs[args[1]] = Directory(cur_dir, args[1])

                    cur_dir.add_child_dir(dirs[args[1]])
                    print(f"add child {args[1]} to {cur_dir}")
    
    for d in dirs.values():
        print(d, d.children, d.parent)
    
    assert False
    return sum(
        [d.get_size() for d in dirs.values() if d.get_size() <= 100000]
    )


def part_two(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        pass


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == 95437
    # assert part_two(f"{cur_dir}/test.txt") == 0
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))