package tree

import (
	"container/heap"
	"encoding/json"
	"fmt"
	"go-algo/collection"
	mathcstm "go-algo/mathext"
	"go-algo/slice"
	"math"
	"sort"
	"sync"
)

type BST struct {
	Id    string
	Value int
	Left  *BST
	Right *BST
}

type BinaryTree struct {
	Id    string
	Value int
	Left  *BinaryTree
	Right *BinaryTree
}

type AdjacencyListNode struct {
	Name     string
	Children []*AdjacencyListNode
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Node struct {
	Val       int
	Neighbors []*Node
}

func CreateTreeNode(vals []int) *TreeNode {
	nodeSet := map[int]*TreeNode{}
	for i, val := range vals {
		if val == -1<<31 {
			continue
		}
		node := &TreeNode{val, nil, nil}
		nodeSet[i] = node
	}

	for i := range vals {
		if vals[i] == -1<<31 {
			continue
		}
		left := 2*i + 1
		right := left + 1
		if left < len(vals) && nodeSet[left] != nil {
			nodeSet[i].Left = nodeSet[left]
		}
		if right < len(vals) && nodeSet[right] != nil {
			nodeSet[i].Right = nodeSet[right]
		}
	}
	return nodeSet[0]
}

func CreateBinaryTree(jsonStr string) *BinaryTree {
	var itree interface{}
	bytes := []byte(jsonStr)
	err := json.Unmarshal(bytes, &itree)
	if err != nil {
		fmt.Println(err)
	}
	tree := itree.(map[string]interface{})
	var root *BinaryTree
	var binaryTreeMap = map[string]*BinaryTree{}
	var nodeMap = map[string]interface{}{}

	nodes := tree["nodes"].([]interface{})
	for _, val := range nodes {
		node := val.(map[string]interface{})
		tNode := BinaryTree{Id: node["id"].(string), Value: int(node["value"].(float64))}
		binaryTreeMap[tNode.Id] = &tNode
		nodeMap[tNode.Id] = node
		if tree["root"].(string) == tNode.Id {
			root = &tNode
		}
	}

	for id := range binaryTreeMap {
		left := nodeMap[id].(map[string]interface{})["left"]
		right := nodeMap[id].(map[string]interface{})["right"]
		if left != nil {
			binaryTreeMap[id].Left = binaryTreeMap[left.(string)]
		}
		if right != nil {
			binaryTreeMap[id].Right = binaryTreeMap[right.(string)]
		}
	}

	return root
}

func CreateBST(jsonStr string) *BST {
	var itree interface{}
	bytes := []byte(jsonStr)
	err := json.Unmarshal(bytes, &itree)
	if err != nil {
		fmt.Println(err)
	}
	tree := itree.(map[string]interface{})
	var root *BST
	var bstMap = map[string]*BST{}
	var nodeMap = map[string]interface{}{}

	nodes := tree["nodes"].([]interface{})
	for _, val := range nodes {
		node := val.(map[string]interface{})
		tNode := BST{Id: node["id"].(string), Value: int(node["value"].(float64))}
		bstMap[tNode.Id] = &tNode
		nodeMap[tNode.Id] = node
		if tree["root"].(string) == tNode.Id {
			root = &tNode
		}
	}

	for id := range bstMap {
		left := nodeMap[id].(map[string]interface{})["left"]
		right := nodeMap[id].(map[string]interface{})["right"]
		if left != nil {
			bstMap[id].Left = bstMap[left.(string)]
		}
		if right != nil {
			bstMap[id].Right = bstMap[right.(string)]
		}
	}

	return root
}

func (tree *BST) FindClosestValue(target int) int {
	closest := math.MaxInt32
	var traverse func(node *BST)
	traverse = func(node *BST) {
		if node.Value == target {
			closest = target
		} else if node.Value > target && node.Left != nil {
			traverse(node.Left)
		} else if node.Value < target && node.Right != nil {
			traverse(node.Right)
		}

		if math.Abs(float64(node.Value-target)) < math.Abs(float64(closest-target)) {
			closest = node.Value
		}
	}
	traverse(tree)
	return closest
}

func BranchSums(root *BinaryTree) []int {
	var results []int
	var traverse func(node *BinaryTree, pathSum int)
	traverse = func(node *BinaryTree, pathSum int) {
		if node != nil {
			if node.Left == nil && node.Right == nil {
				results = append(results, pathSum+node.Value)
			} else {
				traverse(node.Left, pathSum+node.Value)
				traverse(node.Right, pathSum+node.Value)
			}
		}
	}

	traverse(root, 0)
	return results
}

func NodeDepths(root *BinaryTree) int {
	var wg sync.WaitGroup
	var sync = make(chan int, 1)
	depthSum := 0

	var traverse func(node *BinaryTree, depthSum *int, depth int)
	traverse = func(node *BinaryTree, depthSum *int, depth int) {
		defer wg.Done()
		if node != nil {
			sync <- 1
			*depthSum += depth
			<-sync

			wg.Add(1)
			go traverse(node.Left, depthSum, depth+1)

			wg.Add(1)
			go traverse(node.Right, depthSum, depth+1)
		}
	}

	wg.Add(1)
	go traverse(root, &depthSum, 0)
	wg.Wait()
	return depthSum
}

func (n *AdjacencyListNode) DepthFirstSearch(array []string) []string {
	array = append(array, n.Name)
	for _, child := range n.Children {
		array = child.DepthFirstSearch(array)
	}
	return array
}

func TreeDiameter(root *BinaryTree) (diameter int) {
	findDepth(root, &diameter)
	return
}

func findDepth(node *BinaryTree, maxDiameter *int) (depth int) {
	if node == nil {
		return 0
	} else {
		lDepth := findDepth(node.Left, maxDiameter) + 1
		rDepth := findDepth(node.Right, maxDiameter) + 1
		*maxDiameter = mathcstm.MaxInt(*maxDiameter, lDepth+rDepth-1)
		return mathcstm.MaxInt(lDepth, rDepth)
	}
}

func isValidBST(root *TreeNode) bool {
	var validate func(node *TreeNode, lo, hi int) bool
	validate = func(node *TreeNode, lo, hi int) bool {
		if node == nil {
			return true
		} else {
			return lo < node.Val && node.Val < hi &&
				validate(node.Left, lo, node.Val) &&
				validate(node.Right, node.Val, hi)
		}
	}
	return validate(root, -1<<63, 1<<63-1)
}

func flatten(root *TreeNode) {
	preOrder := []*TreeNode{}
	var traversePreOrder func(node *TreeNode)
	traversePreOrder = func(node *TreeNode) {
		if node == nil {
			return
		} else {
			preOrder = append(preOrder, node)
			traversePreOrder(node.Left)
			traversePreOrder(node.Right)
		}
	}
	traversePreOrder(root)
	for i := range preOrder {
		if i+1 < len(preOrder) {
			preOrder[i].Right = preOrder[i+1]
			preOrder[i].Left = nil
		}
	}
}

func maxPathSum(root *TreeNode) int {
	maxSum := -1 << 31

	var depthSum func(node *TreeNode) int
	depthSum = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		leftSum := mathcstm.MaxInt(depthSum(node.Left), 0)
		rightSum := mathcstm.MaxInt(depthSum(node.Right), 0)
		totalSum := leftSum + rightSum + node.Val
		maxSum = mathcstm.MaxInt(maxSum, totalSum)
		return mathcstm.MaxInt(0, mathcstm.MaxInt(leftSum+node.Val, rightSum+node.Val))
	}
	depthSum(root)
	return maxSum
}

