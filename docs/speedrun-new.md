# Speedrun ⚡💨

## What is Speedrun?

To quote Wikipedia:

> Speedrunning is the act of playing a video game, or section of a video game, with the goal of completing it as fast as possible. Speedrunning often involves following planned routes, which may incorporate sequence breaking and can exploit glitches that allow sections to be skipped or completed more quickly than intended.

AlgoMonster's Speedrun feature is designed to help you go through as many questions as quickly as possible. It is the third step of the 3-step system. Instead of writing code for each problem, you will be given a multiple choice related to the techniques and templates used to solve the problem. This cuts down the time to go through many problems significantly.

## Why Speedrun?

- **Train your intuition**: In a real interview, you will be spending at least half the time identifying the algorithm to solve the question and explaining your approach to the interviewer.
- **Reinforces your learning**: Going through a few more problems after learning the patterns and templates reinforces what you've learned. Seeing many problems helps train your "intuition" when faced with a new problem.
- **Increase your luck**: There are only so many problems out there. The more you see, the greater chance you may encounter a problem at a real interview. You never know!
- **Most importantly, it saves you time!** You can go through many more problems in a shorter amount of time.

## Speedrun Questions

---

## Array Patterns

### Sliding Window Pattern

#### Problem 1: Maximum Average Subarray

Given an array of integers and an integer k, find the maximum average value of any contiguous subarray of length k.

Example 1:
```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```

Example 2:
```
Input: nums = [5], k = 1
Output: 5.00
```

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

**Question**: Which of the following implementations correctly finds the maximum average of a contiguous subarray of length k?

```python
def findMaxAverage(nums, k):
    # Calculate the sum of first k elements
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
    # Slide the window and update the maximum sum
    for i in range(k, len(nums)):
        ### YOUR IMPLEMENTATION HERE ###
        
    return max_sum / k
```

- [ ] ```
    current_sum += nums[i] - nums[i-1]
    max_sum = max(max_sum, current_sum)
    ```

- [ ] ```
    current_sum = current_sum - nums[i-k] + nums[i]
    max_sum = max(max_sum, current_sum)
    ```

- [ ] ```
    window_sum = sum(nums[i-k+1:i+1])
    max_sum = max(max_sum, window_sum) 
    ```

- [ ] ```
    current_sum += nums[i]
    if i >= k:
        current_sum -= nums[i-k]
    max_sum = max(max_sum, current_sum)
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
current_sum = current_sum - nums[i-k] + nums[i]
max_sum = max(max_sum, current_sum)
```

This implementation correctly slides the window by removing the first element of the previous window and adding the next element of the array. We then update the maximum sum found so far.

The time complexity is O(n) and the space complexity is O(1), which makes it efficient for large arrays.
</details>

---

#### Problem 2: Minimum Size Subarray Sum

Given an array of positive integers `nums` and a positive integer `target`, find the minimal length of a contiguous subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

Example 1:
```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

Example 2:
```
Input: target = 4, nums = [1,4,4]
Output: 1
```

Example 3:
```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

**Question**: Select the correct implementation of a sliding window algorithm to find the minimum size subarray with sum at least `target`.

```python
def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        # Expand window
        current_sum += nums[right]
        
        # Shrink window if possible
        ### YOUR IMPLEMENTATION HERE ###
            
    return min_length if min_length != float('inf') else 0
```

- [ ] ```
    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= nums[left]
        left += 1
    ```

- [ ] ```
    if current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= nums[left]
        left += 1
    ```

- [ ] ```
    if current_sum >= target:
        min_length = min(min_length, right - left + 1)
    ```

- [ ] ```
    for left in range(len(nums)):
        if current_sum >= target:
            min_length = min(min_length, right - left + 1)
            break
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
while current_sum >= target:
    min_length = min(min_length, right - left + 1)
    current_sum -= nums[left]
    left += 1
```

This implementation continuously shrinks the window from the left side as long as the current sum is greater than or equal to the target. For each valid window, we update the minimum length. This ensures we find the smallest possible window that satisfies the condition.

The time complexity is O(n) as each element is processed at most twice (added and removed from the window once). The space complexity is O(1).
</details>

---

### Two Pointers Pattern

#### Problem 3: Container With Most Water

You are given an integer array `height` of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water (area). Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The container bordered by height indices 1 and 8 (0-indexed) contains 49 units of water.
```

Example 2:
```
Input: height = [1,1]
Output: 1
```

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

**Question**: Which implementation of the two-pointer approach correctly calculates the maximum area of water the container can hold?

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        ### YOUR IMPLEMENTATION HERE ###
        
    return max_area
```

- [ ] ```
    area = min(height[left], height[right]) * (right - left)
    max_area = max(max_area, area)
    if height[left] <= height[right]:
        left += 1
    else:
        right -= 1
    ```

- [ ] ```
    area = max(height[left], height[right]) * (right - left)
    max_area = max(max_area, area)
    if height[left] <= height[right]:
        left += 1
    else:
        right -= 1
    ```

