# Trees Algorithms Cheatsheet for SWE Interviews

## When to Use

- **Trie (Prefix Tree)**: When working with string dictionaries, auto-complete, spell-checkers, or prefix matching
- **Union-Find (Disjoint Set)**: When tracking connected components, detecting cycles in undirected graphs, or in Kruskal's algorithm
- **Segment Tree**: When performing range queries (sum, min, max) with frequent updates to array elements
- **Binary Search Tree**: When you need ordered data with efficient insertion, deletion, and lookup
- **AVL/Red-Black Trees**: When you need a self-balancing search tree for guaranteed O(log n) operations
- **Binary Indexed Tree (Fenwick Tree)**: For efficient prefix sums and range sum queries with updates
- **Quadtree/Octree**: For spatial partitioning, collision detection, or image compression
- **Heap**: When you need to repeatedly find and remove the minimum/maximum element
- **B-Tree/B+ Tree**: When working with data too large to fit in memory (databases, file systems)
- **Decision Trees**: For classification, regression, and other machine learning applications

## Trie Data Structure

A trie (prefix tree) is a tree-like data structure used for efficient retrieval of keys in a dataset of strings.

### Visualization

```
        root
       /    \
      a      b
     / \     |
    p   c    e
   /     \    \
  p       t    d
 /
l
```

This trie stores: "apple", "act", "bed"

### Basic Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Maps character to TrieNode
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            # Create node if not exists
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### Common Operations

```python
# Delete a word
def delete(self, word):
    def _delete(node, word, depth=0):
        # Base case: reached end of word
        if depth == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
            return len(node.children) == 0

        char = word[depth]
        if char not in node.children:
            return False

        # Recursive delete in subtree
        should_delete_curr = _delete(node.children[char], word, depth + 1)

        # Delete current node's reference if child can be deleted and
        # current node is not end of another word
        if should_delete_curr:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word

        return False

    _delete(self.root, word)
```

### Time & Space Complexity

- **Insert**: O(m) time, where m is the length of the word
- **Search**: O(m) time
- **Delete**: O(m) time
- **Space**: O(n * m) where n is number of words and m is average length

## Union-Find (Disjoint Set)

Union-Find is used to track a set of elements partitioned into disjoint subsets, with efficient operations for:

1. Finding which set an element belongs to
2. Merging two sets

### Visualization

```
Initially: [0] [1] [2] [3] [4]  (Each element in its own set)

After Union(0,1) and Union(2,3):
[0,1] [2,3] [4]

After Union(1,2):
[0,1,2,3] [4]
```

### Basic Implementation

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Each element is its own parent initially
        self.rank = [0] * n           # Rank (approximate depth) for union by rank

    def find(self, x):
        # Find with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        # Merge smaller rank tree into larger
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True  # Union successful

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### Variations

```python
# Size-based Union-Find
class UnionFindSize:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n  # Size of each set
        self.count = n       # Number of components

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Always merge smaller set into larger
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        self.count -= 1  # One less component
        return True

    def get_size(self, x):
        return self.size[self.find(x)]
```

### Time & Space Complexity

- **Find**: Amortized O(α(n)) ≈ O(1) time where α is the inverse Ackermann function
- **Union**: Amortized O(α(n)) ≈ O(1) time
- **Space**: O(n)

## Segment Tree

A segment tree is a binary tree used for range queries and updates on arrays.

### Visualization

For array [1, 3, 5, 7, 9, 11]:

```
                [36]            // Sum of range [0-5]
              /      \
          [9]          [27]     // Sums of [0-2] and [3-5]
        /     \      /     \
     [4]     [5]    [16]   [11] // Smaller ranges
    /   \    /  \   /  \
  [1]  [3] [5]  [] [7] [9]      // Individual elements
```