func cloneGraph(node *Node) *Node {
	nodeMap := make(map[*Node]*Node)

	var clone func(node *Node) *Node
	clone = func(node *Node) *Node {
		if node == nil {
			return nil
		} else if nodeMap[node] != nil {
			return nodeMap[node]
		}

		cpy := &Node{node.Val, nil}
		nodeMap[node] = cpy
		if len(node.Neighbors) > 0 {
			for i := range node.Neighbors {
				cpy.Neighbors = append(cpy.Neighbors, clone(node.Neighbors[i]))
			}
		}
		return cpy
	}
	return clone(node)
}

func rightSideView(root *TreeNode) (results []int) {
	if root == nil {
		return results
	} else if root.IsLeaf() {
		results = append(results, root.Val)
		return results
	}

	que := []*TreeNode{root}
	var node *TreeNode
	for len(que) > 0 {
		qLen := len(que)
		for i := 0; i < qLen; i++ {
			node, que = que[0], que[1:]
			if node.Left != nil {
				que = append(que, node.Left)
			}
			if node.Right != nil {
				que = append(que, node.Right)
			}
			if i == qLen-1 {
				results = append(results, node.Val)
			}
		}
	}

	return results
}

type AncestorTreeNode struct {
	Node, Ancestor *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	stk := []*TreeNode{root}
	levelOrder := make([]*TreeNode, 0)
	var node *TreeNode
	pIdx, qIdx, nIdx := -1, -1, 0
	for len(stk) > 0 {
		levelLen := len(stk)
		for i := 0; i < levelLen; i++ {
			node, stk = stk[0], stk[1:]
			levelOrder = append(levelOrder, node)
			if pIdx == -1 && node == p {
				pIdx = nIdx
			}
			if qIdx == -1 && node == q {
				qIdx = nIdx
			}
			if pIdx != -1 && qIdx != -1 {
				break
			}
			if node != nil {
				stk = append(stk, node.Left)
				stk = append(stk, node.Right)
			}
			nIdx++
		}
		if pIdx != -1 && qIdx != -1 {
			break
		}
	}

	for pIdx != qIdx {
		if pIdx > qIdx {
			pIdx = (pIdx - 1) / 2
		} else {
			qIdx = (qIdx - 1) / 2
		}
	}
	return levelOrder[pIdx]
}