- [ ] ```
    area = min(height[left], height[right]) * (right - left)
    max_area = max(max_area, area)
    left += 1
    right -= 1
    ```

- [ ] ```
    area = min(height[left], height[right]) * (right - left)
    max_area = max(max_area, area)
    if height[left] <= height[right]:
        right -= 1
    else:
        left += 1
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
area = min(height[left], height[right]) * (right - left)
max_area = max(max_area, area)
if height[left] <= height[right]:
    left += 1
else:
    right -= 1
```

The area of water contained is determined by the minimum height of the two boundaries multiplied by the distance between them. To maximize the area, we should try to maintain the higher boundary and move the shorter one, because:
1. The width decreases with each step
2. Moving the higher boundary can only result in the same or smaller area
3. Moving the shorter boundary gives a chance to find a taller boundary that might increase the area

The time complexity is O(n) where n is the length of the height array, and the space complexity is O(1).
</details>

---

#### Problem 4: Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are trapped.
```

Example 2:
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

**Question**: Which implementation correctly uses the two-pointer technique to calculate water trapped between bars?

```python
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    
    while left < right:
        ### YOUR IMPLEMENTATION HERE ###
        
    return water
```

- [ ] ```
    if height[left] < height[right]:
        left_max = max(left_max, height[left])
        water += left_max - height[left]
        left += 1
    else:
        right_max = max(right_max, height[right])
        water += right_max - height[right]
        right -= 1
    ```

- [ ] ```
    left_max = max(left_max, height[left])
    right_max = max(right_max, height[right])
    if left_max < right_max:
        water += left_max - height[left]
        left += 1
    else:
        water += right_max - height[right]
        right -= 1
    ```

- [ ] ```
    if height[left] < height[right]:
        water += max(0, min(left_max, right_max) - height[left])
        left += 1
    else:
        water += max(0, min(left_max, right_max) - height[right])
        right -= 1
    ```

- [ ] ```
    water += max(0, min(height[left], height[right]) - min(height[left:right+1]))
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
if height[left] < height[right]:
    left_max = max(left_max, height[left])
    water += left_max - height[left]
    left += 1
else:
    right_max = max(right_max, height[right])
    water += right_max - height[right]
    right -= 1
```

This solution uses the two-pointer approach efficiently. The key insight is:
1. We maintain two pointers (left and right) and their maximum heights seen so far
2. We always move the pointer pointing to the smaller height
3. If the current height is smaller than the maximum seen from that direction, we can trap water at that position equal to the difference

The time complexity is O(n) where n is the length of the height array, and the space complexity is O(1).
</details>

---

### Binary Search Pattern

#### Problem 5: Search in Rotated Sorted Array

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or -1 if it is not in `nums`.

Example 1:
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

Example 3:
```
Input: nums = [1], target = 0
Output: -1
```

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is possibly rotated at an unknown pivot index
- -10^4 <= target <= 10^4

**Question**: Which implementation correctly performs binary search in a rotated sorted array?

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        ### YOUR IMPLEMENTATION HERE ###
            
    return -1
```

- [ ] ```
    if nums[left] <= nums[mid]:  # Left portion is sorted
        if nums[left] <= target <= nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:  # Right portion is sorted
        if nums[mid] <= target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    ```

- [ ] ```
    if nums[left] <= nums[mid]:  # Left portion is sorted
        if nums[left] <= target and target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:  # Right portion is sorted
        if nums[mid] < target and target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    ```

- [ ] ```
    if nums[mid] <= nums[right]:  # Right portion is sorted
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    else:  # Left portion is sorted
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    ```

- [ ] ```
    if target > nums[mid]:
        left = mid + 1
    else:
        right = mid - 1
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
if nums[left] <= nums[mid]:  # Left portion is sorted
    if nums[left] <= target and target < nums[mid]:
        right = mid - 1
    else:
        left = mid + 1
else:  # Right portion is sorted
    if nums[mid] < target and target <= nums[right]:
        left = mid + 1
    else:
        right = mid - 1
```

This implementation correctly handles the rotated sorted array by first determining which half of the array is sorted. Then it checks if the target lies within the sorted portion:
1. If the left half is sorted, check if target is in that range
2. If the right half is sorted, check if target is in that range
3. Move the pointers accordingly to eliminate the half that doesn't contain the target

The time complexity is O(log n) and the space complexity is O(1).
</details>

---

#### Problem 6: Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

Example 3:
```
Input: nums = [], target = 0
Output: [-1,-1]
```

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array
- -10^9 <= target <= 10^9

**Question**: You need to find the first and last position of `target` in a sorted array using binary search. Which implementation correctly finds the first occurrence of the target?

```python
def searchRange(nums, target):
    def find_first():
        left, right = 0, len(nums) - 1
        first_pos = -1
        
        while left <= right:
            mid = (left + right) // 2
            ### YOUR IMPLEMENTATION HERE ###
                
        return first_pos
    
    # Implementation for finding last position and overall solution not shown
```

