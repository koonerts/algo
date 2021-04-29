package tree

import (
	"container/heap"
	"encoding/json"
	"fmt"
	"go-algo/collection"
	"go-algo/ext/mathext"
	"go-algo/ext/sliceext"
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
	Val        int
	ChildNodes []*Node
}

type AccountNode struct {
	name, email string
}

type AccountUnionFind struct {
	roots map[string]AccountNode
	sizes map[string]int
}

type ColorNode struct {
	Color      string
	ChildNodes []*ColorNode
}

func BuildTreePre(inOrder, preOrder []int) *TreeNode {
	var build func(bound int) *TreeNode
	build = func(bound int) *TreeNode {
		if len(inOrder) == 0 || inOrder[0] == bound {
			return nil
		}
		root := &TreeNode{Val: preOrder[0]}
		preOrder = preOrder[1:]
		root.Left = build(root.Val)
		inOrder = inOrder[1:]
		root.Right = build(bound)
		return root
	}
	return build(-1<<31)
}

func BuildTreePost(inOrder, postOrder []int) *TreeNode {
	var build func(bound int) *TreeNode
	build = func(bound int) *TreeNode {
		lenIn, lenPost := len(inOrder), len(postOrder)
		if lenIn == 0 || inOrder[lenIn-1] == bound {
			return nil
		}
		root := &TreeNode{Val: postOrder[lenPost-1]}
		postOrder = postOrder[:lenPost-1]
		root.Right = build(root.Val)
		inOrder = inOrder[:lenIn-1]
		root.Left = build(bound)
		return root
	}
	return build(-1<<31)
}


/*
func ReconstructTree(connections [][]int) *TreeNode {
	inDegree, graph := map[int]int{}, map[int][]int{}
	for _, conn := range connections {
		inDegree[conn[1]] += 1
		graph[conn[0]] = append(graph[conn[0]], conn[1])
	}

	var head *TreeNode
	for nodeVal, degree := range inDegree {
		if degree == 0 {
			head = &TreeNode{Val: nodeVal}
			break
		}
	}

	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {

	}
	return nil
}
*/

func EqualColoredRoots(root *ColorNode) []*ColorNode {
	results := []*ColorNode{}
	var dfs func(node *ColorNode) (red, blue, black int)
	dfs = func(node *ColorNode) (red, blue, black int) {
		if node == nil {
			return 0, 0, 0
		}

		redCnt, blueCnt, blackCnt := 0, 0, 0
		for _, childNode := range node.ChildNodes {
			childRed, childBlue, childBlack := dfs(childNode)
			redCnt += childRed
			blueCnt += childBlue
			blackCnt += childBlack
		}
		if node.Color == "RED" {
			redCnt++
		}
		if node.Color == "BLUE" {
			blueCnt++
		}
		if node.Color == "BLACK" {
			blackCnt++
		}
		if redCnt == blueCnt && redCnt == blackCnt {
			results = append(results, node)
		}

		return redCnt, blueCnt, blackCnt
	}
	dfs(root)
	return results
}

func NewAccountUnionFind() *AccountUnionFind {
	return &AccountUnionFind{map[string]AccountNode{}, map[string]int{}}
}

func (auf *AccountUnionFind) insert(p AccountNode) {
	auf.roots[p.email] = p
	auf.sizes[p.email] += 1
}

func (auf *AccountUnionFind) Union(p, q AccountNode) {
	proot, qroot := auf.Find(p.email), auf.Find(q.email)
	if proot.email == "" {
		auf.insert(p)
		proot = p
	}
	if qroot.email == "" {
		auf.insert(q)
		qroot = q
	}

	if proot == qroot {
		return
	}
	if auf.sizes[proot.email] >= auf.sizes[qroot.email] {
		auf.roots[qroot.email] = proot
		auf.sizes[proot.email] += auf.sizes[qroot.email]
	} else {
		auf.roots[proot.email] = qroot
		auf.sizes[qroot.email] += auf.sizes[proot.email]
	}
}

func (auf *AccountUnionFind) Find(email string) AccountNode {
	if _, ok := auf.roots[email]; !ok {
		return AccountNode{email: ""}
	}

	f := auf.roots[email]
	for f != auf.roots[f.email] {
		auf.roots[f.email] = auf.roots[auf.roots[f.email].email]
		f = auf.roots[f.email]
	}
	return f
}