func getTreeNode(root *TreeNode, val int) (returnNode *TreeNode) {
	var traverse func(node *TreeNode)
	traverse = func(node *TreeNode) {
		if returnNode == nil {
			if node == nil {
				return
			}

			if node.Val == val {
				returnNode = node
			} else {
				traverse(node.Left)
				traverse(node.Right)
			}
		}
	}
	traverse(root)
	return
}

func (node *TreeNode) IsLeaf() bool {
	return node.Left == nil && node.Right == nil
}

func binaryTreePaths(root *TreeNode) (paths []string) {
	if root == nil {
		return
	} else if root.IsLeaf() {
		paths = append(paths, fmt.Sprintf("%d", root.Val))
		return
	}

	var traverse func(node *TreeNode, path string)
	traverse = func(node *TreeNode, path string) {
		if node == nil {
			return
		} else if node.IsLeaf() {
			paths = append(paths, path+fmt.Sprintf("%s%d", "->", node.Val))
		} else {
			if node.Left != nil {
				traverse(node.Left, path+fmt.Sprintf("%s%d", "->", node.Val))
			}
			if node.Right != nil {
				traverse(node.Right, path+fmt.Sprintf("%s%d", "->", node.Val))
			}
		}
	}
	traverse(root.Left, fmt.Sprintf("%d", root.Val))
	traverse(root.Right, fmt.Sprintf("%d", root.Val))
	return
}

// TODO: Come back to
func alienOrder(words []string) (order string) {
	// inDegree, adjGraph := make(map[string]int), make(map[string][]string)
	return
}

type VertTreeNode struct {
	node *TreeNode
	col  int
}

func verticalOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	nodeMap := map[int][]int{}
	minCol := 0
	maxCol := 0

	q := []VertTreeNode{VertTreeNode{root, 0}}
	var vertNode VertTreeNode
	for len(q) > 0 {
		levelLength := len(q)
		for i := 0; i < levelLength; i++ {
			vertNode, q = q[0], q[1:]
			minCol, maxCol = mathcstm.MinInt(minCol, vertNode.col), mathcstm.MaxInt(maxCol, vertNode.col)

			/*if nodeMap[vertNode.col] == nil {
				nodeMap[vertNode.col] = &[]int{}
			}*/
			nodeMap[vertNode.col] = append(nodeMap[vertNode.col], vertNode.node.Val)
			if vertNode.node.Left != nil {
				q = append(q, VertTreeNode{vertNode.node.Left, vertNode.col - 1})
			}
			if vertNode.node.Right != nil {
				q = append(q, VertTreeNode{vertNode.node.Right, vertNode.col + 1})
			}
		}
	}

	results := make([][]int, 0, len(nodeMap))
	for col := minCol; col < maxCol+1; col++ {
		results = append(results, nodeMap[col])
	}

	return results
}

func FindKthLargestValueInBst(tree *BST, k int) int {
	stk := []*BST{}
	node := tree
	ih := &collection.IntMinHeap{}
	for len(stk) > 0 || node != nil {
		for node != nil {
			stk = append(stk, node)
			node = node.Left
		}
		node, stk = stk[len(stk)-1], stk[:len(stk)-1]
		if len(*ih) < k || node.Value > (*ih)[0] {
			heap.Push(ih, node.Value)
			if len(*ih) > k {
				heap.Pop(ih)
			}
		}
		node = node.Right
	}
	return (*ih)[0]
}