### Basic Implementation (Sum Segment Tree)

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        # Size of segment tree: 2*2^ceil(log2(n)) - 1
        self.tree = [0] * (4 * self.n)  # 4n is a safe upper bound
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            # Leaf node
            self.tree[node] = arr[start]
            return

        mid = (start + end) // 2
        # Build left and right subtrees
        self.build(arr, 2 * node + 1, start, mid)
        self.build(arr, 2 * node + 2, mid + 1, end)

        # Internal node has sum of both children
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index, value, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1

        if start == end:
            # Leaf node
            self.tree[node] = value
            return

        mid = (start + end) // 2

        if index <= mid:
            # Update in left subtree
            self.update(index, value, 2 * node + 1, start, mid)
        else:
            # Update in right subtree
            self.update(index, value, 2 * node + 2, mid + 1, end)

        # Update current node
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query_sum(self, left, right, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1

        # No overlap
        if left > end or right < start:
            return 0

        # Complete overlap
        if left <= start and right >= end:
            return self.tree[node]

        # Partial overlap - query both children
        mid = (start + end) // 2
        left_sum = self.query_sum(left, right, 2 * node + 1, start, mid)
        right_sum = self.query_sum(left, right, 2 * node + 2, mid + 1, end)

        return left_sum + right_sum
```

### Variations

```python
# Minimum Segment Tree
def build_min(self, arr, node, start, end):
    if start == end:
        self.tree[node] = arr[start]
        return

    mid = (start + end) // 2
    self.build_min(arr, 2 * node + 1, start, mid)
    self.build_min(arr, 2 * node + 2, mid + 1, end)

    self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

def query_min(self, left, right, node=0, start=0, end=None):
    if end is None:
        end = self.n - 1

    if left > end or right < start:
        return float('inf')  # Identity for min

    if left <= start and right >= end:
        return self.tree[node]

    mid = (start + end) // 2
    left_min = self.query_min(left, right, 2 * node + 1, start, mid)
    right_min = self.query_min(left, right, 2 * node + 2, mid + 1, end)

    return min(left_min, right_min)
```

### Time & Space Complexity

- **Build**: O(n) time
- **Query**: O(log n) time
- **Update**: O(log n) time
- **Space**: O(n)

## Iterative DFS (Depth-First Search)

While recursive DFS is common for trees, iterative DFS is often preferred in interviews to avoid potential stack overflow.

### Basic Implementation - Preorder Traversal

```python
def preorder_iterative(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

### Inorder Traversal

```python
def inorder_iterative(root):
    result = []
    stack = []
    curr = root

    while curr or stack:
        # Go left as far as possible
        while curr:
            stack.append(curr)
            curr = curr.left

        # Process current node and go right
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result
```

### Postorder Traversal

```python
def postorder_iterative(root):
    if not root:
        return []

    result = []
    stack = [(root, False)]  # (node, visited_right)

    while stack:
        node, visited_right = stack.pop()

        if visited_right:
            # Both children processed
            result.append(node.val)
        else:
            # Push current node again with flag
            stack.append((node, True))

            # Push right then left (LIFO)
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return result

# Alternative approach using two stacks
def postorder_two_stacks(root):
    if not root:
        return []

    result = []
    s1 = [root]
    s2 = []

    # First stack helps us process nodes in reverse postorder
    while s1:
        node = s1.pop()
        s2.append(node)

        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    # Second stack gives us the postorder
    while s2:
        result.append(s2.pop().val)

    return result
```

### Time & Space Complexity

- **Time**: O(n) where n is the number of nodes
- **Space**: O(h) where h is the height of the tree (worst case O(n))

## Interview Tips

- **Trie**:
  - Great for prefix matching problems
  - Often used for autocomplete, spell checkers
  - Optimize space by removing unnecessary nodes (only create children when needed)

- **Union-Find**:
  - Excellent for dynamic connectivity problems
  - Path compression + union by rank gives nearly constant-time operations
  - Be careful with 0 vs 1-indexed arrays

- **Segment Tree**:
  - Consider lazy propagation for range updates
  - Can be adapted for different operations (sum, min, max, GCD)
  - Understand the requirements before deciding on implementation

- **Iterative DFS**:
  - Highlight to interviewer that it avoids stack overflow
  - Often clearer for complex traversal patterns
  - Use explicit stack to simulate the recursive call stack

## Common Interview Questions

1. Implement Trie (LeetCode #208)
2. Word Search II (LeetCode #212) - Trie
3. Number of Islands II (LeetCode #305) - Union-Find
4. Graph Valid Tree (LeetCode #261) - Union-Find
5. Range Sum Query - Mutable (LeetCode #307) - Segment Tree
6. Kth Largest Element in an Array (LeetCode #215) - Segment Tree approach
7. Binary Tree Inorder Traversal (LeetCode #94) - Iterative approach
8. Binary Search Tree Iterator (LeetCode #173) - Iterative traversal
