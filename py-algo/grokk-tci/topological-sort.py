from collections import deque

def topological_sort(vertices, edges):
    """
    Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its
    vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

    Given a directed graph, find the topological ordering of its vertices.

    Example 1:
    Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
    Output: Following are the two valid topological sorts for the given graph:
    1) 3, 2, 0, 1
    2) 3, 2, 1, 0
    """
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph
    q = deque()

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    for node, cnt in in_degree.items():
        if cnt == 0:
            q.append(node)

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            sortedOrder.append(node)

            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)

    return sortedOrder


def is_scheduling_possible(tasks, prerequisites):
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
    Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

    Example 1:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: true
    Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
    before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]

    Example 2:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
    Output: false
    Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.

    Example 3:
    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output: true
    Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
    """
    in_degrees_map = {i:0 for i in range(tasks)}
    adjacency_map = {i:[] for i in range(tasks)}
    scheduled_tasks = 0
    q = deque()

    for pre_req, task in prerequisites:
        adjacency_map[pre_req].append(task)
        in_degrees_map[task] += 1

    for task, degree in in_degrees_map.items():
        if degree == 0: q.append(task)

    while q:
        for _ in range(len(q)):
            task = q.popleft()
            scheduled_tasks += 1

            for child_task in adjacency_map[task]:
                in_degrees_map[child_task] -= 1
                if in_degrees_map[child_task] == 0:
                    q.append(child_task)

    return scheduled_tasks == tasks


def find_order(tasks, prerequisites):
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which need to be completed before it can be scheduled.

    Given the number of tasks and a list of prerequisite pairs, write a method to
    find the ordering of tasks we should pick to finish all tasks.

    Example 1:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: [0, 1, 2]
    Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
    before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]

    Example 2:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
    Output: []
    Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.

    Example 3:
    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output: [0 1 4 3 2 5]
    Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
    """
    in_degrees_map = {i:0 for i in range(tasks)}
    adjacency_map = {i:[] for i in range(tasks)}
    sorted_order = []
    q = deque()

    for pre_req, task in prerequisites:
        adjacency_map[pre_req].append(task)
        in_degrees_map[task] += 1

    for task, degree in in_degrees_map.items():
        if degree == 0: q.append(task)

    while q:
        for _ in range(len(q)):
            task = q.popleft()
            sorted_order.append(task)

            for child_task in adjacency_map[task]:
                in_degrees_map[child_task] -= 1
                if in_degrees_map[child_task] == 0:
                    q.append(child_task)

    return sorted_order if len(sorted_order) == tasks else []


def print_orders(tasks, prerequisites):
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

    Example 1:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: [0, 1, 2]
    Explanation: There is only possible ordering of the tasks.

    Example 2:
    Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
    Output:
    1) [3, 2, 0, 1]
    2) [3, 2, 1, 0]
    Explanation: There are two possible orderings of the tasks meeting all prerequisites.

    Example 3:
    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output:
    1) [0, 1, 4, 3, 2, 5]
    2) [0, 1, 3, 4, 2, 5]
    3) [0, 1, 3, 2, 4, 5]
    4) [0, 1, 3, 2, 5, 4]
    5) [1, 0, 3, 4, 2, 5]
    6) [1, 0, 3, 2, 4, 5]
    7) [1, 0, 3, 2, 5, 4]
    8) [1, 0, 4, 3, 2, 5]
    9) [1, 3, 0, 2, 4, 5]
    10) [1, 3, 0, 2, 5, 4]
    11) [1, 3, 0, 4, 2, 5]
    12) [1, 3, 2, 0, 5, 4]
    13) [1, 3, 2, 0, 4, 5]
    """
    in_degrees_map = {i:0 for i in range(tasks)}
    adjacency_map = {i:[] for i in range(tasks)}
    sorted_orders = deque([[]])
    sources = deque()

    for parent_task, child_task in prerequisites:
        adjacency_map[parent_task].append(child_task)
        in_degrees_map[child_task] += 1

    for task, degree in in_degrees_map.items():
        if degree == 0: sources.append(task)

    while sources:
        level_orders = []
        for _ in range(len(sources)):
            task = sources.popleft()

            for child_task in adjacency_map[task]:
                in_degrees_map[child_task] -= 1
                if in_degrees_map[child_task] == 0:
                    sources.append(child_task)

    # TODO: Come back to

    for order in sorted_orders:
        print(order)


def find_order_alien_dict(words):
    """
    There is a dictionary containing words from an alien language for which we don’t know the ordering of the alphabets.
    Write a method to find the correct order of the alphabets in the alien language.
    It is given that the input is a valid dictionary and there exists an ordering among its alphabets.

    Example 1:
    Input: Words: ["ba", "bc", "ac", "cab"]
    Output: bac
    Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
    from the given words we can conclude the following ordering among its characters:

    1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
    2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

    From the above two points, we can conclude that the correct character order is: "bac"

    Example 2:
    Input: Words: ["cab", "aaa", "aab"]
    Output: cab
    Explanation: From the given words we can conclude the following ordering among its characters:

    1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
    2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'

    From the above two points, we can conclude that the correct character order is: "cab"

    Example 3:
    Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
    Output: ywxz
    Explanation: From the given words we can conclude the following ordering among its characters:

    1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
    2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
    3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
    4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
    5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'

    From the above five points, we can conclude that the correct character order is: "ywxz"
    """
    # TODO: Come back to
    return ""


def can_construct(originalSeq, sequences):
    """
    Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be
    uniquely reconstructed from the array of sequences.

    Unique reconstruction means that we need to find if originalSeq is the only sequence such that all
    sequences in the array are subsequences of it.

    Example 1:
    Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
    Output: true
    Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct
    [1, 2, 3, 4], in other words, all the given sequences uniquely define the order of numbers
    in the 'originalSeq'.

    Example 2:
    Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
    Output: false
    Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely reconstruct
    [1, 2, 3, 4]. There are two possible sequences we can construct from the given sequences:
    1) [1, 2, 3, 4]
    2) [1, 2, 4, 3]

    Example 3:
    Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
    Output: true
    Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct
    [3, 1, 4, 2, 5].
    """
    # TODO: Come back to
    return False


def find_trees(nodes, edges):
    """
    We are given an undirected graph that has characteristics of a k-ary tree.
    In such a graph, we can choose any node as the root to make a k-ary tree.
    The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT).
    There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs.
    Write a method to find all MHTs of the given graph and return a list of their roots.

    Example 1:
    Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
    Output:[1, 2]
    Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, we can see that the
    height of the trees with roots '1' or '2' is three which is minimum.

    Example 2:
    Input: vertices: 4, Edges: [[0, 1], [0, 2], [2, 3]]
    Output:[0, 2]
    Explanation: Choosing '0' or '2' as roots give us MHTs. In the below diagram, we can see that the
    height of the trees with roots '0' or '2' is three which is minimum.

    Example 3:
    Input: vertices: 4, Edges: [[0, 1], [1, 2], [1, 3]]
    Output:[1]
    """
    # TODO: Write your code here
    return []
