from typing import Dict, List


class Directory():
    parent: "Directory" = None
    dir_name: str = None
    children: List["Directory"] = []
    size = 0

    def __init__(self, parent, name):
        self.parent = parent
        self.dir_name = name
        self.children = []
        self.size = 0
    
    def add_file(self, size):
        self.size += size
    
    def add_child_dir(self, dir):
        self.children.append(dir)
    
    def get_size(self):
        return sum(
            [c.get_size() for c in self.children]
        ) + self.size
    
    def get_path(self):
        path = self.dir_name
        if self.parent:
            if self.parent.dir_name == "/":
                parent_path = ""
            else:
                parent_path = f"{self.parent.get_path()}/"
            path = f"{parent_path}{path}"
        return path
        
    def __repr__(self) -> str:
        return self.get_path()


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
                        cur_dir = cur_dir.parent
                        prev_dir = cur_dir.parent
                    else:
                        if args[2] == "/":
                            new_dir = Directory(cur_dir, args[2])
                            dirs[new_dir.get_path()] = new_dir

                        if cur_dir and cur_dir.get_path() + args[2] not in dirs:
                            new_dir = Directory(cur_dir, args[2])
                            dirs[new_dir.get_path()] = new_dir

                        prev_dir = cur_dir
                        cur_dir = new_dir
                        if prev_dir:
                            prev_dir.add_child_dir(cur_dir)
                elif args[1] == "ls":
                    continue
            else:
                if args[0].isnumeric():
                    cur_dir.add_file(int(args[0]))
    
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