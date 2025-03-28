# Algorithm Learning Activities & Games

This document contains practical activities and games to reinforce the accelerated learning strategies from the lesson plan.

## 1. Pattern Recognition Games

### Algorithm Bingo

**Materials**: Create bingo cards with algorithm patterns instead of numbers.
**How to Play**:

1. Generate 10-15 problem descriptions.
2. As each problem is read, mark the algorithm pattern you think solves it.
3. Check solutions after marking 5 problems.
4. "Bingo" is achieved by correctly identifying 5 patterns in a row.

**Example Card**:

```
|   Sliding    |    Two     |    Binary   |     BFS     |   Kadane's  |
|   Window     |  Pointers  |   Search    |             |  Algorithm  |
|-------------|------------|-------------|-------------|-------------|
|   Prefix    |  Dynamic   |             |  Monotonic  |  Backtrack  |
|    Sum      | Programming|   (FREE)    |   Stack     |             |
|-------------|------------|-------------|-------------|-------------|
|   Greedy    |   Union    |    Heap     |     Bit     |    DFS      |
|  Algorithm  |    Find    |             | Manipulation|             |
|-------------|------------|-------------|-------------|-------------|
|    Trie     | Topological|   Quick     |    Two      |   Floyd's   |
|             |    Sort    |   Select    |    Heaps    |   Cycle     |
|-------------|------------|-------------|-------------|-------------|
|    Graph    |  Recursion |   Divide &  | Palindrome  |    LCS      |
|Shortest Path|            |   Conquer   |  Technique  |             |
```

### Pattern Trigger Matching

**Materials**: Two sets of cards - one with problem features, one with algorithm names.
**How to Play**:

1. Place algorithm cards face up.
2. Draw a problem feature card.
3. Match it with the most appropriate algorithm in 10 seconds.
4. Check against an answer key.

**Example Cards**:

- Problem Features:
  - "Find subarray with target sum"
  - "Search in sorted rotated array"
  - "Find minimum spanning tree"
  - "Detect cycle in linked list"
  - "Find all permutations of string"

- Algorithms:
  - Sliding Window
  - Modified Binary Search
  - Kruskal's/Prim's
  - Fast & Slow Pointers
  - Backtracking

### Algorithm Taboo

**Materials**: Cards with algorithm names and 5 "taboo" words you can't say.
**How to Play**:

1. Partner tries to guess the algorithm being described.
2. You cannot use the taboo words on the card.
3. 60-second time limit per card.

**Example Card**:

```
BINARY SEARCH

Taboo Words:
1. Middle
2. Sorted
3. Half
4. Log
5. Divide
```

## 2. Implementation Sprint Activities

### Time Attack Implementation

**Materials**: Timer, set of standard algorithm problems.
**How to Play**:

1. Select an algorithm you've already learned.
2. Write it from scratch with these time limits:
   - Easy patterns: 5 minutes
   - Medium patterns: 10 minutes
   - Complex patterns: 15 minutes
3. Compare with reference implementation.
4. Note any sections that slowed you down.

### Template Skeleton Race

**Materials**: Pre-written template skeletons with critical sections removed.
**How to Play**:

1. Fill in the missing parts of algorithm templates.
2. Time yourself and track improvement over sessions.

**Example Template**:

```python
def merge_sort(arr):
    # Base case
    if ______:
        return arr

    # Divide
    mid = ______
    left = merge_sort(______)
    right = merge_sort(______)

    # Merge
    return ______
```

### Pair Programming Ping-Pong

**Materials**: Problem statement, timer, partner.
**How to Play**:

1. Partner A writes a function signature and the first few lines.
2. Partner B continues, adding the next logical section.
3. Switch every 3 minutes until implementation is complete.
4. Review together and optimize.

## 3. Pattern-to-Problem Mapping Activities

### Algorithm Jeopardy

**Materials**: Jeopardy-style board with patterns as categories and difficulty levels as values.
**How to Play**:

1. Choose a category and difficulty.
2. Read the problem description.
3. Identify the correct algorithm pattern and explain why.
4. For higher difficulties, also explain approach details.

**Example Board**:

