package design

import (
	"encoding/json"
	. "go-algo/tree"
	"log"
)

type Codec struct {
	NilIndexMap map[int]bool
}

func NewCodec() Codec {
	return Codec{}
}

func (this *Codec) Serialize(root *TreeNode) string {
	levelTraversal := []int{}
	if root == nil {
		bytes, _ := json.Marshal(levelTraversal)
		return string(bytes)
	}

	q := []*TreeNode{root}
	var node *TreeNode
	for len(q) > 0 {
		qLen := len(q)
		for i := 0; i < qLen; i++ {
			node, q = q[0], q[1:]
			levelTraversal = append(levelTraversal, node.Val)
			if node.Val != -1<<31 {
				left := node.Left
				right := node.Right

				if left == nil {
					left = &TreeNode{Val: -1 << 31}
				}
				if right == nil {
					right = &TreeNode{Val: -1 << 31}
				}
				q = append(q, left)
				q = append(q, right)
			}
		}
	}
	bytes, _ := json.Marshal(levelTraversal)
	return string(bytes)
}

func (this *Codec) Deserialize(data string) *TreeNode {
	var nums []int
	if err := json.Unmarshal([]byte(data), &nums); err != nil {
		log.Panicln(err)
	}
	if len(nums) == 0 {
		return nil
	}

	var root *TreeNode
	visited := map[int]*TreeNode{}
	var construct func(idx int)
	construct = func(idx int) {
		if idx >= len(nums) {
			return
		}
		if nums[idx] != -1<<31 {
			var node *TreeNode
			if visited[idx] != nil {
				node = visited[idx]
			} else {
				node = &TreeNode{Val: nums[idx]}
				visited[idx] = node
			}

			if root == nil {
				root = node
			}

			parentIdx := (idx - 1) / 2
			if parentIdx*2+1 == idx {
				visited[parentIdx].Left = node
			} else if parentIdx*2+2 == idx {
				visited[parentIdx].Right = node
			}
		}
		construct(idx + 1)
	}
	construct(0)
	return root
}