- [ ] ```
    if nums[mid] == target:
        first_pos = mid
        return first_pos
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
    ```

- [ ] ```
    if nums[mid] == target:
        first_pos = mid
        right = mid - 1
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
    ```

- [ ] ```
    if nums[mid] == target:
        first_pos = mid
        left = mid + 1
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
    ```

- [ ] ```
    if nums[mid] == target:
        if mid == 0 or nums[mid-1] != target:
            return mid
        right = mid - 1
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
if nums[mid] == target:
    first_pos = mid
    right = mid - 1
elif nums[mid] < target:
    left = mid + 1
else:
    right = mid - 1
```

This implementation correctly finds the first occurrence of the target by continuing to search to the left even after finding a match. Key points:
1. When we find a target match, we update `first_pos` to store the current position
2. We still continue searching in the left half (setting `right = mid - 1`) to find potentially earlier occurrences
3. If the mid value is less than target, we search in the right half
4. If the mid value is greater than target, we search in the left half

This ensures we find the leftmost occurrence of the target in O(log n) time.
</details>

---

### Kadane's Algorithm

#### Problem 7: Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

Example 2:
```
Input: nums = [1]
Output: 1
```

Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
```

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

**Question**: Which implementation correctly uses Kadane's algorithm to find the maximum subarray sum?

```python
def maxSubArray(nums):
    ### YOUR IMPLEMENTATION HERE ###
    return max_sum
```

- [ ] ```
    max_sum = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            max_sum = max(max_sum, sum(nums[i:j+1]))
    return max_sum
    ```

- [ ] ```
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
    ```

- [ ] ```
    max_sum = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)
    return max_sum
    ```

- [ ] ```
    max_sum = float('-inf')
    for window_size in range(1, len(nums) + 1):
        for i in range(len(nums) - window_size + 1):
            max_sum = max(max_sum, sum(nums[i:i+window_size]))
    return max_sum
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
max_sum = current_sum = nums[0]
for num in nums[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)
return max_sum
```

This is the correct implementation of Kadane's algorithm. The key insights are:
1. We track two variables: `current_sum` (the maximum sum ending at the current position) and `max_sum` (the global maximum subarray sum)
2. For each number, we decide whether to start a new subarray (`num`) or extend the previous subarray (`current_sum + num`)
3. We update the global maximum if the current sum is larger

This handles negative numbers correctly and works when the array contains all negative numbers.

The time complexity is O(n) and the space complexity is O(1).
</details>

---

## Linked List Patterns

### Fast & Slow Pointers

#### Problem 8: Linked List Cycle

Given the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

Example 1:
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

Example 2:
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

Example 3:
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

Constraints:
- The number of the nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list

**Question**: Which implementation correctly uses the fast and slow pointer technique to detect a cycle in a linked list?

```python
def hasCycle(head):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False
    ```

- [ ] ```
    if not head or not head.next:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
    ```

- [ ] ```
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    ```

- [ ] ```
    slow = head
    if not head or not head.next:
        return False
    fast = head.next
    while slow != fast:
        slow = slow.next
        if not fast or not fast.next:
            return False
        fast = fast.next
    return True
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

This implementation correctly uses the Floyd's Cycle-Finding Algorithm (also known as the "tortoise and hare" algorithm):
1. Initialize both `slow` and `fast` pointers to the head
2. Move `slow` one step and `fast` two steps at a time
3. If there's a cycle, the fast pointer will eventually catch up to the slow pointer
4. If there's no cycle, the fast pointer will reach the end of the list (null)

The time complexity is O(n) where n is the number of nodes in the linked list. The space complexity is O(1) as we're only using two pointers regardless of the list size.
</details>

---

#### Problem 9: Find the Middle of Linked List

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