```
|             | Sliding Window | Two Pointers | Binary Search | Dynamic Programming | Graph Traversal |
|-------------|----------------|--------------|---------------|---------------------|-----------------|
| $100 (Easy) |                |              |               |                     |                 |
| $200        |                |              |               |                     |                 |
| $300        |                |              |               |                     |                 |
| $400        |                |              |               |                     |                 |
| $500 (Hard) |                |              |               |                     |                 |
```

### Algorithm Detective

**Materials**: Set of algorithm implementations with patterns disguised or obfuscated.
**How to Play**:

1. Study the implementation without any labels.
2. Identify which core algorithm pattern is being used.
3. Explain the key indicators that revealed the pattern.

**Example**: An implementation of Dijkstra's algorithm with variable names changed and implementation details modified, but core pattern intact.

## 4. Visual Learning Activities

### Algorithm Storyboarding

**Materials**: Index cards, markers/pencils.
**How to Play**:

1. Break down an algorithm into 6-8 key steps.
2. Draw a simple visual for each step.
3. Arrange in sequence and practice explaining using only visuals.
4. Test recall by shuffling cards and reordering.

### State Transition Theater

**Materials**: Props representing data structures (cups for array elements, string for pointers, etc.)
**How to Play**:

1. Assign people to represent different elements or pointers.
2. Physically act out the algorithm steps.
3. Freeze at key moments to discuss state.

**Example**: For Quick Sort, people hold numbers and physically swap positions during partitioning.

### Algorithm Flow Diagrams

**Materials**: Template flowchart symbols, large sheet of paper.
**How to Play**:

1. Create a detailed flow diagram of an algorithm.
2. Include decision points, loops, and state changes.
3. Have someone trace a sample input through your diagram.
4. Refine diagram based on feedback.

## 5. Template Mastery Activities

### Code Reconstruction Challenge

**Materials**: Algorithm templates cut into sections, timer.
**How to Play**:

1. Shuffle template code sections.
2. Race to correctly order the pieces.
3. Once ordered, implement the missing connections between sections.

### Template Adaptation Game

**Materials**: Base algorithm template, list of modifications.
**How to Play**:

1. Start with a standard template (e.g., BFS).
2. Draw a modification card (e.g., "Adapt to find shortest path", "Add cycle detection").
3. Modify the template to handle the new requirement.
4. Compare with reference implementation.

**Example Modification Cards**:

- "Adapt DFS to detect cycles"
- "Modify binary search for rotated array"
- "Convert knapsack solution to use bottom-up approach"
- "Add memoization to recursive solution"

### Template Mad Libs

**Materials**: Algorithm templates with key parts replaced by blanks.
**How to Play**:

1. Fill in the blanks without seeing the original.
2. Compare your version with the optimal version.
3. Discuss differences and why they matter.

**Example**:

```python
def binary_search(arr, target):
    left = ______
    right = ______

    while ______:
        mid = ______

        if arr[mid] == target:
            return ______
        elif arr[mid] < target:
            ______ = ______
        else:
            ______ = ______

    return ______
```

## 6. Time-Boxing Practice

### Algorithm Lightning Round

**Materials**: Stopwatch, set of problems.
**How to Play**:

1. Set progressively shorter time limits for solving problems.
2. Start with comfortable time, then reduce by 20% each round.
3. Focus on getting working solution, not optimized solution.
4. Review which steps took longest.

### The 25-5 Technique

**Materials**: Timer, problem set, notebook.
**How to Play**:

1. 25 minutes: Work intensely on a problem.
2. 5 minutes: Review and identify what you learned/struggled with.
3. If solved, move to next problem; if not, decide whether to continue or look at hint.

### Rapid Algorithm Prototyping

**Materials**: Timer, whiteboard/paper, set of problems.
**How to Play**:

1. 5 minutes: Plan approach (no coding).
2. 15 minutes: Implement core algorithm (skip edge cases).
3. 5 minutes: Add edge case handling.
4. 5 minutes: Analyze and improve.

## 7. Simplification Games

### Edge Case Collection

**Materials**: Problem statement, shared document.
**How to Play**:

