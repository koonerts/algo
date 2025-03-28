# Linked Lists Algorithms Cheatsheet for SWE Interviews

## When to Use

- **Fast & Slow Pointers**: When detecting cycles, finding the middle node, or locating a node at a specific position from the end
- **Reversing Linked Lists**: When you need to reverse part or all of a linked list
- **Two Pointers**: When manipulating the linked list structure (removing elements, merging lists, etc.)
- **Merge Intervals**: When working with sorted linked lists that need to be combined
- **In-place Operations**: When you need to modify a linked list without using extra space
- **Recursive Solutions**: When traversing or modifying the list using the call stack
- **Dummy Head**: When the head of the list might change during operations
- **Stack/Queue Implementation**: When implementing these data structures using linked lists
- **LRU Cache**: When building a cache with linked list + hashmap for constant-time operations

## Fast & Slow Pointers Algorithm

The Fast & Slow pointers technique (also known as Floyd's Tortoise and Hare algorithm) uses two pointers moving at different speeds to solve various linked list problems efficiently.

### Step 1: Understanding the Pattern

Two pointers traverse the linked list:

- **Slow pointer**: Moves one step at a time
- **Fast pointer**: Moves two steps at a time

### Step 2: Visualization

For detecting a cycle in a linked list:

```
Initially:
1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycles back)
S    F

After 1 iteration:
1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycles back)
     S         F

After 2 iterations:
1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycles back)
          S              F

After 3 iterations:
1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycles back)
          S    F

Eventually they meet, confirming a cycle exists.
```

### Step 3: Basic Implementation

#### Cycle Detection

```python
def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # Move one step
        fast = fast.next.next     # Move two steps

        if slow == fast:          # Cycle detected
            return True

    return False  # Fast pointer reached end, no cycle
# Time: O(n), Space: O(1)
```

#### Finding Cycle Start

```python
def detect_cycle(head):
    if not head or not head.next:
        return None

    # Phase 1: Detect cycle using fast & slow
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # This is the start of the cycle
# Time: O(n), Space: O(1)
```

### Step 4: Common Variations

#### Finding Middle of Linked List

```python
def middle_node(head):
    if not head:
        return None

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # Middle node (or right middle for even length)
# Time: O(n), Space: O(1)
```

#### Checking if Linked List is Palindrome

```python
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    current = slow
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    # Compare first and second half
    first = head
    second = prev
    while second:  # Second half might be shorter
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True
# Time: O(n), Space: O(1)
```

#### Finding Nth Node From End

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head

    fast = slow = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        if not fast:
            return head  # n is larger than list length
        fast = fast.next

    # Move both pointers until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove nth node from end
    slow.next = slow.next.next

    return dummy.next
# Time: O(n), Space: O(1)
```

## Interview Tips

- **Time & Space Complexity**:
  - Most fast & slow pointer algorithms: O(n) time, O(1) space

- **Edge Cases**:
  - Empty list
  - Single node list
  - Lists with only two nodes
  - No cycle present (for cycle detection)

- **Common Patterns**:
  - Finding a midpoint or partition point
  - Detecting cycles
  - Finding kth element from end
  - Checking if list is a palindrome

- **Helpful Tricks**:
  - Using a dummy node at the start to handle edge cases
  - Resetting pointers to head for multi-phase algorithms
  - Drawing out the algorithm step by step to verify

## Common Interview Questions

1. Linked List Cycle (LeetCode #141)
2. Linked List Cycle II (LeetCode #142)
3. Middle of the Linked List (LeetCode #876)
4. Palindrome Linked List (LeetCode #234)
5. Remove Nth Node From End of List (LeetCode #19)
6. Reorder List (LeetCode #143)
7. Intersection of Two Linked Lists (LeetCode #160)

---

# Iterative Linked List Reversal Cheatsheet

## Step 1: Understanding Linked List Reversal

Reversing a linked list means changing the direction of all pointers:

- Original: `A -> B -> C -> D -> NULL`
- Reversed: `NULL <- A <- B <- C <- D`

### Visualization

```
Initial State:
NULL  1 -> 2 -> 3 -> 4 -> NULL
 ^    ^
prev  curr

Iteration 1:
NULL <- 1    2 -> 3 -> 4 -> NULL
       ^     ^
      prev  curr

Iteration 2:
NULL <- 1 <- 2    3 -> 4 -> NULL
            ^     ^
           prev  curr

Iteration 3:
NULL <- 1 <- 2 <- 3    4 -> NULL
                 ^     ^
                prev  curr

Final:
NULL <- 1 <- 2 <- 3 <- 4
                      ^
                     prev (new head)
```

## Step 2: Basic Implementation

```python
def reverse_list(head):
    prev = None
    current = head

    while current:
        # Store next node before changing pointer
        next_temp = current.next

        # Reverse the pointer
        current.next = prev

        # Move prev and current forward
        prev = current
        current = next_temp

    # prev is the new head
    return prev
# Time: O(n), Space: O(1)
```

## Step 3: Common Variations

### Reverse a Sublist (Between Positions m and n)

```python
def reverse_between(head, m, n):
    if not head or m == n:
        return head

    # Create a dummy node to handle case where m=1
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move to position m-1
    for _ in range(m - 1):
        prev = prev.next

    # Start reversal from position m
    current = prev.next
    tail = current  # Will become the last node of reversed section

    # Standard reversal logic for n-m+1 nodes
    for _ in range(n - m + 1):
        next_temp = current.next
        current.next = prev.next
        prev.next = current
        tail.next = next_temp
        current = next_temp

    return dummy.next
# Time: O(n), Space: O(1)
```

### Reverse Nodes in k-Group

```python
def reverse_k_group(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while True:
        # Check if there are k nodes left
        kth_node = get_kth(prev_group_end.next, k)
        if not kth_node:
            break

        next_group_start = kth_node.next

        # Reverse current k-group
        current = prev_group_end.next
        prev = kth_node.next

        while current != next_group_start:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        # Connect with previous group
        temp = prev_group_end.next
        prev_group_end.next = kth_node
        prev_group_end = temp

    return dummy.next

def get_kth(start, k):
    """Helper function to get kth node from start"""
    while start and k > 1:
        start = start.next
        k -= 1
    return start
# Time: O(n), Space: O(1)
```

## Interview Tips

- **Time & Space Complexity**:
  - Linked list reversal: O(n) time, O(1) space

- **Edge Cases**:
  - Empty list
  - Single node list
  - When reversing a sublist, watch bounds (m=1, m=n, etc.)

- **Common Patterns**:
  - Using a dummy node to simplify handling the head
  - Three-pointer technique (prev, current, next)
  - Tracking the original tail of reversed section

- **Step-by-Step Approach**:
  1. Draw out the list and pointers for each step
  2. Keep track of connections before and after the reversed part
  3. For partial reversals, identify the nodes that connect the reversed part to the rest of the list

## Common Interview Questions

1. Reverse Linked List (LeetCode #206)
2. Reverse Linked List II (LeetCode #92)
3. Reverse Nodes in k-Group (LeetCode #25)
4. Swap Nodes in Pairs (LeetCode #24)
5. Reorder List (LeetCode #143)