Example 2:
```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

Constraints:
- The number of nodes in the list is in the range [1, 100]
- 1 <= Node.val <= 100

**Question**: Which implementation correctly finds the middle node of a linked list using the fast and slow pointer technique?

```python
def middleNode(head):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    ```

- [ ] ```
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    return nodes[len(nodes) // 2]
    ```

- [ ] ```
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    ```

- [ ] ```
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    
    middle = count // 2
    current = head
    for _ in range(middle):
        current = current.next
    return current
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
```

This implementation efficiently finds the middle of a linked list using two pointers:
1. The `slow` pointer moves one step at a time
2. The `fast` pointer moves two steps at a time
3. When the `fast` pointer reaches the end of the list, the `slow` pointer will be at the middle

This works for both odd and even length lists. If the list has an even number of nodes, it returns the second middle node as required.

The time complexity is O(n) where n is the number of nodes in the linked list. The space complexity is O(1).
</details>

---

## Tree Patterns

### Tree Traversal

#### Problem 10: Binary Tree Level Order Traversal

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

Example 2:
```
Input: root = [1]
Output: [[1]]
```

Example 3:
```
Input: root = []
Output: []
```

Constraints:
- The number of nodes in the tree is in the range [0, 2000]
- -1000 <= Node.val <= 1000

**Question**: Which implementation correctly performs a level order traversal of a binary tree?

```python
def levelOrder(root):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level)
    
    return result
    ```

- [ ] ```
    if not root:
        return []
    
    result = []
    
    def dfs(node, level):
        if not node:
            return
        
        if len(result) <= level:
            result.append([])
        
        result[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return result
    ```

- [ ] ```
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return [result]
    ```

- [ ] ```
    if not root:
        return []
    
    result = []
    current_level = [root]
    
    while current_level:
        values = []
        next_level = []
        
        for node in current_level:
            values.append(node.val)
            
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        result.append(values)
        current_level = next_level
    
    return result
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
if not root:
    return []

result = []
current_level = [root]

while current_level:
    values = []
    next_level = []
    
    for node in current_level:
        values.append(node.val)
        
        if node.left:
            next_level.append(node.left)
        if node.right:
            next_level.append(node.right)
    
    result.append(values)
    current_level = next_level

return result
```

This implementation correctly performs a level-order traversal (BFS) of a binary tree:
1. It uses a list to track nodes at the current level
2. For each level, it processes all nodes, collects their values, and gathers their children for the next level
3. It maintains a separate array for each level's values

The time complexity is O(n) where n is the number of nodes in the tree. The space complexity is O(n) in the worst case.
</details>

---

### Depth-First Search (DFS)

#### Problem 11: Path Sum

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

A leaf is a node with no children.

Example 1:
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path 5->4->11->2 adds up to 22.
```

Example 2:
```
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There is no root-to-leaf path that adds up to 5.
```

Example 3:
```
Input: root = [1,2], targetSum = 1
Output: false
Explanation: The sum of the path 1->2 is 3, which does not equal 1.
```

Constraints:
- The number of nodes in the tree is in the range [0, 5000]
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

**Question**: Which implementation correctly determines if there's a path from root to leaf where the sum of values equals `targetSum`?

```python
def hasPathSum(root, targetSum):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    def dfs(node, current_sum):
        if not node:
            return False
        
        current_sum += node.val
        
        # If it's a leaf node, check if the sum matches
        if not node.left and not node.right:
            return current_sum == targetSum
        
        # Check left and right subtrees
        return dfs(node.left, current_sum) or dfs(node.right, current_sum)
    
    return dfs(root, 0)
    ```

- [ ] ```
    if not root:
        return False
    
    targetSum -= root.val
    
    # If it's a leaf and the remaining sum is 0, we found a valid path
    if not root.left and not root.right:
        return targetSum == 0
    
    # Check both subtrees
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
    ```

- [ ] ```
    stack = [(root, targetSum)]
    
    while stack:
        node, remaining = stack.pop()
        if not node:
            continue
        
        remaining -= node.val
        if not node.left and not node.right and remaining == 0:
            return True
        
        stack.append((node.right, remaining))
        stack.append((node.left, remaining))
    
    return False
    ```

- [ ] ```
    if not root:
        return targetSum == 0
    
    queue = [(root, root.val)]
    
    while queue:
        node, current_sum = queue.pop(0)
        
        if not node.left and not node.right and current_sum == targetSum:
            return True
        
        if node.left:
            queue.append((node.left, current_sum + node.left.val))
        if node.right:
            queue.append((node.right, current_sum + node.right.val))
    
    return False
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
if not root:
    return False

targetSum -= root.val

# If it's a leaf and the remaining sum is 0, we found a valid path
if not root.left and not root.right:
    return targetSum == 0

# Check both subtrees
return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
```

This implementation uses a recursive DFS approach that:
1. Subtracts the current node's value from the target sum
2. Checks if we've reached a leaf node and the remaining sum is 0
3. Recursively checks the left and right subtrees

The approach is elegant and concise while correctly handling all edge cases.

The time complexity is O(n) where n is the number of nodes in the tree. The space complexity is O(h) where h is the height of the tree due to the recursion stack.
</details>

---

## Graph Patterns

### Breadth-First Search (BFS)

#### Problem 12: Number of Islands

Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

Example 2:
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

**Question**: Which implementation correctly counts the number of islands using BFS?

```python
def numIslands(grid):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                grid[i][j] = '0'  # Mark as visited
                
                # BFS to find all connected land cells
                queue = [(i, j)]
                while queue:
                    row, col = queue.pop(0)
                    
                    # Check all 4 adjacent cells
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if (0 <= r < rows and 0 <= c < cols and
                            grid[r][c] == '1'):
                            queue.append((r, c))
                            grid[r][c] = '0'  # Mark as visited
    
    return count
    ```

- [ ] ```
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    visited = set()
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and (i, j) not in visited:
                count += 1
                queue = [(i, j)]
                visited.add((i, j))
                
                while queue:
                    row, col = queue.pop(0)
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if (0 <= r < rows and 0 <= c < cols and
                            grid[r][c] == '1' and (r, c) not in visited):
                            queue.append((r, c))
                            visited.add((r, c))
    
    return count
    ```

- [ ] ```
    def dfs(grid, i, j):
        if (i < 0 or i >= len(grid) or
            j < 0 or j >= len(grid[0]) or
            grid[i][j] == '0'):
            return
        
        grid[i][j] = '0'  # Mark as visited
        
        # Check all 4 adjacent cells
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)
    
    if not grid:
        return 0
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j)
    
    return count
    ```

- [ ] ```
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    visited = set()
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < rows and 0 <= nj < cols and 
                        grid[ni][nj] == '1'):
                        grid[ni][nj] = '0'  # Mark as visited
    
    return count
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
if not grid:
    return 0

rows, cols = len(grid), len(grid[0])
count = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '1':
            count += 1
            grid[i][j] = '0'  # Mark as visited
            
            # BFS to find all connected land cells
            queue = [(i, j)]
            while queue:
                row, col = queue.pop(0)
                
                # Check all 4 adjacent cells
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows and 0 <= c < cols and
                        grid[r][c] == '1'):
                        queue.append((r, c))
                        grid[r][c] = '0'  # Mark as visited

return count
```

This implementation correctly uses BFS to count islands by:
1. Iterating through each cell in the grid
2. When a land cell ('1') is found, incrementing the island count
3. Using BFS to explore all connected land cells and mark them as visited
4. Continuing the process until all cells have been checked

The time complexity is O(m×n) where m is the number of rows and n is the number of columns. The space complexity is O(min(m,n)) in the worst case for the queue.
</details>

---

### Depth-First Search (DFS)

#### Problem 13: Course Schedule

There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return `true` if you can finish all courses. Otherwise, return `false`.

Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are 2 courses to take. To take course 1 you should have finished course 0.
```

Example 2:
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should have finished course 1. This is impossible.
```

Constraints:
- 1 <= numCourses <= 10^5
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs [ai, bi] are distinct

**Question**: Which implementation correctly determines if it's possible to finish all courses using DFS to detect cycles?

```python
def canFinish(numCourses, prerequisites):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    # Build adjacency list
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    visited = [0] * numCourses
    
    def dfs(course):
        # If currently visiting this node, we found a cycle
        if visited[course] == 1:
            return False
        
        # If already visited and found no cycle, skip
        if visited[course] == 2:
            return True
        
        # Mark as currently visiting
        visited[course] = 1
        
        # Visit all prerequisites
        for prereq in graph[course]:
            if not dfs(prereq):
                return False
        
        # Mark as completely visited
        visited[course] = 2
        return True
    
    # Check all courses
    for course in range(numCourses):
        if not dfs(course):
            return False
    
    return True
    ```

- [ ] ```
    # Build adjacency list
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    visited = [0] * numCourses
    
    def dfs(course):
        # If currently visiting this node, we found a cycle
        if visited[course] == 1:
            return False
        
        # If already visited and found no cycle, skip
        if visited[course] == 2:
            return True
        
        # Mark as currently visiting
        visited[course] = 1
        
        # Visit all dependent courses
        for next_course in graph[course]:
            if not dfs(next_course):
                return False
        
        # Mark as completely visited
        visited[course] = 2
        return True
    
    # Check all courses
    for course in range(numCourses):
        if not dfs(course):
            return False
    
    return True
    ```

- [ ] ```
    # Count in-degrees for each course
    in_degree = [0] * numCourses
    graph = [[] for _ in range(numCourses)]
    
    # Build graph and count in-degrees
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Start with courses that have no prerequisites
    queue = [course for course in range(numCourses) if in_degree[course] == 0]
    
    # Process courses
    courses_taken = 0
    while queue:
        current = queue.pop(0)
        courses_taken += 1
        
        # Update in-degrees of dependent courses
        for next_course in graph[current]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return courses_taken == numCourses
    ```

- [ ] ```
    # Build adjacency matrix
    matrix = [[False] * numCourses for _ in range(numCourses)]
    for course, prereq in prerequisites:
        matrix[course][prereq] = True
    
    # Floyd-Warshall algorithm to find cycles
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
    
    # Check for cycles (a course depends on itself)
    for i in range(numCourses):
        if matrix[i][i]:
            return False
    
    return True
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
# Build adjacency list
graph = [[] for _ in range(numCourses)]
for course, prereq in prerequisites:
    graph[prereq].append(course)

# 0 = unvisited, 1 = visiting, 2 = visited
visited = [0] * numCourses

def dfs(course):
    # If currently visiting this node, we found a cycle
    if visited[course] == 1:
        return False
    
    # If already visited and found no cycle, skip
    if visited[course] == 2:
        return True
    
    # Mark as currently visiting
    visited[course] = 1
    
    # Visit all dependent courses
    for next_course in graph[course]:
        if not dfs(next_course):
            return False
    
    # Mark as completely visited
    visited[course] = 2
    return True

# Check all courses
for course in range(numCourses):
    if not dfs(course):
        return False

return True
```

This implementation correctly:
1. Builds a directed graph where an edge from course A to course B means B depends on A
2. Uses DFS with three states (unvisited, visiting, visited) to detect cycles
3. If a cycle is found, returns false as it's impossible to complete all courses
4. If no cycle is found, returns true

The time complexity is O(V+E) where V is the number of courses and E is the number of prerequisites. The space complexity is O(V+E) for the graph and visited array.
</details>

---

## Dynamic Programming Patterns

### 0/1 Knapsack Pattern

#### Problem 14: Partition Equal Subset Sum

Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

Example 2:
```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

**Question**: Which implementation correctly determines if the array can be partitioned into two equal-sum subsets using dynamic programming?

```python
def canPartition(nums):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    total_sum = sum(nums)
    
    # If the total sum is odd, we can't partition into equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # dp[i][j] = can we make sum j using the first i elements
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Base case: we can always make sum 0 with any number of elements
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < nums[i-1]:
                # If current number is greater than current sum
                # We can't include it, so use previous result
                dp[i][j] = dp[i-1][j]
            else:
                # Either include current number or exclude it
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
    return dp[n][target]
    ```

- [ ] ```
    total_sum = sum(nums)
    
    # If the total sum is odd, we can't partition into equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    
    # dp[j] = can we make sum j
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        # We need to iterate backwards to avoid using the same element multiple times
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]
    ```

- [ ] ```
    total_sum = sum(nums)
    
    # If the total sum is odd, we can't partition into equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    memo = {}
    
    def dfs(index, remaining):
        # Base case: found a valid subset
        if remaining == 0:
            return True
        
        # Base case: out of bounds or remaining is negative
        if index >= len(nums) or remaining < 0:
            return False
        
        # Use memoization
        if (index, remaining) in memo:
            return memo[(index, remaining)]
        
        # Either include the current number or skip it
        memo[(index, remaining)] = (dfs(index + 1, remaining - nums[index]) or 
                                  dfs(index + 1, remaining))
        
        return memo[(index, remaining)]
    
    return dfs(0, target)
    ```

- [ ] ```
    total_sum = sum(nums)
    
    # If the total sum is odd, we can't partition into equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = set([0])
    
    for num in nums:
        next_dp = dp.copy()
        for val in dp:
            next_dp.add(val + num)
        dp = next_dp
    
    return target in dp
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
total_sum = sum(nums)

