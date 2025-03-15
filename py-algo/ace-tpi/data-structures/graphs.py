from collections import deque
from heapq import *


class Node:
    def __init__(self, d):
        self.data = d
        self.neighbors: list[Node] = []


def clone(root: Node) -> Node:
    stk = [root]
    node_map = {}

    new_root = None
    while stk:
        node = stk.pop()
        if node.data not in node_map:
            new_node = Node(node.data)
            if not new_root:
                new_root = new_node

            node_map[node] = new_node
            for n in node.neighbors:
                if n not in node_map:
                    stk.append(n)

    for orig_node, new_node in node_map.items():
        for n in orig_node.neighbors:
            new_node.neighbors.append(node_map[n])
    return new_root


def clone_dfs_recursive(root: Node) -> Node:
    def clone_rec(node: Node):
        nonlocal node_map, new_root

        if node not in node_map:
            new_node = Node(node.data)
            if not new_root:
                new_root = new_node
            node_map[node] = new_node
            for n in node.neighbors:
                clone_rec(n)

    node_map = {}
    new_root: Node = None
    clone_rec(root)
    for orig_node, new_node in node_map.items():
        for n in orig_node.neighbors:
            new_node.neighbors.append(node_map[n])

    return new_root


def is_scheduling_possible(tasks, prerequisites):
    graph, in_degree = {}, {}
    for i in range(tasks):
        graph[i], in_degree[i] = [], 0

    for task, pre_req in prerequisites:
        in_degree[pre_req] += 1
        graph[task].append(pre_req)

    q = deque()
    for task in in_degree:
        if in_degree[task] == 0:
            q.append(task)

    task_cnt = 0
    while q:
        task_cnt += 1
        task = q.popleft()

        for pre_req in graph[task]:
            in_degree[pre_req] -= 1
            if in_degree[pre_req] == 0:
                q.append(pre_req)
    return task_cnt == tasks


def find_order(tasks, prerequisites):
    graph, in_degree = {}, {}
    for i in range(tasks):
        graph[i], in_degree[i] = [], 0

    for task, pre_req in prerequisites:
        in_degree[pre_req] += 1
        graph[task].append(pre_req)

    q = deque()
    for task in in_degree:
        if in_degree[task] == 0:
            q.append(task)

    sorted_tasks = []
    while q:
        task = q.popleft()
        sorted_tasks.append(task)

        for pre_req in graph[task]:
            in_degree[pre_req] -= 1
            if in_degree[pre_req] == 0:
                q.append(pre_req)
    return sorted_tasks if len(sorted_tasks) == tasks else []


def print_orders(tasks, prerequisites):
    # TODO: Write your code here
    print()


def convertMax(maxHeap):
    # Write your code here
    pass


def main():
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print(
        "Is scheduling possible: "
        + str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]))
    )
    print(
        "Is scheduling possible: "
        + str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]]))
    )


main()
