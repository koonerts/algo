package main

import (
	"encoding/json"
	"fmt"
	"math"
	"sync"
)

type BST struct {
	Id string
	Value int
	Left  *BST
	Right *BST
}

type BinaryTree struct {
	Id string
	Value int
	Left  *BinaryTree
	Right *BinaryTree
}

type Node struct {
	Name     string
	Children []*Node
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
		tNode := BinaryTree{Id:node["id"].(string), Value:int(node["value"].(float64))}
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

		if math.Abs(float64(node.Value - target)) < math.Abs(float64(closest - target)) {
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
			sync<-1
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

func (n *Node) DepthFirstSearch(array []string) []string {
	array = append(array, n.Name)
	for _, child := range n.Children {
		array = child.DepthFirstSearch(array)
	}
	return array
}