func AccountsMerge(accounts [][]string) [][]string {
	accM := map[string]AccountNode{}
	auf := NewAccountUnionFind()
	for _, acc := range accounts {
		name := acc[0]
		parentAcc := acc[1]
		for i := 1; i < len(acc); i++ {
			accNode := auf.Find(acc[i])
			if accNode.email == "" {
				accNode = AccountNode{name: name, email: acc[i]}
				accM[accNode.email] = accNode
				auf.Union(accM[parentAcc], accNode)
				continue
			}
			auf.Union(accM[parentAcc], accNode)
		}
	}

	rootToChildren := map[AccountNode][]string{}
	for _, accountNode := range accM {
		root := auf.Find(accountNode.email)
		if _, ok := rootToChildren[root]; !ok {
			rootToChildren[root] = []string{root.name, root.email}
			if root != accountNode {
				rootToChildren[root] = append(rootToChildren[root], accountNode.email)
			}
			continue
		}
		rootToChildren[root] = append(rootToChildren[root], accountNode.email)
	}

	res := make([][]string, 0, len(rootToChildren))
	for _, lst := range rootToChildren {
		sort.Strings(lst[1:])
		n := 1
		for i := 1; i < len(lst); i++ {
			if lst[i] != lst[i-1] {
				lst[n] = lst[i]
				n++
			}
		}
		lst = lst[:n]
		res = append(res, lst)
	}
	return res
}

type Direction int

const (
	North Direction = iota + 1
	West
	East
	South
)

func IsRobotBounded(instructions string) bool {
	x, y, dir := 0, 0, North
	for i := 0; i < 4; i++ {
		for j := range instructions {
			if instructions[j] == 'G' {
				x, y = getNextCoordinates(x, y, dir)
			} else {
				dir = turnRobot(dir, instructions[j])
			}
		}
	}
	return x == 0 && y == 0
}

func turnRobot(currDir Direction, instruction byte) Direction {
	if instruction == 'L' {
		if currDir == North {
			return West
		} else if currDir == West {
			return South
		} else if currDir == South {
			return East
		} else if currDir == East {
			return North
		}
	} else if instruction == 'R' {
		if currDir == North {
			return East
		} else if currDir == East {
			return South
		} else if currDir == South {
			return West
		} else if currDir == West {
			return North
		}
	}
	return currDir
}

func getNextCoordinates(x, y int, currDir Direction) (int, int) {
	if currDir == North {
		return x, y + 1
	} else if currDir == West {
		return x - 1, y
	} else if currDir == East {
		return x + 1, y
	} else {
		return x, y - 1
	}
}

func ShortestDistanceToAllBuildings(grid [][]int) int {
	buildings := []int{}
	dirs := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	cols := len(grid[0])
	for i := range grid {
		for j := range grid[0] {
			point := i*cols + j
			if grid[i][j] == 1 {
				buildings = append(buildings, point)
			}
		}
	}

	minSteps := 1<<31 - 1
	minDistPoint := []int{-1, -1}
	dists := make([][]int, len(grid))
	for i := range dists {
		dists[i] = make([]int, cols)
	}

	for i := range buildings {
		r, c := buildings[i]/cols, buildings[i]%cols
		que := [][]int{{r, c}}
		seen := map[int]bool{}
		buildingReachedCnt := 0
		for len(que) > 0 {
			point := que[0]
			que = que[1:]
			for _, dir := range dirs {
				newX, newY := point[0]+dir[0], point[1]+dir[1]

				if !(newX >= 0 && newY >= 0 && newX < len(grid) && newY < cols) || grid[newX][newY] == 2 {
					continue
				}

				hash := newX*cols + newY
				if seen[hash] {
					continue
				}
				seen[hash] = true
				if grid[newX][newY] == 1 {
					buildingReachedCnt++
					continue
				}

				dists[newX][newY] += dists[point[0]][point[1]] + 1
				que = append(que, []int{newX, newY})
				if i == len(buildings)-1 {
					if dists[newX][newY] < minSteps {
						minSteps = dists[newX][newY]
						minDistPoint[0], minDistPoint[1] = newX, newY
					}
				}
			}
		}

		if buildingReachedCnt != len(buildings) {
			return -1
		}
	}
	if minDistPoint[0] == -1 {
		return -1
	}

	dist := 0
	for i := range buildings {
		r, c := buildings[i]/cols, buildings[i]%cols
		dist += getDist(r, c, minDistPoint[0], minDistPoint[1])
	}
	return dist
}

func getDist(x1, y1, x2, y2 int) int {
	return mathext.AbsInt(x1-x2) + mathext.AbsInt(y1-y2)
}