# If the total sum is odd, we can't partition into equal subsets
if total_sum % 2 != 0:
    return False

target = total_sum // 2

# dp[j] = can we make sum j
dp = [False] * (target + 1)
dp[0] = True

for num in nums:
    # We need to iterate backwards to avoid using the same element multiple times
    for j in range(target, num - 1, -1):
        dp[j] = dp[j] or dp[j - num]

return dp[target]
```

This implementation efficiently solves the problem using a 1D DP approach:
1. It first checks if the total sum is odd (which would make equal partitioning impossible)
2. It uses a boolean DP array where dp[j] represents whether a subset with sum j is possible
3. For each number, it iterates through the DP array backwards to avoid counting the same number multiple times
4. It returns whether a subset with sum equal to half the total is possible

The time complexity is O(n*target) where n is the length of nums and target is half the sum of all elements. The space complexity is O(target).
</details>

---

### Fibonacci Sequence Pattern

#### Problem 15: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

Example 2:
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

Constraints:
- 1 <= n <= 45

**Question**: Which implementation correctly calculates the number of ways to climb the stairs using a Fibonacci-like dynamic programming approach?

```python
def climbStairs(n):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Calculate using recursion with memoization
    memo = {}
    
    def dp(i):
        if i <= 0:
            return 0
        if i == 1:
            return 1
        if i == 2:
            return 2
        
        if i in memo:
            return memo[i]
        
        memo[i] = dp(i-1) + dp(i-2)
        return memo[i]
    
    return dp(n)
    ```

- [ ] ```
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Calculate using iterative approach
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    
    return b
    ```

- [ ] ```
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    # Calculate using DP array
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
    ```

- [ ] ```
    # Calculate using binomial coefficients
    ways = 0
    for i in range(n // 2 + 1):
        # Choose i positions for 2-steps out of n-i total steps
        from math import comb
        ways += comb(n - i, i)
    
    return ways
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
# Base cases
if n <= 0:
    return 0
if n == 1:
    return 1
if n == 2:
    return 2

# Calculate using iterative approach
a, b = 1, 2
for _ in range(3, n+1):
    a, b = b, a + b

return b
```

This implementation uses the Fibonacci pattern efficiently:
1. It handles the base cases directly
2. For larger n, it uses an iterative approach with just two variables
3. In each iteration, it updates these variables in a Fibonacci-like sequence
4. It returns the final value which represents the number of ways to climb n stairs

The time complexity is O(n) and the space complexity is O(1), making it very efficient compared to the recursive or array-based approaches.
</details>

---

## Backtracking Patterns

### Subsets Pattern

#### Problem 16: Subsets

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

Example 2:
```
Input: nums = [0]
Output: [[],[0]]
```

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique

**Question**: Which implementation correctly generates all subsets using backtracking?

```python
def subsets(nums):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    result = []
    
    def backtrack(start, current):
        # Add the current subset to the result
        result.append(current[:])
        
        # Generate all other subsets by adding one more element
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
    ```

- [ ] ```
    result = [[]]
    
    for num in nums:
        result += [curr + [num] for curr in result]
    
    return result
    ```

- [ ] ```
    n = len(nums)
    result = []
    
    # Generate all subsets using bit manipulation
    for i in range(1 << n):  # 2^n combinations
        subset = []
        for j in range(n):
            # Check if jth bit is set in i
            if i & (1 << j):
                subset.append(nums[j])
        result.append(subset)
    
    return result
    ```

- [ ] ```
    def recursive_subsets(index):
        if index == len(nums):
            return [[]]
        
        # Generate all subsets without current element
        subsets_without = recursive_subsets(index + 1)
        
        # Generate all subsets with current element
        subsets_with = []
        for subset in subsets_without:
            subsets_with.append(subset + [nums[index]])
        
        # Combine them
        return subsets_without + subsets_with
    
    return recursive_subsets(0)
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
result = []

def backtrack(start, current):
    # Add the current subset to the result
    result.append(current[:])
    
    # Generate all other subsets by adding one more element
    for i in range(start, len(nums)):
        current.append(nums[i])
        backtrack(i + 1, current)
        current.pop()

backtrack(0, [])
return result
```

This implementation uses backtracking to generate all possible subsets:
1. It maintains a current subset and adds it to the result at each step
2. It uses a start index to ensure elements are only considered once and in order
3. For each element, it tries both including and excluding it in the current subset
4. It uses backtracking to undo choices and explore all possibilities

The time complexity is O(n * 2^n) where n is the length of nums, as there are 2^n subsets and each may take O(n) time to process. The space complexity is O(n) for the recursion stack.
</details>

---

## Heap Patterns

### Top K Elements Pattern

#### Problem 17: Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

Example 2:
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

Constraints:
- 1 <= k <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4

**Question**: Which implementation efficiently finds the kth largest element in an array using a heap?

```python
def findKthLargest(nums, k):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    nums.sort()
    return nums[len(nums) - k]
    ```

- [ ] ```
    import heapq
    
    # Use a min heap of size k
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    
    return heap[0]
    ```

- [ ] ```
    import heapq
    
    # Build a max heap (by negating values)
    heap = [-num for num in nums]
    heapq.heapify(heap)
    
    # Pop k-1 elements
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    # Return the kth largest
    return -heapq.heappop(heap)
    ```

- [ ] ```
    # Use QuickSelect algorithm
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # Move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # Move elements smaller than pivot to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # Move pivot to its final place
        nums[store_index], nums[right] = nums[right], nums[store_index]
        return store_index
    
    def select(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        # Choose a random pivot
        import random
        pivot_index = random.randint(left, right)
        
        # Find the pivot position in a sorted array
        pivot_index = partition(left, right, pivot_index)
        
        # If the pivot is in the right position
        if k_smallest == pivot_index:
            return nums[k_smallest]
        # If the pivot is larger than k_smallest
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        # If the pivot is smaller than k_smallest
        else:
            return select(pivot_index + 1, right, k_smallest)
    
    # Find the kth largest element
    return select(0, len(nums) - 1, len(nums) - k)
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
import heapq

# Use a min heap of size k
heap = []
for num in nums:
    if len(heap) < k:
        heapq.heappush(heap, num)
    elif num > heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, num)

return heap[0]
```

This implementation efficiently finds the kth largest element using a min-heap of size k:
1. It maintains a min-heap with the k largest elements seen so far
2. For each new element, if it's larger than the smallest element in the heap, it replaces it
3. After processing all elements, the smallest element in the heap is the kth largest element

The time complexity is O(n log k) where n is the length of nums and k is the given parameter. The space complexity is O(k) for the heap.

This approach is particularly efficient when k is much smaller than n.
</details>

---

## Stack & Queue Patterns

### Stack Applications

#### Problem 18: Valid Parentheses

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
```
Input: s = "()"
Output: true
```

Example 2:
```
Input: s = "()[]{}"
Output: true
```

Example 3:
```
Input: s = "(]"
Output: false
```

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

**Question**: Which implementation correctly checks if a string has valid parentheses using a stack?

```python
def isValid(s):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    stack = []
    
    # Map closing brackets to their opening counterparts
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty or brackets don't match
            if not stack or mapping[char] != stack.pop():
                return False
    
    # Valid if stack is empty (all brackets matched)
    return len(stack) == 0
    ```

- [ ] ```
    # Count opening and closing brackets
    count_parentheses = 0
    count_brackets = 0
    count_braces = 0
    
    for char in s:
        if char == '(':
            count_parentheses += 1
        elif char == ')':
            count_parentheses -= 1
        elif char == '[':
            count_brackets += 1
        elif char == ']':
            count_brackets -= 1
        elif char == '{':
            count_braces += 1
        elif char == '}':
            count_braces -= 1
        
        # If any count becomes negative, brackets are not matched
        if count_parentheses < 0 or count_brackets < 0 or count_braces < 0:
            return False
    
    # Valid if all counts are 0
    return count_parentheses == 0 and count_brackets == 0 and count_braces == 0
    ```

- [ ] ```
    # Replace matched pairs until no more replacements can be made
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    
    # Valid if no brackets remain
    return s == ''
    ```

- [ ] ```
    def check(s, left, right):
        if left >= right:
            return True
        
        # Find matching closing bracket
        if s[left] == '(':
            match = ')'
        elif s[left] == '[':
            match = ']'
        elif s[left] == '{':
            match = '}'
        else:
            return False
        
        # Find matching closing bracket position
        nested = 1
        for i in range(left + 1, right + 1):
            if s[i] == s[left]:
                nested += 1
            elif s[i] == match:
                nested -= 1
                if nested == 0:
                    # Check substring validity
                    return check(s, left + 1, i - 1) and check(s, i + 1, right)
        
        return False
    
    return check(s, 0, len(s) - 1)
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
stack = []

# Map closing brackets to their opening counterparts
mapping = {')': '(', '}': '{', ']': '['}

for char in s:
    # If it's an opening bracket, push to stack
    if char in '({[':
        stack.append(char)
    # If it's a closing bracket
    elif char in ')}]':
        # If stack is empty or brackets don't match
        if not stack or mapping[char] != stack.pop():
            return False

# Valid if stack is empty (all brackets matched)
return len(stack) == 0
```

This implementation correctly uses a stack to validate parentheses:
1. It pushes opening brackets onto the stack
2. When a closing bracket is encountered, it checks if it matches the most recent opening bracket
3. If the stack is empty or the brackets don't match, the string is invalid
4. After processing all characters, the string is valid only if all brackets have been matched (stack is empty)

The time complexity is O(n) where n is the length of the string. The space complexity is O(n) in the worst case.
</details>

---

### Monotonic Stack

#### Problem 19: Daily Temperatures

Given an array of integers `temperatures` representing daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0`.

Example 1:
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

Example 2:
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

Example 3:
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

**Question**: Which implementation correctly calculates the waiting days using a monotonic stack?

```python
def dailyTemperatures(temperatures):
    ### YOUR IMPLEMENTATION HERE ###
```

- [ ] ```
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Store indices of temperatures
    
    for i in range(n):
        # Pop elements from stack while current temperature is higher
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            answer[prev_idx] = i - prev_idx
        
        stack.append(i)
    
    return answer
    ```

- [ ] ```
    n = len(temperatures)
    answer = [0] * n
    
    # Brute force approach
    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                break
    
    return answer
    ```

- [ ] ```
    n = len(temperatures)
    hottest = 0
    answer = [0] * n
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        if temperatures[i] >= hottest:
            hottest = temperatures[i]
            continue
        
        days = 1
        while temperatures[i + days] <= temperatures[i]:
            days += answer[i + days]
        
        answer[i] = days
    
    return answer
    ```

- [ ] ```
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Store indices of temperatures
    
    for i in range(n-1, -1, -1):
        # Pop elements from stack while current temperature is higher or equal
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()
        
        if stack:
            answer[i] = stack[-1] - i
        
        stack.append(i)
    
    return answer
    ```

<details>
<summary>Answer</summary>

The correct answer is:
```
n = len(temperatures)
answer = [0] * n
stack = []  # Store indices of temperatures

for i in range(n):
    # Pop elements from stack while current temperature is higher
    while stack and temperatures[i] > temperatures[stack[-1]]:
        prev_idx = stack.pop()
        answer[prev_idx] = i - prev_idx
    
    stack.append(i)

return answer
```

This implementation uses a monotonic stack to efficiently solve the problem:
1. It maintains a stack of indices of temperatures in decreasing order
2. For each new temperature, it pops elements from the stack while the current temperature is higher
3. For each popped element, it calculates the days to wait as the difference between the current index and the popped index
4. It then pushes the current index onto the stack

This approach ensures that we only process each temperature once, making it efficient.

The time complexity is O(n) where n is the length of the temperatures array. The space complexity is O(n) in the worst case.
</details>

---

## When to Speedrun?

The following Speedrun sections are ready. Check back to this page or create a free account to receive email notifications when a new section comes out.

- Array Patterns
- Linked List Patterns
- Tree Patterns
- Graph Patterns
- Dynamic Programming Patterns
- Backtracking Patterns
- Heap Patterns
- Stack & Queue Patterns