1. Collaboratively build the most comprehensive list of edge cases for a problem.
2. Award points for valid cases others didn't think of.
3. For each edge case, identify which algorithm modification handles it.

### Complexity Ladder

**Materials**: Problem statement with difficulty variants.
**How to Play**:

1. Start with simplest version of problem (e.g., array is sorted, no duplicates).
2. Solve it optimally.
3. Add complexity one constraint at a time (e.g., now array has duplicates).
4. Adapt solution for each new constraint.

**Example Progression**:

1. Find element in sorted array → Binary Search
2. Find element in sorted array with duplicates → Binary Search with post-processing
3. Find element in rotated sorted array → Modified Binary Search
4. Find element in rotated sorted array with duplicates → Further modified approach

### Algorithm Building Blocks

**Materials**: Cards with algorithm components.
**How to Play**:

1. Identify fundamental building blocks of complex algorithms.
2. Practice implementing each block separately.
3. Combine blocks to solve more complex problems.

**Example Building Blocks**:

- Two-pointer technique
- Hash map for frequency counting
- BFS queue management
- Recursive DFS pattern

## 8. Language-Specific Optimization

### Standard Library Scavenger Hunt

**Materials**: List of algorithm tasks, language documentation.
**How to Play**:

1. For each task, find the most efficient standard library function/method.
2. Implement a solution using it.
3. Compare with traditional implementation.

**Example Tasks**:

- Sort a list in reverse order
- Find all permutations of a string
- Implement a max heap
- Find the intersection of two arrays

### Algorithm Translation Challenge

**Materials**: Algorithm implementation in one language.
**How to Play**:

1. Translate algorithm to another language, optimizing for that language's strengths.
2. Benchmark both versions.
3. Identify language-specific features that improved performance.

### Syntactic Sugar Speed Run

**Materials**: List of common algorithm operations.
**How to Play**:

1. Write the most concise, idiomatic code for each operation in your language.
2. Create a personal cheatsheet from your solutions.
3. Practice until you can write each pattern from memory.

**Example Operations**:

- Initialize a 2D matrix
- Find maximum value and its index in array
- Create a counter dictionary from list elements
- Merge two sorted arrays

## Active Recall Activities

### Flash Card Drills

**Materials**: Digital or physical flashcards for algorithms.
**How to Play**:

1. Create cards with algorithm pattern on front, key characteristics on back.
2. Review in spaced repetition system.
3. Advanced: Include time & space complexity, example problems.

**Example Card Format**:

```
Front:
Sliding Window Pattern

Back:
- Use: Find subarrays satisfying constraints
- Time: O(N) where N is array length
- Key implementation detail: Expand window, contract when constraint violated
- Example problems: Max sum subarray of size K, Longest substring with K distinct chars
```

### Algorithm Reconstruction

**Materials**: Timer, paper.
**How to Play**:

1. Study an algorithm implementation for 5 minutes.
2. Close all references.
3. Wait 10 minutes (do something else).
4. Reconstruct the algorithm from memory.
5. Compare with original.

### Blank Page Challenge

**Materials**: Blank paper, timer.
**How to Play**:

1. Without any references, write down all algorithm patterns you can remember.
2. For each, note key characteristics, time/space complexity, and example problems.
3. Check against master list and note gaps in recall.

## Concept Mapping Activities

### Algorithm Family Tree

**Materials**: Large paper, markers, algorithm list.
**How to Play**:

1. Create a hierarchical diagram organizing algorithms by:
   - Problem domain (array, graph, string)
   - Technique (divide & conquer, dynamic programming)
   - Relationships between algorithms
2. Add example problems at leaf nodes.

### Decision Flowchart Construction

**Materials**: Flowchart template, algorithm characteristics.
**How to Play**:

1. Create a decision tree for selecting algorithms.
2. Start with high-level questions (Data structure? Optimization goal?).
3. End with specific algorithm recommendations.
4. Test with sample problems.

**Example First-Level Questions**:

- "Are you working with a graph/tree?"
- "Are you searching for a value?"
- "Do you need to optimize something?"
- "Are you working with subarrays/substrings?"

