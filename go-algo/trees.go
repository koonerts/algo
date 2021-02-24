package main

import (
	"encoding/json"
	"fmt"
	"math"
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
	Val int
	Neighbors []*Node
}

func createTreeNode(vals []int) *TreeNode {
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

func createBinaryTree(jsonStr string) *BinaryTree {
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
		*maxDiameter = MaxInt(*maxDiameter, lDepth+rDepth-1)
		return MaxInt(lDepth, rDepth)
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
	maxSum := -1<<31

	var depthSum func(node *TreeNode) int
	depthSum = func(node *TreeNode) int {
		if node == nil {return 0}

		leftSum := MaxInt(depthSum(node.Left), 0)
		rightSum := MaxInt(depthSum(node.Right), 0)
		totalSum := leftSum+rightSum+node.Val
		maxSum = MaxInt(maxSum, totalSum)
		return MaxInt(0, MaxInt(leftSum + node.Val, rightSum + node.Val))
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

func rightSideView(root *TreeNode) (result []int) {
	if root == nil { return nil }
	stk := []*TreeNode{root}
	for len(stk) > 0 {
		levelLength := len(stk)
		for i := 0; i < levelLength; i++ {
			node := stk[0]
			stk = stk[1:]
			if node.Left != nil {
				stk = append(stk, node.Left)
			}
			if node.Right != nil {
				stk = append(stk, node.Right)
			}
			if i == levelLength-1 {
				result = append(result, node.Val)
			}
		}
	}
	return
}

func numIslands(grid [][]byte) (cnt int) {
	if len(grid) == 0 {
		return 0
	}

	var clearIsland func(i, j int)
	clearIsland = func(i, j int) {
		if 0 <= i && i < len(grid) && 0 <= j && j < len(grid[i]) && grid[i][j] == '1' {
			grid[i][j] = '0'
			clearIsland(i+1, j)
			clearIsland(i-1, j)
			clearIsland(i, j+1)
			clearIsland(i, j-1)
		}
	}

	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == '1' {
				cnt++
				clearIsland(i, j)
			}
		}
	}
	return
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
			pIdx = (pIdx-1)/2
		} else {
			qIdx = (qIdx-1)/2
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
			paths = append(paths, path + fmt.Sprintf("%s%d", "->", node.Val))
		} else {
			if node.Left != nil {
				traverse(node.Left, path + fmt.Sprintf("%s%d", "->", node.Val))
			}
			if node.Right != nil {
				traverse(node.Right, path + fmt.Sprintf("%s%d", "->", node.Val))
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
	col int
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
			minCol, maxCol = MinInt(minCol, vertNode.col), MaxInt(maxCol, vertNode.col)

			/*if nodeMap[vertNode.col] == nil {
				nodeMap[vertNode.col] = &[]int{}
			}*/
			nodeMap[vertNode.col] = append(nodeMap[vertNode.col], vertNode.node.Val)
			if vertNode.node.Left != nil {
				q = append(q, VertTreeNode{vertNode.node.Left, vertNode.col-1})
			}
			if vertNode.node.Right != nil {
				q = append(q, VertTreeNode{vertNode.node.Right, vertNode.col+1})
			}
		}
	}

	results := make([][]int, 0, len(nodeMap))
	for col := minCol; col < maxCol+1; col++ {
		results = append(results, nodeMap[col])
	}

	return results
}