from concurrent import futures
import string
import sys
import copy
from time import time


def make_graph(lines, start_letter):
    start_index = []
    end_index = (0, 0)
    graph = []
    for i, line in enumerate(lines):
        graph.append([string.ascii_letters.index(l) for l in line])
        if start_letter in line:
            start_index.extend(
                [(i, l) for l, t in enumerate(line) if t == start_letter]
            )

        if "E" in line:
            end_index = (i, line.index("E"))

    for start in start_index:
        graph[start[0]][start[1]] = 0
    graph[end_index[0]][end_index[1]] = 25
    return graph, start_index, end_index


def do_path_search(graph, start, end, shortest_path):
    previous_nodes = {}
    shortest_path[start] = 0
    visited = set()
    nodes = set([start])
    while nodes:
        min_node = None
        for node in nodes:
            if min_node is None:
                min_node = node
            elif shortest_path[node] < shortest_path[min_node]:
                min_node = node

        neighbors = [
            (min_node[0] - 1, min_node[1]),
            (min_node[0] + 1, min_node[1]),
            (min_node[0], min_node[1] - 1),
            (min_node[0], min_node[1] + 1),
        ]

        for n in neighbors:
            if n[0] < 0 or n[0] == len(graph):
                continue  # not in graph
            if n[1] < 0 or n[1] == len(graph[n[0]]):
                continue  # not in graph
            if (graph[n[0]][n[1]] - graph[min_node[0]][min_node[1]]) > 1:
                continue  # can't move to this neighbor

            if n not in visited:
                nodes.add(n)
                val = shortest_path[min_node] + 1
                if val < shortest_path[n]:
                    shortest_path[n] = val
                    previous_nodes[n] = min_node

        visited.add(min_node)
        nodes.discard(min_node)

    path = []
    if end in previous_nodes:
        node = end
        while node != start:
            path.append(node)
            node = previous_nodes[node]

    return path


def part_one(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        graph, start, end = make_graph(lines, "S")
        all_nodes = []
        shortest_path = {}
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                all_nodes.append((i, j))
                shortest_path[(i, j)] = sys.maxsize
        
        return len(do_path_search(graph, start[0], end, all_nodes, shortest_path, 0))


def part_two(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        graph, start, end = make_graph(lines, "a")
        paths = []
        all_nodes = []
        shortest_path = {}
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                all_nodes.append((i, j))
                shortest_path[(i, j)] = sys.maxsize

        for s in start:
            shortest_path_copy = copy.deepcopy(shortest_path)
            paths.append(do_path_search(graph, s, end, shortest_path_copy))

        return min([len(s) for s in paths if s])


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    print("part 1 test")
    assert part_one(f"{cur_dir}/test.txt") == 31
    print("part 2 test")
    assert part_two(f"{cur_dir}/test.txt") == 29
    part_1_time_start = time()
    print("part 1 real", part_one(f"{cur_dir}/input.txt"))
    end_part_1 = time()
    print("took", end_part_1 - part_1_time_start, "to run part 1")
    print("part 2 real", part_two(f"{cur_dir}/input.txt"))
    print("took", time() - end_part_1, "to run part 2")