### Pattern Connection Map

**Materials**: Index cards with algorithm names, string.
**How to Play**:

1. Place algorithm cards on table.
2. Use string to connect related algorithms.
3. Label each connection with the relationship.
4. Discuss why these algorithms are related.

**Example Connections**:

- BFS → Dijkstra's (Both use queues, Dijkstra's is weighted BFS)
- Merge Sort → Quick Sort (Both divide & conquer, different approaches)
- Kadane's → DP (Kadane's is specialized DP for max subarray)

## Integration Activities

### Algorithm Mashup Challenge

**Materials**: Algorithm pattern cards.
**How to Play**:

1. Draw two random algorithm pattern cards.
2. Create a problem that requires both patterns to solve optimally.
3. Implement the combined solution.

**Example Combinations**:

- Binary Search + Two Pointers
- BFS + DP
- Sliding Window + Heap

### Real-World Application Hunt

**Materials**: News articles, technical blogs, product descriptions.
**How to Play**:

1. Find real-world examples of algorithm applications.
2. Identify which algorithm patterns are likely being used.
3. Explain how the pattern applies to the use case.

**Example Applications**:

- Google Maps navigation → Dijkstra's/A* algorithms
- Netflix recommendations → Collaborative filtering/matrix algorithms
- Autocomplete → Trie data structure

### Weekly Implementation Project

**Materials**: Weekly project prompt integrating multiple algorithms.
**How to Play**:

1. Assign a mini-project requiring multiple algorithm patterns.
2. Implement a working solution.
3. Present to group, explaining algorithm choices.

**Example Projects**:

- Build a simple autocomplete system (Trie + ranking algorithm)
- Create a maze solver (BFS/DFS + backtracking)
- Implement a simple route planner (Graph algorithms)

## Progress Tracking Games

### Algorithm Mastery Grid

**Materials**: Grid with algorithm patterns and mastery levels.
**How to Play**:

1. Create a visual progress tracker.
2. For each algorithm, track progress through levels:
   - Level 1: Can recognize the pattern
   - Level 2: Can implement with help
   - Level 3: Can implement from memory
   - Level 4: Can optimize and handle edge cases
   - Level 5: Can teach it to others
3. Color code or mark levels as you advance.

### Pattern Achievement Unlocked

**Materials**: "Achievement badges" for algorithm milestones.
**How to Play**:

1. Define specific achievements for each algorithm pattern.
2. Award yourself badges as you complete them.
3. Display your "achievement wall" for motivation.

**Example Achievements**:

- "Binary Search Master" - Implement 5 variations of binary search
- "Graph Navigator" - Solve problems using 3 different graph algorithms
- "DP Wizard" - Solve a hard DP problem without hints

### Weekly Algorithm Retrospective

**Materials**: Learning journal, algorithm problem record.
**How to Play**:

1. Schedule weekly 30-minute reviews.
2. Analyze patterns in problems you struggled with.
3. Identify algorithm concepts needing reinforcement.
4. Plan focused practice for the coming week.

## Competitive Practice Games

### Algorithm Time Trials

**Materials**: Set of algorithm problems, timer.
**How to Play**:

1. Implement the same algorithm multiple times over different days.
2. Track implementation time and correctness.
3. Analyze improvement over time.

### Problem Solving Kata

**Materials**: Set of similar problems using the same algorithm pattern.
**How to Play**:

1. Practice the same pattern on progressively harder problems.
2. Aim for increasingly clean, efficient implementation.

**Example Kata Sequence**:

1. Merge two sorted arrays
2. Merge K sorted arrays
3. Merge K sorted linked lists
4. Implement external merge sort for large files

### Mock Interview Rotation

**Materials**: Interview problems, timer, peers.
**How to Play**:

1. Take turns being interviewer and candidate.
2. Interviewer selects problem without revealing algorithm pattern.
3. Candidate solves while thinking aloud.
4. Provide feedback on pattern recognition, implementation, communication.

---

These activities make algorithm learning more engaging and effective by applying active learning principles. Adapt them to your personal learning style and available time. The key is consistent practice with deliberate focus on your improvement areas.
