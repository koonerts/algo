# Graphs Algorithms Cheatsheet for SWE Interviews

## Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights.

### Visualization

```
Graph:
A --- 3 --- B
|           |
1           2
|           |
C --- 1 --- D

Shortest paths from A:
A -> A: 0
A -> B: 3
A -> C: 1
A -> D: 2 (via A -> C -> D)
```

### Implementation

```python
import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary with infinity for all nodes except start
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to track vertices to visit next
    priority_queue = [(0, start)]  # (distance, node)
    
    # Track the shortest path
    previous = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we've already found a shorter path, skip
        if current_distance > distances[current_node]:
            continue
            
        # Check all neighbors of current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If we found a shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances, previous

# Reconstructing the path from start to end
def get_path(previous, start, end):
    path = []
    current = end
    
    while current != start:
        path.append(current)
        current = previous[current]
        if current is None:
            return []  # No path exists
            
    path.append(start)
    return path[::-1]  # Reverse to get path from start to end
```

### Time & Space Complexity

- **Time**: O((V + E) log V) with binary heap implementation
- **Space**: O(V)

### Variants

- **Dijkstra with early termination**: Stop when the target node is processed
- **Bidirectional Dijkstra**: Run Dijkstra from both start and end simultaneously

## Prim's Algorithm

Prim's algorithm finds a minimum spanning tree (MST) for a weighted undirected graph.

### Visualization

```
Original graph:
    A
   /|\
  4 7 1
 /  |  \
B---2---C
 \     /
  5   3
   \ /
    D

MST:
    A
   / \
  4   1
 /     \
B---2---C
       /
      3
     /
    D

Total weight: 10
```

### Implementation

```python
import heapq

def prim(graph):
    # Pick an arbitrary starting vertex
    start_vertex = next(iter(graph))
    
    # Track visited vertices
    visited = {start_vertex}
    
    # Track edges in MST
    mst = []
    
    # Priority queue of edges (weight, src, dest)
    edges = [(weight, start_vertex, to) 
             for to, weight in graph[start_vertex].items()]
    heapq.heapify(edges)
    
    total_weight = 0
    
    # Continue until all vertices are in MST
    while edges and len(visited) < len(graph):
        weight, src, dest = heapq.heappop(edges)
        
        # Skip if destination already in MST
        if dest in visited:
            continue
            
        # Add edge to MST
        visited.add(dest)
        mst.append((src, dest, weight))
        total_weight += weight
        
        # Add edges from new vertex
        for next_dest, next_weight in graph[dest].items():
            if next_dest not in visited:
                heapq.heappush(edges, (next_weight, dest, next_dest))
                
    return mst, total_weight
```

### Time & Space Complexity

- **Time**: O(E log V) with binary heap implementation
- **Space**: O(V + E)

## Kruskal's Algorithm

Kruskal's algorithm also finds a minimum spanning tree for a weighted undirected graph, but uses a different approach from Prim's.

### Visualization

```
Original graph:
    A
   /|\
  4 7 1
 /  |  \
B---2---C
 \     /
  5   3
   \ /
    D

Sort edges by weight:
(A, C): 1
(B, C): 2
(C, D): 3
(A, B): 4
(B, D): 5
(A, D): 7

Add edges to MST in order (skipping if they create cycles):
(A, C): 1 - add
(B, C): 2 - add
(C, D): 3 - add
(A, B): 4 - add
(B, D): 5 - skip (creates cycle)
(A, D): 7 - skip (creates cycle)

Total weight: 10
```

### Implementation

```python
def kruskal(graph):
    # Edge list representation: (weight, src, dest)
    edges = []
    for src in graph:
        for dest, weight in graph[src].items():
            if src < dest:  # Add each edge only once
                edges.append((weight, src, dest))
                
    # Sort edges by weight
    edges.sort()
    
    # Track each vertex's parent for union-find
    parent = {v: v for v in graph}
    
    # Find function for union-find
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])  # Path compression
        return parent[v]
        
    # Union function
    def union(v1, v2):
        parent[find(v1)] = find(v2)
        
    mst = []
    total_weight = 0
    
    # Process edges in ascending weight order
    for weight, src, dest in edges:
        # Skip if adding edge would create cycle
        if find(src) != find(dest):
            union(src, dest)
            mst.append((src, dest, weight))
            total_weight += weight
            
    return mst, total_weight
```

