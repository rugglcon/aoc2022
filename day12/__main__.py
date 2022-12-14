import math
from queue import PriorityQueue
import string
import sys

def make_graph(lines):
    start_index = (0, 0)
    end_index = (0, 0)
    graph = []
    for i, line in enumerate(lines):
        graph.append(
            [string.ascii_letters.index(l) for l in line]
        )
        if "S" in line:
            start_index = (i, line.index("S"))
        
        if "E" in line:
            end_index = (i, line.index("E"))
    
    graph[start_index[0]][start_index[1]] = 0
    graph[end_index[0]][end_index[1]] = 25
    return graph, start_index, end_index


def part_one(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        graph, start, end = make_graph(lines)
        visited = set()
        all_nodes = []
        shortest_path = {}
        previous_nodes = {}
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                all_nodes.append((i, j))
                shortest_path[(i, j)] = sys.maxsize

        shortest_path[start] = 0

        while all_nodes:
            min_node = None
            for node in all_nodes:
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
                    continue # not actually a neighbor
                if n[1] < 0 or n[1] == len(graph[n[0]]):
                    continue # not actually a neighbor
                if (graph[n[0]][n[1]] - graph[min_node[0]][min_node[1]]) > 1:
                    continue # can't move to this neighbor
                val = shortest_path[min_node] + (graph[n[0]][n[1]] - graph[min_node[0]][min_node[1]])
                if val < shortest_path[n]:
                    shortest_path[n] = val
                    previous_nodes[n] = min_node
            
            all_nodes.remove(min_node)
        
        path = []
        node = end
        while node != start:
            path.append(node)
            node = previous_nodes[node]

        return len(path)


def part_two(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
        pass


if __name__ == "__main__":
    cur_dir = __file__.split("/")[0]
    assert part_one(f"{cur_dir}/test.txt") == 31
    # assert part_two(f"{cur_dir}/test.txt") == 0
    print(part_one(f"{cur_dir}/input.txt"), part_two(f"{cur_dir}/input.txt"))