type ZigZagDirection int

const (
	LeftToRight ZigZagDirection = 1
	RightToLeft ZigZagDirection = -1
)

func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	zdir := LeftToRight
	q := []*TreeNode{root}
	var node *TreeNode
	var results [][]int
	for len(q) > 0 {
		qLen := len(q)
		levelResults := make([]int, 0, qLen)
		for i := 0; i < qLen; i++ {
			node, q = q[0], q[1:]
			levelResults = append(levelResults, node.Val)
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}
		if zdir == RightToLeft {
			slice.ReverseIntSlice(levelResults)
		}
		results = append(results, levelResults)
		zdir *= -1
	}
	return results
}

func HeightBalancedBinaryTree(tree *BinaryTree) bool {
	var isBalanced = true
	var depth func(node *BinaryTree) int
	depth = func(node *BinaryTree) int {
		if node == nil {
			return 0
		} else if isBalanced == false {
			return -1
		} else {
			left := depth(node.Left)
			right := depth(node.Right)
			if mathcstm.AbsInt(left-right) > 1 {
				isBalanced = false
			}
			return mathcstm.MaxInt(left, right) + 1
		}
	}
	depth(tree)
	return isBalanced
}

func BranchSumsLarger(arr []int64) string {
	if len(arr) <= 1 {
		return ""
	} else if len(arr) == 2 {
		return "Left"
	} else if len(arr) == 3 {
		if arr[1] > arr[2] {
			return "Left"
		}
		return "Right"
	}

	var lsum, rsum int64
	var findSums func(i int, side string)
	findSums = func(i int, side string) {
		if i > len(arr) {
			return
		}
		if arr[i] != -1 {
			if side == "Left" {
				lsum += arr[i]
			} else {
				rsum += arr[i]
			}
		}
		lChild := 2*i + 1
		findSums(lChild, side)
		findSums(lChild+1, side)
	}
	findSums(1, "Left")
	findSums(2, "Right")

	if lsum > rsum {
		return "Left"
	} else if rsum > lsum {
		return "Right"
	}
	return ""
}

func RoadsAndLibraries(n int32, c_lib int32, c_road int32, cities [][]int32) int64 {
	if c_road >= c_lib { return int64(c_lib*n) }
	uf := collection.NewUnionFind(n)
	for _, edge := range cities {
		uf.Union(edge[0], edge[1])
	}

	var minCost int64
	for _, root := range uf.GetDistinctRoots() {
		minCost += int64(c_lib)
		minCost += int64(c_road * (uf.GetSize(root)-1))
	}
	return minCost
}

func FindItinerary(tickets [][]string) []string {
	adjMap := map[string][]string{}
	for _, ticket := range tickets {
		if _, ok := adjMap[ticket[0]]; !ok {
			adjMap[ticket[0]] = []string{ticket[1]}
		} else {
			adjMap[ticket[0]] = append(adjMap[ticket[0]], ticket[1])
		}
	}
	for city := range adjMap {
		sort.Strings(adjMap[city])
	}

	res := []string{}
	vis := map[string]bool{}
	var traverse func(city string)
	traverse = func(city string) {
		res = append(res, city)
		for _, toCity := range adjMap[city] {
			flight := fmt.Sprintf("%s|%s", city, toCity)
			if !vis[flight] {
				vis[flight] = true
				traverse(toCity)
			}
		}

	}
	traverse("JFK")
	return res
}

func CanFinish(numCourses int, prerequisites [][]int) bool {
	inDegree, adjMap := map[int]int{}, map[int][]int{}
	for i := 0; i < numCourses; i++ {
		inDegree[i] = 0
		adjMap[i] = []int{}
	}
	for _, preReq := range prerequisites {
		inDegree[preReq[0]] += 1
		adjMap[preReq[1]] = append(adjMap[preReq[1]], preReq[0])
	}

	que := []int{}
	for course := range inDegree {
		if inDegree[course] == 0 {
			que = append(que, course)
		}
	}

	finishedCourses := 0
	var course int
	for len(que) > 0 {
		finishedCourses++
		course, que = que[0], que[1:]
		for _, child := range adjMap[course] {
			inDegree[child] -= 1
			if inDegree[child] == 0 {
				que = append(que, child)
			}
		}
	}
	return finishedCourses == numCourses
}