### Time & Space Complexity

- **Time**: O(E log E) for sorting edges, which is O(E log V) since E ≤ V²
- **Space**: O(V + E)

## Topological Sort

Topological sorting arranges the vertices of a directed acyclic graph (DAG) in such a way that for every directed edge (u, v), vertex u comes before v in the ordering.

### Visualization

```
DAG:
A → B → C
↓   ↓
D → E

Possible topological orderings:
A, B, D, E, C
A, B, D, C, E
A, D, B, E, C
A, D, B, C, E
```

### Implementation (Kahn's Algorithm)

```python
from collections import defaultdict, deque

def topological_sort(graph):
    # Count incoming edges for each vertex
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1
            
    # Initialize queue with vertices that have no incoming edges
    queue = deque([u for u in graph if in_degree[u] == 0])
    
    result = []
    
    while queue:
        # Remove a vertex with no incoming edges
        u = queue.popleft()
        result.append(u)
        
        # Decrease in-degree of all adjacent vertices
        for v in graph[u]:
            in_degree[v] -= 1
            
            # If in-degree becomes 0, add to queue
            if in_degree[v] == 0:
                queue.append(v)
                
    # Check for cycle
    if len(result) != len(graph):
        return []  # Graph has a cycle
        
    return result
```

### DFS Approach

```python
def topological_sort_dfs(graph):
    visited = set()
    temp = set()  # For cycle detection
    result = []
    
    def dfs(u):
        # If vertex is in temp, we found a cycle
        if u in temp:
            return False
            
        # If already visited, skip
        if u in visited:
            return True
            
        temp.add(u)
        
        # Visit all neighbors
        for v in graph.get(u, []):
            if not dfs(v):
                return False
                
        # Remove from temp
        temp.remove(u)
        visited.add(u)
        
        # Add to result
        result.append(u)
        return True
        
    # Call DFS on all vertices
    for vertex in graph:
        if vertex not in visited:
            if not dfs(vertex):
                return []  # Graph has a cycle
                
    return result[::-1]  # Reverse for correct order
```

### Time & Space Complexity

- **Time**: O(V + E)
- **Space**: O(V)

### Applications

- **Dependency Resolution**: Course prerequisites, build systems
- **Task Scheduling**: Job scheduling with dependencies
- **Compile Order**: Determining order to compile files in a project

## Interview Tips

- **Dijkstra's Algorithm**:
  - Only works with non-negative edge weights
  - Use a priority queue to always process the next closest vertex
  - Can be modified to terminate early when the target is found

- **Prim's vs. Kruskal's**:
  - Both find a minimum spanning tree
  - Prim's grows a single tree from a starting point
  - Kruskal's manages a forest of trees, merging as it goes
  - Prim's is typically better for dense graphs
  - Kruskal's is typically better for sparse graphs

- **Topological Sort**:
  - Only works on directed acyclic graphs (DAGs)
  - Multiple valid orderings may exist
  - Great way to detect cycles in a directed graph

- **Edge Cases**:
  - Empty graphs
  - Disconnected graphs
  - Graphs with cycles (especially for topological sort)

## Common Interview Questions

1. Network Delay Time (LeetCode #743) - Dijkstra
2. Path with Minimum Effort (LeetCode #1631) - Dijkstra
3. Min Cost to Connect All Points (LeetCode #1584) - Prim's or Kruskal's
4. Course Schedule (LeetCode #207) - Cycle detection with topological sort
5. Course Schedule II (LeetCode #210) - Topological sort
6. Alien Dictionary (LeetCode #269) - Topological sort
7. Reconstruct Itinerary (LeetCode #332) - Eulerian path with topological ordering