func RemoveInvalidParentheses(s string) []string {
	visited := map[string]bool{}
	que := []string{s}
	visited[s] = true
	found := false
	results := []string{}

	var isValid = func(expr string) bool {
		count := 0
		for i := range expr {
			ch := expr[i]
			if ch != '(' && ch != ')' {
				continue
			} else if ch == '(' {
				count++
			} else if ch == ')' {
				count--
				if count < 0 {
					return false
				}
			}
		}
		return count == 0
	}

	var appendCandidates = func(expr string) {
		for i := range expr {
			ch := expr[i]
			if ch != '(' && ch != ')' {
				continue
			}
			candidate := expr[:i] + expr[i+1:]
			if !visited[candidate] {
				que = append(que, candidate)
				visited[candidate] = true
			}
		}
	}

	var expr string
	for len(que) > 0 {
		expr, que = que[0], que[1:]
		if isValid(expr) {
			results = append(results, expr)
			found = true
		}
		if !found {
			appendCandidates(expr)
		}
	}

	if len(results) == 0 {
		results = append(results, "")
	}
	return results
}

func RangeSumBST(root *TreeNode, low int, high int) int {
	sum := 0
	stk := []*TreeNode{root}
	var node *TreeNode
	for len(stk) > 0 {
		n := len(stk)
		node, stk = stk[n-1], stk[:n-1]
		if low <= node.Val && node.Val <= high {
			sum += node.Val
		}
		if low < node.Val && node.Left != nil {
			stk = append(stk, node.Left)
		}
		if node.Val < high && node.Right != nil {
			stk = append(stk, node.Right)
		}
	}
	return sum
}

func TreeToDoublyList(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	} else if root.Left == nil && root.Right == nil {
		root.Left = root
		root.Right = root
		return root
	}

	stk := []*TreeNode{}
	node := root
	var head, prev *TreeNode

	for node != nil || len(stk) > 0 {
		for node != nil {
			stk = append(stk, node)
			node = node.Left
		}

		n := len(stk)
		node, stk = stk[n-1], stk[:n-1]
		if head == nil {
			head = node
		}

		if prev != nil {
			prev.Right = node
			node.Left = prev
		}

		prev = node
		node = node.Right
	}
	if head != nil && prev != nil && prev != head {
		head.Left = prev
		prev.Right = head
	}
	return head
}

func PruneTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	if root.IsLeaf() && root.Val == 0 {
		return nil
	}

	var containsOne func(node *TreeNode) bool
	containsOne = func(node *TreeNode) bool {
		if node == nil {
			return false
		}

		keepLeft := containsOne(node.Left)
		keepRight := containsOne(node.Right)

		if !keepLeft {
			node.Left = nil
		}
		if !keepRight {
			node.Right = nil
		}
		return node.Val == 1 || keepLeft || keepRight
	}
	hasNodes := containsOne(root)
	if hasNodes {
		return root
	}
	return nil
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

func CalcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	eqMap := map[string]map[string]float64{}
	for i, eq := range equations {
		if eqMap[eq[0]] == nil {
			eqMap[eq[0]] = map[string]float64{}
		}
		if eqMap[eq[1]] == nil {
			eqMap[eq[1]] = map[string]float64{}
		}
		eqMap[eq[0]][eq[1]] = values[i]
		eqMap[eq[1]][eq[0]] = 1 / values[i]
	}

	var dfs func(from, to string, currProduct float64, visited map[string]bool) float64
	dfs = func(from, to string, currProduct float64, visited map[string]bool) float64 {
		visited[from] = true
		var retVal float64 = -1
		if val, ok := eqMap[from][to]; ok {
			retVal = currProduct * val
		} else {
			for neighbor, weight := range eqMap[from] {
				if visited[neighbor] {
					continue
				}
				retVal = dfs(neighbor, to, currProduct*weight, visited)
				if retVal != -1 {
					break
				}
			}
		}
		visited[from] = false
		return retVal
	}

	results := make([]float64, 0, len(queries))
	for _, query := range queries {
		if eqMap[query[0]] == nil || eqMap[query[1]] == nil {
			results = append(results, -1)
		} else if query[0] == query[1] {
			results = append(results, 1)
		} else {
			vis := map[string]bool{}
			results = append(results, dfs(query[0], query[1], 1, vis))
		}
	}
	return results
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
		*maxDiameter = mathext.MaxInt(*maxDiameter, lDepth+rDepth-1)
		return mathext.MaxInt(lDepth, rDepth)
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

		leftSum := mathext.MaxInt(depthSum(node.Left), 0)
		rightSum := mathext.MaxInt(depthSum(node.Right), 0)
		totalSum := leftSum + rightSum + node.Val
		maxSum = mathext.MaxInt(maxSum, totalSum)
		return mathext.MaxInt(0, mathext.MaxInt(leftSum+node.Val, rightSum+node.Val))
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
		if len(node.ChildNodes) > 0 {
			for i := range node.ChildNodes {
				cpy.ChildNodes = append(cpy.ChildNodes, clone(node.ChildNodes[i]))
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
	var ancestor *TreeNode
	var traverse func(node *TreeNode) int
	traverse = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		l, r := traverse(node.Left), traverse(node.Right)
		curr := 0
		if node == p || node == q {
			curr = 1
		}
		if l+r+curr >= 2 {
			ancestor = node
		}

		return curr
	}
	traverse(root)
	return ancestor
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

func VerticalOrder(root *TreeNode) [][]int {
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
			minCol, maxCol = mathext.MinInt(minCol, vertNode.col), mathext.MaxInt(maxCol, vertNode.col)

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

func VerticalOrder2(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	nodeMap := map[int][]int{}
	q := []VertTreeNode{VertTreeNode{root, 0}}
	var vertNode VertTreeNode
	for len(q) > 0 {
		levelLength := len(q)
		for i := 0; i < levelLength; i++ {
			vertNode, q = q[0], q[1:]
			nodeMap[vertNode.col] = append(nodeMap[vertNode.col], vertNode.node.Val)
			if vertNode.node.Left != nil {
				q = append(q, VertTreeNode{vertNode.node.Left, vertNode.col - 1})
			}
			if vertNode.node.Right != nil {
				q = append(q, VertTreeNode{vertNode.node.Right, vertNode.col + 1})
			}
		}
	}

	keys := make([]int, 0, len(nodeMap))
	for key := range nodeMap {
		keys = append(keys, key)
	}

	sort.Ints(keys)
	res := make([][]int, len(keys))
	i := 0
	for _, key := range keys {
		res[i] = nodeMap[key]
		i++
	}
	return res
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
			sliceext.ReverseIntSlice(levelResults)
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
			if mathext.AbsInt(left-right) > 1 {
				isBalanced = false
			}
			return mathext.MaxInt(left, right) + 1
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

/*func RoadsAndLibraries(n int32, c_lib int32, c_road int32, cities [][]int32) int64 {
	if c_road >= c_lib { return int64(c_lib*n) }
	uf := collection.NewUnionFindMap(n)
	for _, edge := range cities {
		uf.Union(edge[0], edge[1])
	}

	var minCost int64
	for _, root := range uf.GetDistinctRoots() {
		minCost += int64(c_lib)
		minCost += int64(c_road * (uf.GetSize(root)-1))
	}
	return minCost
}*/

func FindItinerary(tickets [][]string) []string {
	adjMap := map[string][]string{}
	pathCnt := 0
	for _, ticket := range tickets {
		if _, ok := adjMap[ticket[0]]; !ok {
			adjMap[ticket[0]] = []string{ticket[1]}
		} else {
			adjMap[ticket[0]] = append(adjMap[ticket[0]], ticket[1])
		}
		pathCnt++
	}

	vis := map[string][]bool{}
	for city := range adjMap {
		sort.Strings(adjMap[city])
		vis[city] = make([]bool, len(adjMap[city]))
	}
	res := make([]string, pathCnt+1)
	res[0] = "JFK"

	var dfs func(currCity string, idx int)
	dfs = func(currCity string, idx int) {
		for i, toCity := range adjMap[currCity] {
			if vis[currCity][i] {
				continue
			}
			vis[currCity][i] = true
			res[idx] = toCity
			dfs(toCity, idx+1)
			if res[pathCnt] != "" {
				break
			}
			res[idx] = ""
			vis[currCity][i] = false
		}
	}

	dfs("JFK", 1)
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

func NumIslands2(m int, n int, positions [][]int) []int {
	uf := collection.NewUnionFindMap()
	islandsCounts := []int{}
	directions := [][]int{{0, -1}, {0, 1}, {-1, 0}, {1, 0}}
	for _, pos := range positions {
		posHash := pos[0]*n + pos[1]
		if !uf.Insert(posHash) {
			islandsCounts = append(islandsCounts, uf.GetConnectionComponents())
			continue
		}
		uf.Union(posHash, posHash)
		for _, dir := range directions {
			newX, newY := pos[0]+dir[0], pos[1]+dir[1]
			islandNode := uf.Find(newX*n + newY)
			if newX < 0 || newY < 0 || newX >= m || newY >= n || islandNode == -1 {
				continue
			}
			uf.Union(posHash, islandNode)
		}
		islandsCounts = append(islandsCounts, uf.GetConnectionComponents())
	}
	return islandsCounts
}

func FindMostFrequent(root *BST) int {
	return -1
}
